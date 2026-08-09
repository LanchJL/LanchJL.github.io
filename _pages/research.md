---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
nav: main
lang_alt: /zh/research/
---

Questioning what the model is told
======

A recognition model trained on a fixed label set fails the moment the world offers
something outside it. The usual response is to give the model more --- more parameters,
more modules, more data. My work asks a cheaper question first: **is the supervision
itself correct?**

Zero-shot learning turns out to be full of inherited assumptions that nobody re-examines.
One attribute vector stands in for a whole class. Every composition is implicitly assumed
equally likely. Every wrong answer is punished the same amount. Attribute, object and
composition are measured on three scales that never meet. Each of these limits
generalization more than capacity does --- and each can be replaced, usually without
costing anything at inference time.

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

Prior CZSL work sits at one of two extremes: learn each primitive on its own
(*non-connected*), or bind them into a single dependent composition (*fully-connected*).
Humans do neither --- we adapt a primitive *in light of* what it is composed with. That
middle ground is hard to express in real space, where attribute, object and composition
end up as three independent measures with no dynamic link between them.

**IMAX** extends the CZSL distance metric into **complex space**, which unifies those
three measures in one scheme. The move that makes it work is **phase**: phase information
enters both training and inference as the metric of attribute-object dependency, while
the primitives themselves are still acquired independently --- so dependency and
independence stop being mutually exclusive. A visual-bias-based extraction module selects
attribute evidence conditioned on object prototypes. Evaluated on three benchmarks,
including open-world classification.
[Code](https://github.com/LanchJL/IMAX)

### Not every mistake is equally wrong — CIA, *Pattern Recognition 2026*

Existing CZSL objectives penalize every incorrect composition identically. Mistaking
*sliced banana* for *ripe banana* is scored exactly like mistaking it for *rusty car* ---
even though one of those errors is nearly right. Discarding that structure encourages
severe overfitting to seen classes and hides the genuine visual-semantic relationships a
model should be learning.

**CIA** supplies the missing hierarchy. Compositions are grouped into **affinity
cliques** built from both semantic and visual affinity, at multiple levels, and those
cliques drive a **one-to-many** alignment between visual and semantic features instead of
a single hard target. The emphasis shifts from direct classification to uncovering the
compositional structure itself. Evaluated on MIT-States, UT-Zappos and C-GQA in both
closed-world and open-world settings.
[Code](https://github.com/LanchJL/CIA-CZSL)

II. Extending to unseen domains — IMEC, *IJCV 2025*
------

Language lets a model reach domains it has never seen: describe the target in words, and
shift the training features accordingly. The catch is modal --- language and pixel-level
images are not the same kind of thing, so semantically guided augmentation pulls the
feature manifold away from where real target images actually live, and image content
collapses under the semantic guidance.

**IMEC** reverses the usual target-style mining so that semantic content survives the
transfer. Global semantics conditionally generate style vectors, which are *imbued* into
visual features; local semantics then supply minor perturbations that *enrich* those
vectors by dispersing them, since a real domain has internal variation a single
synthesized point cannot express; finally a dimensional activation strategy *calibrates*
which semantic content is kept. The result joins abstract semantic knowledge to concrete
image detail, narrowing the gap between synthetic and real target samples.

It is evaluated across **semantic segmentation, object detection and image
classification**, and improves the source domain as well as the target.
[Code](https://github.com/LanchJL/IMEC-ZSDE)

A companion paper (**ICRA 2026**) addresses the same task through language-guided
attribute alignment and semantic consistency.

III. Test-time adaptation of vision-language models
------

A pre-trained vision-language model carries broad knowledge but no guarantee about the
distribution it will actually meet. My current work asks how such a model should
**reorganize its own evidence at test time** --- unlabelled, online, and without a second
training pass. A related line returns to compositional zero-shot learning, treating an
object prior as evidence to be regulated rather than noise to be removed.

Six papers on these questions are currently under review; titles are listed under
[Publications](/publications/).

IV. Applied work — computational pathology
------

I work on **multimodal pathology analysis for kidney transplantation**, in collaboration
with the Department of Kidney Transplantation, Zhongshan Hospital, Fudan University,
where I am responsible for the full model implementation, training and evaluation on
gigapixel whole-slide images.

It is a useful reality check. Pathology presents the same structure my methodological
work addresses --- severe class imbalance, long-tailed lesion categories, annotations that
disagree across stains and centers --- but without the convenience of a clean benchmark.
