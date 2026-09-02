# lanchjl.github.io

Academic homepage and CV source of **Chenyi Jiang (江宸逸)**, Ph.D. candidate at
Nanjing University of Science and Technology.

Built on [AcademicPages](https://github.com/academicpages/academicpages.github.io)
(a Jekyll fork of Minimal Mistakes), with a plugin-free bilingual setup.

This source was recovered from the public LanchJL/LanchJL.github.io repository and
is the source of truth for the homepage text, publication metadata, and standalone CV
builders. The surrounding resume/ directory contains exported PDFs and application
drafts.

## Layout

| Path | Purpose |
|---|---|
| `_pages/*.md` | English pages, served at `/` |
| `_pages/zh-*.md` | Chinese pages, served at `/zh/` |
| `_publications/` | One file per paper; `first_author: true` drives the grouping |
| `_data/under_review.yml` | Aggregate count of papers under review (titles kept private) |
| `_data/navigation.yml` | Two menus: `main` (English) and `zh` (Chinese) |
| `_sass/layout/_print.scss` | Print stylesheet — makes `/cv/` export as a clean PDF |

## Bilingual mechanism

GitHub Pages only allows whitelisted Jekyll plugins, so no i18n plugin is used.
Instead each page declares which menu it uses and where its translation lives:

```yaml
nav: zh            # which menu in _data/navigation.yml (defaults to `main`)
lang_alt: /cv/     # the counterpart page the language toggle links to
```

`_includes/masthead.html` reads both and renders the matching menu plus an EN / 中文
toggle.

## Local preview

Ruby is installed at `C:\Ruby33-x64` and is not on the system PATH, so use the wrapper:

```
serve.cmd
```

Then open <http://127.0.0.1:4000>.

`--incremental` is deliberately not used: incremental builds do not invalidate pages
when `_config.yml` changes, which silently serves a stale sidebar and navigation.

## Adding a paper

Create `_publications/YYYY-MM-DD-slug.md`:

```yaml
---
title: "Paper Title"
collection: publications
first_author: true
category: manuscripts      # or `conferences`
permalink: /publication/YYYY-MM-DD-slug
excerpt: 'One sentence on the contribution.'
date: YYYY-MM-DD
venue: 'Journal or Conference, volume'
paperurl: 'https://doi.org/...'
citation: '<b>Chenyi Jiang</b>, Co Author. (YYYY). &quot;Title.&quot; <i>Venue</i>.'
---
```

The publications page, the CV, and the counts on the About page all read from this
collection, so adding the file is the only step required.

## Exporting the CV as PDF

Two routes, for two audiences.

**From the site.** Open `/cv/` (or `/zh/cv/`) and use the browser's Print → Save as
PDF. The print stylesheet hides the navigation and sidebar and expands the content to
the full page width.

**The academic CV.** For postdoc applications, generate the standalone document:

```
python scripts/build_cv.py --pdf
```

It reads `_publications/` and the aggregate count in `_data/under_review.yml`, so it
cannot drift out of step with the site, writes `../resume/CV-Chenyi-Jiang.html`, and prints it through headless
Chrome to `../resume/CV-江宸逸-南京理工大学.pdf`.

The `--pdf` step exists because the browser print dialog stamps the file path and the
date into the page margins by default. That looks careless on a CV and is easy to
forget to switch off; `--no-pdf-header-footer` settles it. When this repository is
kept under the materials directory as resume/homepage, the generated files are
written to the parent resume/ directory automatically.

Add `--target <name>` for a per-application variant (see `TARGETS` in the script).

**The Chinese CV.** For applications to mainland institutions:

```
python scripts/build_cv_zh.py --pdf
```

It reuses the publication loading from `build_cv.py`, so the two languages cannot
disagree about the record. It is not a translation: mainland academic CVs are read for
venue tier, so each paper carries an explicit CCF label, and the research summary is
dropped (that belongs in the research plan, not the CV). Education, awards and skills
exist separately in each script — change one and change the other.

Neither CV nor the site exposes exact titles or target venues for papers under review.
Several are under double-blind review, and a CV gets forwarded further than the person
it was sent to. The public repository stores only the aggregate count; keep full records
in a private application-materials location.

Content with no home in the site data — education, awards, service, skills — is
declared at the top of `scripts/build_cv.py`.
