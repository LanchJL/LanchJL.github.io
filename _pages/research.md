---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
nav: main
lang_alt: /zh/research/
---

Visual-semantic generalization beyond the training distribution
======

My research asks how visual models can generalize when the semantic combinations,
domains, or visual evidence at test time differ from those seen in training. The main
body of my work is compositional and generalized zero-shot recognition: transferring
knowledge from seen states and objects to unseen compositions, while learning
visual-semantic correspondences that reflect actual visual variation.

Across these settings, I study where a semantic decomposition fails to match visual
evidence: one attribute vector may be too coarse for a class, component deviations may
be imbalanced, composition priors may be skewed, or a hard one-to-one target may ignore
affinity between classes. The resulting methods use instance-aware attributes,
data-derived priors, component balancing, composition-aware geometry, and hierarchical
affinity constraints.

The methodological projects below have public code.

<nav class="research-map" aria-label="Research sections">
  <a href="#research-attributes"><span>01</span><strong>Attribute grounding</strong><small>IAB</small></a>
  <a href="#research-compositions"><span>02</span><strong>Compositional structure</strong><small>ProLT · MUST · IMAX · CIA</small></a>
  <a href="#research-domains"><span>03</span><strong>Unseen domains</strong><small>IMEC</small></a>
  <a href="#research-adaptation"><span>04</span><strong>Test-time adaptation</strong><small>Vision-language models</small></a>
  <a href="#research-applied"><span>05</span><strong>Applied multimodality</strong><small>Kidney pathology</small></a>
</nav>

<div id="research-attributes" class="research-anchor"></div>

I. Attribute-based zero-shot learning
------

Zero-shot learning transfers recognition from seen classes to unseen ones through a
shared semantic space --- in practice, a vector of attributes per class. Everything rests
on that vector being a faithful description of the images it stands for. It usually is
not.

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

<div id="research-compositions" class="research-anchor"></div>

II. Compositional zero-shot learning
------

Compositional zero-shot learning (CZSL) raises the stakes: a model sees *sliced apple*
and *ripe banana* during training and must recognize *sliced banana* at test time. The
naive assumption --- that a composition is the sum of its parts --- breaks down because a
state changes appearance depending on what it modifies. "Sliced" looks nothing alike on
an apple and on bread.

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

<div id="research-domains" class="research-anchor"></div>

III. Extending to unseen domains — IMEC, *IJCV 2025*
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
which semantic content is kept. The result narrows the gap between synthetic and real
target samples without treating language as a pixel-level substitute.

It is evaluated across **semantic segmentation, object detection and image
classification**, and improves the source domain as well as the target.
[Code](https://github.com/LanchJL/IMEC-ZSDE)

A co-authored paper at **ICRA 2026** addresses zero-shot domain adaptation through
language-guided attribute alignment and semantic consistency.

<div id="research-adaptation" class="research-anchor"></div>

IV. Test-time adaptation of vision-language models
------

A pre-trained vision-language model carries broad knowledge but no guarantee about the
distribution it will actually meet. My current work asks how such a model should
**reorganize its own evidence at test time** --- unlabelled, online, and without a second
training pass. A related line continues the compositional work of section II.

{{ site.data.under_review.count }} first-author papers on these questions are currently
under review: {{ site.data.under_review.vlm_tta }} on VLM-TTA and
{{ site.data.under_review.czsl }} on CZSL. Their titles are withheld on the public
[Publications](/publications/) page during anonymous review.

<div id="research-applied" class="research-anchor"></div>

V. Applied work — multimodal kidney transplant pathology
------

I contribute to a **multimodal diagnostic and prognostic model for kidney
transplantation**, in collaboration with the Department of Kidney Transplantation,
Zhongshan Hospital, Fudan University. I am responsible for the full model
implementation, training, and evaluation.

The model has to read across modalities that share almost nothing: gigapixel whole-slide
images in several stains, longitudinal laboratory results, and clinical records. Getting
them to inform a single prediction is a harder version of a problem I already work on ---
IMEC exists because language and pixels are not the same kind of thing, and a biopsy
slide and a creatinine trajectory are further apart still.

The data combine several sources of variation: multi-stain gigapixel whole-slide images,
longitudinal laboratory results, and clinical records. This work gives my methodological
questions a setting with class imbalance, long-tailed outcomes, and heterogeneous
annotations rather than a clean benchmark alone.
