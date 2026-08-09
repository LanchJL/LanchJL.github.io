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
advised by **Prof. Haofeng Zhang**. I expect to defend in **2027**.

You can reach me at [jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn),
or look through my [CV](/cv/).

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
prepared it for.

Publications
======

**14 peer-reviewed papers, 6 as first author**, including *IEEE TPAMI*, two in *IJCV*,
*AAAI*, *IJCAI* and two in *Pattern Recognition*. Six further papers are under review.

Full list on the [Publications](/publications/) page, or on
[Google Scholar](https://scholar.google.com/citations?user=R9ruXHMAAAAJ).

News
======

* **2026** --- *Language-Guided Attribute Alignment for ZSDA* accepted to **ICRA 2026**.
* **2026** --- *Clique-Based Inter-Class Affinity for CZSL* accepted to **Pattern Recognition**.
* **2025** --- Awarded the **National Scholarship for Doctoral Students**.
* **2025** --- *Imbuing, Enrichment and Calibration* accepted to **IJCV**.
* **2025** --- *Imaginary-Connected Embedding in Complex Space* accepted to **IEEE TPAMI**.
* **2024** --- *ProLT* accepted to **AAAI**; *Evolutionary GZSL* accepted to **IJCAI**.
