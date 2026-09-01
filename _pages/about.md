---
permalink: /
title: "About me"
author_profile: true
nav: main
lang_alt: /zh/
redirect_from:
  - /about/
  - /about.html
---

I am a Ph.D. candidate in Computer Science and Technology at the **School of Computer
Science and Engineering, Nanjing University of Science and Technology (NJUST)**,
advised by **Prof. Haofeng Zhang**. I expect to defend in **March 2027**.

My research concerns **visual-semantic generalization beyond the training distribution**.
Most of my published work studies compositional and generalized zero-shot recognition:
how to recognize an unseen state-object combination from seen primitives, and how to
learn visual-semantic correspondences when their visual variation is uneven. I have
published **14 peer-reviewed papers, 6 as first author**. The record includes *IEEE TPAMI*,
two papers in *IJCV*, *AAAI*, *IJCAI*, and two papers in *Pattern Recognition*; six further
first-author papers are under review. More recently, I have extended this question to
language-guided unseen-domain extension and label-free test-time adaptation of
vision-language models.

### Research in one sentence

The recurring problem in my work is a mismatch between the semantic structure used for
learning and the visual evidence it is meant to explain. I address that mismatch at
several levels: within-class variation and local attributes (IAB), composition-induced
priors and component imbalance (ProLT and MUST), composition-dependent geometry and
inter-class affinity (IMAX and CIA), and calibrated language-guided transfer to an
unseen domain (IMEC). My current work carries this question into **label-free, online
test-time adaptation of vision-language models**.

### Three connected directions

- **Compositional and generalized zero-shot recognition.** IAB, ProLT, MUST, IMAX, and
  CIA study how attributes, objects, compositions, and visual evidence should be related
  when test combinations are unseen.
- **Generalization across domains.** IMEC uses language to extend a model to an unseen
  domain while preserving visual content; a co-authored ICRA paper studies language-guided
  attribute alignment for zero-shot domain adaptation.
- **Vision-language adaptation at test time.** Four of my six current first-author
  submissions study label-free adaptation after deployment; the other two continue the
  compositional recognition line.

Reach me at [jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn), or read the
[CV](/cv/) and [Research](/research/) pages. I expect to defend in 2027 and welcome
conversations about postdoctoral research in visual-semantic generalization,
compositional recognition, domain adaptation, and test-time adaptation.

Education
======

* **2023 – 2027** (expected) · Ph.D., Computer Science and Technology ·
  *Nanjing University of Science and Technology*
* **2021 – 2023** · M.Sc., Pattern Recognition and Intelligent Systems ·
  *Nanjing University of Science and Technology*
* **2017 – 2021** · B.Sc., Mathematics and Applied Mathematics ·
  *Fuzhou University*

Direct master's-to-Ph.D. track, advised by Prof. Haofeng Zhang. Admitted to NJUST by
national postgraduate recommendation.

Selected first-author publications
======

{% assign firsts = site.publications | where: "first_author", true | sort: "date" | reverse %}
{% for p in firsts %}
- **{{ p.title }}**<br />
  <span class="pub-venue">{{ p.venue_short }}</span>{% if p.codeurl %} · [code]({{ p.codeurl }}){% endif %}{% if p.paperurl %} · [paper]({{ p.paperurl }}){% endif %}
{% endfor %}

Awards and service
======

* **National Scholarship for Doctoral Students**, 2025
* **Outstanding Doctoral Candidate Program**, NJUST — selected in 2025 and retained
  funding after the 2026 review
* **First-Class Academic Scholarship**, NJUST — awarded multiple times
* Reviewer for **NeurIPS**, **ICML**, **ICLR**, **AAAI**, *Pattern Recognition*, and
  *IEEE Transactions on Circuits and Systems for Video Technology*

---
