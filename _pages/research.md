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
one, where a model must reorganize its own evidence at test time, on a distribution
nobody labelled.

Every project below has released code.

I. Compositional and zero-shot recognition
------

In compositional zero-shot learning (CZSL), a model sees *sliced apple* and *ripe
banana* during training and must recognize *sliced banana* at test time. The naive
assumption --- that a composition is the sum of its parts --- breaks down because a state
changes appearance depending on what it modifies: "sliced" looks nothing alike on an
apple and on bread.

### The granularity of attributes — IAB, *IJCV 2024*

Conventional zero-shot methods fit every image of a class to one class-level attribute
vector. That is an information bottleneck twice over: within-class variation is
discarded, and the attributes carry no location information, so they mismatch the local
regions they are supposed to describe.

**IAB** adapts both sides of the correspondence during training. *Near-Instance-Wise
Attribute Adaptation* (NAA) turns a single class attribute vector into several basis
vectors spanning a subspace closer to the individual sample, and *Vision Attribute
Relation Strengthening* (VARS) locates attribute-related regions in the feature map,
supplying the missing spatial grounding. Evaluated on four ZSL benchmarks under both ZSL
and the harder generalized (GZSL) setting.
[Code](https://github.com/LanchJL/IAB-GZSL) &middot;
[Paper](https://doi.org/10.1007/s11263-024-02021-x)

### Compositional bias is a distribution problem — ProLT, *AAAI 2024*

Prevailing methods disentangle states and objects directly from visual features. ProLT
takes a data-side view instead: experimentally, the visual bias produced by diverse
state-object interrelationships **closely approximates a long-tailed distribution**.

That reframes CZSL as a proximate class-imbalance problem. The paper derives the role of
the class prior mathematically and folds the composition-induced bias into both training
and inference as an estimated proximate prior, pushing the classifier toward more
discernible per-composition prototypes --- **without introducing additional parameters**.
[Code](https://github.com/LanchJL/ProLT) &middot;
[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28026)

### Balancing the two components — MUST, *Pattern Recognition 2024*

Manually labelled semantics and actual visual features diverge, and they diverge
*unevenly* across state classes and object classes --- an imbalance existing methods
ignore. **MUST** treats CZSL as unbalanced multi-label classification: it splits
composition classification into two consecutive stages to measure how entangled the two
components are, then uses that measurement to sharpen decision boundaries for the
classes suffering the largest visual deviation. It is a plug-in that improves several
CZSL frameworks on MIT-States, UT-Zappos and C-GQA.
[Code](https://github.com/LanchJL/MUST) &middot;
[Paper](https://doi.org/10.1016/j.patcog.2024.110451)

### The geometry of composition — IMAX, *IEEE TPAMI 2025*

CZSL metrics usually measure the state and the object independently. **IMAX** extends
the distance metric into **complex space**, which unifies those separate measures in one
scheme, and uses the imaginary component to carry the coupling between an attribute and
the object it modifies --- closer to how people understand an attribute as something that
only exists *on* something. A visual-bias-based extraction module selects attribute
evidence conditioned on object prototypes.
[Code](https://github.com/LanchJL/IMAX)

### Class structure rather than isolated compositions — CIA, *Pattern Recognition 2026*

Transfer in CZSL is usually modelled composition by composition. **CIA** models affinity
between *groups* of classes as cliques, so structure --- not just individual pairs ---
transfers to unseen combinations. Built on CLIP (ViT-L/14), evaluated including the
open-world setting.
[Code](https://github.com/LanchJL/CIA-CZSL)

II. Extending to unseen domains — IMEC, *IJCV 2025*
------

Zero-shot domain extension (ZSDE) asks a **semantic segmentation** model to work in a
target domain for which no labels, and no images, were available at training time ---
only a *description* of it in language. Building on prompt-driven domain adaptation, the
failure modes are specific: the synthesized feature manifold drifts away from the real
target domain, and semantics collapse as style is transferred.

**IMEC** answers with three stages. *Imbuing* injects a learnable offset at semantic
anchors so the feature layer can represent the target distribution at all. *Enrichment*
adds directional perturbation, because a real domain has internal variation that a single
synthesized point cannot express. *Calibration* selects dimension activations, keeping
the transferred style while pulling the semantics back. Trained on Cityscapes / GTA5 and
extended to adverse-condition targets such as ACDC.
[Code](https://github.com/LanchJL/IMEC-ZSDE)

A related line applies language-guided attribute alignment and semantic consistency to
zero-shot domain adaptation (**ICRA 2026**).

III. Test-time adaptation of vision-language models
------

A pre-trained vision-language model carries broad knowledge but no guarantee about the
distribution it will actually meet. My current work asks how such a model should
**reorganize its own evidence at test time** --- unlabelled, online, and without a second
training pass.

The threads I am pursuing: projecting predictions onto topological anchors under a
reliability constraint; Bayesian online inference over an adaptive cache, so that what
the model remembers from the test stream is itself filtered; regularizing semantic
uncertainty through a reliability graph; and building *exclusionary* distributions that
rule out confidently wrong candidates instead of merely reinforcing confident ones.

A related question returns to CZSL with a sharper framing: an object prior is not simply
noise to be removed. Separating **object-existence evidence** from **object-induced
bias** makes it possible to regulate the shortcut at the representation, optimization and
inference levels while keeping the evidence intact.

These papers are under review; see [Publications](/publications/).

IV. Applied work — computational pathology
------

I work on **multimodal pathology analysis for kidney transplantation**, in collaboration
with the Department of Kidney Transplantation, Zhongshan Hospital, Fudan University,
where I am responsible for the full model implementation, training and evaluation on
gigapixel whole-slide images.

It is a useful reality check. Pathology presents the same structure my methodological
work addresses --- severe class imbalance, long-tailed lesion categories, annotations that
disagree across stains and centers --- but without the convenience of a clean benchmark.
