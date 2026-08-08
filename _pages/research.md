---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
nav: main
lang_alt: /zh/research/
---

From static semantic alignment to dynamic structural reasoning
======

A recognition model trained on a fixed label set fails the moment the world offers
something outside it. My work traces that failure from its most static form --- a
mismatch between an image and a hand-written attribute vector --- to its most dynamic
one, where the model must reorganize its own evidence at test time, on a distribution
nobody labelled.

I. Compositional zero-shot learning
------

In compositional zero-shot learning (CZSL), a model sees *sliced apple* and *ripe
banana* during training and must recognize *sliced banana* at test time. The naive
assumption --- that a composition is the sum of its parts --- breaks down because a state
changes appearance depending on what it modifies: "sliced" looks nothing alike on an
apple and on bread.

**Attribute granularity.** Class-level attribute vectors impose an information
bottleneck: every image of a class is fit to the same target, discarding within-class
variation, and the attributes carry no location information to match against local
image regions. *Estimation of Near-Instance-Level Attribute Bottleneck* (**IJCV 2024**,
with Philip H. S. Torr and Ling Shao) adapts both attribute vectors and visual features
during training so their correspondence reflects the actual image.

**Representation geometry.** *Imaginary-Connected Embedding in Complex Space*
(**TPAMI 2025**) places attribute--object pairs in complex space, where the imaginary
component encodes the coupling between a state and the object it modifies, rather than
treating primitive independence and primitive dependence as competing assumptions.

**Class structure.** *Clique-Based Inter-Class Affinity* (**Pattern Recognition 2026**)
models transfer at the level of class groups rather than isolated compositions.

**The distributional argument.** *ProLT* (**AAAI 2024**) makes a different kind of
claim: the visual bias CZSL suffers from is not only a representation defect. It
closely approximates a **long-tailed distribution** --- which turns CZSL into a class
imbalance problem with a derivable class prior, correcting predictions without adding
any module at inference time.

II. Test-time adaptation of vision-language models
------

A pre-trained vision-language model carries broad knowledge but no guarantee about the
distribution it will actually meet. My current work asks how such a model should
**reorganize its own evidence at test time** --- unlabelled, online, without a second
training pass.

*Imbuing, Enrichment and Calibration* (**IJCV 2025**) approaches the problem from the
domain side: when language is used to extend recognition into an unseen domain, the
feature manifold diverges and semantics collapse. IMEC injects a learnable offset at
semantic anchors, enriches it with directional perturbation to reflect within-domain
variation, and calibrates by dimension-wise activation selection --- preserving style
while correcting semantic drift.

Work currently under review extends this to the test stream itself: reliability-guided
projection onto topological anchors, Bayesian online inference over an adaptive cache,
semantic uncertainty regularization, and exclusionary distributions that suppress
confidently wrong candidates rather than merely boosting confident ones.

A related thread returns to CZSL with a sharper question: an object prior is not simply
noise to be removed. *Controlling Object-Induced Shortcuts* separates **object-existence
evidence** from **object-induced bias**, regulating the shortcut at the representation,
optimization, and inference levels while keeping the evidence intact.

Applied work
------

Alongside the methodological line, I work on a collaboration with Fudan University on
**multimodal pathology analysis for kidney transplantation**, where I am responsible
for the full model implementation, training and evaluation on gigapixel whole-slide
images. It is a useful reality check: pathology
data presents severe class imbalance and long-tailed lesion categories --- the same
structure my methodological work addresses, without the convenience of a clean
benchmark.
