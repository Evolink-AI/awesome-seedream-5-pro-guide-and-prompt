<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

用於評估 Seedream 5.0 Pro 影像生成與編輯工作流的來源佐證指南、提示詞模式與視覺範例。

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 介紹

官方發布材料將 Seedream 5.0 Pro 描述為面向可控視覺生產的影像生成與編輯模型。材料重點包括區域定向編輯、草圖引導編輯、錨點定位、圖層分離、材質與色彩控制、多參考圖合成、電影感影像與多語文字渲染。

這個倉庫是 **guide and prompt** 內容入口。它把有來源佐證的提示詞模式和媒體範例集中在一起，讓使用者可以檢查要測什麼，只複製來源材料中出現的提示詞，並在可用時走向 EvoLink 轉換路徑。

在 EvoLink 試用模型入口: [開啟 Seedream 5.0 Pro 的 EvoLink 路徑](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**快速開始:** 本倉庫不聲稱已驗證 EvoLink Seedream 5.0 Pro 的首次 API 執行路徑。在記錄當前模型執行證據之前，請使用以下公開轉換路徑:

1. [開啟 EvoLink 取得 Seedream 5.0 Pro 存取](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [取得你的 EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. 將官方 ModelArk 參考作為技術背景: [閱讀 Seedream 5.0 Pro ModelArk 文件](https://docs.byteplus.com/en/docs/ModelArk/1541523).

執行狀態: 官方材料將 `dola-seedream-5-0-pro-260628` 列為 Seedream 5.0 Pro 模型 ID，但本倉庫尚未完成會消耗額度的 EvoLink API smoke test。不要把相鄰影像模型範例視為 Seedream 5.0 Pro 已驗證的首次執行證據。

<a id="news"></a>

## 📰 最新消息

- **2026-07-08:** 根據 Seedream 5.0 Pro 官方發布材料與媒體匯出建立初始本地 scaffold。

<a id="menu"></a>

## 📑 目錄

- [🍌 介紹](#introduction)
- [📰 最新消息](#news)
- [📑 目錄](#menu)
- [🧭 互動式編輯分類](#interactive-editing-categories)
- [🎛️ 受控編輯提示詞模式](#controlled-editing-prompt-patterns)
  - [Case 1: 用區域框物件描述進行定向編輯](#case-1)
  - [Case 2: 在網格狀場景中進行錨點位置編輯](#case-2)
  - [Case 3: 多參考圖靜物構圖](#case-3)
- [🎬 視覺能力展示](#visual-capability-gallery)
- [🧩 模型備註](#model-notes)
- [🙏 致謝](#acknowledge)

<a id="interactive-editing-categories"></a>

## 🧭 互動式編輯分類

Seedream 5.0 Pro 官方材料把可控編輯拆成六類實用模式。先用這張表判斷應該給模型什麼控制訊號，再選擇下面的提示詞模式。

| 分類 | 使用者提供什麼 | 適合什麼場景 |
|---|---|---|
| 互動控制 | 選區、點、箭頭、標註框或座標，用來指向目標區域。 | 帶明確空間意圖的局部生成或局部修改。 |
| 草圖編輯 | 塗鴉、色塊、線條或簡單草圖，並配合自然語言指令。 | 把粗略視覺意圖轉成真實物件或細節。 |
| 錨點 / 位置編輯 | 網格狀或清晰排列場景中的文字錨點。 | 移動或重新定位指定物件，同時減少誤改非目標區域。 |
| 圖層分離 | 要求模型拆分前景、背景和元件的提示詞。 | 下游拖曳、縮放、重組和可重用素材工作流。 |
| 精準顏色與材質響應 | 十六進位 / 顏色代碼和材質描述。 | 產品變體、品牌色匹配和材質替換。 |
| 多圖融合編輯 | 多張參考圖，並給出統一布局、風格或材質指令。 | 把產品、風格、紋理或物件組合成一張連貫圖像。 |

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ 受控編輯提示詞模式


<a id="case-1"></a>

### Case 1: 用區域框物件描述進行定向編輯

<table>
  <tr>
    <td width="50%" valign="top"><img src="assets/media/003-arrows-annotation-boxes.gif" alt="Interaction arrows and annotation boxes"></td>
    <td width="50%" valign="top"><img src="assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" alt="Region-box annotation example"></td>
  </tr>
</table>

**Source mapping:** Prompt and media are paired in official section 3.1.1 (interaction control).

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: Official.

<a id="case-2"></a>

### Case 2: 在網格狀場景中進行錨點位置編輯

<table>
  <tr>
    <td width="50%" valign="top"><strong>之前</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>之後</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Source mapping:** Prompt and media are paired in official section 3.1.3 (anchor/position editing).

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: Official.

<a id="case-3"></a>

### Case 3: 多參考圖靜物構圖

**Source mapping:** Prompt comes from official section 3.1.6 (multi-image fusion). The media below is from official section 3.1.5 (precise color/material response), so it is marked as related different-case media, not a paired output.

![Related different-case material-response media](assets/media/014-Feishu-Docs-Image.gif)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: Official.

<a id="visual-capability-gallery"></a>

## 🎬 視覺能力展示

官方材料還包含草圖引導編輯、圖層分離、電影敘事影像與多語文字渲染的額外視覺樣本。

<table>
  <tr>
    <td width="50%" valign="top"><strong>草圖引導塗鴉</strong><br><img src="assets/media/005-doodles.gif" alt="Sketch-guided doodles example"></td>
    <td width="50%" valign="top"><strong>草圖引導色塊</strong><br><img src="assets/media/006-color-block.gif" alt="Sketch-guided color block example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>草圖引導線條</strong><br><img src="assets/media/007-lines.gif" alt="Sketch-guided lines example"></td>
    <td width="50%" valign="top"><strong>簡單草圖控制</strong><br><img src="assets/media/008-simple-sketches.gif" alt="Simple sketch control example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>圖層分離範例</strong><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Layer separation example"></td>
    <td width="50%" valign="top"><strong>圖層分離變體</strong><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Layer separation variant"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>電影感網球玻璃碎裂</strong><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Cinematic tennis glass shatter"></td>
    <td width="50%" valign="top"><strong>電影感拳擊動作</strong><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Cinematic action boxing"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>阿拉伯語與英語文字渲染</strong><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong>韓語文字渲染</strong><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 模型備註

| 領域 | 來源佐證備註 |
|---|---|
| 模型 ID | 官方材料列出 `dola-seedream-5-0-pro-260628`；在它成為首次執行證據之前，仍需要 EvoLink 執行驗證。 |
| 輸入圖片 | 來源材料表示 Seedream 5.0 Pro 支援最多 10 張輸入圖片。 |
| 輸出解析度 | 來源材料表示 Pro 的公開定位不應宣稱 4K；它描述的輸出級別約為 <= 2.36M 像素與 > 2.36M 像素。 |
| 原生提示詞語言 | Source material lists Arabic, English, Russian, Indonesian, Spanish, German, Turkish, Portuguese, Malay, Vietnamese, French, Japanese, Korean, Tagalog, and Thai. |
| Seedream 到 Seedance 路徑 | 來源材料表示，在帳號與審核條件下，Seedream 5.0 Pro/Lite 的輸出可成為 Seedance 系列 image-to-video 工作流的可信輸入。 |

<a id="acknowledge"></a>

## 🙏 致謝

本倉庫由 2026-07-08 匯出的 Seedream 5.0 Pro 官方發布材料建立。

- 私有來源 URL：記錄在本地審計證據中，不作為 README 公開連結暴露。
- 執行備註：本倉庫審計尚未執行會消耗額度的 EvoLink API smoke test。
