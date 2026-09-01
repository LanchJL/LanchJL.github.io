# -*- coding: utf-8 -*-
"""生成中文学术简历（面向国内高校博士后申请）。

论文数据从 build_cv.py 复用，因此不会与英文版和网站脱节。
中文版与英文版的差别不只是语言：

  - 国内高校先扫刊物层次，所以每条论文标注「准确且最有利」的分级
    （CCF 优先，CCF 未收录或等级偏低时改用 JCR 分区与影响因子）；
  - 不写英文版那段研究陈述（那属于研究计划，不属于简历）；
  - 奖励荣誉与主持项目的位置提前。

教育背景、奖励等静态内容在本文件里另有一份中文的。改其中一处时记得
同步另一处——论文数据是共享的，这些不是。

    python scripts/build_cv_zh.py --pdf
"""
import io
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_cv import load_publications, load_under_review, to_pdf  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT = os.path.dirname(ROOT)
OUTPUT_DIR = PARENT if os.path.basename(PARENT).lower() == "resume" else os.path.join(PARENT, "resume")
OUT = os.path.join(OUTPUT_DIR, "CV-Chenyi-Jiang-zh.html")

# 每篇论文的分级标注。原则：取「准确且最有利」的那个体系。
#
# 中科院分区数据于 2026-08 从 LetPub 逐本核对（2025 年 3 月升级版）。
# 核对中有两处与直觉相反，不要凭印象改：
#
#   - IJCV 是计算机科学 2 区且非 TOP，所以两篇 IJCV 用 CCF-A 更有利；
#   - Pattern Recognition 与 ESWA 都是 1 区 TOP，远好于 CCF-B / 未收录。
#
# 影响因子一律不标：核对时各源数字互相矛盾（PR 出现 7.6 / 8.6 / 8.98
# 三个值），且 IF 每年更新，写错是可查的。分区本身已足够。
#
# 格式：slug -> (主标签, 补充说明)
TIER = {
    # CCF-A，其中仅 TPAMI 同时是中科院一区 TOP
    "imaginary-connected-embedding-tpami": ("CCF-A", "中科院一区 TOP"),
    "instance-attribute-bottleneck-ijcv": ("CCF-A", ""),
    "imbuing-enrichment-calibration-ijcv": ("CCF-A", ""),
    "proximate-long-tail-czsl-aaai": ("CCF-A", ""),
    "evolutionary-gzsl-ijcai": ("CCF-A", ""),
    # 中科院一区 TOP 强于 CCF-B / 未被 CCF 收录
    "mutual-balancing-czsl-pr": ("中科院一区", "TOP · CCF-B"),
    "clique-inter-class-affinity-czsl": ("中科院一区", "TOP · CCF-B"),
    "spatial-frequency-czsl-eswa": ("中科院一区", "TOP"),
    "text-vision-fusion-czsl": ("中科院一区", "TOP"),
    # 中科院分区偏低（TOMM 三区），CCF 更有利
    "contextual-interaction-adversarial-tomm": ("CCF-B", ""),
    "language-guided-attribute-alignment-icra": ("CCF-B", ""),
    "calibrate-prototypes-few-shot": ("JCR Q1", ""),
    # 留空：中文简历不必每篇都标，空着是中性的，标 CCF-C / 三区反而
    # 主动传达"低档"。两篇均为二作。
    "multi-domain-attribute-updater-gzsl": ("", ""),
    "same-tail-attribute-prototype-accv": ("", ""),
}

NAME = "江宸逸"
NAME_EN = "Chenyi Jiang"

POSITION = ("南京理工大学 计算机科学与工程学院　博士研究生（硕博连读）<br>"
            "导师：张浩峰 教授　·　预计 2027 年 3 月毕业")

CONTACT = [
    ("邮箱", "jiangchenyi@njust.edu.cn", "mailto:jiangchenyi@njust.edu.cn"),
    ("主页", "lanchjl.github.io", "https://lanchjl.github.io"),
    ("Scholar", "Google Scholar",
     "https://scholar.google.com/citations?user=R9ruXHMAAAAJ"),
    ("GitHub", "LanchJL", "https://github.com/LanchJL"),
]

INTERESTS = ("组合与广义零样本识别　·　视觉—语义表示学习　·　语言驱动的跨域适应与泛化　·　"
             "视觉语言模型　·　测试时自适应")

SUMMARY = ("我的研究关注训练分布之外的视觉—语义泛化，主体是组合与广义零样本识别。"
           "我研究在测试组合未见时，属性、物体、组合及其视觉证据应如何建立关系；近期进一步"
           "延伸到语言驱动的未见域扩展，以及无标签视觉语言模型的测试时自适应。")

