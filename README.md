# lanchjl.github.io

Academic homepage of **Chenyi Jiang (江宸逸)**, Ph.D. candidate at Nanjing University
of Science and Technology.

Built on [AcademicPages](https://github.com/academicpages/academicpages.github.io)
(a Jekyll fork of Minimal Mistakes), with a plugin-free bilingual setup.

## Layout

| Path | Purpose |
|---|---|
| `_pages/*.md` | English pages, served at `/` |
| `_pages/zh-*.md` | Chinese pages, served at `/zh/` |
| `_publications/` | One file per paper; `first_author: true` drives the grouping |
| `_data/under_review.yml` | Papers under review / in preparation |
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

Open `/cv/` (or `/zh/cv/`) and use the browser's Print → Save as PDF. The print
stylesheet hides the navigation, sidebar and footer, and expands the content to the
full page width.
