---
permalink: /zh/
title: "个人简介"
author_profile: true
nav: zh
lang_alt: /
---

我是**南京理工大学计算机科学与工程学院**计算机科学与技术专业博士研究生，
导师为**张浩峰教授**，预计 **2027 年**毕业。

欢迎通过 [jiangchenyi@njust.edu.cn](mailto:jiangchenyi@njust.edu.cn) 与我联系，
或查看我的[简历](/zh/cv/)。

研究方向
======

我的研究反复回到同一个问题：**模型到底被要求去拟合什么，而这个目标本身对吗？**

零样本方法沿用了大量未经审视的监督——
一个类别共用一个属性向量、组合之间隐含的均匀先验、
对每个错误答案施加同等惩罚、彼此从不交流的多个距离度量。
这些都是假设，而每一个的代价都比模型容量更大地限制了泛化。
我的多数论文做的是同一件事：
找出其中一个假设，指出它的代价，然后替换掉它——
而且通常**不在推理阶段增加任何参数**。

| | 被默认接受的假设 | 替换为 |
|---|---|---|
| **1** | 一个属性向量描述一个类的所有图像 | 近实例级属性，并锚定到它所描述的区域 —— *IJCV 2024* |
| **2** | 组合偏差是表征层面的缺陷 | 它高度接近长尾分布，可用可推导的类先验修正 —— *AAAI 2024* |
| **3** | 状态与物体是两个彼此独立的维度 | 复数空间：相位承载依赖，基元仍独立获取 —— *TPAMI 2025* |
| **4** | 所有错误组合都错得一样 | 亲和类群，以及视觉—语义的一对多对齐 —— *Pattern Recognition 2026* |
| **5** | 语言可以原封不动地把特征带进未见域 | 反转风格挖掘，再校准哪些语义得以留存 —— *IJCV 2025* |

这条线推到极限，就到了**测试阶段**——
那里已经没有监督可供修正，模型必须自己构造。
这正是我当前的工作：一个预训练视觉语言模型在遇到无人为它准备过的分布时，
如何在无标签、在线、且不进行第二次训练的前提下，重新组织自己的证据。

学术成果
======

已发表/录用同行评议论文 **14 篇，其中第一作者 6 篇**，
包括 *IEEE TPAMI*、*IJCV*（2 篇）、*AAAI*、*IJCAI* 与 *Pattern Recognition*（2 篇）；
另有 6 项成果在投。

完整列表见[论文](/zh/publications/)页面或
[Google Scholar](https://scholar.google.com/citations?user=R9ruXHMAAAAJ)。

近况
======

* **2026** —— *Language-Guided Attribute Alignment for ZSDA* 被 **ICRA 2026** 录用
* **2026** —— *Clique-Based Inter-Class Affinity for CZSL* 被 **Pattern Recognition** 录用
* **2025** —— 获**博士研究生国家奖学金**
* **2025** —— *Imbuing, Enrichment and Calibration* 被 **IJCV** 录用
* **2025** —— *Imaginary-Connected Embedding in Complex Space* 被 **IEEE TPAMI** 录用
* **2024** —— *ProLT* 被 **AAAI** 录用；*Evolutionary GZSL* 被 **IJCAI** 录用
