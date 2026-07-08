<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

用于评估 Seedream 5.0 Pro 图像生成与编辑工作流的来源佐证指南、提示词模式与视觉示例。

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 介绍

官方发布材料将 Seedream 5.0 Pro 描述为面向可控视觉生产的图像生成与编辑模型。材料重点包括区域定向编辑、草图引导编辑、锚点定位、图层分离、材质与色彩控制、多参考图合成、电影感图像与多语文字渲染。

这个仓库是 **guide and prompt** 内容入口。它把有来源佐证的提示词模式和媒体示例集中在一起，让用户可以检查要测试什么，只复制来源材料中出现的提示词，并在可用时走向 EvoLink 转换路径。

在 EvoLink 试用模型入口: [打开 Seedream 5.0 Pro 的 EvoLink 路径](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**快速开始:** 本仓库不声称已验证 EvoLink Seedream 5.0 Pro 的首次 API 运行路径。在记录当前模型运行证据之前，请使用以下公开转换路径:

1. [打开 EvoLink 获取 Seedream 5.0 Pro 访问](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [获取你的 EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. 将官方 ModelArk 参考作为技术背景: [阅读 Seedream 5.0 Pro ModelArk 文档](https://docs.byteplus.com/en/docs/ModelArk/1541523).

运行状态: 官方材料将 `dola-seedream-5-0-pro-260628` 列为 Seedream 5.0 Pro 模型 ID，但本仓库尚未完成会消耗额度的 EvoLink API smoke test。不要把相邻图像模型示例视为 Seedream 5.0 Pro 已验证的首次运行证据。

<a id="news"></a>

## 📰 最新消息

- **2026-07-08:** 根据 Seedream 5.0 Pro 官方发布材料与媒体导出建立初始本地 scaffold。

<a id="menu"></a>

## 📑 目录

- [🍌 介绍](#introduction)
- [📰 最新消息](#news)
- [📑 目录](#menu)
- [🎛️ 受控编辑提示词模式](#controlled-editing-prompt-patterns)
  - [Case 1: 用区域框物体描述进行定向编辑](#case-1)
  - [Case 2: 在网格状场景中进行锚点位置编辑](#case-2)
  - [Case 3: 多参考图静物构图](#case-3)
- [🎬 视觉能力展示](#visual-capability-gallery)
- [🧩 模型备注](#model-notes)
- [🙏 致谢](#acknowledge)

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ 受控编辑提示词模式

以下案例不是编造示例。它们来自 `docs/source-notes.md` 摘要的 Seedream 5.0 Pro 官方来源材料，经复制或翻译而成。

<a id="case-1"></a>

### Case 1: [用区域框物体描述进行定向编辑](docs/source-notes.md#included-public-cases) (by [@官方](docs/source-notes.md))

![Region-box annotation example](assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.png)

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: 官方.

<a id="case-2"></a>

### Case 2: [在网格状场景中进行锚点位置编辑](docs/source-notes.md#included-public-cases) (by [@官方](docs/source-notes.md))

<table>
  <tr>
    <td width="50%" valign="top"><strong>之前</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>之后</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: 官方.

<a id="case-3"></a>

### Case 3: [多参考图静物构图](docs/source-notes.md#included-public-cases) (by [@官方](docs/source-notes.md))

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.png)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: 官方.

<a id="visual-capability-gallery"></a>

## 🎬 视觉能力展示

官方材料还包含草图引导编辑、图层分离、电影叙事图像与多语文字渲染的额外视觉样本。

<table>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">草图引导涂鸦</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/005-doodles.png" alt="Sketch-guided doodles example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">草图引导色块</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/006-color-block.png" alt="Sketch-guided color block example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">草图引导线条</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/007-lines.png" alt="Sketch-guided lines example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">简单草图控制</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/008-simple-sketches.png" alt="Simple sketch control example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">图层分离示例</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Layer separation example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">图层分离变体</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Layer separation variant"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">电影感网球玻璃碎裂</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Cinematic tennis glass shatter"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">电影感拳击动作</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Cinematic action boxing"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">阿拉伯语与英语文字渲染</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">韩语文字渲染</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 模型备注

| 领域 | 来源佐证备注 |
|---|---|
| 模型 ID | 官方材料列出 `dola-seedream-5-0-pro-260628`；在它成为首次运行证据之前，仍需要 EvoLink 运行验证。 |
| 输入图片 | 来源材料表示 Seedream 5.0 Pro 支持最多 10 张输入图片。 |
| 输出分辨率 | 来源材料表示 Pro 的公开定位不应宣称 4K；它描述的输出级别约为 <= 2.36M 像素与 > 2.36M 像素。 |
| 原生提示词语言 | Source material lists Arabic, English, Russian, Indonesian, Spanish, German, Turkish, Portuguese, Malay, Vietnamese, French, Japanese, Korean, Tagalog, and Thai. |
| Seedream 到 Seedance 路径 | 来源材料表示，在账号与审核条件下，Seedream 5.0 Pro/Lite 的输出可成为 Seedance 系列 image-to-video 工作流的可信输入。 |

<a id="acknowledge"></a>

## 🙏 致谢

本仓库由 2026-07-08 导出的 Seedream 5.0 Pro 官方发布材料建立。

- 公开来源备注: `docs/source-notes.md`
- 私有来源 URL：记录在本地审计证据中，不作为 README 公开链接暴露。
- 运行备注：本仓库审计尚未执行会消耗额度的 EvoLink API smoke test。
