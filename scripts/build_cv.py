# -*- coding: utf-8 -*-
"""Build the academic CV as a standalone, print-ready HTML file.

Publication data is read from _publications/ and _data/under_review.yml so the
CV cannot drift out of step with the website. Everything that has no home in
those files — education, awards, service, skills — is declared below.

    python scripts/build_cv.py

Then open the output and use the browser's Print -> Save as PDF.
"""
import io
import os
import re
import glob
import datetime
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(ROOT, "_publications")
UNDER_REVIEW = os.path.join(ROOT, "_data", "under_review.yml")
PARENT = os.path.dirname(ROOT)
# The recovered source lives in a resume/homepage folder here, while the
# original Windows layout was code/homepage beside code/resume.
OUTPUT_DIR = PARENT if os.path.basename(PARENT).lower() == "resume" else os.path.join(PARENT, "resume")
OUT = os.path.join(OUTPUT_DIR, "CV-Chenyi-Jiang.html")

# --------------------------------------------------------------------------
# Content that does not live in the site data files.
# --------------------------------------------------------------------------

NAME_EN = "Chenyi Jiang"
NAME_ZH = "江宸逸"

CONTACT = [
    ("Email", "jiangchenyi@njust.edu.cn", "mailto:jiangchenyi@njust.edu.cn"),
    ("Homepage", "lanchjl.github.io", "https://lanchjl.github.io"),
    ("Scholar", "Google Scholar",
     "https://scholar.google.com/citations?user=R9ruXHMAAAAJ"),
    ("GitHub", "github.com/LanchJL", "https://github.com/LanchJL"),
]

POSITION = ("Ph.D. Candidate, School of Computer Science and Engineering<br>"
            "Nanjing University of Science and Technology, Nanjing, China")

INTERESTS = ("Compositional and generalized zero-shot recognition &middot; "
             "visual-semantic representation learning &middot; "
             "language-guided domain adaptation and generalization &middot; "
             "vision-language models &middot; test-time adaptation")

# --------------------------------------------------------------------------
# Per-application variants.
#
# Deliberately narrow. Only two things change: which interests are named first,
# and which first-author papers lead the selected list. Everything else — the
# publication record, education, awards — is identical in every version,
# because a CV that reshapes itself per reader is both a maintenance trap and
# easy to catch. The tailoring that actually matters belongs in the cover
# letter, not here.
#
#   python scripts/build_cv.py --target zheng-um
# --------------------------------------------------------------------------

TARGETS = {
    "zheng-um": {
        "note": "Prof. Zhedong Zheng, University of Macau — uncertainty "
                "estimation, data-centric AI, and domain adaptation.",
        "interests": (
            "Visual-semantic generalization beyond the training distribution &middot; "
            "language-guided domain adaptation &middot; label-free adaptation of "
            "vision-language models &middot; compositional and generalized zero-shot "
            "recognition"),
        # Lead with the domain-adaptation and data-viewpoint work rather than
        # strict reverse chronology.
        "lead": ["imbuing-enrichment-calibration-ijcv",
                 "proximate-long-tail-czsl-aaai",
                 "imaginary-connected-embedding-tpami"],
    },

    "kong-um": {
        "note": "Prof. Shu Kong, University of Macau (Visual Intelligence Lab) — "
                "unseen-category recognition, few-shot and zero-shot learning, "
                "personalised visual intelligence.",
        # Lead with the established compositional recognition record, then name
        # the newer vision-language direction without making it sound like the
        # whole publication record is VLM work.
        "interests": (
            "Compositional and generalized zero-shot recognition &middot; "
            "visual-semantic representation learning &middot; recognition of "
            "unseen categories and compositions &middot; vision-language models"),
        "lead": ["instance-attribute-bottleneck-ijcv",
                 "proximate-long-tail-czsl-aaai",
                 "imaginary-connected-embedding-tpami"],
    },
}

