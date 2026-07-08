<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink 横幅"></a>

# Awesome Seedream 5.0 Pro 指南与 Prompt

用于评估 Seedream 5.0 Pro 图像生成与编辑工作流的有来源支撑指南、prompt 模式和可视化示例。

[![MIT 许可证](assets/badges/license-mit.svg)](LICENSE)
[![在 EvoLink 使用](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![获取 API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 介绍

Seedream 5.0 Pro 在官方发布材料中被定位为可控的图像生成与编辑模型。本指南把公开 README 对齐官方能力菜单：交互控制、草图编辑、图层编辑、锚点 / 位置编辑、图层分离、多图融合、效果样例与多语言文字渲染。

**你可以用这个仓库检查有来源支撑的案例，只复制官方材料中实际出现的 prompt，并理解每个能力分类如何对应到可见 case。**

在 EvoLink 试用模型入口：[打开 EvoLink 上的 Seedream 5.0 Pro](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta)。

**快速开始:** 本仓库不声称 EvoLink 上的 Seedream 5.0 Pro 首次 API 路径已完成验证。在 runtime 证据被记录前，请使用公开模型入口、API key 控制台与官方技术参考。

1. [打开 Seedream 5.0 Pro 的 EvoLink 路径](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link)。
2. [获取你的 EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)。
3. [阅读官方 ModelArk 技术参考](https://docs.byteplus.com/en/docs/ModelArk/1541523)。

> [!NOTE]
> 来源政策：使用官方发布材料。私有 Lark/Feishu URL 只保留在本地审计证据中，不作为 README 的公开来源页暴露。

<a id="news"></a>

## 📰 更新

- **July 8, 2026:** 根据官方菜单与官方修正后的 case 清单重新整理初版指南。

<a id="menu"></a>

## 📑 目录

- [🍌 介绍](#introduction)
- [📰 更新](#news)
- [📑 目录](#menu)
- [🎛️ 交互控制](#interaction-control)
  - [Case 1: 用于空间意图的箭头和标注框](#case-1)
  - [Case 2: 用于定向编辑的区域框对象描述](#case-2)
- [✏️ 草图编辑](#sketch-editing)
  - [Case 3: 涂鸦引导的对象生成](#case-3)
  - [Case 4: 色块引导的编辑](#case-4)
  - [Case 5: 线条引导的细节编辑](#case-5)
  - [Case 6: 从简单草图到精细图像](#case-6)
- [🧱 图层编辑](#layer-editing)
  - [Case 7: 海报文字与图形图层编辑：Avery Turns](#case-7)
  - [Case 8: 海报优惠图层编辑：Happy Hour](#case-8)
  - [Case 9: 设计版式中的时尚图像图层编辑](#case-9)
  - [Case 10: 运动海报图形图层编辑](#case-10)
  - [Case 11: 海报元素编辑：Public Joy](#case-11)
  - [Case 12: 具备精确纹理响应的材质表面替换](#case-12)
- [📍 锚点 / 位置编辑](#anchor-position-editing)
  - [Case 13: 网格位置对象移动](#case-13)
- [🧩 图层分离](#layer-separation)
  - [Case 14: 前景 / 人物图层分离](#case-14)
- [🖼️ 多图融合编辑](#multi-image-fusion-editing)
  - [Case 15: 七张参考图输入/输出静物构图](#case-15)
- [🎬 视觉质量与叙事](#visual-quality-narrative)
  - [Case 16: 电影感网球玻璃碎裂](#case-16)
  - [Case 17: 电影感拳击动作](#case-17)
  - [Case 18: 3D 动画风格场景](#case-18)
  - [Case 19: 视觉概念艺术](#case-19)
  - [Case 20: 游戏场景视觉](#case-20)
- [🌐 多语言文字渲染](#multilingual-text-rendering)
  - [Case 21: 阿拉伯语与英语欢迎牌](#case-21)
  - [Case 22: 韩语 24 小时营业标牌](#case-22)
  - [Case 23: 泰语清洁提示标牌](#case-23)
  - [Case 24: 法语创作海报](#case-24)
  - [Case 25: 俄语未来海报](#case-25)
- [🧩 模型备注](#model-notes)
- [🙏 致谢](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ 交互控制

使用框、点、箭头、标注或坐标来指定目标区域。

案例数量：**2**。

<a id="case-1"></a>

### Case 1: 用于空间意图的箭头和标注框

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif" width="720" alt="用于空间意图的箭头和标注框">

> [!NOTE]
> 在编辑前使用箭头、框和标注明确目标区域。

---

<a id="case-2"></a>

### Case 2: 用于定向编辑的区域框对象描述

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="用于定向编辑的区域框对象描述">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ 草图编辑

使用涂鸦、色块、线条或简单草图作为视觉引导。

案例数量：**4**。

<a id="case-3"></a>

### Case 3: 涂鸦引导的对象生成

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif" width="720" alt="涂鸦引导的对象生成">

> [!NOTE]
> 使用松散涂鸦作为视觉控制信号，让模型渲染目标对象。

---

<a id="case-4"></a>

### Case 4: 色块引导的编辑

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif" width="720" alt="色块引导的编辑">

> [!NOTE]
> 使用大块色块指定粗略构图、颜色区域或对象位置。

---

<a id="case-5"></a>

### Case 5: 线条引导的细节编辑

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif" width="720" alt="线条引导的细节编辑">

> [!NOTE]
> 当形状边界比长文本描述更重要时，使用简单线条进行引导。

---

<a id="case-6"></a>

### Case 6: 从简单草图到精细图像

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif" width="720" alt="从简单草图到精细图像">

> [!NOTE]
> 在保留草图意图的同时，把极简草图转成更完整的渲染图。

---

<a id="layer-editing"></a>

## 🧱 图层编辑

在保留整体构图的同时编辑海报、图形、文字、材质或表面图层。

案例数量：**6**。

<a id="case-7"></a>

### Case 7: 海报文字与图形图层编辑：Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" width="720" alt="海报文字与图形图层编辑：Avery Turns">

> [!NOTE]
> 在保留整体设计结构的同时编辑可见海报元素。

---

<a id="case-8"></a>

### Case 8: 海报优惠图层编辑：Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif" width="720" alt="海报优惠图层编辑：Happy Hour">

> [!NOTE]
> 无需重建整张海报即可修改促销标识或图形元素。

---

<a id="case-9"></a>

### Case 9: 设计版式中的时尚图像图层编辑

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" width="720" alt="设计版式中的时尚图像图层编辑">

> [!NOTE]
> 在已构成的视觉版式中调整分层主体。

---

<a id="case-10"></a>

### Case 10: 运动海报图形图层编辑

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif" width="720" alt="运动海报图形图层编辑">

> [!NOTE]
> 在保持文字排版和构图对齐的同时编辑赛车海报图形。

---

<a id="case-11"></a>

### Case 11: 海报元素编辑：Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif" width="720" alt="海报元素编辑：Public Joy">

> [!NOTE]
> 在保留原始设计语言的同时修改海报元素。

---

<a id="case-12"></a>

### Case 12: 具备精确纹理响应的材质表面替换

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif" width="720" alt="具备精确纹理响应的材质表面替换">

> [!NOTE]
> 在保持对象结构完整的同时替换材质和颜色目标。

---

<a id="anchor-position-editing"></a>

## 📍 锚点 / 位置编辑

使用网格式锚点或相对位置来精确移动特定目标。

案例数量：**1**。

<a id="case-13"></a>

### Case 13: 网格位置对象移动

<table>
<tr>
<td width="50%" valign="top">

**编辑前：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" width="420" alt="网格位置对象移动编辑前">

</td>
<td width="50%" valign="top">

**编辑后：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" width="420" alt="网格位置对象移动编辑后">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 图层分离

分离前景、背景和可复用组件，以便后续编辑。

案例数量：**1**。

<a id="case-14"></a>

### Case 14: 前景 / 人物图层分离

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" width="720" alt="前景 / 人物图层分离">

> [!NOTE]
> 从海报式背景中分离前景主体，以便后续复用。

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ 多图融合编辑

将多张参考图融合成一个连贯构图，并遵循单条指令完成编辑。

案例数量：**1**。

<a id="case-15"></a>

### Case 15: 七张参考图输入/输出静物构图

<table>
<tr>
<td width="50%" valign="top">

**输入：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" width="420" alt="七张参考图静物构图输入">

</td>
<td width="50%" valign="top">

**输出：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" width="420" alt="七张参考图静物构图输出">

</td>
</tr>
</table>

> [!NOTE]
> 将七张白底参考图作为输入组，并在同一个成对 case 中生成静物摄影输出。


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 视觉质量与叙事

按电影动作、3D / 动画、概念艺术和游戏场景输出组织效果样例。

案例数量：**5**。

<a id="case-16"></a>

### Case 16: 电影感网球玻璃碎裂

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="电影感网球玻璃碎裂">

> [!NOTE]
> 生成包含玻璃碎片、动作节奏和电影感光照的高动态场景。

---

<a id="case-17"></a>

### Case 17: 电影感拳击动作

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="电影感拳击动作">

> [!NOTE]
> 渲染具有更强运动感、冲击感和场景纵深的动作场景。

---

<a id="case-18"></a>

### Case 18: 3D 动画风格场景

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="3D 动画风格场景">

> [!NOTE]
> 用于角色或娱乐视觉的风格化 3D / 动画输出。

---

<a id="case-19"></a>

### Case 19: 视觉概念艺术

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="视觉概念艺术">

> [!NOTE]
> 用于氛围、视觉方向和情绪探索的概念艺术风格生成。

---

<a id="case-20"></a>

### Case 20: 游戏场景视觉

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="游戏场景视觉">

> [!NOTE]
> 用于环境、布景或 key art 探索的游戏化场景生成。

---

<a id="multilingual-text-rendering"></a>

## 🌐 多语言文字渲染

按渲染语言和本地文字使用场景组织多语言样例。

案例数量：**5**。

<a id="case-21"></a>

### Case 21: 阿拉伯语与英语欢迎牌

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" width="720" alt="阿拉伯语与英语欢迎牌">

> [!NOTE]
> 在同一画面中原生渲染阿拉伯语和英语文字。

---

<a id="case-22"></a>

### Case 22: 韩语 24 小时营业标牌

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" width="720" alt="韩语 24 小时营业标牌">

> [!NOTE]
> 面向本地化店面或标牌内容的韩语文字渲染。

---

<a id="case-23"></a>

### Case 23: 泰语清洁提示标牌

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="泰语清洁提示标牌">

> [!NOTE]
> 面向本地公共空间或活动视觉的泰语文字渲染。

---

<a id="case-24"></a>

### Case 24: 法语创作海报

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="法语创作海报">

> [!NOTE]
> 面向产品、时尚和活动资产的法语文字渲染。

---

<a id="case-25"></a>

### Case 25: 俄语未来海报

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" width="720" alt="俄语未来海报">

> [!NOTE]
> 为本地化视觉概念渲染字符结构清晰的俄语文字。

---

<a id="model-notes"></a>

## 🧩 模型备注

| 领域 | 有来源支撑的备注 |
|---|---|
| 模型 ID | 官方材料列出 `dola-seedream-5-0-pro-260628`；在它成为首次运行证据之前，仍需要 EvoLink runtime 验证。 |
| 输入图像 | 官方材料说明 Seedream 5.0 Pro 最多支持 10 张输入图像。 |
| 输出分辨率 | 不要声称 Pro 支持 4K；来源材料描述的输出档位围绕 `<= 2.36M` 像素和 `> 2.36M` 像素。 |
| 原生 prompt 语言 | 官方材料列出阿拉伯语、英语、俄语、印尼语、西班牙语、德语、土耳其语、葡萄牙语、马来语、越南语、法语、日语、韩语、他加禄语和泰语。 |
| Seedream 到 Seedance 路径 | 官方材料说明，在满足账号和审核条件时，Seedream 5.0 Pro/Lite 输出可以成为 Seedance 系列图生视频流程的可信输入。 |

<a id="acknowledge"></a>

## 🙏 致谢

本仓库基于 2026 年 7 月 8 日导出的 Seedream 5.0 Pro 官方发布材料，以及官方对 case 清单的修正创建。

- 官方私有来源 URL 只保留在本地审计证据中。
- 只有官方材料提供 prompt 文本的地方才包含 prompt 代码块。
- 只有媒体的 case 保持为纯媒体展示；不会编造缺失的 prompt。

*如果任何公开 case 边界需要修正，请带着具体来源证据提交 issue 或 patch。*
