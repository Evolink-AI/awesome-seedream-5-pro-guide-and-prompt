<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Source-backed guide, prompt patterns, and visual examples for evaluating Seedream 5.0 Pro image generation and editing workflows.

[License](LICENSE) · [Try Seedream 5 Pro on EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge) · [Get an EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key) · [Read BytePlus ModelArk docs](https://docs.byteplus.com/en/docs/ModelArk/1541523)

</div>

## 🍌 Introduction

Seedream 5.0 Pro is presented in official launch material as an image generation and editing model for controllable visual production. The source material emphasizes region-directed edits, sketch-guided edits, anchor positioning, layer separation, material and color control, multi-reference composition, cinematic imagery, and multilingual text rendering.

This repository is a **guide and prompt** surface. It keeps source-backed prompt patterns and media examples in one place so builders can inspect what to test, copy only the prompts that appear in the source material, and move toward an EvoLink conversion path when access is available.

Try the model entry point on EvoLink: [Open the Seedream 5.0 Pro EvoLink path](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

## ⚡ Quick Start

The current repository does not claim that an EvoLink Seedream 5.0 Pro first-run API route has been verified. Use this path as the public conversion route until current-model runtime evidence is recorded:

1. [Open EvoLink for Seedream 5.0 Pro access](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Get your EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. Treat the official ModelArk reference as technical background: [Read the Seedream 5.0 Pro ModelArk docs](https://docs.byteplus.com/en/docs/ModelArk/1541523).

Runtime status: the official material names `dola-seedream-5-0-pro-260628` as the Seedream 5.0 Pro model ID, but this repository has not completed a credit-consuming EvoLink API smoke test. Do not treat adjacent image-model examples as verified Seedream 5.0 Pro first-run evidence.

## 📰 News

- **2026-07-08:** Initial local scaffold created from official Seedream 5.0 Pro launch material and media export.

## 📑 Menu

- [🍌 Introduction](#-introduction)
- [⚡ Quick Start](#-quick-start)
- [📰 News](#-news)
- [📑 Menu](#-menu)
- [🎛️ Controlled Editing Prompt Patterns](#-controlled-editing-prompt-patterns)
  - [Case 1: Region-box object description for targeted editing](#case-1-region-box-object-description-for-targeted-editing)
  - [Case 2: Anchor-position edit on a grid-like scene](#case-2-anchor-position-edit-on-a-grid-like-scene)
  - [Case 3: Multi-reference still-life composition](#case-3-multi-reference-still-life-composition)
- [🎬 Visual Capability Gallery](#-visual-capability-gallery)
- [🧩 Model Notes](#-model-notes)
- [🙏 Acknowledge](#-acknowledge)

## 🎛️ Controlled Editing Prompt Patterns

The cases below are not invented examples. They are copied or translated from official Seedream 5.0 Pro source material summarized in `docs/source-notes.md`.

### Case 1: Region-box object description for targeted editing

![Region-box annotation example](assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.png)

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: 官方.

### Case 2: Anchor-position edit on a grid-like scene

| Before | After |
|---|---|
| ![Anchor positioning example before edit](assets/media/015-Feishu-Docs-Image.png) | ![Anchor positioning example after edit](assets/media/016-Feishu-Docs-Image.png) |

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: 官方.

### Case 3: Multi-reference still-life composition

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.png)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: 官方.

## 🎬 Visual Capability Gallery

### Sketch-guided editing

Use doodles, color blocks, lines, or simple sketches as control inputs, then combine them with natural-language instructions.

| Doodles | Color block | Lines | Simple sketches |
|---|---|---|---|
| ![Doodles](assets/media/005-doodles.png) | ![Color block](assets/media/006-color-block.png) | ![Lines](assets/media/007-lines.png) | ![Simple sketches](assets/media/008-simple-sketches.png) |

### Layer separation

The source material describes layer separation as outputting one background layer plus multiple element layers as PNG files with alpha channels.

| Layer example 1 | Layer example 2 | Layer example 3 |
|---|---|---|
| ![Layer separation example 1](assets/media/017-Feishu-Docs-Image.png) | ![Layer separation example 2](assets/media/018-Feishu-Docs-Image.png) | ![Layer separation example 3](assets/media/019-Feishu-Docs-Image.png) |

### Cinematic narrative images

| Tennis / glass shatter | Action / boxing | 3D animation | Visual concept | Game scene |
|---|---|---|---|---|
| ![Cinematic tennis glass shatter](assets/media/020-Cinematic-narrative-tennis-glass-shatter.png) | ![Cinematic action boxing](assets/media/021-Cinematic-narrative-action-boxing.png) | ![Cinematic 3D animation](assets/media/022-Cinematic-narrative-3D-animation.png) | ![Cinematic visual concept](assets/media/023-Cinematic-narrative-visual-concept.png) | ![Cinematic game scene](assets/media/024-Cinematic-narrative-game-scene.png) |

### Multilingual text rendering examples

The official material describes stronger native support for Arabic, English, Russian, Indonesian, Spanish, German, Turkish, Portuguese, Malay, Vietnamese, French, Japanese, Korean, Tagalog, and Thai prompts. The examples below are visual samples from the same source export.

| Arabic / English | Korean | Thai | French | Russian |
|---|---|---|---|---|
| ![Arabic welcome text](assets/media/025-Welcome.png) | ![Korean open 24 hours text](assets/media/026-24-Open-24-hours.png) | ![Thai clean-place notice](assets/media/027-Please-help-keep-the-place-clean-together.png) | ![French made in France text](assets/media/028-CREATION-FRANCAISE-Made-in-France.png) | ![Russian future text](assets/media/029-Future.png) |

## 🧩 Model Notes

| Area | Source-backed note |
|---|---|
| Model ID | Official material lists `dola-seedream-5-0-pro-260628`; EvoLink runtime verification is still required before this becomes first-run evidence. |
| Input images | Source material says Seedream 5.0 Pro supports up to 10 input images. |
| Output resolution | Source material says the public positioning should not claim 4K for Pro; it describes output tiers around <= 2.36M pixels and > 2.36M pixels. |
| Native prompt languages | Source material lists Arabic, English, Russian, Indonesian, Spanish, German, Turkish, Portuguese, Malay, Vietnamese, French, Japanese, Korean, Tagalog, and Thai. |
| Seedream to Seedance path | Source material says Seedream 5.0 Pro/Lite outputs can become trusted inputs for Seedance-family image-to-video workflows, with account and moderation conditions. |

## 🙏 Acknowledge

This repository was created from official Seedream 5.0 Pro launch material exported on 2026-07-08.

- Public provenance note: `docs/source-notes.md`
- Private source URL: recorded in local audit evidence, not exposed as a public README link.
- Runtime note: a credit-consuming EvoLink API smoke test has not been run in this repository audit.
