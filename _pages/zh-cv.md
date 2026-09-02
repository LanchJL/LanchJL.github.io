---
layout: archive
title: "简历"
permalink: /zh/cv/
author_profile: true
nav: zh
lang_alt: /cv/
---

{% include base_path %}

<p class="cv-print-hint no-print">
  <a href="javascript:window.print()">打印 / 另存为 PDF</a>
  &middot; 更新于 {{ site.time | date: "%Y 年 %-m 月" }}
</p>

<div class="cv-header" markdown="1">

# 江宸逸 &nbsp;<span class="cv-name-zh">Chenyi Jiang</span>

南京理工大学 计算机科学与工程学院 博士研究生

[jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn) &middot;
[Google Scholar](https://scholar.google.com/citations?user=R9ruXHMAAAAJ) &middot;
[GitHub](https://github.com/LanchJL) &middot;
[lanchjl.github.io](https://lanchjl.github.io)

</div>

研究概况
======

我的研究关注**训练分布之外的视觉—语义泛化**，主体是组合与广义零样本识别。
我研究在测试组合未见时，属性、物体、组合及其视觉证据应如何建立关系；近期进一步
延伸到语言驱动的未见域扩展，以及无标签视觉语言模型的测试时自适应。

教育背景
======

* **博士，计算机科学与技术**，2023 -- 2027
  南京理工大学 计算机科学与工程学院 &middot; 导师：张浩峰 教授
  硕博连读；2024 年 12 月完成开题，预计 2027 年 3 月答辩。

* **硕士，模式识别与智能系统**，2021 -- 2023
  南京理工大学 计算机科学与工程学院 &middot; 2023 年转博

* **学士，数学与应用数学**，2017 -- 2021
  福州大学 &middot; 获推荐免试资格保送南京理工大学

研究方向
======

组合与广义零样本识别 &middot; 视觉—语义表示学习 &middot; 语言驱动的跨域适应与泛化 &middot;
视觉语言模型 &middot; 测试时自适应

论文发表
======

已发表/录用同行评议论文 14 篇，其中**第一作者 6 篇**
（CCF-A 类 4 篇：TPAMI、IJCV ×2、AAAI）。
完整列表见[论文]({{ base_path }}/zh/publications/)页面。

**第一作者**

{% for post in site.publications reversed %}{% if post.first_author %}1. {{ post.citation }}
{% endif %}{% endfor %}

**合作论文**

{% for post in site.publications reversed %}{% unless post.first_author %}1. {{ post.citation }}
{% endunless %}{% endfor %}

在投 / 待投稿
======

目前有 {{ site.data.under_review.count }} 篇第一作者稿件在审：其中
{{ site.data.under_review.vlm_tta }} 篇关于视觉语言模型测试时自适应（VLM-TTA），
{{ site.data.under_review.czsl }} 篇关于组合零样本学习（CZSL）。匿名评审期间，
公开版简历不展示题目与投稿地；在适当的私发申请材料中可以提供完整记录。

科研项目
======

* **江苏省研究生科研与实践创新计划**——
  *零样本学习中的可迁移特征语义嵌入方法*。主持，已结题。

* **肾移植多模态诊断与预后模型**（与**复旦大学中山医院肾移植科**合作）。
  **负责全部模型代码实现与训练测试**。
  模型融合多种染色的千兆像素全切片图像、纵向患者检验数据与临床信息记录。

奖励荣誉
======

* **博士研究生国家奖学金**，2025 年
* **优秀博士培养对象**，南京理工大学——2025 年入选，2026 年获得继续资助
* **一等学业奖学金**，南京理工大学——多次获得

学术服务
======

担任 **NeurIPS**、**ICML**、**ICLR**、**AAAI**、
*Pattern Recognition*、*IEEE TCSVT* 审稿人。

技术能力
======

* **深度学习**——PyTorch、torchvision、timm；Linux GPU 服务器上的训练与评估流程
* **视觉语言模型**——CLIP；提示学习与测试时自适应
* **科学计算**——NumPy、SciPy、scikit-learn、pandas
* **图像处理**——OpenCV、Pillow、OpenSlide（千兆像素全切片病理图像）、einops、h5py
* **数学基础**——数学本科出身；概率建模与视觉—语义关系分析