EDUCATION = [
    ("2023 – 2027（预计）", "博士，计算机科学与技术",
     "南京理工大学 计算机科学与工程学院",
     "导师：张浩峰 教授。硕博连读；2024 年 12 月完成开题，预计 2027 年 3 月答辩。"),
    ("2021 – 2023", "硕士，模式识别与智能系统",
     "南京理工大学 计算机科学与工程学院", "2023 年转博。"),
    ("2017 – 2021", "学士，数学与应用数学", "福州大学",
     "获推荐免试资格保送南京理工大学。"),
]

PROJECTS = [
    ("江苏省研究生科研与实践创新计划", "主持，已结题",
     "零样本学习中的可迁移特征语义嵌入方法。"),
    ("肾移植多模态诊断与预后模型", "与复旦大学中山医院肾移植科合作",
     "负责全部模型代码实现与训练测试。模型融合多种染色的千兆像素全切片图像、"
     "纵向患者检验数据与临床信息记录。"),
]

AWARDS = [
    ("2025", "博士研究生<b>国家奖学金</b>"),
    ("", "<b>优秀博士培养对象</b>，南京理工大学"
         "——2025 年入选，2026 年获得继续资助"),
    ("", "<b>一等学业奖学金</b>，南京理工大学（多次获得）"),
]

SERVICE = ("担任 <b>NeurIPS</b>、<b>ICML</b>、<b>ICLR</b>、<b>AAAI</b>、"
           "<i>Pattern Recognition</i>、<i>IEEE TCSVT</i> 审稿人。")

SKILLS = [
    ("深度学习", "PyTorch、torchvision、timm；Linux GPU 服务器上的训练与评测流程"),
    ("视觉语言模型", "CLIP：微调、提示学习、测试时自适应"),
    ("数值计算", "NumPy、SciPy、scikit-learn、pandas"),
    ("图像处理", "OpenCV、Pillow、OpenSlide（千兆像素全切片图像）、einops、h5py"),
    ("数学基础", "数学本科出身；概率建模与视觉—语义关系分析"),
]

CSS = """
@page { size: A4; margin: 15mm 16mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Microsoft YaHei","PingFang SC","Source Han Sans SC","Noto Sans CJK SC",sans-serif;
  font-size: 10.2pt; line-height: 1.72; color: #1a1a1a;
  margin: 0 auto; max-width: 195mm; padding: 14mm 10mm; background: #fff;
}
@media print { body { padding: 0; max-width: none; } }
a { color: #26455c; text-decoration: none; }
@media print { a { color: #1a1a1a; } }

header { border-bottom: 1.4pt solid #1a1a1a; padding-bottom: 8px; margin-bottom: 13px; }
h1 { font-size: 20pt; margin: 0 0 3px; font-weight: 600; letter-spacing: 2px; }
h1 .en { font-size: 0.55em; font-weight: 400; color: #555; margin-left: 10px; letter-spacing: 0; }
.position { font-size: 9.6pt; color: #333; line-height: 1.5; margin-bottom: 4px; }
.contact { font-size: 9.2pt; color: #333; }
.contact span { margin-right: 14px; white-space: nowrap; }
.contact b { font-weight: 400; color: #888; }

h2 { font-size: 10.6pt; font-weight: 600; color: #26455c; letter-spacing: 1px;
     margin: 15px 0 6px; padding-left: 8px; border-left: 3pt solid #26455c;
     break-after: avoid; page-break-after: avoid; }
p { margin: 0 0 6px; }

.entry { margin-bottom: 7px; break-inside: avoid; page-break-inside: avoid; }
.entry-head { display: flex; justify-content: space-between; gap: 12px; align-items: baseline; }
.entry-title { font-weight: 600; }
.entry-when { font-size: 9.2pt; color: #666; white-space: nowrap; }
.entry-where { color: #444; font-size: 9.8pt; }
.entry-note { font-size: 9.4pt; color: #555; margin-top: 1px; }

ol.pubs { margin: 0; padding-left: 20px; }
ol.pubs li { margin-bottom: 5px; break-inside: avoid; page-break-inside: avoid; }
.tag { display: inline-block; font-size: 8.2pt; white-space: nowrap; font-weight: 600; color: #26455c;
       border: 0.6pt solid #26455c; border-radius: 2px; padding: 0 4px; margin-right: 5px; }
.tier-extra { font-size: 8.4pt; color: #777; margin-right: 5px; }
.links { font-size: 8.6pt; color: #666; }

.subhead { font-size: 9.6pt; font-weight: 600; color: #333; margin: 9px 0 4px;
           break-after: avoid; page-break-after: avoid; }
.stat { font-size: 9.6pt; color: #444; margin-bottom: 6px; }

table.skills { width: 100%; border-collapse: collapse; }
table.skills td { padding: 2px 0; vertical-align: top; }
table.skills td.k { width: 96px; padding-right: 12px; font-weight: 600; white-space: nowrap; }

ul.awards { margin: 0; padding-left: 18px; }
ul.awards li { margin-bottom: 3px; break-inside: avoid; }
ul.awards .yr { color: #666; font-size: 9.2pt; margin-right: 6px; }

footer { margin-top: 14px; padding-top: 5px; border-top: 0.5pt solid #ccc;
         font-size: 8.8pt; color: #777; text-align: right; }
"""