SUMMARY = [
    """I study visual-semantic generalization beyond the training distribution, with a
    primary focus on compositional and generalized zero-shot recognition. My work examines
    how attributes, objects, compositions, and visual evidence should be related when test
    combinations are unseen. Recent work extends the same question to language-guided
    unseen-domain extension and label-free test-time adaptation of vision-language models.""",
]

EDUCATION = [
    ("2023 &ndash; 2027",
     "Ph.D. in Computer Science and Technology",
     "Nanjing University of Science and Technology",
     "Advisor: Prof. Haofeng Zhang. Direct master&rsquo;s-to-Ph.D. track; proposal "
     "defended December 2024, dissertation defence expected March 2027."),
    ("2021 &ndash; 2023",
     "M.Sc. in Pattern Recognition and Intelligent Systems",
     "Nanjing University of Science and Technology",
     "Transferred to the doctoral track in 2023."),
    ("2017 &ndash; 2021",
     "B.Sc. in Mathematics and Applied Mathematics",
     "Fuzhou University",
     "Admitted to NJUST through the national postgraduate recommendation scheme."),
]

GRANTS = [
    ("Jiangsu Provincial Graduate Research and Practice Innovation Program",
     "Principal investigator &middot; completed",
     "Transferable Feature-Semantic Embedding Methods for Zero-Shot Learning."),
    ("Multimodal diagnosis and prognosis for kidney transplantation",
     "Department of Kidney Transplantation, Zhongshan Hospital, Fudan University",
     "Responsible for the full model implementation, training and evaluation. The "
     "model fuses multi-stain gigapixel whole-slide images with longitudinal "
     "laboratory results and clinical records."),
]

AWARDS = [
    ("2025", "National Scholarship for Doctoral Students"),
    ("", "Outstanding Doctoral Candidate Program, NJUST &mdash; selected 2025, "
         "continued funding awarded in 2026"),
    ("", "First-Class Academic Scholarship, NJUST &mdash; awarded multiple times"),
]

SERVICE = ("Reviewer for <b>NeurIPS</b>, <b>ICML</b>, <b>ICLR</b>, <b>AAAI</b>, "
           "<i>Pattern Recognition</i>, and <i>IEEE Transactions on Circuits and "
           "Systems for Video Technology</i>.")

# Every line here has to survive one follow-up question in an interview, so it
# lists tools actually used in the repositories rather than method names lifted
# from paper titles. Those belong in the publication list, where they are
# attached to a paper that can be discussed.
SKILLS = [
    ("Deep learning",
     "PyTorch, torchvision, timm; training and evaluation pipelines on Linux GPU "
     "servers"),
    ("Vision-language",
     "CLIP: fine-tuning, prompt-based adaptation, and test-time adaptation"),
    ("Numerical", "NumPy, SciPy, scikit-learn, pandas"),
    ("Imaging",
     "OpenCV, Pillow, OpenSlide (gigapixel whole-slide images), einops, h5py"),
    ("Mathematics", "B.Sc. in mathematics; probability modeling and visual-semantic "
     "relation analysis"),
]


# --------------------------------------------------------------------------
# Reading the site data.
# --------------------------------------------------------------------------

def parse_front_matter(path):
    text = io.open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        km = re.match(r"^([a-z_]+)\s*:\s*(.*)$", line)
        if not km:
            continue
        key, val = km.group(1), km.group(2).strip()
        if val and val[0] in "'\"" and val[-1] == val[0]:
            val = val[1:-1]
        fm[key] = val
    return fm


def load_publications():
    pubs = []
    for f in glob.glob(os.path.join(PUB_DIR, "*.md")):
        fm = parse_front_matter(f)
        if not fm.get("title"):
            continue
        fm["_first"] = str(fm.get("first_author", "")).lower() == "true"
        fm["_date"] = fm.get("date", "1900-01-01")
        pubs.append(fm)
    pubs.sort(key=lambda p: p["_date"], reverse=True)
    return pubs


