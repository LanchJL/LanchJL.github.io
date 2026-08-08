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

**I am looking for postdoctoral positions starting in 2027.** If our interests overlap,
I would be glad to hear from you --- see my [CV](/cv/) or write to
[jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn).

Research
======

My work follows one trajectory: **from static semantic alignment to dynamic structural
reasoning.** The question underneath it is how a recognition model generalizes to
categories, compositions, and domains it never saw during training --- and, increasingly,
how it can keep correcting itself *at test time*, when the training distribution is
already behind it.

That trajectory has moved through five stages:

| | Problem | Contribution |
|---|---|---|
| **1** | Attributes are modelled at class level, erasing within-class variation | Near-instance-level attribute bottleneck — *IJCV 2024* |
| **2** | States and objects treated as independent axes | Imaginary-connected embedding in complex space — *TPAMI 2025* |
| **3** | Class relations ignored during transfer | Clique-based inter-class affinity — *Pattern Recognition 2026* |
| **4** | Unseen domains cause manifold divergence and semantic collapse | Imbuing–Enrichment–Calibration — *IJCV 2025* |
| **5** | Test-time evidence is noisy and unverified | Reliability-guided test-time adaptation for VLMs — *under review* |

Along the way, *ProLT* (**AAAI 2024**) made a different kind of argument: the visual bias
that compositional zero-shot learning suffers from is not only a representation defect
but closely approximates a **long-tailed distribution**, which makes it correctable by a
derivable class prior rather than by additional modules at inference.

My current focus is **test-time adaptation of vision-language models** --- how a
pre-trained VLM should reorganize its own evidence when it meets a distribution it was
never trained on, without labels and without a second training pass.

Publications
======

**14 peer-reviewed papers, 6 as first author**, including *IEEE TPAMI*, two in *IJCV*,
*AAAI*, *IJCAI* and two in *Pattern Recognition*. Five further papers are under review
or in preparation.

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
