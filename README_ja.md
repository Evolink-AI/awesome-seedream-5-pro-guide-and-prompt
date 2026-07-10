<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink バナー"></a>

# Awesome Seedream 5.0 Pro ガイドとプロンプト

Seedream 5.0 Pro の画像生成・編集ワークフローを評価するための、出典に基づくガイド、プロンプトパターン、ビジュアル例です。

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![EvoLinkで使う](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![APIキーを取得](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 はじめに

Seedream 5.0 Pro は、公式ローンチ資料では制御可能な画像生成・編集モデルとして説明されています。このガイドは、インタラクション制御、スケッチ編集、レイヤー編集、アンカー位置編集、レイヤー分離、複数画像融合、効果サンプル、多言語テキスト描画という公式能力メニューに README を合わせます。

**このリポジトリでは、公式資料に基づく例を確認し、公式資料に存在する prompt だけをコピーし、各カテゴリがどの可視ケースに対応するかを把握できます。**

EvoLink のモデル入口を試す: [EvoLink で Seedream 5.0 Pro を開く](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**クイックスタート:** このリポジトリは、EvoLink 上の Seedream 5.0 Pro 初回実行 API ルートが検証済みだとは主張しません。runtime 証拠が記録されるまでは、公開モデル入口、API キーダッシュボード、公式技術リファレンスを使用してください。

1. [Seedream 5.0 Pro の EvoLink パスを開く](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API キーを取得する](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [公式 ModelArk 技術リファレンスを読む](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> ソース方針: 公式ローンチ資料を使用します。非公開 Lark/Feishu URL はローカル監査証拠にのみ保持し、README の公開ソースページとしては出しません。

<a id="news"></a>

## 📰 更新情報

- **2026年7月10日:** 公開ソース付きのコミュニティ事例を4件追加し、39件すべてのタイトルと要点をローカライズし、クリック再生できる動画ポスターを追加しました。
- **July 8, 2026:** 公式メニューと公式修正済みケース一覧に基づいて初期ガイドを再構成しました。

<a id="menu"></a>

## 📑 メニュー

- [🍌 はじめに](#introduction)
- [📰 更新情報](#news)
- [📑 メニュー](#menu)
- [🎛️ インタラクション制御](#interaction-control)
  - [Case 1: 空間意図を示す矢印と注釈ボックス](#case-1)
  - [Case 2: 対象編集のための領域ボックス別オブジェクト説明](#case-2)
- [✏️ スケッチ編集](#sketch-editing)
  - [Case 3: 落書きガイドによるオブジェクト生成](#case-3)
  - [Case 4: 色ブロックでガイドする編集](#case-4)
  - [Case 5: 線でガイドするディテール編集](#case-5)
  - [Case 6: 簡単なスケッチから洗練された画像へ](#case-6)
- [🧱 レイヤー編集](#layer-editing)
  - [Case 7: ポスターの文字・グラフィックレイヤー編集: Avery Turns](#case-7)
  - [Case 8: ポスターのオファーレイヤー編集: Happy Hour](#case-8)
  - [Case 9: デザインレイアウト内のファッション画像レイヤー編集](#case-9)
  - [Case 10: スポーツポスターのグラフィックレイヤー編集](#case-10)
  - [Case 11: ポスター要素の編集: Public Joy](#case-11)
  - [Case 12: 正確なテクスチャ応答による素材表面の置換](#case-12)
- [📍 アンカー / 位置編集](#anchor-position-editing)
  - [Case 13: グリッド位置に基づくオブジェクト移動](#case-13)
- [🧩 レイヤー分離](#layer-separation)
  - [Case 14: 前景 / 人物レイヤー分離](#case-14)
- [🖼️ 複数画像融合編集](#multi-image-fusion-editing)
  - [Case 15: 7枚参照の入力/出力静物構図](#case-15)
- [🎬 ビジュアル品質とナラティブ](#visual-quality-narrative)
  - [Case 16: ガラスが砕けるシネマティックなテニスシーン](#case-16)
  - [Case 17: シネマティックなボクシングアクション](#case-17)
  - [Case 18: 3Dアニメーション風シーン](#case-18)
  - [Case 19: ビジュアルコンセプトアート](#case-19)
  - [Case 20: ゲームシーンビジュアル](#case-20)
- [🌐 多言語テキスト描画](#multilingual-text-rendering)
  - [Case 21: アラビア語と英語のウェルカムサイン](#case-21)
  - [Case 22: 韓国語の24時間営業サイン](#case-22)
  - [Case 23: タイ語の清潔保持サイン](#case-23)
  - [Case 24: フランス語のクリエーションポスター](#case-24)
  - [Case 25: ロシア語の未来ポスター](#case-25)
- [🧾 公式機能ギャラリー](#official-capability-gallery)
- [🧪 コミュニティユースケース](#community-use-cases)
  - [編集と入力制御ワークフロー](#community-editing-control)
  - [プロダクト・UI・ポスターデザイン](#community-product-interface-design)
  - [技術図・構造化ビジュアル](#community-technical-structured-visuals)
  - [映画的・キャラクター・スタイル表現](#community-cinematic-character-visuals)
  - [コンセプトアート・環境・世界構築](#community-concept-environment-worldbuilding)
  - [モデル比較と評価](#community-model-comparisons)
- [🙏 謝辞](#acknowledge)

<a id="official-capability-gallery"></a>

## 🧾 公式機能ギャラリー

公式ギャラリーでは、オーナー提供のローンチ事例を基準となる機能リファレンスとしてまとめています。

<a id="interaction-control"></a>

## 🎛️ インタラクション制御

ボックス、点、矢印、注釈マーク、座標を使って対象領域を指定します。

ケース数: **2**.

<a id="case-1"></a>

### Case 1: 空間意図を示す矢印と注釈ボックス

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif?v=20260709-camo" height="420" alt="空間意図を示す矢印と注釈ボックス">

---

<a id="case-2"></a>

### Case 2: 対象編集のための領域ボックス別オブジェクト説明

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" height="420" alt="対象編集のための領域ボックス別オブジェクト説明">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ スケッチ編集

落書き、色ブロック、線、簡単なスケッチを視覚ガイドとして使います。

ケース数: **4**.

<a id="case-3"></a>

### Case 3: 落書きガイドによるオブジェクト生成

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif?v=20260709-camo" height="420" alt="落書きガイドによるオブジェクト生成">

---

<a id="case-4"></a>

### Case 4: 色ブロックでガイドする編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif?v=20260709-camo" height="420" alt="色ブロックでガイドする編集">

---

<a id="case-5"></a>

### Case 5: 線でガイドするディテール編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif?v=20260709-camo" height="420" alt="線でガイドするディテール編集">

---

<a id="case-6"></a>

### Case 6: 簡単なスケッチから洗練された画像へ

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif?v=20260709-camo" height="420" alt="簡単なスケッチから洗練された画像へ">

---

<a id="layer-editing"></a>

## 🧱 レイヤー編集

ポスター、グラフィック、文字、素材、表面のレイヤーを、全体構図を保ったまま編集します。

ケース数: **6**.

<a id="case-7"></a>

### Case 7: ポスターの文字・グラフィックレイヤー編集: Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" height="420" alt="ポスターの文字・グラフィックレイヤー編集: Avery Turns">

---

<a id="case-8"></a>

### Case 8: ポスターのオファーレイヤー編集: Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="ポスターのオファーレイヤー編集: Happy Hour">

---

<a id="case-9"></a>

### Case 9: デザインレイアウト内のファッション画像レイヤー編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" height="420" alt="デザインレイアウト内のファッション画像レイヤー編集">

---

<a id="case-10"></a>

### Case 10: スポーツポスターのグラフィックレイヤー編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="スポーツポスターのグラフィックレイヤー編集">

---

<a id="case-11"></a>

### Case 11: ポスター要素の編集: Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="ポスター要素の編集: Public Joy">

---

<a id="case-12"></a>

### Case 12: 正確なテクスチャ応答による素材表面の置換

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="正確なテクスチャ応答による素材表面の置換">

---

<a id="anchor-position-editing"></a>

## 📍 アンカー / 位置編集

グリッド状のアンカーや相対位置を使い、特定対象を正確に移動します。

ケース数: **1**.

<a id="case-13"></a>

### Case 13: グリッド位置に基づくオブジェクト移動

<table>
<tr>
<td width="50%" valign="top">

**変更前:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" height="300" alt="グリッド位置に基づくオブジェクト移動の変更前">

</td>
<td width="50%" valign="top">

**変更後:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" height="300" alt="グリッド位置に基づくオブジェクト移動の変更後">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 レイヤー分離

前景、背景、再利用可能なコンポーネントを分離し、後工程の編集に使います。

ケース数: **1**.

<a id="case-14"></a>

### Case 14: 前景 / 人物レイヤー分離

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" height="420" alt="前景 / 人物レイヤー分離">

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ 複数画像融合編集

複数の参照画像を、単一の指示に従って一貫した構図に統合します。

ケース数: **1**.

<a id="case-15"></a>

### Case 15: 7枚参照の入力/出力静物構図

<table>
<tr>
<td width="50%" valign="top">

**入力:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" height="300" alt="7枚参照の静物構図入力">

</td>
<td width="50%" valign="top">

**出力:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" height="300" alt="7枚参照の静物構図出力">

</td>
</tr>
</table>

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 ビジュアル品質とナラティブ

効果サンプルをシネマティックアクション、3D / アニメーション、コンセプトアート、ゲームシーンで分類します。

ケース数: **5**.

<a id="case-16"></a>

### Case 16: ガラスが砕けるシネマティックなテニスシーン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" height="420" alt="ガラスが砕けるシネマティックなテニスシーン">

---

<a id="case-17"></a>

### Case 17: シネマティックなボクシングアクション

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" height="420" alt="シネマティックなボクシングアクション">

---

<a id="case-18"></a>

### Case 18: 3Dアニメーション風シーン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" height="420" alt="3Dアニメーション風シーン">

---

<a id="case-19"></a>

### Case 19: ビジュアルコンセプトアート

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" height="420" alt="ビジュアルコンセプトアート">

---

<a id="case-20"></a>

### Case 20: ゲームシーンビジュアル

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" height="420" alt="ゲームシーンビジュアル">

---

<a id="multilingual-text-rendering"></a>

## 🌐 多言語テキスト描画

多言語サンプルを描画言語とローカルテキスト用途で分類します。

ケース数: **5**.

<a id="case-21"></a>

### Case 21: アラビア語と英語のウェルカムサイン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" height="420" alt="アラビア語と英語のウェルカムサイン">

---

<a id="case-22"></a>

### Case 22: 韓国語の24時間営業サイン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" height="420" alt="韓国語の24時間営業サイン">

---

<a id="case-23"></a>

### Case 23: タイ語の清潔保持サイン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" height="420" alt="タイ語の清潔保持サイン">

---

<a id="case-24"></a>

### Case 24: フランス語のクリエーションポスター

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" height="420" alt="フランス語のクリエーションポスター">

---

<a id="case-25"></a>

### Case 25: ロシア語の未来ポスター

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" height="420" alt="ロシア語の未来ポスター">

---

<a id="community-use-cases"></a>

## 🧪 コミュニティ活用事例

公開ソースに基づく 39 件のコミュニティ事例を、ユーザーのタスクと出力目的別に分類しています。タグはモデル比較、プロンプト公開状況、画像入力、複数画像出力などの補助属性を示します。

<a id="community-editing-control"></a>

### 編集・入力制御ワークフロー

<a id="community-usecase-1"></a>

### Community Use Case 1: [日本語によるすっぴん画像編集指示](https://x.com/renataro9/status/2075059699112652908) (by [@renataro9](https://x.com/renataro9))

**ソース投稿は、入力同士の関係が最終画像と同じくらい重要になる画像編集または入力制御ワークフローを示しています。**

Type: Tutorial | Date: 2026-07-09 | Category: 編集・入力制御ワークフロー

Tags: `image-input` `multi-image` `prompt-available` `tutorial`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/043/01.jpg" height="180" alt="日本語によるすっぴん画像編集指示 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/043/02.jpg" height="180" alt="日本語によるすっぴん画像編集指示 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
すっぴんメイクにして
```

</details>

---

<a id="community-usecase-2"></a>

### Community Use Case 2: [構図を維持して一つの被写体だけを変更するローカライズ済みアニメ編集](https://x.com/haruuraeadss/status/2075035201391255593) (by [@haruuraeadss](https://x.com/haruuraeadss))

**ソース投稿は、入力同士の関係が最終画像と同じくらい重要になる画像編集または入力制御ワークフローを示しています。**

Type: Tutorial | Date: 2026-07-09 | Category: 編集・入力制御ワークフロー

Tags: `multi-image` `prompt-available` `tutorial`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/052/01.jpg" height="180" alt="構図を維持して一つの被写体だけを変更するローカライズ済みアニメ編集 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/052/02.jpg" height="180" alt="構図を維持して一つの被写体だけを変更するローカライズ済みアニメ編集 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
元画像の構図、人物の横顔、顔の輪郭、髪型、花飾り、白いドレス、藤の花の背景、全体の淡いピンクとラベンダーの幻想的な雰囲気はそのまま維持してください。 局所的に、少女の視線の先にいる紫の蝶を、より美しく印象的な「光をまとった宝石のような蝶」に変更してください。蝶の羽は透明感のある紫、水晶、ラベンダー、淡いピンクのグラデーションで、細かな発光粒子と繊細な羽脈を持たせてください。 蝶から少女の瞳へ向かって、細い光の粒子と柔らかな魔法の軌跡を追加してください。光は強すぎず、白飛びさせず、既存の明るく儚い花園の空気感に自然に溶け込ませてください。 少女の紫色の瞳には、蝶の光が小さく反射しているような宝石風のハイライトを少しだけ追加してください。瞳の形、顔立ち、表情、年齢感は変えないでください。 前髪の一部にも、蝶の淡い紫光がわずかに反射しているようにしてください。ただし髪色全体は変えず、ピンクブロンドの柔らかさを維持してください。 全体は高品質な日本アニメイラスト、幻想的、透明感、春の花園、上品、繊細、儚い美しさ。過度な発光、派手な魔法陣、強いコントラスト、顔の変形、衣装変更、背景変更は避けて…
```

</details>

---

<a id="community-usecase-3"></a>

### Community Use Case 3: [画像入力による猫のメカ化](https://x.com/JennyAITech/status/2074870477651398972) (by [@JennyAITech](https://x.com/JennyAITech))

**ソース投稿は、入力同士の関係が最終画像と同じくらい重要になる画像編集または入力制御ワークフローを示しています。**

Type: Demo | Date: 2026-07-08 | Category: 編集・入力制御ワークフロー

Tags: `image-input` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/058/01.jpg" height="180" alt="画像入力による猫のメカ化 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/058/02.jpg" height="180" alt="画像入力による猫のメカ化 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
a pic of my cat, asked for a mecha version
```

</details>

---

<a id="community-usecase-36"></a>

### Community Use Case 36: [Niji7のソース画像を使った参照画像バリエーション](https://x.com/Naonekozamurai/status/2075407158129353026) (by [@Naonekozamurai](https://x.com/Naonekozamurai))

**既存のイラストを視覚的な土台にして、Seedreamで制御された別バージョンを生成します。**

Type: Demo | Date: 2026-07-10 | Category: 編集・入力制御ワークフロー

Tags: `image-input` `multi-image` `reference-variation`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/071/01.jpg" height="180" alt="Niji7のソース画像を使った参照画像バリエーション メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/071/02.jpg" height="180" alt="Niji7のソース画像を使った参照画像バリエーション メディア"></td>
</tr></table>

---

<a id="community-usecase-38"></a>

### Community Use Case 38: [人物同一性を維持するメイク転写](https://x.com/YaZoraiz/status/2075189150127726801) (by [@YaZoraiz](https://x.com/YaZoraiz))

**参照画像からメイクを転写しながら、対象人物の同一性を維持します。**

Type: Evaluation | Date: 2026-07-09 | Category: 編集・入力制御ワークフロー

Tags: `identity-preservation` `image-input` `model-comparison` `multi-image`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/01.jpg" height="180" alt="人物同一性を維持するメイク転写 メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/02.jpg" height="180" alt="人物同一性を維持するメイク転写 メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/03.jpg" height="180" alt="人物同一性を維持するメイク転写 メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/04.jpg" height="180" alt="人物同一性を維持するメイク転写 メディア"></td>
</tr></table>

---


<a id="community-product-interface-design"></a>

### 製品・インターフェース・ポスターデザイン

<a id="community-usecase-4"></a>

### Community Use Case 4: [市場マイクロストラクチャーの詳細を含む取引端末インターフェース](https://x.com/MishikaAI/status/2074879603446026333) (by [@MishikaAI](https://x.com/MishikaAI))

**ソース投稿は、Seedreamが実用的な商用ビジュアル、インターフェース、製品広告、ポスター形式の出力を生成できるかを検証しています。**

Type: Demo | Date: 2026-07-08 | Category: 製品・インターフェース・ポスターデザイン

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/004/01.jpg" height="340" alt="市場マイクロストラクチャーの詳細を含む取引端末インターフェース メディア">

<details open>
<summary>Prompt</summary>

```
a full trading terminal — K-lines, order book, bid/ask, volume, timestamps
```

</details>

---

<a id="community-usecase-5"></a>

### Community Use Case 5: [サイバーパンク・アンドロイドのグラフィックポスター](https://x.com/ComfyUI/status/2075027793491226677) (by [@ComfyUI](https://x.com/ComfyUI))

**ソース投稿は、Seedreamが実用的な商用ビジュアル、インターフェース、製品広告、ポスター形式の出力を生成できるかを検証しています。**

Type: Demo | Date: 2026-07-09 | Category: 製品・インターフェース・ポスターデザイン

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/042/01.jpg" height="340" alt="サイバーパンク・アンドロイドのグラフィックポスター メディア">

<details open>
<summary>Prompt</summary>

```
A sci-fi cyberpunk graphic design poster. In the center, a striking portrait of a female android with glossy, liquid chrome skin. A vivid swirling streak of neon orange, yellow, and pink liquid paint brush stroke horizontally covers her eyes, soft smudged color overlay with smooth flowing pigment texture, no cracks or broken facial surfaces. The background is a dark, textured charcoal gray. Behind the central figure, large bold white futuristic typography reads "Seedream 5.0 Pro" with a subtle…
```

</details>

---

<a id="community-usecase-6"></a>

### Community Use Case 6: [高級スポーツシューズの広告セット](https://x.com/iamrealsnow/status/2075063569486598281) (by [@iamrealsnow](https://x.com/iamrealsnow))

**ソース投稿は、Seedreamが実用的な商用ビジュアル、インターフェース、製品広告、ポスター形式の出力を生成できるかを検証しています。**

Type: Demo | Date: 2026-07-09 | Category: 製品・インターフェース・ポスターデザイン

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/01.jpg" height="180" alt="高級スポーツシューズの広告セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/02.jpg" height="180" alt="高級スポーツシューズの広告セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/03.jpg" height="180" alt="高級スポーツシューズの広告セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/04.jpg" height="180" alt="高級スポーツシューズの広告セット メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
Ultra-realistic premium sports footwear commercial advertisement featuring a modern running shoe floating horizontally at the center of a futuristic cyan and deep blue gradient background. The sneaker is displayed in a clean side profile with ultra-detailed breathable knit mesh texture, glossy air-cushion sole, realistic stitching, premium materials, and crisp branding. Soft cinematic studio lighting creates realistic reflections, shadows, and depth. The composition is designed as a futuristic…
```

</details>

---

<a id="community-usecase-7"></a>

### Community Use Case 7: [子ども向け粘土工作の広告ポスター](https://x.com/Strength04_X/status/2075063250656621054) (by [@Strength04_X](https://x.com/Strength04_X))

**ソース投稿は、Seedreamが実用的な商用ビジュアル、インターフェース、製品広告、ポスター形式の出力を生成できるかを検証しています。**

Type: Demo | Date: 2026-07-09 | Category: 製品・インターフェース・ポスターデザイン

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/050/01.jpg" height="340" alt="子ども向け粘土工作の広告ポスター メディア">

<details open>
<summary>Prompt</summary>

```
A messy fun kids advertisement poster. A laughing young girl age 6 with clay all over her hands proudly shows a lumpy clay sculpture beside a giant colorful clay set box 3x her height overflowing with clay blocks in every color, "SQUISHCRAFT" written in big squishy letters on the box. Bright cheerful craft room background with clay sculptures tools and colorful handprints on the walls. Big squishy rounded typography "SQUISHCRAFT" in rainbow colors filling the background. Tagline bottom: "Get yo…
```

</details>

---


<a id="community-technical-structured-visuals"></a>

### 技術図・ダイアグラム・シーケンスプロンプト

<a id="community-usecase-8"></a>

### Community Use Case 8: [計測情報を多用した技術ブループリント](https://x.com/LiamEtherson/status/2074862867442962667) (by [@LiamEtherson](https://x.com/LiamEtherson))

**ソース投稿は、図解、技術レイアウト、ショットリスト、複数フレームのシーケンス論理を含む構造化プロンプトへの追従性を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: 技術図・ダイアグラム・シーケンスプロンプト

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/003/01.jpg" height="340" alt="計測情報を多用した技術ブループリント メディア">

<details open>
<summary>Prompt</summary>

```
technical blueprint with abundant measurement values
```

</details>

---

<a id="community-usecase-9"></a>

### Community Use Case 9: [分解技術図を備えたコンセプトカーのブループリント](https://x.com/AiwithZohaib/status/2074880584107909602) (by [@AiwithZohaib](https://x.com/AiwithZohaib))

**ソース投稿は、図解、技術レイアウト、ショットリスト、複数フレームのシーケンス論理を含む構造化プロンプトへの追従性を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: 技術図・ダイアグラム・シーケンスプロンプト

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/005/01.jpg" height="340" alt="分解技術図を備えたコンセプトカーのブループリント メディア">

<details open>
<summary>Prompt</summary>

```
a blueprint-style technical drawing of a concept car: front/side/rear views, exploded parts, measurements everywhere
```

</details>

---

<a id="community-usecase-10"></a>

### Community Use Case 10: [ショットリスト駆動のグレースケール場面設計](https://x.com/munzxsdv/status/2074865454485483885) (by [@munzxsdv](https://x.com/munzxsdv))

**ソース投稿は、図解、技術レイアウト、ショットリスト、複数フレームのシーケンス論理を含む構造化プロンプトへの追従性を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: 技術図・ダイアグラム・シーケンスプロンプト

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/007/01.jpg" height="340" alt="ショットリスト駆動のグレースケール場面設計 メディア">

<details open>
<summary>Prompt</summary>

```
a shot list — panel-by-panel direction, camera moves, grayscale spec
```

</details>

---

<a id="community-usecase-11"></a>

### Community Use Case 11: [単一プロンプトによる16コマの騎兵ストーリーボード](https://x.com/sulekhat95/status/2074966196563431636) (by [@sulekhat95](https://x.com/sulekhat95))

**ソース投稿は、図解、技術レイアウト、ショットリスト、複数フレームのシーケンス論理を含む構造化プロンプトへの追従性を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: 技術図・ダイアグラム・シーケンスプロンプト

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/062/01.jpg" height="340" alt="単一プロンプトによる16コマの騎兵ストーリーボード メディア">

<details open>
<summary>Prompt</summary>

```
16-panel storyboard from ONE prompt: numbered frames, consistent characters, coherent camera logic across a whole cavalry charge
```

</details>

---

<a id="community-usecase-37"></a>

### Community Use Case 37: [一つのプロンプトから生成する分解技術図](https://x.com/Ciri_ai/status/2075248022515294567) (by [@Ciri_ai](https://x.com/Ciri_ai))

**Seedreamを使い、一つの指示からラベル付きの分解技術構図を生成します。**

Type: Demo | Date: 2026-07-09 | Category: 技術図・ダイアグラム・シーケンスプロンプト

Tags: `diagram` `multi-image` `structured-layout`

<table><tr>
<td width="33%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/072/01.jpg" height="180" alt="一つのプロンプトから生成する分解技術図 メディア"></td>
<td width="33%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/072/02.jpg" height="180" alt="一つのプロンプトから生成する分解技術図 メディア"></td>
<td width="33%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/072/03.jpg" height="180" alt="一つのプロンプトから生成する分解技術図 メディア"></td>
</tr></table>

---


<a id="community-cinematic-character-visuals"></a>

### シネマティック・キャラクター・スタイル表現

<a id="community-usecase-12"></a>

### Community Use Case 12: [ミニチュア分身をモチーフにした魚眼エディトリアルポートレート](https://x.com/magnific/status/2074872903938846900) (by [@magnific](https://x.com/magnific))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: シネマティック・キャラクター・スタイル表現

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/008/01.jpg" height="180" alt="ミニチュア分身をモチーフにした魚眼エディトリアルポートレート メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/008/02.jpg" height="180" alt="ミニチュア分身をモチーフにした魚眼エディトリアルポートレート メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
Shot on cinema camera with subtle halation effect, 35mm film grain, fashion editorial photography in the style of Y2K revival magazine covers. Extreme fisheye lens, distorted wide perspective pulling the scene toward the curved edges, low camera angle from the street. A young man around 20 years old with messy dark hair with soft curtain bangs, smooth youthful skin with natural texture and a few freckles, wearing small oval sunglasses with pink tinted lenses, a colorful beaded necklace, silver…
```

</details>

---

<a id="community-usecase-13"></a>

### Community Use Case 13: [溶ける世界のランドマークのコンセプト生成](https://x.com/magnific/status/2074918700709523881) (by [@magnific](https://x.com/magnific))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: シネマティック・キャラクター・スタイル表現

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/011/01.jpg" height="180" alt="溶ける世界のランドマークのコンセプト生成 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/011/02.jpg" height="180" alt="溶ける世界のランドマークのコンセプト生成 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
world's landmarks, melting like wax
```

</details>

---

<a id="community-usecase-14"></a>

### Community Use Case 14: [写実的なハイファッションポートレート照明](https://x.com/BubbleBrain/status/2074856963591290979) (by [@BubbleBrain](https://x.com/BubbleBrain))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: シネマティック・キャラクター・スタイル表現

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/017/01.jpg" height="340" alt="写実的なハイファッションポートレート照明 メディア">

<details open>
<summary>Prompt</summary>

```
This is a highly photorealistic, high-fashion full-body portrait with an overall dark-toned, dreamy, and hazy atmosphere, filled with the flowing beauty of light and shadow. The scene uses refined artificial lighting that is soft yet richly layered, with sparkling highlights, crystal-clear reflections, and a subtle lomo film texture in certain areas, creating a surreal and luxurious fashion mood that feels both realistic and dreamlike. The subject is a young adult Taiwanese woman with short pin…
```

</details>

---

<a id="community-usecase-15"></a>

### Community Use Case 15: [サンフランシスコの夕暮れを写した自然なスマートフォン写真](https://x.com/mattworkman/status/2074850550349222210) (by [@mattworkman](https://x.com/mattworkman))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: シネマティック・キャラクター・スタイル表現

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/018/01.jpg" height="340" alt="サンフランシスコの夕暮れを写した自然なスマートフォン写真 メディア">

<details open>
<summary>Prompt</summary>

```
a Korean girl in her twenties on her iPhone in San Francisco at sunset
```

</details>

---

<a id="community-usecase-16"></a>

### Community Use Case 16: [幻想的な堕天使戦士のキービジュアル](https://x.com/SimplyAnnisa/status/2074900816662774189) (by [@SimplyAnnisa](https://x.com/SimplyAnnisa))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: シネマティック・キャラクター・スタイル表現

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/028/01.jpg" height="340" alt="幻想的な堕天使戦士のキービジュアル メディア">

<details open>
<summary>Prompt</summary>

```
A divine fallen angel warrior kneeling in the center of an ancient celestial temple, thrusting a massive flaming holy sword into a cracked white marble floor, the impact creating glowing lava-like fractures and flying debris. Gigantic pure white feathered wings spread wide behind the warrior, wearing ornate gold and crimson medieval armor with intricate engravings, a flowing dark red cape, and ram-like curled white horns. Glowing crimson eyes stare downward with an intense, wrathful expression.…
```

</details>

---

<a id="community-usecase-17"></a>

### Community Use Case 17: [日本風カジュアルポートレートのスタイリングセット](https://x.com/Cia0_exe/status/2075033845032993261) (by [@Cia0_exe](https://x.com/Cia0_exe))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-09 | Category: シネマティック・キャラクター・スタイル表現

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/01.jpg" height="180" alt="日本風カジュアルポートレートのスタイリングセット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/02.jpg" height="180" alt="日本風カジュアルポートレートのスタイリングセット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/03.jpg" height="180" alt="日本風カジュアルポートレートのスタイリングセット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/04.jpg" height="180" alt="日本風カジュアルポートレートのスタイリングセット メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A beautiful young Japanese woman, natural and effortless beauty, soft glowing skin, wearing a fitted black tank top layered under an oversized cool white shirt worn open, casual chic styling. Cinematic movie-grade shot, anamorphic lens flare, shallow depth of field with creamy bokeh, slow dolly-in camera movement, dramatic rim lighting from golden hour sun, subtle film grain, volumetric light rays through window, color graded like a Denis Villeneuve film teal and warm amber tones, 35mm anamorph…
```

</details>

---

<a id="community-usecase-18"></a>

### Community Use Case 18: [ARRI風のシネマティックな都市クローズアップ](https://x.com/df_reno/status/2075055332452106476) (by [@df_reno](https://x.com/df_reno))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-09 | Category: シネマティック・キャラクター・スタイル表現

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/01.jpg" height="180" alt="ARRI風のシネマティックな都市クローズアップ メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/02.jpg" height="180" alt="ARRI風のシネマティックな都市クローズアップ メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/03.jpg" height="180" alt="ARRI風のシネマティックな都市クローズアップ メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/04.jpg" height="180" alt="ARRI風のシネマティックな都市クローズアップ メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
超写实电影剧照，一位女性在昏暗的都市环境中仰望天空，画面极具感染力。使用 ARRI Alexa Mini LF 摄影机和 Panavision C 系列 50mm 变形镜头拍摄，光圈 T2，加装 Black Pro-Mist 1/8 滤镜，采用 2.39:1 变形宽银幕构图。低角度特写镜头，镜头略低于女性面部，营造出亲密的电影视角。女性位于画面右侧，左侧留出大片空白。 右上角背景中存在强烈的人工光源，产生强烈的变形镜头水平光晕、蓝白色的光晕、镜头内部反射、电影光晕效果以及柔和的高光。 光源并非阳光，而是远处城市路灯或工业灯光，并因浅景深而呈现出模糊效果。柔和的青色环境光部分照亮了女性的脸庞，展现出逼真的肌肤纹理、自然的毛孔、细微的瑕疵，嘴唇微张，眼神充满情感地向上凝视。前景包含模糊的暗色调环境元素。中景是女性的脸部和头发。背景是高度虚化的城市建筑，点缀着抽象的光影。深邃的阴影、低对比度的黑色、冷色调的蓝色调、逼真的夜景电影感、柯达胶片质感、细腻的颗粒感、变形光晕、朦胧的氛围，以及真实的电影画面。 A vast grassy field filled with several larg…
```

</details>

---

<a id="community-usecase-19"></a>

### Community Use Case 19: [立体駐車場を舞台にしたファッション編集セット](https://x.com/ChillaiKalan__/status/2075071088137208063) (by [@ChillaiKalan__](https://x.com/ChillaiKalan__))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-09 | Category: シネマティック・キャラクター・スタイル表現

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/01.jpg" height="180" alt="立体駐車場を舞台にしたファッション編集セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/02.jpg" height="180" alt="立体駐車場を舞台にしたファッション編集セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/03.jpg" height="180" alt="立体駐車場を舞台にしたファッション編集セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/04.jpg" height="180" alt="立体駐車場を舞台にしたファッション編集セット メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A stylish young woman with long layered black hair and soft curtain bangs, wearing sleek black rectangular sunglasses, an oversized chocolate-brown tailored blazer with matching wide-leg trousers, and a fitted mocha-brown camisole. She carries a large structured ivory leather tote bag with gold hardware over one shoulder. Standing confidently with one hand in her pocket, looking back over her shoulder. Shot in a modern open-air parking structure beneath a concrete overpass, with parked cars sof…
```

</details>

---

<a id="community-usecase-20"></a>

### Community Use Case 20: [虹色ガラスフラワーのエディトリアルポスター](https://x.com/ComfyUI/status/2075027810666914062) (by [@ComfyUI](https://x.com/ComfyUI))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-09 | Category: シネマティック・キャラクター・スタイル表現

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/044/01.jpg" height="340" alt="虹色ガラスフラワーのエディトリアルポスター メディア">

<details open>
<summary>Prompt</summary>

```
An editorial graphic design poster on a solid black background. The central elements are exquisite, translucent 3D glass flowers with iridescent, holographic petals in shades of electric blue, violet, and soft purple. In the background, large, bold white sans-serif typography reads "Seedream 5.0 Pro", elegantly layered behind and interwoven with the glass petals. The layout is filled with clean blocks of small white placeholder body text and delicate thin white vector lines, creating a futurist…
```

</details>

---

<a id="community-usecase-21"></a>

### Community Use Case 21: [複数のショットプロンプトを使ったアニメ調スケートボードシーケンス](https://x.com/asatoucan/status/2075060881067769903) (by [@asatoucan](https://x.com/asatoucan))

**ソース投稿は、表示されたメディア出力を通じて、シネマティック、キャラクター、ファッション、スタイルの描画品質を検証しています。**

Type: Demo | Date: 2026-07-09 | Category: シネマティック・キャラクター・スタイル表現

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/01.jpg" height="180" alt="複数のショットプロンプトを使ったアニメ調スケートボードシーケンス メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/02.jpg" height="180" alt="複数のショットプロンプトを使ったアニメ調スケートボードシーケンス メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/03.jpg" height="180" alt="複数のショットプロンプトを使ったアニメ調スケートボードシーケンス メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/04.jpg" height="180" alt="複数のショットプロンプトを使ったアニメ調スケートボードシーケンス メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A girl with a sharp bob cut, purple hair with black accent strands, stylized layered hair flowing in the wind, wearing layered cloth with black accents, riding a skateboard through a vibrant concrete skate park, captured from a dramatic high angle looking down at the front profile, dynamic action pose, body leaning into a turn, skate park ramps, rails, and colorful graffiti walls sprawling below, cel shaded, toon shading, hard shadows, bold outlines, anime style, vibrant flat colors, crisp line…
```

</details>

---

<a id="community-usecase-39"></a>

### Community Use Case 39: [エンドツーエンド解説動画におけるSeedreamキーフレーム](https://x.com/alisaqqt/status/2075241584615108812) (by [@alisaqqt](https://x.com/alisaqqt))

**複数モデルのパイプライン内でSeedreamをキーフレーム生成に使い、完成した解説動画を制作します。**

Type: Integration | Date: 2026-07-09 | Category: シネマティック・キャラクター・スタイル表現

Tags: `integration` `keyframes` `video`

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/074/demo.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/074/poster.jpg" height="340" alt="エンドツーエンド解説動画におけるSeedreamキーフレーム メディア"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/074/demo.mp4)

---


<a id="community-concept-environment-worldbuilding"></a>

### コンセプトアート・環境・世界構築

<a id="community-usecase-22"></a>

### Community Use Case 22: [太陽光発電式の砂漠研究基地コンセプト](https://x.com/ashen_one/status/2074915677815886071) (by [@ashen_one](https://x.com/ashen_one))

**ソース投稿は、単一オブジェクトの編集ではなく、環境、室内、SF、世界構築の構成力を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: コンセプトアート・環境・世界構築

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/021/01.jpg" height="340" alt="太陽光発電式の砂漠研究基地コンセプト メディア">

<details open>
<summary>Prompt</summary>

```
A solar-powered research station in a desert, featuring domed structures, solar panels, and various equipment for energy and research management.
```

</details>

---

<a id="community-usecase-23"></a>

### Community Use Case 23: [非現実的なスケールのシネマティックSF世界構築セット](https://x.com/AllaAisling/status/2075036565147906511) (by [@AllaAisling](https://x.com/AllaAisling))

**ソース投稿は、単一オブジェクトの編集ではなく、環境、室内、SF、世界構築の構成力を検証しています。**

Type: Demo | Date: 2026-07-09 | Category: コンセプトアート・環境・世界構築

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/01.jpg" height="180" alt="非現実的なスケールのシネマティックSF世界構築セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/02.jpg" height="180" alt="非現実的なスケールのシネマティックSF世界構築セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/03.jpg" height="180" alt="非現実的なスケールのシネマティックSF世界構築セット メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/04.jpg" height="180" alt="非現実的なスケールのシネマティックSF世界構築セット メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
An industrial civilization is constructing an entire planet inside an enormous orbital shipyard. Giant robotic arms hold continents in place while molten oceans are poured into gigantic basins. Thousands of spacecraft weld mountain ranges together. The unfinished world glows from its molten core. Unreal scale, NASA realism, cinematic science fiction. Gigantic floating whales drift above endless wheat fields while enormous wind-powered harvesting machines extend hundreds of meters into the sky t…
```

</details>

---

<a id="community-usecase-24"></a>

### Community Use Case 24: [MBTIタイプ別の寝室デザインバリエーション](https://x.com/FloraTechAI/status/2074866317484794131) (by [@FloraTechAI](https://x.com/FloraTechAI))

**ソース投稿は、単一オブジェクトの編集ではなく、環境、室内、SF、世界構築の構成力を検証しています。**

Type: Demo | Date: 2026-07-08 | Category: コンセプトアート・環境・世界構築

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/01.jpg" height="180" alt="MBTIタイプ別の寝室デザインバリエーション メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/02.jpg" height="180" alt="MBTIタイプ別の寝室デザインバリエーション メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/03.jpg" height="180" alt="MBTIタイプ別の寝室デザインバリエーション メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/04.jpg" height="180" alt="MBTIタイプ別の寝室デザインバリエーション メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
design a bedroom for each MBTI type
```

</details>

---


<a id="community-model-comparisons"></a>

### モデル比較・評価

<a id="community-usecase-25"></a>

### Community Use Case 25: [4つの中国語プロンプトによるSeedreamのマルチタスク能力サンプル](https://x.com/op7418/status/2074862226905948549) (by [@op7418](https://x.com/op7418))

**ソース投稿は一つのスレッドで複数のタスクを試しているため、単一用途の事例よりも広範な能力確認に適しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `capability-sampling` `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/01.jpg" height="180" alt="4つの中国語プロンプトによるSeedreamのマルチタスク能力サンプル メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/02.jpg" height="180" alt="4つの中国語プロンプトによるSeedreamのマルチタスク能力サンプル メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/03.jpg" height="180" alt="4つの中国語プロンプトによるSeedreamのマルチタスク能力サンプル メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/04.jpg" height="180" alt="4つの中国語プロンプトによるSeedreamのマルチタスク能力サンプル メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
1. 一句话让它生成《黑神话：水浒传》的一个游戏截图 2. 让他生成一张茶叶制作和品种的科普图 3. 给它一个参考图，让它基于这个参考图的组件生成一个 Web 的 UI 设计稿 4. 让他用一张图介绍《凡人修仙传：人界篇》的剧情
```

</details>

---

<a id="community-usecase-26"></a>

### Community Use Case 26: [写実的な車内セルフィー構図でのSeedreamとGPT Image 2の比較](https://x.com/johnAGI168/status/2074870910469677387) (by [@johnAGI168](https://x.com/johnAGI168))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/006/01.jpg" height="180" alt="写実的な車内セルフィー構図でのSeedreamとGPT Image 2の比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/006/02.jpg" height="180" alt="写実的な車内セルフィー構図でのSeedreamとGPT Image 2の比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
生成一张真实感车内自拍视频首帧照片，横屏 16:9。画面像固定在副驾驶前方或中控台附近的小型广角相机拍摄，轻微广角，近距离车内第一视角，像社交媒体短视频截图。 主角是一位成年女性，气质清冷、安静、精致，整体像日常车内自拍视频里的主角。她脸型小巧偏鹅蛋脸，五官自然精致，鼻梁挺，嘴唇自然，表情平静、淡淡的，有一点冷感但不夸张。她正面面向镜头或略微看向前方，能清楚看到完整正脸，不低头，不侧脸。她戴细框透明或浅银色眼镜，长直发偏浅棕色，带轻微空气刘海，头发自然垂落在肩侧。穿简洁灰色无袖针织连衣裙或灰色无袖上衣搭配同色下装，造型干净日常、端庄自然。 她坐在驾驶位，安全带已经插好并固定完成：黑色安全带清楚地从肩膀斜跨过上身到腰侧，状态自然贴合身体，不是在拉安全带，也不是正在插卡扣。她一只手自然放在方向盘附近或轻扶方向盘，另一只手放低在座椅边或腿侧，姿态像准备开车前刚坐正的一瞬间。表情专注平静，眼神可以看向镜头，也可以略微看向前方道路。 车内是红棕色真皮座椅和红棕色门板，方向盘在画面右前方形成明显前景，仪表台、车窗边缘和后排座椅可见。车窗外是白天城市道路旁的绿化、树木和轻微模糊的街景，但车子此刻看…
```

</details>

---

<a id="community-usecase-27"></a>

### Community Use Case 27: [クリーンなライフスタイルポートレートでのSeedreamとGPT Image 2の比較](https://x.com/liyue_ai/status/2074890690686005590) (by [@liyue_ai](https://x.com/liyue_ai))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/012/01.jpg" height="180" alt="クリーンなライフスタイルポートレートでのSeedreamとGPT Image 2の比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/012/02.jpg" height="180" alt="クリーンなライフスタイルポートレートでのSeedreamとGPT Image 2の比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
摄影风格：冷白清透CCD生活照风 写真方向：轻熟生活照 场景方向：酒店泳池外步道 / 白色躺椅 / 浅蓝池水 / 简洁遮阳伞 服装方向：浅鼠尾草色修身无袖针织短裙 气质标签：温柔、清透、轻熟、安静、有吸引力 五官方向：真实清透自然脸，安静干净，不网红 五官细节：柔和鹅蛋脸，面部轮廓自然；清亮杏眼，眼神温柔安静；鼻型流畅小巧；唇形柔软克制，低饱和裸粉唇色；整体是安静、通透、舒服的生活感美人脸 发型方向：自然黑长发或低扎发，发丝顺滑，额前少量碎发，带一点微风感 身形方向：轻盈纤细，上围饱满自然 线条强调：强 镜头方向：大腿及上半身 姿态动作：站在泳池步道边，身体轻微侧向镜头，一只手自然垂落，另一只手轻扶裙侧 光线氛围：高色温晴天自然光 + 水面反射光 + 冷白极弱柔闪 滤镜效果：冷白高光 + 蓝白清透生活照色彩 + 轻颗粒 + 轻数码噪点 + 轻微过曝 画幅比例：9:16 补充要求：连衣裙贴身柔软，突出胸部轮廓、腰线和整体修长感，人物五官要安静耐看，整体要冷白清爽，不要商业泳池大片感
```

</details>

---

<a id="community-usecase-28"></a>

### Community Use Case 28: [ブループリント調スポーツカーでのGPT Image 2との比較](https://x.com/marmaduke091/status/2074866077499105416) (by [@marmaduke091](https://x.com/marmaduke091))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/019/01.jpg" height="180" alt="ブループリント調スポーツカーでのGPT Image 2との比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/019/02.jpg" height="180" alt="ブループリント調スポーツカーでのGPT Image 2との比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A technical drawing of a futuristic sports car in blueprint style. Include line drawings of the sports car from the front, side, and rear views, exploded parts sketches, parts assembly diagrams, and structural diagrams of disassembled components. Use abundant lines and measurement values to indicate the dimensions of each part, with grayscale tones expressing the overall sketch relationship. In addition to the main design, also show scattered thumbnails from different angles.
```

</details>

---

<a id="community-usecase-29"></a>

### Community Use Case 29: [参照画像のカメラ角度変更比較](https://x.com/hasamaru_studio/status/2075052934409375918) (by [@hasamaru_studio](https://x.com/hasamaru_studio))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-09 | Category: モデル比較・評価

Tags: `image-input` `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/01.jpg" height="180" alt="参照画像のカメラ角度変更比較 メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/02.jpg" height="180" alt="参照画像のカメラ角度変更比較 メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/03.jpg" height="180" alt="参照画像のカメラ角度変更比較 メディア"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/04.jpg" height="180" alt="参照画像のカメラ角度変更比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
リファレンス画像のスタイルを保ったまま、もう少し高い位置からの画角に変更してもらいました。
```

</details>

---

<a id="community-usecase-30"></a>

### Community Use Case 30: [巨大な飲料缶を使った広告構図の比較](https://x.com/emmanuel_2m/status/2075000101362131350) (by [@emmanuel_2m](https://x.com/emmanuel_2m))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/023/01.jpg" height="180" alt="巨大な飲料缶を使った広告構図の比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/023/02.jpg" height="180" alt="巨大な飲料缶を使った広告構図の比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A premium infographic-style advertisement featuring an oversized Pepsi can placed beside a young woman. The can is scaled to be nearly the same size as her entire seated body, creating a striking surreal proportion. The woman sits casually leaning against the giant can, one arm resting on it, interacting naturally. The Pepsi can is ultra-detailed with crisp branding, condensation droplets, realistic reflections, and metallic texture. The logo is clean, sharp, and properly proportioned. Composit…
```

</details>

---

<a id="community-usecase-31"></a>

### Community Use Case 31: [成都旅行スクラップブックポスターの比較](https://x.com/DeepBlueAIX/status/2074872447229419956) (by [@DeepBlueAIX](https://x.com/DeepBlueAIX))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/031/01.jpg" height="180" alt="成都旅行スクラップブックポスターの比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/031/02.jpg" height="180" alt="成都旅行スクラップブックポスターの比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
成都旅游 · 小红书手帐风海报 一张竖版 9:16 的小红书风格拼贴海报，主题为**「成都旅游城市漫游计划」**。整体采用手帐风设计，像旅行日记一样丰富、有生活感和轻松氛围。 画面以成都城市旅行为核心内容，包含宽窄巷子、锦里古街、春熙路、IFS熊猫、成都大熊猫繁育研究基地、东郊记忆、都江堰、青城山等真实场景照片，以拼贴方式散落在画面中，搭配撕纸边框与胶带装饰。画面中穿插熊猫元素、茶馆、人民公园、盖碗茶、街头巷尾、夜市、美食街、城市天际线等真实旅行场景，充分展现成都悠闲惬意的慢生活氛围。 整体视觉使用天蓝色作为主色调，并点缀粉色、浅黄色与柔和绿色，营造清新明亮又富有烟火气的城市旅行氛围。 画面中加入大量手帐元素，例如手绘箭头、涂鸦星星、对话气泡、便签标签、贴纸装饰、旅行地图、定位图标、拍立得照片、胶带、旅行印章、熊猫贴纸、相机、咖啡杯、小花、云朵、笑脸图标等，使画面具有强烈的小红书「种草笔记」视觉风格。 主标题为**「成都达人计划 / Chengdu City Guide」，采用手写感或涂鸦字体，具有明显的年轻化社交媒体风格。画面中穿插中英文混排文字，如「City Walk Cheng…
```

</details>

---

<a id="community-usecase-32"></a>

### Community Use Case 32: [アニメキービジュアルの比較](https://x.com/roco_kn_roco/status/2074890020260094137) (by [@roco_kn_roco](https://x.com/roco_kn_roco))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/034/01.jpg" height="340" alt="アニメキービジュアルの比較 メディア">

<details open>
<summary>Prompt</summary>

```
新作アニメのキービジュアルを作って下さい
```

</details>

---

<a id="community-usecase-33"></a>

### Community Use Case 33: [署名制約付き旅行ポスターの比較](https://x.com/Bic_Revelation/status/2074959714366922857) (by [@Bic_Revelation](https://x.com/Bic_Revelation))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/056/01.jpg" height="180" alt="署名制約付き旅行ポスターの比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/056/02.jpg" height="180" alt="署名制約付き旅行ポスターの比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
With its crystal-clear waters, white sandy beaches, and vibrant coral reefs, the Maldives is a tropical paradise perfect for exotic and tranquil visuals. SIGNATURE: 'BicRevelation' cursive script lower-left.
```

</details>

---

<a id="community-usecase-34"></a>

### Community Use Case 34: [幻想的な村の水車でのGPT Image 2との比較](https://x.com/emmanuel_2m/status/2075000114427375742) (by [@emmanuel_2m](https://x.com/emmanuel_2m))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-08 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/065/01.jpg" height="180" alt="幻想的な村の水車でのGPT Image 2との比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/065/02.jpg" height="180" alt="幻想的な村の水車でのGPT Image 2との比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
stylized stylized fantasy village watermill, two-story half-timbered red-clay tower w/ thatched conical roof, big wooden water-wheel, attached small thatched cottage, wooden walkways and stairs, lush green meadow w/ stones, painterly Genshin-Impact / Studio Ghibli env art, fluffy cumulus clouds, sunny midday
```

</details>

---

<a id="community-usecase-35"></a>

### Community Use Case 35: [コモ湖のファッション場面でのBanana Proとの比較](https://x.com/cso6709/status/2075046425277399261) (by [@cso6709](https://x.com/cso6709))

**ソース投稿は、同一または近い視覚タスクでSeedream 5.0 Proと別モデルを比較しています。**

Type: Evaluation | Date: 2026-07-09 | Category: モデル比較・評価

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/066/01.jpg" height="180" alt="コモ湖のファッション場面でのBanana Proとの比較 メディア"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/066/02.jpg" height="180" alt="コモ湖のファッション場面でのBanana Proとの比較 メディア"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A straight-on medium-wide cinematic shot at eye-level, static locked frame, 4:5 vertical, captures a sun-bright late-morning inside a Lake Como villa courtyard room, camera perpendicular to the wall plane with no tilt, the atmosphere crisp and alive like the minute before heading out for gelato, the wall behind the scene a warm hand-troweled sable butter-yellow lime plaster slightly uneven with soft sun-bleach along the upper right edge, the floor matte burnt-terracotta chili tile grounding the…
```

</details>

---

<a id="acknowledge"></a>

## 🙏 謝辞

このリポジトリは、2026年7月8日にエクスポートされた Seedream 5.0 Pro の公式ローンチ資料と、ユースケースギャラリーで引用している公開コミュニティ投稿をもとに作成されています。

公式サンプル、製品資料、技術リファレンスを提供してくれた Seedream チームに感謝します。

このリポジトリで引用している公開投稿のコミュニティ作者に感謝します：

- [@renataro9](https://x.com/renataro9), [@haruuraeadss](https://x.com/haruuraeadss), [@JennyAITech](https://x.com/JennyAITech), [@MishikaAI](https://x.com/MishikaAI), [@ComfyUI](https://x.com/ComfyUI), [@iamrealsnow](https://x.com/iamrealsnow), [@Strength04_X](https://x.com/Strength04_X), [@LiamEtherson](https://x.com/LiamEtherson)
- [@AiwithZohaib](https://x.com/AiwithZohaib), [@munzxsdv](https://x.com/munzxsdv), [@sulekhat95](https://x.com/sulekhat95), [@magnific](https://x.com/magnific), [@BubbleBrain](https://x.com/BubbleBrain), [@mattworkman](https://x.com/mattworkman), [@SimplyAnnisa](https://x.com/SimplyAnnisa), [@Cia0_exe](https://x.com/Cia0_exe)
- [@df_reno](https://x.com/df_reno), [@ChillaiKalan__](https://x.com/ChillaiKalan__), [@asatoucan](https://x.com/asatoucan), [@ashen_one](https://x.com/ashen_one), [@AllaAisling](https://x.com/AllaAisling), [@FloraTechAI](https://x.com/FloraTechAI), [@op7418](https://x.com/op7418), [@johnAGI168](https://x.com/johnAGI168)
- [@liyue_ai](https://x.com/liyue_ai), [@marmaduke091](https://x.com/marmaduke091), [@hasamaru_studio](https://x.com/hasamaru_studio), [@emmanuel_2m](https://x.com/emmanuel_2m), [@DeepBlueAIX](https://x.com/DeepBlueAIX), [@roco_kn_roco](https://x.com/roco_kn_roco), [@Bic_Revelation](https://x.com/Bic_Revelation), [@cso6709](https://x.com/cso6709)
- [@Naonekozamurai](https://x.com/Naonekozamurai), [@Ciri_ai](https://x.com/Ciri_ai), [@YaZoraiz](https://x.com/YaZoraiz), [@alisaqqt](https://x.com/alisaqqt)

作者が attribution の変更または削除を希望する場合は、該当する公開投稿リンクを添えて issue を開いてください。
