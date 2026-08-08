---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
nav: main
lang_alt: /zh/cv/
---

{% include base_path %}

<p class="cv-print-hint no-print">
  <a href="javascript:window.print()">Print / Save as PDF</a>
  &middot; last updated {{ site.time | date: "%B %Y" }}
</p>

<div class="cv-header" markdown="1">

# Chenyi Jiang &nbsp;<span class="cv-name-zh">江宸逸</span>

Ph.D. candidate, School of Computer Science and Engineering
Nanjing University of Science and Technology, Nanjing, China

[jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn) &middot;
[Google Scholar](https://scholar.google.com/citations?user=R9ruXHMAAAAJ) &middot;
[GitHub](https://github.com/LanchJL) &middot;
[lanchjl.github.io](https://lanchjl.github.io)

</div>

Education
======

* **Ph.D., Computer Science and Technology**, 2023 -- 2027 (expected)
  Nanjing University of Science and Technology &middot; Advisor: Prof. Haofeng Zhang
  Direct master's-to-Ph.D. track; dissertation proposal defended December 2024.

* **M.Sc., Pattern Recognition and Intelligent Systems**, 2021 -- 2023
  Nanjing University of Science and Technology
  Transferred to the doctoral track in 2023.

* **B.Sc., Mathematics and Applied Mathematics**, 2017 -- 2021
  Fuzhou University &middot; admitted to NJUST by national postgraduate recommendation

Research interests
======

Zero-shot and compositional zero-shot learning &middot; test-time adaptation of
vision-language models &middot; long-tailed and imbalanced recognition &middot;
cross-domain generalization

Publications
======

14 peer-reviewed papers, 6 as first author (4 in CCF-A venues: TPAMI, IJCV ×2, AAAI).
Full list with links on the [Publications]({{ base_path }}/publications/) page.

**First author**

{% for post in site.publications reversed %}{% if post.first_author %}1. {{ post.citation }}
{% endif %}{% endfor %}

**Co-authored**

{% for post in site.publications reversed %}{% unless post.first_author %}1. {{ post.citation }}
{% endunless %}{% endfor %}

Under review / in preparation
======

{% for p in site.data.under_review %}1. {{ p.title }} --- *{{ p.status_en }}*
{% endfor %}

Grants and projects
======

* **Jiangsu Provincial Graduate Research and Practice Innovation Program** ---
  *Transferable Feature-Semantic Embedding Methods for Zero-Shot Learning*.
  Principal investigator; completed.

* **Multimodal pathology analysis for kidney transplantation** (collaboration with
  Fudan University). **Responsible for the full model implementation, training and
  evaluation** across the pipeline --- whole-slide segmentation and lesion
  classification on gigapixel images. An applied counterpart to my methodological
  work on imbalanced and long-tailed recognition.

Awards and honors
======

* **National Scholarship for Doctoral Students**, 2025
* **Outstanding Doctoral Candidate Program** (优秀博士培养对象), NJUST ---
  selected 2025; passed the 2026 review with continued funding
* **First-Class Academic Scholarship**, NJUST --- awarded every year since entering
  the doctoral program (2023, 2024, 2025)

Academic service
======

Reviewer for **NeurIPS**, **ICML**, **ICLR**, **AAAI**, *Pattern Recognition*, and
*IEEE Transactions on Circuits and Systems for Video Technology*.

Technical skills
======

* **Deep learning** --- PyTorch, torchvision, timm; multi-GPU training and experiment
  management on Linux GPU servers
* **Vision-language models** --- CLIP / OpenCLIP; prompt-based adaptation, cache-based
  test-time adaptation, Bayesian online inference
* **Scientific computing** --- NumPy, SciPy, scikit-learn, pandas
* **Image processing** --- OpenCV, Pillow, OpenSlide (gigapixel whole-slide pathology
  images), einops, h5py
* **Mathematics** --- B.Sc. in mathematics; the class-prior derivation in *ProLT* and
  the Bayesian formulation in my test-time adaptation work are direct products of that
  background