def load_under_review():
    """Minimal reader for the flat list in _data/under_review.yml."""
    items, cur = [], None
    for raw in io.open(UNDER_REVIEW, encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.strip().startswith("#") or not line.strip():
            continue
        if line.startswith("- "):
            if cur:
                items.append(cur)
            cur = {}
            line = "  " + line[2:]
        m = re.match(r"^\s+([a-z_]+)\s*:\s*(.*)$", line)
        if m and cur is not None:
            val = m.group(2).strip()
            if val and val[0] in "'\"" and val[-1] == val[0]:
                val = val[1:-1]
            cur[m.group(1)] = val
    if cur:
        items.append(cur)
    return items


# --------------------------------------------------------------------------
# Rendering.
# --------------------------------------------------------------------------

CSS = """
@page { size: A4; margin: 15mm 16mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: Georgia, Cambria, "Times New Roman", serif;
  font-size: 10.2pt; line-height: 1.5; color: #1a1a1a;
  margin: 0 auto; max-width: 195mm; padding: 14mm 10mm; background: #fff;
}
@media print { body { padding: 0; max-width: none; } }
a { color: #26455c; text-decoration: none; }
@media print { a { color: #1a1a1a; } }

header { border-bottom: 1.4pt solid #1a1a1a; padding-bottom: 8px; margin-bottom: 14px; }
h1 { font-size: 21pt; margin: 0 0 2px; letter-spacing: 0.3px; font-weight: normal; }
h1 .zh { font-size: 0.62em; color: #555; margin-left: 8px; }
.position { font-size: 9.6pt; color: #333; line-height: 1.45; margin-bottom: 5px; }
.contact { font-size: 9.2pt; color: #333; }
.contact span { margin-right: 14px; white-space: nowrap; }
.contact b { font-weight: normal; color: #777; }

h2 {
  font-family: Calibri, "Segoe UI", sans-serif;
  font-size: 9.6pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1.6px; color: #26455c;
  margin: 17px 0 6px; padding-bottom: 2px;
  border-bottom: 0.6pt solid #bbb;
  break-after: avoid; page-break-after: avoid;
}
section { break-inside: auto; }

p { margin: 0 0 7px; }
.summary { text-align: justify; }

.entry { margin-bottom: 8px; break-inside: avoid; page-break-inside: avoid; }
.entry-head { display: flex; justify-content: space-between; gap: 12px; align-items: baseline; }
.entry-title { font-weight: bold; }
.entry-when { font-size: 9.2pt; color: #666; white-space: nowrap; }
.entry-where { font-style: italic; color: #333; }
.entry-note { font-size: 9.4pt; color: #444; margin-top: 1px; }

ol.pubs { margin: 0; padding-left: 20px; }
ol.pubs li { margin-bottom: 6px; break-inside: avoid; page-break-inside: avoid; }
ol.pubs .links { font-size: 8.8pt; color: #666; }
ol.pubs .links a { color: #26455c; }
@media print { ol.pubs .links a { color: #444; } }

.subhead {
  font-family: Calibri, "Segoe UI", sans-serif;
  font-size: 9.2pt; font-weight: 700; color: #333;
  margin: 9px 0 4px; letter-spacing: 0.4px;
  break-after: avoid; page-break-after: avoid;
}

table.skills { width: 100%; border-collapse: collapse; }
table.skills td { padding: 2px 0; vertical-align: top; }
/* Sized for the longest label in bold, plus a gutter so it cannot run up
   against the value column. Check this if a longer label is added. */
table.skills td.k { width: 140px; padding-right: 14px; font-weight: bold; white-space: nowrap; }

ul.awards { margin: 0; padding-left: 18px; }
ul.awards li { margin-bottom: 3px; break-inside: avoid; }
ul.awards .yr { color: #666; font-size: 9.2pt; }

footer { margin-top: 16px; font-size: 8.8pt; color: #777; text-align: right; }
"""


def render(target=None):
    cfg = TARGETS.get(target, {}) if target else {}
    if target and not cfg:
        raise SystemExit("unknown target %r; known: %s"
                         % (target, ", ".join(sorted(TARGETS))))

    pubs = load_publications()
    first = [p for p in pubs if p["_first"]]
    co = [p for p in pubs if not p["_first"]]
    ur = load_under_review()

    interests = cfg.get("interests", INTERESTS)

    # Promote the named papers to the front, keeping the rest in date order.
    lead = cfg.get("lead", [])
    if lead:
        def rank(p):
            for i, slug in enumerate(lead):
                if slug in p.get("permalink", ""):
                    return i
            return len(lead)
        first = sorted(first, key=rank)

    def pub_items(lst):
        out = []
        for p in lst:
            links = []
            if p.get("paperurl"):
                links.append('<a href="%s">paper</a>' % p["paperurl"])
            if p.get("codeurl"):
                links.append('<a href="%s">code</a>' % p["codeurl"])
            tail = (' <span class="links">[%s]</span>' % " &middot; ".join(links)) if links else ""
            out.append("<li>%s%s</li>" % (p.get("citation", p["title"]), tail))
        return "\n".join(out)

    contact = " ".join(
        '<span><b>%s</b> <a href="%s">%s</a></span>' % (k, url, v)
        for k, v, url in CONTACT)

    edu = "\n".join(
        '<div class="entry"><div class="entry-head">'
        '<span class="entry-title">%s</span><span class="entry-when">%s</span></div>'
        '<div class="entry-where">%s</div>'
        '<div class="entry-note">%s</div></div>' % (deg, when, where, note)
        for when, deg, where, note in EDUCATION)

    grants = "\n".join(
        '<div class="entry"><div class="entry-head">'
        '<span class="entry-title">%s</span></div>'
        '<div class="entry-where">%s</div>'
        '<div class="entry-note">%s</div></div>' % (t, role, note)
        for t, role, note in GRANTS)

    awards = "\n".join(
        '<li><span class="yr">%s</span> &nbsp; %s</li>' % (yr, txt)
        for yr, txt in AWARDS)

    skills = "\n".join(
        '<tr><td class="k">%s</td><td>%s</td></tr>' % (k, v) for k, v in SKILLS)

    # The target venue is deliberately not printed, here or on the site. Several
    # of these are under double-blind review, and a CV circulates further than
    # the person it was sent to. `venue` stays in _data/under_review.yml for
    # reference; it is simply not rendered.
    def ur_line(i):
        who = "<b>Chenyi Jiang</b> et al. " if str(i.get("first_author", "")).lower() == "true" else ""
        return "<li>%s&ldquo;%s.&rdquo; <span class=\"links\">%s</span></li>" % (
            who, i["title"], i.get("status_en", "Under review"))

    ur_items = "\n".join(ur_line(i) for i in ur)

    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Curriculum Vitae &mdash; %(name)s</title>
<style>%(css)s</style>
</head>
<body>

<header>
  <h1>%(name)s <span class="zh">%(zh)s</span></h1>
  <div class="position">%(position)s</div>
  <div class="contact">%(contact)s</div>
</header>

<section>
  <h2>Research Interests</h2>
  <p>%(interests)s</p>
</section>

<section>
  <h2>Research Summary</h2>
  %(summary)s
</section>

<section>
  <h2>Education</h2>
  %(education)s
</section>

<section>
  <h2>Publications</h2>
  <p style="font-size:9.4pt;color:#444;margin-bottom:6px;">
    %(n_total)d peer-reviewed papers, %(n_first)d as first author
    (4 in CCF-A venues: IEEE TPAMI, IJCV &times;2, AAAI);
    %(n_ur)d further papers under review.
  </p>

  <div class="subhead">First author</div>
  <ol class="pubs">%(first)s</ol>

  <div class="subhead">Co-authored</div>
  <ol class="pubs">%(co)s</ol>

  <div class="subhead">Under review</div>
  <ol class="pubs">%(ur)s</ol>
</section>

<section>
  <h2>Grants and Projects</h2>
  %(grants)s
</section>

<section>
  <h2>Awards and Honours</h2>
  <ul class="awards">%(awards)s</ul>
</section>

<section>
  <h2>Academic Service</h2>
  <p>%(service)s</p>
</section>

<section>
  <h2>Technical Skills</h2>
  <table class="skills">%(skills)s</table>
</section>

<footer>References available on request &middot; last updated %(updated)s</footer>

</body>
</html>
""" % dict(
        name=NAME_EN, zh=NAME_ZH, css=CSS, position=POSITION, contact=contact,
        interests=interests,
        summary="\n  ".join('<p class="summary">%s</p>' % re.sub(r"\s+", " ", p).strip()
                            for p in SUMMARY),
        education=edu,
        n_total=len(pubs), n_first=len(first), n_ur=len(ur),
        first=pub_items(first), co=pub_items(co), ur=ur_items,
        grants=grants, awards=awards, service=SERVICE, skills=skills,
        updated=datetime.date.today().strftime("%B %Y"),
    )

    out = OUT if not target else OUT.replace(".html", "-%s.html" % target)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8").write(html)
    print("wrote %s" % out)
    print("  %d publications (%d first-author, %d co-authored), %d under review"
          % (len(pubs), len(first), len(co), len(ur)))
    if cfg:
        print("  target : %s" % cfg["note"])
        print("  leading: %s" % ", ".join(cfg.get("lead", [])))
    return out


CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
]


def to_pdf(html_path, pdf_path):
    """Print the CV through headless Chrome.

    Done here rather than by hand because the browser's print dialog defaults to
    stamping the file path and today's date into the page margins, which looks
    careless on a CV and is easy to forget to turn off. --no-pdf-header-footer
    settles it once.
    """
    import subprocess
    exe = next((p for p in CHROME if os.path.exists(p)), None)
    if not exe:
        print("  no Chrome or Edge found; open the HTML and print to PDF by hand")
        return False
    url = "file:///" + html_path.replace("\\", "/")
    output_dir = os.path.dirname(os.path.abspath(pdf_path))
    os.makedirs(output_dir, exist_ok=True)
    # Render to a sibling temporary file so a failed browser run cannot make a
    # stale PDF look newly generated or leave a half-written final file.
    fd, temp_pdf = tempfile.mkstemp(prefix=".cv-", suffix=".pdf", dir=output_dir)
    os.close(fd)
    try:
        result = subprocess.run(
            [exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             "--print-to-pdf=" + temp_pdf, url],
            check=False, capture_output=True, text=True, timeout=120)
        if result.returncode == 0 and os.path.isfile(temp_pdf) and os.path.getsize(temp_pdf):
            os.replace(temp_pdf, pdf_path)
            print("  pdf    : %s (%.0f KB)" % (pdf_path, os.path.getsize(pdf_path) / 1024))
            return True
        detail = " ".join((result.stderr or "").splitlines()[-2:]).strip()
        print("  pdf    : failed (Chrome exit %d)%s" %
              (result.returncode, ": " + detail if detail else ""))
        return False
    except (OSError, subprocess.TimeoutExpired) as exc:
        print("  pdf    : failed (%s)" % exc)
        return False
    finally:
        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)


if __name__ == "__main__":
    import sys
    tgt = None
    if "--target" in sys.argv:
        tgt = sys.argv[sys.argv.index("--target") + 1]
    html = render(tgt)
    if "--pdf" in sys.argv:
        # The filename a recruiter or PI sees in their inbox.
        pdf = os.path.join(os.path.dirname(html), "CV-江宸逸-南京理工大学.pdf")
        if tgt:
            pdf = pdf.replace(".pdf", "-%s.pdf" % tgt)
        to_pdf(html, pdf)
