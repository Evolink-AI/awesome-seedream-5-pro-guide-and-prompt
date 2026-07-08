<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Source-backed guide, prompt patterns, and visual examples for evaluating Seedream 5.0 Pro image generation and editing workflows.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Introduction

Seedream 5.0 Pro is presented in official launch material as a controllable image generation and editing model. This guide keeps the public README aligned with the official capability menu: interaction control, sketch editing, layer editing, anchor positioning, layer separation, multi-image fusion, visual effect samples, and multilingual text rendering.

**Use this repository to inspect source-backed examples, copy only prompts that appear in the official material, and understand how each capability category maps to visible cases.**

Try the model entry point on EvoLink: [Open Seedream 5.0 Pro on EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Quick start:** This repository does not claim that an EvoLink Seedream 5.0 Pro first-run API route has been verified. Use the public model entry, API-key dashboard, and official technical reference until runtime evidence is recorded.

1. [Open the Seedream 5.0 Pro EvoLink path](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Get your EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [Read the official ModelArk technical reference](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> Source policy: official owner-provided launch material. Private Lark/Feishu URLs are retained only in local audit evidence and are not exposed as public README source pages.

<a id="news"></a>

## 📰 News

- **July 8, 2026:** Initial guide rebuilt around the official menu and owner-corrected case inventory.

<a id="menu"></a>

## 📑 Menu

- [🍌 Introduction](#introduction)
- [📰 News](#news)
- [📑 Menu](#menu)
- [🎛️ Interaction Control](#interaction-control)
  - [Case 1: Arrows and annotation boxes for spatial intent](#case-1)
  - [Case 2: Region-box object description for targeted editing](#case-2)
- [✏️ Sketch Editing](#sketch-editing)
  - [Case 3: Doodle-guided object generation](#case-3)
  - [Case 4: Color-block guided editing](#case-4)
  - [Case 5: Line-guided detail editing](#case-5)
  - [Case 6: Simple sketch to refined image](#case-6)
- [🧱 Layer Editing](#layer-editing)
  - [Case 7: Poster text and graphic layer edit: Avery Turns](#case-7)
  - [Case 8: Poster offer layer edit: Happy Hour](#case-8)
  - [Case 9: Fashion image layer edit inside a design layout](#case-9)
  - [Case 10: Sports poster graphic layer edit](#case-10)
  - [Case 11: Poster element edit: Public Joy](#case-11)
  - [Case 12: Material surface swap with precise texture response](#case-12)
- [📍 Anchor / Position Editing](#anchor-position-editing)
  - [Case 13: Grid-position object movement](#case-13)
- [🧩 Layer Separation](#layer-separation)
  - [Case 14: Foreground/person layer separation](#case-14)
  - [Case 15: Scene component layers for object reuse](#case-15)
  - [Case 16: Recombined layered scene output](#case-16)
- [🖼️ Multi-image Fusion Editing](#multi-image-fusion-editing)
  - [Case 17: Seven-reference still-life composition](#case-17)
- [🎬 Visual Quality & Narrative](#visual-quality-narrative)
  - [Case 18: Cinematic tennis glass shatter](#case-18)
  - [Case 19: Cinematic boxing action](#case-19)
  - [Case 20: 3D animation style scene](#case-20)
  - [Case 21: Visual concept art](#case-21)
  - [Case 22: Game scene visual](#case-22)
- [🌐 Multilingual Text Rendering](#multilingual-text-rendering)
  - [Case 23: Arabic and English welcome sign](#case-23)
  - [Case 24: Korean open-24-hours sign](#case-24)
  - [Case 25: Thai cleanliness sign](#case-25)
  - [Case 26: French creation poster](#case-26)
  - [Case 27: Russian future poster](#case-27)
- [🧩 Model Notes](#model-notes)
- [🙏 Acknowledge](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ Interaction Control

Use boxes, points, arrows, annotation marks, or coordinates to specify the target region.

Case count: **2**.

<a id="case-1"></a>

### Case 1: Arrows and annotation boxes for spatial intent

<img src="assets/media/003-arrows-annotation-boxes.gif" width="720" alt="Arrows and annotation boxes for spatial intent">

> [!NOTE]
> Use arrows, boxes, and annotations to make the target area explicit before editing.

---

<a id="case-2"></a>

### Case 2: Region-box object description for targeted editing

<img src="assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="Region-box object description for targeted editing">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ Sketch Editing

Use doodles, color blocks, lines, or simple sketches as visual guidance.

Case count: **4**.

<a id="case-3"></a>

### Case 3: Doodle-guided object generation

<img src="assets/media/005-doodles.gif" width="720" alt="Doodle-guided object generation">

> [!NOTE]
> Use loose doodles as the visual control signal and let the model render the intended object.

---

<a id="case-4"></a>

### Case 4: Color-block guided editing

<img src="assets/media/006-color-block.gif" width="720" alt="Color-block guided editing">

> [!NOTE]
> Use broad color blocks to specify rough composition, color zones, or object placement.

---

<a id="case-5"></a>

### Case 5: Line-guided detail editing

<img src="assets/media/007-lines.gif" width="720" alt="Line-guided detail editing">

> [!NOTE]
> Use simple line guidance when the shape boundary matters more than a long text description.

---

<a id="case-6"></a>

### Case 6: Simple sketch to refined image

<img src="assets/media/008-simple-sketches.gif" width="720" alt="Simple sketch to refined image">

> [!NOTE]
> Turn a minimal sketch into a more complete rendered image while preserving the sketch intent.

---

<a id="layer-editing"></a>

## 🧱 Layer Editing

Edit poster, graphic, text, material, or surface layers while preserving the broader composition.

Case count: **6**.

<a id="case-7"></a>

### Case 7: Poster text and graphic layer edit: Avery Turns

<img src="assets/media/009-Feishu-Docs-Image.gif" width="720" alt="Poster text and graphic layer edit: Avery Turns">

> [!NOTE]
> Edit visible poster elements while preserving the overall design structure.

---

<a id="case-8"></a>

### Case 8: Poster offer layer edit: Happy Hour

<img src="assets/media/010-Feishu-Docs-Image.gif" width="720" alt="Poster offer layer edit: Happy Hour">

> [!NOTE]
> Change a promotion badge or graphic element without rebuilding the whole poster.

---

<a id="case-9"></a>

### Case 9: Fashion image layer edit inside a design layout

<img src="assets/media/011-Feishu-Docs-Image.gif" width="720" alt="Fashion image layer edit inside a design layout">

> [!NOTE]
> Adjust a layered subject inside a composed visual layout.

---

<a id="case-10"></a>

### Case 10: Sports poster graphic layer edit

<img src="assets/media/012-Feishu-Docs-Image.gif" width="720" alt="Sports poster graphic layer edit">

> [!NOTE]
> Edit a racing poster graphic while keeping typography and composition aligned.

---

<a id="case-11"></a>

### Case 11: Poster element edit: Public Joy

<img src="assets/media/013-Feishu-Docs-Image.gif" width="720" alt="Poster element edit: Public Joy">

> [!NOTE]
> Modify poster elements while preserving the source design language.

---

<a id="case-12"></a>

### Case 12: Material surface swap with precise texture response

<img src="assets/media/014-Feishu-Docs-Image.gif" width="720" alt="Material surface swap with precise texture response">

> [!NOTE]
> Swap material and color targets while keeping the object structure intact.

---

<a id="anchor-position-editing"></a>

## 📍 Anchor / Position Editing

Use grid-like anchors or relative positions to move a specific target precisely.

Case count: **1**.

<a id="case-13"></a>

### Case 13: Grid-position object movement

<table>
<tr>
<td width="50%" valign="top">

**Before:**

<img src="assets/media/015-Feishu-Docs-Image.png" width="420" alt="Grid-position object movement before">

</td>
<td width="50%" valign="top">

**After:**

<img src="assets/media/016-Feishu-Docs-Image.png" width="420" alt="Grid-position object movement after">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 Layer Separation

Separate foreground, background, and reusable components for downstream editing.

Case count: **3**.

<a id="case-14"></a>

### Case 14: Foreground/person layer separation

<img src="assets/media/017-Feishu-Docs-Image.png" width="720" alt="Foreground/person layer separation">

> [!NOTE]
> Separate a foreground subject from a poster-like background for later reuse.

---

<a id="case-15"></a>

### Case 15: Scene component layers for object reuse

<img src="assets/media/018-Feishu-Docs-Image.png" width="720" alt="Scene component layers for object reuse">

> [!NOTE]
> Expose independently editable scene components for drag, scale, and recomposition workflows.

---

<a id="case-16"></a>

### Case 16: Recombined layered scene output

<img src="assets/media/019-Feishu-Docs-Image.png" width="720" alt="Recombined layered scene output">

> [!NOTE]
> Use separated assets to rebuild a coherent scene after component-level editing.

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ Multi-image Fusion Editing

Combine multiple reference images into one coherent composition under a single instruction.

Case count: **1**.

<a id="case-17"></a>

### Case 17: Seven-reference still-life composition

> [!NOTE]
> Official material provides the prompt for this case without a paired public output image in the export used for this repository.

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 Visual Quality & Narrative

Group the effect samples by cinematic action, 3D/animation, concept art, and game-scene output.

Case count: **5**.

<a id="case-18"></a>

### Case 18: Cinematic tennis glass shatter

<img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="Cinematic tennis glass shatter">

> [!NOTE]
> High-motion scene generation with glass fragments, action timing, and cinematic lighting.

---

<a id="case-19"></a>

### Case 19: Cinematic boxing action

<img src="assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="Cinematic boxing action">

> [!NOTE]
> Action-scene rendering with a stronger sense of motion, impact, and scene depth.

---

<a id="case-20"></a>

### Case 20: 3D animation style scene

<img src="assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="3D animation style scene">

> [!NOTE]
> Stylized 3D/animation output for character or entertainment visuals.

---

<a id="case-21"></a>

### Case 21: Visual concept art

<img src="assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="Visual concept art">

> [!NOTE]
> Concept-art style generation for atmosphere, visual direction, and mood exploration.

---

<a id="case-22"></a>

### Case 22: Game scene visual

<img src="assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="Game scene visual">

> [!NOTE]
> Game-like scene generation for environment, set, or key-art exploration.

---

<a id="multilingual-text-rendering"></a>

## 🌐 Multilingual Text Rendering

Group the multilingual samples by rendered language and local-text use case.

Case count: **5**.

<a id="case-23"></a>

### Case 23: Arabic and English welcome sign

<img src="assets/media/025-Welcome.png" width="720" alt="Arabic and English welcome sign">

> [!NOTE]
> Native multilingual rendering with Arabic and English text in the same visual.

---

<a id="case-24"></a>

### Case 24: Korean open-24-hours sign

<img src="assets/media/026-24-Open-24-hours.png" width="720" alt="Korean open-24-hours sign">

> [!NOTE]
> Korean text rendering for localized storefront or signage content.

---

<a id="case-25"></a>

### Case 25: Thai cleanliness sign

<img src="assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="Thai cleanliness sign">

> [!NOTE]
> Thai text rendering for local public-space or campaign visuals.

---

<a id="case-26"></a>

### Case 26: French creation poster

<img src="assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="French creation poster">

> [!NOTE]
> French text rendering for product, fashion, and campaign assets.

---

<a id="case-27"></a>

### Case 27: Russian future poster

<img src="assets/media/029-Future.png" width="720" alt="Russian future poster">

> [!NOTE]
> Russian text rendering with clear character structure for localized visual concepts.

---

<a id="model-notes"></a>

## 🧩 Model Notes

| Area | Source-backed note |
|---|---|
| Model ID | Official material lists `dola-seedream-5-0-pro-260628`; EvoLink runtime verification is still required before this becomes first-run evidence. |
| Input images | Official material says Seedream 5.0 Pro supports up to 10 input images. |
| Output resolution | Do not claim 4K for Pro; the source material describes output tiers around `<= 2.36M` pixels and `> 2.36M` pixels. |
| Native prompt languages | Official material lists Arabic, English, Russian, Indonesian, Spanish, German, Turkish, Portuguese, Malay, Vietnamese, French, Japanese, Korean, Tagalog, and Thai. |
| Seedream to Seedance path | Official material says Seedream 5.0 Pro/Lite outputs can become trusted inputs for Seedance-family image-to-video workflows, with account and moderation conditions. |

<a id="acknowledge"></a>

## 🙏 Acknowledge

This repository was created from official Seedream 5.0 Pro launch material exported on July 8, 2026 and from owner corrections about the case inventory.

- Official private source URLs are retained only in local audit evidence.
- Prompt blocks are included only where the official material provides prompt text.
- Media-only cases remain media-only; missing prompts are not invented.

*If any public case boundary needs correction, open an issue or send a patch with concrete source evidence.*