TPL = """<!doctype html>
<html lang="zh-Hans">
<head><meta charset="utf-8"><title>%(name)s - 简历</title><style>%(css)s</style></head>
<body>

<header>
  <h1>%(name)s <span class="en">%(name_en)s</span></h1>
  <div class="position">%(position)s</div>
  <div class="contact">%(contact)s</div>
</header>

<section><h2>研究方向</h2><p>%(interests)s</p></section>

<section><h2>研究概况</h2><p>%(summary)s</p></section>

<section><h2>教育背景</h2>%(education)s</section>

<section>
  <h2>论文发表</h2>
  <p class="stat">已发表 / 录用同行评议论文 <b>%(n_total)d 篇</b>，其中
  <b>第一作者 %(n_first)d 篇</b>（含 CCF-A 类 4 篇：IEEE TPAMI、IJCV &times;2、AAAI）；
  另有 <b>%(n_ur)d 篇一作在投</b>。</p>
  <div class="subhead">第一作者</div>
  <ol class="pubs">%(first)s</ol>
  <div class="subhead">合作论文</div>
  <ol class="pubs">%(co)s</ol>
  <div class="subhead">在投</div>
  <ol class="pubs">%(ur)s</ol>
</section>

<section><h2>科研项目</h2>%(projects)s</section>

<section><h2>奖励荣誉</h2><ul class="awards">%(awards)s</ul></section>

<section><h2>学术服务</h2><p>%(service)s</p></section>

<section><h2>技术能力</h2><table class="skills">%(skills)s</table></section>

<footer>%(name)s　·　更新于 %(updated)s</footer>
</body></html>
"""


def build():
    pubs = load_publications()
    first = [p for p in pubs if p["_first"]]
    co = [p for p in pubs if not p["_first"]]
    ur = load_under_review()

    def items(lst):
        out = []
        for p in lst:
            slug = p.get("permalink", "")
            tag = ""
            for key, (badge, extra) in TIER.items():
                if key in slug:
                    if badge:
                        tag = '<span class="tag">%s</span>' % badge
                    if extra:
                        tag += '<span class="tier-extra">%s</span>' % extra
                    break
            links = []
            if p.get("paperurl"):
                links.append('<a href="%s">论文</a>' % p["paperurl"])
            if p.get("codeurl"):
                links.append('<a href="%s">代码</a>' % p["codeurl"])
            tail = ""
            if links:
                tail = ' <span class="links">[%s]</span>' % " &middot; ".join(links)
            out.append("<li>%s%s%s</li>" % (tag, p.get("citation", p["title"]), tail))
        return "\n".join(out)

    # 在投不写投稿地：其中数篇处于双盲评审，而简历会被转发。
    ur_items = "\n".join(
        '<li><b>江宸逸</b> 等. %s <span class="links">在投</span></li>' % i["title"]
        for i in ur)

    contact = " ".join('<span><b>%s</b> <a href="%s">%s</a></span>' % (k, u, v)
                       for k, v, u in CONTACT)

    edu = "\n".join(
        '<div class="entry"><div class="entry-head">'
        '<span class="entry-title">%s</span><span class="entry-when">%s</span></div>'
        '<div class="entry-where">%s</div><div class="entry-note">%s</div></div>'
        % (deg, when, where, note) for when, deg, where, note in EDUCATION)

    proj = "\n".join(
        '<div class="entry"><div class="entry-head">'
        '<span class="entry-title">%s</span><span class="entry-when">%s</span></div>'
        '<div class="entry-note">%s</div></div>' % (t, role, note)
        for t, role, note in PROJECTS)

    awards = "\n".join('<li><span class="yr">%s</span>%s</li>' % (y, t)
                       for y, t in AWARDS)
    skills = "\n".join('<tr><td class="k">%s</td><td>%s</td></tr>' % (k, v)
                       for k, v in SKILLS)

    today = datetime.date.today()
    html = TPL % dict(
        name=NAME, name_en=NAME_EN, css=CSS, position=POSITION, contact=contact,
        interests=INTERESTS, summary=SUMMARY, education=edu,
        n_total=len(pubs), n_first=len(first), n_ur=len(ur),
        first=items(first), co=items(co), ur=ur_items,
        projects=proj, awards=awards, service=SERVICE, skills=skills,
        updated="%d 年 %d 月" % (today.year, today.month))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s" % OUT)
    print("  %d 篇（一作 %d，合作 %d），在投 %d 篇"
          % (len(pubs), len(first), len(co), len(ur)))
    return OUT


if __name__ == "__main__":
    path = build()
    if "--pdf" in sys.argv:
        pdf = os.path.join(os.path.dirname(path), "简历-江宸逸-南京理工大学.pdf")
        to_pdf(path, pdf)
