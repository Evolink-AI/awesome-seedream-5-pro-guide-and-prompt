<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink 橫幅"></a>

# Awesome Seedream 5.0 Pro 指南與 Prompt

用於評估 Seedream 5.0 Pro 圖像生成與編輯工作流的有來源支撐指南、prompt 模式和視覺化範例。

[![MIT 授權](assets/badges/license-mit.svg)](LICENSE)
[![在 EvoLink 使用](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![取得 API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 介紹

Seedream 5.0 Pro 在官方發布材料中被定位為可控的圖像生成與編輯模型。本指南把公開 README 對齊官方能力菜單：交互控制、草圖編輯、圖層編輯、錨點 / 位置編輯、圖層分離、多圖融合、效果樣例與多語言文字渲染。

**你可以用這個倉庫檢查有來源支撐的案例，只複製官方材料中實際出現的 prompt，並理解每個能力分類如何對應到可見 case。**

在 EvoLink 試用模型入口：[打開 EvoLink 上的 Seedream 5.0 Pro](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta)。

**快速開始:** 本倉庫不聲稱 EvoLink 上的 Seedream 5.0 Pro 首次 API 路徑已完成驗證。在 runtime 證據被記錄前，請使用公開模型入口、API key 控制台與官方技術參考。

1. [打開 Seedream 5.0 Pro 的 EvoLink 路徑](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link)。
2. [取得你的 EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)。
3. [閱讀官方 ModelArk 技術參考](https://docs.byteplus.com/en/docs/ModelArk/1541523)。

> [!NOTE]
> 來源政策：使用官方發布材料。私有 Lark/Feishu URL 只保留在本地審計證據中，不作為 README 的公開來源頁暴露。

<a id="news"></a>

## 📰 更新

- **July 8, 2026:** 根據官方菜單與官方修正後的 case 清單重新整理初版指南。

<a id="menu"></a>

## 📑 目錄

- [🍌 介紹](#introduction)
- [📰 更新](#news)
- [📑 目錄](#menu)
- [🎛️ 交互控制](#interaction-control)
  - [Case 1: 用於空間意圖的箭頭和標註框](#case-1)
  - [Case 2: 用於定向編輯的區域框物件描述](#case-2)
- [✏️ 草圖編輯](#sketch-editing)
  - [Case 3: 塗鴉引導的物件生成](#case-3)
  - [Case 4: 色塊引導的編輯](#case-4)
  - [Case 5: 線條引導的細節編輯](#case-5)
  - [Case 6: 從簡單草圖到精細圖像](#case-6)
- [🧱 圖層編輯](#layer-editing)
  - [Case 7: 海報文字與圖形圖層編輯：Avery Turns](#case-7)
  - [Case 8: 海報優惠圖層編輯：Happy Hour](#case-8)
  - [Case 9: 設計版式中的時尚圖像圖層編輯](#case-9)
  - [Case 10: 運動海報圖形圖層編輯](#case-10)
  - [Case 11: 海報元素編輯：Public Joy](#case-11)
  - [Case 12: 具備精確紋理回應的材質表面替換](#case-12)
- [📍 錨點 / 位置編輯](#anchor-position-editing)
  - [Case 13: 網格位置物件移動](#case-13)
- [🧩 圖層分離](#layer-separation)
  - [Case 14: 前景 / 人物圖層分離](#case-14)
- [🖼️ 多圖融合編輯](#multi-image-fusion-editing)
  - [Case 15: 七張參考圖輸入/輸出靜物構圖](#case-15)
- [🎬 視覺品質與敘事](#visual-quality-narrative)
  - [Case 16: 電影感網球玻璃碎裂](#case-16)
  - [Case 17: 電影感拳擊動作](#case-17)
  - [Case 18: 3D 動畫風格場景](#case-18)
  - [Case 19: 視覺概念藝術](#case-19)
  - [Case 20: 遊戲場景視覺](#case-20)
- [🌐 多語言文字渲染](#multilingual-text-rendering)
  - [Case 21: 阿拉伯語與英語歡迎牌](#case-21)
  - [Case 22: 韓語 24 小時營業標牌](#case-22)
  - [Case 23: 泰語清潔提示標牌](#case-23)
  - [Case 24: 法語創作海報](#case-24)
  - [Case 25: 俄語未來海報](#case-25)
- [🧩 模型備註](#model-notes)
- [🙏 致謝](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ 交互控制

使用框、點、箭頭、標註或座標來指定目標區域。

案例數量：**2**。

<a id="case-1"></a>

### Case 1: 用於空間意圖的箭頭和標註框

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif?v=20260709-camo" width="720" alt="用於空間意圖的箭頭和標註框">

> [!NOTE]
> 在編輯前使用箭頭、框和標註明確目標區域。

---

<a id="case-2"></a>

### Case 2: 用於定向編輯的區域框物件描述

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="用於定向編輯的區域框物件描述">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ 草圖編輯

使用塗鴉、色塊、線條或簡單草圖作為視覺引導。

案例數量：**4**。

<a id="case-3"></a>

### Case 3: 塗鴉引導的物件生成

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif?v=20260709-camo" width="720" alt="塗鴉引導的物件生成">

> [!NOTE]
> 使用鬆散塗鴉作為視覺控制訊號，讓模型渲染目標物件。

---

<a id="case-4"></a>

### Case 4: 色塊引導的編輯

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif?v=20260709-camo" width="720" alt="色塊引導的編輯">

> [!NOTE]
> 使用大塊色塊指定粗略構圖、顏色區域或物件位置。

---

<a id="case-5"></a>

### Case 5: 線條引導的細節編輯

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif?v=20260709-camo" width="720" alt="線條引導的細節編輯">

> [!NOTE]
> 當形狀邊界比長文字描述更重要時，使用簡單線條進行引導。

---

<a id="case-6"></a>

### Case 6: 從簡單草圖到精細圖像

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif?v=20260709-camo" width="720" alt="從簡單草圖到精細圖像">

> [!NOTE]
> 在保留草圖意圖的同時，把極簡草圖轉成更完整的渲染圖。

---

<a id="layer-editing"></a>

## 🧱 圖層編輯

在保留整體構圖的同時編輯海報、圖形、文字、材質或表面圖層。

案例數量：**6**。

<a id="case-7"></a>

### Case 7: 海報文字與圖形圖層編輯：Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" width="720" alt="海報文字與圖形圖層編輯：Avery Turns">

> [!NOTE]
> 在保留整體設計結構的同時編輯可見海報元素。

---

<a id="case-8"></a>

### Case 8: 海報優惠圖層編輯：Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif" width="720" alt="海報優惠圖層編輯：Happy Hour">

> [!NOTE]
> 無需重建整張海報即可修改促銷標識或圖形元素。

---

<a id="case-9"></a>

### Case 9: 設計版式中的時尚圖像圖層編輯

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" width="720" alt="設計版式中的時尚圖像圖層編輯">

> [!NOTE]
> 在已構成的視覺版式中調整分層主體。

---

<a id="case-10"></a>

### Case 10: 運動海報圖形圖層編輯

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif" width="720" alt="運動海報圖形圖層編輯">

> [!NOTE]
> 在保持文字排版和構圖對齊的同時編輯賽車海報圖形。

---

<a id="case-11"></a>

### Case 11: 海報元素編輯：Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif" width="720" alt="海報元素編輯：Public Joy">

> [!NOTE]
> 在保留原始設計語言的同時修改海報元素。

---

<a id="case-12"></a>

### Case 12: 具備精確紋理回應的材質表面替換

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif" width="720" alt="具備精確紋理回應的材質表面替換">

> [!NOTE]
> 在保持物件結構完整的同時替換材質和顏色目標。

---

<a id="anchor-position-editing"></a>

## 📍 錨點 / 位置編輯

使用網格式錨點或相對位置來精確移動特定目標。

案例數量：**1**。

<a id="case-13"></a>

### Case 13: 網格位置物件移動

<table>
<tr>
<td width="50%" valign="top">

**編輯前：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" width="420" alt="網格位置物件移動編輯前">

</td>
<td width="50%" valign="top">

**編輯後：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" width="420" alt="網格位置物件移動編輯後">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 圖層分離

分離前景、背景和可複用元件，以便後續編輯。

案例數量：**1**。

<a id="case-14"></a>

### Case 14: 前景 / 人物圖層分離

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" width="720" alt="前景 / 人物圖層分離">

> [!NOTE]
> 從海報式背景中分離前景主體，以便後續複用。

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ 多圖融合編輯

將多張參考圖融合成一個連貫構圖，並遵循單條指令完成編輯。

案例數量：**1**。

<a id="case-15"></a>

### Case 15: 七張參考圖輸入/輸出靜物構圖

<table>
<tr>
<td width="50%" valign="top">

**輸入：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" width="420" alt="七張參考圖靜物構圖輸入">

</td>
<td width="50%" valign="top">

**輸出：**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" width="420" alt="七張參考圖靜物構圖輸出">

</td>
</tr>
</table>

> [!NOTE]
> 將七張白底參考圖作為輸入組，並在同一個成對 case 中生成靜物攝影輸出。


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 視覺品質與敘事

按電影動作、3D / 動畫、概念藝術和遊戲場景輸出組織效果樣例。

案例數量：**5**。

<a id="case-16"></a>

### Case 16: 電影感網球玻璃碎裂

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="電影感網球玻璃碎裂">

> [!NOTE]
> 生成包含玻璃碎片、動作節奏和電影感光照的高動態場景。

---

<a id="case-17"></a>

### Case 17: 電影感拳擊動作

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="電影感拳擊動作">

> [!NOTE]
> 渲染具有更強運動感、衝擊感和場景縱深的動作場景。

---

<a id="case-18"></a>

### Case 18: 3D 動畫風格場景

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="3D 動畫風格場景">

> [!NOTE]
> 用於角色或娛樂視覺的風格化 3D / 動畫輸出。

---

<a id="case-19"></a>

### Case 19: 視覺概念藝術

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="視覺概念藝術">

> [!NOTE]
> 用於氛圍、視覺方向和情緒探索的概念藝術風格生成。

---

<a id="case-20"></a>

### Case 20: 遊戲場景視覺

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="遊戲場景視覺">

> [!NOTE]
> 用於環境、佈景或 key art 探索的遊戲化場景生成。

---

<a id="multilingual-text-rendering"></a>

## 🌐 多語言文字渲染

按渲染語言和本地文字使用場景組織多語言樣例。

案例數量：**5**。

<a id="case-21"></a>

### Case 21: 阿拉伯語與英語歡迎牌

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" width="720" alt="阿拉伯語與英語歡迎牌">

> [!NOTE]
> 在同一畫面中原生渲染阿拉伯語和英語文字。

---

<a id="case-22"></a>

### Case 22: 韓語 24 小時營業標牌

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" width="720" alt="韓語 24 小時營業標牌">

> [!NOTE]
> 面向本地化店面或標牌內容的韓語文字渲染。

---

<a id="case-23"></a>

### Case 23: 泰語清潔提示標牌

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="泰語清潔提示標牌">

> [!NOTE]
> 面向本地公共空間或活動視覺的泰語文字渲染。

---

<a id="case-24"></a>

### Case 24: 法語創作海報

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="法語創作海報">

> [!NOTE]
> 面向產品、時尚和活動資產的法語文字渲染。

---

<a id="case-25"></a>

### Case 25: 俄語未來海報

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" width="720" alt="俄語未來海報">

> [!NOTE]
> 為本地化視覺概念渲染字元結構清晰的俄語文字。

---

<a id="model-notes"></a>

## 🧩 模型備註

| 領域 | 有來源支撐的備註 |
|---|---|
| 模型 ID | 官方材料列出 `dola-seedream-5-0-pro-260628`；在它成為首次運行證據之前，仍需要 EvoLink runtime 驗證。 |
| 輸入圖像 | 官方材料說明 Seedream 5.0 Pro 最多支援 10 張輸入圖像。 |
| 輸出解析度 | 不要聲稱 Pro 支援 4K；來源材料描述的輸出檔位圍繞 `<= 2.36M` 像素和 `> 2.36M` 像素。 |
| 原生 prompt 語言 | 官方材料列出阿拉伯語、英語、俄語、印尼語、西班牙語、德語、土耳其語、葡萄牙語、馬來語、越南語、法語、日語、韓語、他加祿語和泰語。 |
| Seedream 到 Seedance 路徑 | 官方材料說明，在滿足帳號和審核條件時，Seedream 5.0 Pro/Lite 輸出可以成為 Seedance 系列圖生影片流程的可信輸入。 |

<a id="acknowledge"></a>

## 🙏 致謝

本倉庫基於 2026 年 7 月 8 日匯出的 Seedream 5.0 Pro 官方發布材料，以及官方對 case 清單的修正建立。

- 官方私有來源 URL 只保留在本地審計證據中。
- 只有官方材料提供 prompt 文本的地方才包含 prompt 程式碼區塊。
- 只有媒體的 case 保持為純媒體展示；不會編造缺失的 prompt。

*如果任何公開 case 邊界需要修正，請帶著具體來源證據提交 issue 或 patch。*
