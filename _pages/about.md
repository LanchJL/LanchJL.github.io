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

<div class="home-hero">
  <p class="home-hero__eyebrow">PH.D. CANDIDATE · NJUST · DEFENDING MARCH 2027</p>
  <h1>Chenyi Jiang <span>江宸逸</span></h1>
  <p class="home-hero__lead">I study how visual models keep their bearings when
  compositions, domains, and visual evidence change.</p>
  <div class="home-hero__actions">
    <a class="home-hero__button" href="/research/">Explore the research <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
    <a class="home-hero__link" href="mailto:jiangchenyi@njust.edu.cn">Start a conversation <i class="fas fa-arrow-up-right-from-square" aria-hidden="true"></i></a>
  </div>
  <dl class="home-stats">
    <div><dt>peer-reviewed papers</dt><dd>14</dd></div>
    <div><dt>first-author papers</dt><dd>6</dd></div>
    <div><dt>expected Ph.D. defense</dt><dd>2027</dd></div>
  </dl>
</div>

I am a Ph.D. candidate in Computer Science and Technology at the **School of Computer
Science and Engineering, Nanjing University of Science and Technology (NJUST)**,
advised by **Prof. Haofeng Zhang**. My published work centers on **visual-semantic
generalization beyond the training distribution**, with six further first-author papers
under review.

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
