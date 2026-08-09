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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(ROOT, "_publications")
UNDER_REVIEW = os.path.join(ROOT, "_data", "under_review.yml")
OUT = os.path.join(os.path.dirname(ROOT), "resume", "CV-Chenyi-Jiang.html")

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

INTERESTS = ("Zero-shot and compositional learning &middot; "
             "test-time adaptation of vision-language models &middot; "
             "long-tailed and imbalanced recognition &middot; "
             "cross-domain generalization &middot; "
             "multimodal medical image analysis")

SUMMARY = """My research asks what a recognition model is actually being told to
match, and whether that target is right. Zero-shot methods inherit a great deal of
supervision without examining it &mdash; one attribute vector per class, an implicitly
uniform prior over compositions, an equal penalty for every wrong answer, distance
measures that never speak to each other. Each is an assumption, and each costs more
generalization than model capacity does. Most of my work locates one such assumption,
shows what it costs, and replaces it, usually without adding parameters at inference.
Pushed to its limit that line arrives at test time, where there is no supervision left
to correct and the model must construct its own &mdash; which is my current focus."""

EDUCATION = [
    ("2023 &ndash; 2027 (expected)",
     "Ph.D. in Computer Science and Technology",
     "Nanjing University of Science and Technology",
     "Advisor: Prof. Haofeng Zhang. Direct master&rsquo;s-to-Ph.D. track; "
     "dissertation proposal defended December 2024."),
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
    ("2025", "Outstanding Doctoral Candidate Program, NJUST &mdash; selected 2025, "
             "passed the 2026 review with continued funding"),
    ("2023&ndash;2025", "First-Class Academic Scholarship, NJUST (awarded every year "
                        "of the doctoral programme)"),
]

SERVICE = ("Reviewer for <b>NeurIPS</b>, <b>ICML</b>, <b>ICLR</b>, <b>AAAI</b>, "
           "<i>Pattern Recognition</i>, and <i>IEEE Transactions on Circuits and "
           "Systems for Video Technology</i>.")

SKILLS = [
    ("Deep learning",
     "PyTorch, torchvision, timm; multi-GPU training and experiment management on "
     "Linux GPU servers"),
    ("Vision-language",
     "CLIP / OpenCLIP; prompt-based adaptation, cache-based test-time adaptation, "
     "Bayesian online inference"),
    ("Scientific computing", "NumPy, SciPy, scikit-learn, pandas"),
    ("Imaging",
     "OpenCV, Pillow, OpenSlide (gigapixel whole-slide images), einops, h5py"),
    ("Mathematics",
     "B.Sc. in mathematics; the class-prior derivation in ProLT and the Bayesian "
     "formulation in the test-time adaptation work follow directly from it"),
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
table.skills td.k { width: 118px; font-weight: bold; white-space: nowrap; }

ul.awards { margin: 0; padding-left: 18px; }
ul.awards li { margin-bottom: 3px; break-inside: avoid; }
ul.awards .yr { color: #666; font-size: 9.2pt; }

footer { margin-top: 16px; font-size: 8.8pt; color: #777; text-align: right; }
"""


def render():
    pubs = load_publications()
    first = [p for p in pubs if p["_first"]]
    co = [p for p in pubs if not p["_first"]]
    ur = load_under_review()

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

    # Unlike the website, the CV names the target venue. The site withholds it
    # because publicising a submission to a double-blind venue during review is
    # a risk; a CV emailed to a specific person is not publicity.
    def ur_line(i):
        who = "<b>Chenyi Jiang</b> et al. " if str(i.get("first_author", "")).lower() == "true" else ""
        status = i.get("status_en", "Under review")
        venue = i.get("venue", "")
        tail = "%s, <i>%s</i>" % (status, venue) if venue else status
        return "<li>%s&ldquo;%s.&rdquo; <span class=\"links\">%s</span></li>" % (
            who, i["title"], tail)

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
  <p class="summary">%(summary)s</p>
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
        interests=INTERESTS, summary=SUMMARY, education=edu,
        n_total=len(pubs), n_first=len(first), n_ur=len(ur),
        first=pub_items(first), co=pub_items(co), ur=ur_items,
        grants=grants, awards=awards, service=SERVICE, skills=skills,
        updated=datetime.date.today().strftime("%B %Y"),
    )

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s" % OUT)
    print("  %d publications (%d first-author, %d co-authored), %d under review"
          % (len(pubs), len(first), len(co), len(ur)))


if __name__ == "__main__":
    render()
