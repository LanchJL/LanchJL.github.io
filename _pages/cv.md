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

Research profile
======

I study **visual-semantic generalization beyond the training distribution**, with a
primary focus on compositional and generalized zero-shot recognition. My work examines
how attributes, objects, compositions, and visual evidence should be related when test
combinations are unseen. Recent work extends the same question to language-guided
unseen-domain extension and label-free test-time adaptation of vision-language models.

Education
======

* **Ph.D., Computer Science and Technology**, 2023 -- 2027
  Nanjing University of Science and Technology &middot; Advisor: Prof. Haofeng Zhang
  Direct master's-to-Ph.D. track; proposal defended December 2024, dissertation
  defence expected March 2027.

* **M.Sc., Pattern Recognition and Intelligent Systems**, 2021 -- 2023
  Nanjing University of Science and Technology
  Transferred to the doctoral track in 2023.

* **B.Sc., Mathematics and Applied Mathematics**, 2017 -- 2021
  Fuzhou University &middot; admitted to NJUST by national postgraduate recommendation

Research interests
======

Compositional and generalized zero-shot recognition &middot; visual-semantic representation
learning &middot; language-guided domain adaptation and generalization &middot; vision-language
models &middot; test-time adaptation

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

Six first-author manuscripts are currently under review. Titles and venues are
withheld on this public CV during anonymous review; a private application CV can
include the full records when appropriate.

Grants and projects
======

* **Jiangsu Provincial Graduate Research and Practice Innovation Program** ---
  *Transferable Feature-Semantic Embedding Methods for Zero-Shot Learning*.
  Principal investigator; completed.

* **Multimodal diagnosis and prognosis for kidney transplantation** --- in collaboration
  with the **Department of Kidney Transplantation, Zhongshan Hospital, Fudan
  University**. **Responsible for the full model implementation, training and
  evaluation.** The model fuses multi-stain gigapixel whole-slide images with
  longitudinal laboratory results and clinical records.

Awards and honors
======

* **National Scholarship for Doctoral Students**, 2025
* **Outstanding Doctoral Candidate Program** (优秀博士培养对象), NJUST ---
  selected 2025; passed the 2026 review with continued funding
* **First-Class Academic Scholarship**, NJUST --- awarded multiple times

Academic service
======

Reviewer for **NeurIPS**, **ICML**, **ICLR**, **AAAI**, *Pattern Recognition*, and
*IEEE Transactions on Circuits and Systems for Video Technology*.

Technical skills
======

* **Deep learning** --- PyTorch, torchvision, timm; training and evaluation pipelines on
  Linux GPU servers
* **Vision-language models** --- CLIP; prompt-based adaptation and test-time adaptation
* **Scientific computing** --- NumPy, SciPy, scikit-learn, pandas
* **Image processing** --- OpenCV, Pillow, OpenSlide (gigapixel whole-slide pathology
  images), einops, h5py
* **Mathematics** --- B.Sc. in mathematics; probability modeling and visual-semantic
  relation analysis
