---
permalink: /zh/
title: "个人简介"
author_profile: true
nav: zh
lang_alt: /
---

<div class="home-hero">
  <p class="home-hero__eyebrow">博士研究生 · 南京理工大学 · 预计 2027 年答辩</p>
  <h1>江宸逸 <span>Chenyi Jiang</span></h1>
  <p class="home-hero__lead">我研究当组合、域和视觉证据发生变化时，视觉模型如何保持泛化能力。</p>
  <div class="home-hero__actions">
    <a class="home-hero__button" href="/zh/research/">探索研究 <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
    <a class="home-hero__link" href="mailto:jiangchenyi@njust.edu.cn">联系交流 <i class="fas fa-arrow-up-right-from-square" aria-hidden="true"></i></a>
  </div>
  <dl class="home-stats">
    <div><dt>同行评议论文</dt><dd>14</dd></div>
    <div><dt>第一作者论文</dt><dd>6</dd></div>
    <div><dt>博士答辩</dt><dd>2027</dd></div>
  </dl>
</div>

我是**南京理工大学计算机科学与工程学院**计算机科学与技术专业博士研究生，导师为
**张浩峰教授**。我的发表工作围绕**训练分布之外的视觉—语义泛化**展开，另有 6 篇一作在投。

### 用一句话概括研究

我的工作反复处理同一个问题：**用于学习的语义结构，是否真正对应了需要解释的视觉证据**？
我分别从类内变化与局部属性（IAB）、组合诱导的先验与分量不平衡（ProLT、MUST）、
组合依赖的几何与类间亲和关系（IMAX、CIA），以及语言驱动未见域迁移中的内容校准（IMEC）
来处理这一问题。当前研究把它推进到**无标签、在线的视觉语言模型测试时自适应**。

### 三条相互连接的方向

- **组合与广义零样本识别。** IAB、ProLT、MUST、IMAX 与 CIA 研究在测试组合未见时，
  属性、物体、组合及其视觉证据应如何建立关系。
- **跨域泛化。** IMEC 用语言将模型扩展到未见域，同时尽量保留视觉内容；ICRA 合作论文
  进一步研究语言引导的属性对齐与零样本域适应。
- **视觉语言模型测试时自适应。** 目前 6 篇一作在投，其中 4 篇研究部署后的无标签适应，
  另外 2 篇延续组合识别方向。

欢迎通过 [jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn) 联系我，
或查看[简历](/zh/cv/)与[研究](/zh/research/)页面。
我预计 2027 年完成博士学业，欢迎围绕视觉—语义泛化、组合识别、跨域适应和测试时
自适应交流博士后研究机会。

教育背景
======

* **2023 – 2027**（预计）· 博士，计算机科学与技术 · *南京理工大学*
* **2021 – 2023** · 硕士，模式识别与智能系统 · *南京理工大学*
* **2017 – 2021** · 学士，数学与应用数学 · *福州大学*

硕博连读，导师张浩峰教授。本科获推荐免试资格保送南京理工大学。

代表性第一作者论文
======

{% assign firsts = site.publications | where: "first_author", true | sort: "date" | reverse %}
{% for p in firsts %}
- **{{ p.title }}**<br />
  <span class="pub-venue">{{ p.venue_short }}</span>{% if p.codeurl %} · [代码]({{ p.codeurl }}){% endif %}{% if p.paperurl %} · [论文]({{ p.paperurl }}){% endif %}
{% endfor %}

奖励与学术服务
======

* **博士研究生国家奖学金**，2025 年
* **优秀博士培养对象**，南京理工大学——2025 年入选，2026 年复审后继续资助
* **一等学业奖学金**，南京理工大学——多次获得
* 担任 **NeurIPS**、**ICML**、**ICLR**、**AAAI**、*Pattern Recognition*、
  *IEEE Transactions on Circuits and Systems for Video Technology* 审稿人

---
