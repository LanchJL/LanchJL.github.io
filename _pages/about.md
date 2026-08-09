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

I work on generalization to what a model has never seen --- zero-shot and compositional
recognition, and more recently the test-time adaptation of vision-language models.
**14 peer-reviewed papers, 6 as first author**, including *IEEE TPAMI*, two in *IJCV*,
*AAAI*, *IJCAI* and two in *Pattern Recognition*; six further papers are under review.

Reach me at [jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn), or read the
[CV](/cv/).

Education
======

* **2023 – 2027** (expected) &middot; Ph.D., Computer Science and Technology &middot;
  *Nanjing University of Science and Technology*
* **2021 – 2023** &middot; M.Sc., Pattern Recognition and Intelligent Systems &middot;
  *Nanjing University of Science and Technology*
* **2017 – 2021** &middot; B.Sc., Mathematics and Applied Mathematics &middot;
  *Fuzhou University*

Direct master's-to-Ph.D. track, advised by Prof. Haofeng Zhang. Admitted to NJUST by
national postgraduate recommendation.

Selected publications
======

First-author work. The [full list](/publications/) has all 14 papers and the six under
review.

{% assign firsts = site.publications | where: "first_author", true | sort: "date" | reverse %}
{% for p in firsts %}
- **{{ p.title }}**<br />
  <span class="pub-venue">{{ p.venue_short }}</span>{% if p.codeurl %} &middot; [code]({{ p.codeurl }}){% endif %}{% if p.paperurl %} &middot; [paper]({{ p.paperurl }}){% endif %}
{% endfor %}

Awards
======

* **National Scholarship for Doctoral Students**, 2025
* **Outstanding Doctoral Candidate Program**, NJUST --- selected 2025, passed the 2026
  review with continued funding
* **First-Class Academic Scholarship**, NJUST --- 2023, 2024, 2025
* **Jiangsu Provincial Graduate Research and Practice Innovation Program** --- principal
  investigator, completed

Research
======

My work keeps returning to one question: **what is a recognition model actually being
told to match, and is that target right?**

Zero-shot methods inherit a great deal of supervision without examining it --- one
attribute vector per class, an implicitly uniform prior over compositions, an equal
penalty for every wrong answer, distance measures that never speak to each other. Each
of these is an assumption, and each costs more generalization than model capacity does.
Most of my papers consist of locating one such assumption, showing what it costs, and
replacing it --- usually without adding parameters at inference time.

| | The assumption | What replaces it |
|---|---|---|
| **1** | One attribute vector describes every image of a class | Near-instance-level attributes, grounded in the regions they describe — *IJCV 2024* |
| **2** | Compositional bias is a defect of representation | It closely approximates a long-tailed distribution, correctable by a derivable class prior — *AAAI 2024* |
| **3** | A state and its object are independent axes | Complex space, where phase carries their dependency and primitives stay independent — *TPAMI 2025* |
| **4** | Every wrong composition is equally wrong | Affinity cliques, and one-to-many visual–semantic alignment — *Pattern Recognition 2026* |
| **5** | Language can carry features into an unseen domain untouched | Reverse the style mining, then calibrate what survives — *IJCV 2025* |

Pushed to its limit, this line arrives at **test time**, where there is no supervision
left to correct and the model has to construct its own. That is what I work on now: how
a pre-trained vision-language model should reorganize its own evidence --- unlabelled,
online, and without a second training pass --- when it meets a distribution nobody
prepared it for. See [Research](/research/) for the longer account.

News
======

* **2026** --- *Language-Guided Attribute Alignment for ZSDA* accepted to **ICRA 2026**.
* **2026** --- *Clique-Based Inter-Class Affinity for CZSL* accepted to **Pattern Recognition**.
* **2025** --- Awarded the **National Scholarship for Doctoral Students**.
* **2025** --- *Imbuing, Enrichment and Calibration* accepted to **IJCV**.
* **2025** --- *Imaginary-Connected Embedding in Complex Space* accepted to **IEEE TPAMI**.
* **2024** --- *ProLT* accepted to **AAAI**; *Evolutionary GZSL* accepted to **IJCAI**.
