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
- [🧾 プロンプトライブラリ](#prompt-library)
- [🧩 モデルメモ](#model-notes)
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

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif?v=20260709-camo" width="720" alt="空間意図を示す矢印と注釈ボックス">

> [!NOTE]
> 編集前に矢印、ボックス、注釈で対象エリアを明確にします。

---

<a id="case-2"></a>

### Case 2: 対象編集のための領域ボックス別オブジェクト説明

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="対象編集のための領域ボックス別オブジェクト説明">

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

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif?v=20260709-camo" width="720" alt="落書きガイドによるオブジェクト生成">

> [!NOTE]
> ラフな落書きを視覚制御信号として使い、意図したオブジェクトをモデルに描画させます。

---

<a id="case-4"></a>

### Case 4: 色ブロックでガイドする編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif?v=20260709-camo" width="720" alt="色ブロックでガイドする編集">

> [!NOTE]
> 大きな色ブロックで大まかな構図、色領域、オブジェクト配置を指定します。

---

<a id="case-5"></a>

### Case 5: 線でガイドするディテール編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif?v=20260709-camo" width="720" alt="線でガイドするディテール編集">

> [!NOTE]
> 形状の輪郭が長い説明より重要なとき、シンプルな線ガイドを使います。

---

<a id="case-6"></a>

### Case 6: 簡単なスケッチから洗練された画像へ

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif?v=20260709-camo" width="720" alt="簡単なスケッチから洗練された画像へ">

> [!NOTE]
> 最小限のスケッチを、意図を保ったままより完成度の高い画像にします。

---

<a id="layer-editing"></a>

## 🧱 レイヤー編集

ポスター、グラフィック、文字、素材、表面のレイヤーを、全体構図を保ったまま編集します。

ケース数: **6**.

<a id="case-7"></a>

### Case 7: ポスターの文字・グラフィックレイヤー編集: Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" width="720" alt="ポスターの文字・グラフィックレイヤー編集: Avery Turns">

> [!NOTE]
> 全体のデザイン構造を保ちながら、ポスター内の可視要素を編集します。

---

<a id="case-8"></a>

### Case 8: ポスターのオファーレイヤー編集: Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="ポスターのオファーレイヤー編集: Happy Hour">

> [!NOTE]
> ポスター全体を作り直さずに、プロモーションバッジやグラフィック要素を変更します。

---

<a id="case-9"></a>

### Case 9: デザインレイアウト内のファッション画像レイヤー編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" width="720" alt="デザインレイアウト内のファッション画像レイヤー編集">

> [!NOTE]
> 構成済みビジュアルレイアウト内のレイヤー化された被写体を調整します。

---

<a id="case-10"></a>

### Case 10: スポーツポスターのグラフィックレイヤー編集

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="スポーツポスターのグラフィックレイヤー編集">

> [!NOTE]
> タイポグラフィと構図を整えたまま、レーシングポスターのグラフィックを編集します。

---

<a id="case-11"></a>

### Case 11: ポスター要素の編集: Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="ポスター要素の編集: Public Joy">

> [!NOTE]
> 元のデザイン言語を保ちながらポスター要素を変更します。

---

<a id="case-12"></a>

### Case 12: 正確なテクスチャ応答による素材表面の置換

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="正確なテクスチャ応答による素材表面の置換">

> [!NOTE]
> オブジェクト構造を保ったまま、素材と色の対象を置き換えます。

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

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" width="420" alt="グリッド位置に基づくオブジェクト移動の変更前">

</td>
<td width="50%" valign="top">

**変更後:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" width="420" alt="グリッド位置に基づくオブジェクト移動の変更後">

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

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" width="720" alt="前景 / 人物レイヤー分離">

> [!NOTE]
> 後で再利用できるよう、ポスター風背景から前景の被写体を分離します。

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

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" width="420" alt="7枚参照の静物構図入力">

</td>
<td width="50%" valign="top">

**出力:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" width="420" alt="7枚参照の静物構図出力">

</td>
</tr>
</table>

> [!NOTE]
> 7枚の白背景参照画像を入力グループとして使い、同じ成対 case の中で静物写真の出力を生成します。

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

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="ガラスが砕けるシネマティックなテニスシーン">

> [!NOTE]
> ガラス片、アクションのタイミング、映画的照明を含む高モーションシーン生成。

---

<a id="case-17"></a>

### Case 17: シネマティックなボクシングアクション

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="シネマティックなボクシングアクション">

> [!NOTE]
> 動き、衝撃、シーンの奥行きがより強いアクションレンダリング。

---

<a id="case-18"></a>

### Case 18: 3Dアニメーション風シーン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="3Dアニメーション風シーン">

> [!NOTE]
> キャラクターやエンタメビジュアル向けのスタイライズされた3D / アニメーション出力。

---

<a id="case-19"></a>

### Case 19: ビジュアルコンセプトアート

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="ビジュアルコンセプトアート">

> [!NOTE]
> 雰囲気、ビジュアル方向性、ムード探索のためのコンセプトアート生成。

---

<a id="case-20"></a>

### Case 20: ゲームシーンビジュアル

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="ゲームシーンビジュアル">

> [!NOTE]
> 環境、セット、キーアート探索のためのゲーム風シーン生成。

---

<a id="multilingual-text-rendering"></a>

## 🌐 多言語テキスト描画

多言語サンプルを描画言語とローカルテキスト用途で分類します。

ケース数: **5**.

<a id="case-21"></a>

### Case 21: アラビア語と英語のウェルカムサイン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" width="720" alt="アラビア語と英語のウェルカムサイン">

> [!NOTE]
> 同じビジュアル内にアラビア語と英語を含むネイティブ多言語描画。

---

<a id="case-22"></a>

### Case 22: 韓国語の24時間営業サイン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" width="720" alt="韓国語の24時間営業サイン">

> [!NOTE]
> ローカライズされた店舗やサイン向けの韓国語テキスト描画。

---

<a id="case-23"></a>

### Case 23: タイ語の清潔保持サイン

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="タイ語の清潔保持サイン">

> [!NOTE]
> 地域の公共空間やキャンペーンビジュアル向けのタイ語テキスト描画。

---

<a id="case-24"></a>

### Case 24: フランス語のクリエーションポスター

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="フランス語のクリエーションポスター">

> [!NOTE]
> 商品、ファッション、キャンペーン向けのフランス語テキスト描画。

---

<a id="case-25"></a>

### Case 25: ロシア語の未来ポスター

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" width="720" alt="ロシア語の未来ポスター">

> [!NOTE]
> ローカライズされたビジュアルコンセプト向けに、明確な文字構造でロシア語を描画します。

---

<a id="community-use-cases"></a>

## 🧪 コミュニティユースケース

この35件のコミュニティ事例は、ユーザータスクと出力用途で分類しています。タグはモデル比較、プロンプトあり、画像入力、複数画像出力などの補助属性です。

ユースケース数: **35**.

<a id="community-editing-control"></a>

### 編集と入力制御ワークフロー

ユースケース数: **3**.

<a id="community-usecase-1"></a>

### Community Use Case 1: [Japanese no-makeup image edit instruction](https://x.com/renataro9/status/2075059699112652908) (by [@renataro9](https://x.com/renataro9))

Type: Tutorial | Date: 2026-07-09 | Category: Editing & Input-Control Workflows

タグ: `image-input` `multi-image` `prompt-available` `tutorial`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/043/01.jpg" width="240" alt="Japanese no-makeup image edit instruction media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/043/02.jpg" width="240" alt="Japanese no-makeup image edit instruction media"></td>
</tr></table>

> [!NOTE]
> The source post demonstrates an image-editing or input-control workflow where the input relationship matters as much as the final image.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
すっぴんメイクにして
```

</details>

---
<a id="community-usecase-2"></a>

### Community Use Case 2: [Localized anime edit preserving composition while changing one subject](https://x.com/haruuraeadss/status/2075035201391255593) (by [@haruuraeadss](https://x.com/haruuraeadss))

Type: Tutorial | Date: 2026-07-09 | Category: Editing & Input-Control Workflows

タグ: `multi-image` `prompt-available` `tutorial`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/052/01.jpg" width="240" alt="Localized anime edit preserving composition while changing one subject media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/052/02.jpg" width="240" alt="Localized anime edit preserving composition while changing one subject media"></td>
</tr></table>

> [!NOTE]
> The source post demonstrates an image-editing or input-control workflow where the input relationship matters as much as the final image.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
元画像の構図、人物の横顔、顔の輪郭、髪型、花飾り、白いドレス、藤の花の背景、全体の淡いピンクとラベンダーの幻想的な雰囲気はそのまま維持してください。 局所的に、少女の視線の先にいる紫の蝶を、より美しく印象的な「光をまとった宝石のような蝶」に変更してください。蝶の羽は透明感のある紫、水晶、ラベンダー、淡いピンクのグラデーションで、細かな発光粒子と繊細な羽脈を持たせてください。 蝶から少女の瞳へ向かって、細い光の粒子と柔らかな魔法の軌跡を追加してください。光は強すぎず、白飛びさせず、既存の明るく儚い花園の空気感に自然に溶け込ませてください。 少女の紫色の瞳には、蝶の光が小さく反射しているような宝石風のハイライトを少しだけ追加してください。瞳の形、顔立ち、表情、年齢感は変えないでください。 前髪の一部にも、蝶の淡い紫光がわずかに反射しているようにしてください。ただし髪色全体は変えず、ピンクブロンドの柔らかさを維持してください。 全体は高品質な日本アニメイラスト、幻想的、透明感、春の花園、上品、繊細、儚い美しさ。過度な発光、派手な魔法陣、強いコントラスト、顔の変形、衣装変更、背景変更は避けて…
```

</details>

---
<a id="community-usecase-3"></a>

### Community Use Case 3: [Image-input cat-to-mecha transformation](https://x.com/JennyAITech/status/2074870477651398972) (by [@JennyAITech](https://x.com/JennyAITech))

Type: Demo | Date: 2026-07-08 | Category: Editing & Input-Control Workflows

タグ: `image-input` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/058/01.jpg" width="240" alt="Image-input cat-to-mecha transformation media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/058/02.jpg" width="240" alt="Image-input cat-to-mecha transformation media"></td>
</tr></table>

> [!NOTE]
> The source post demonstrates an image-editing or input-control workflow where the input relationship matters as much as the final image.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
a pic of my cat, asked for a mecha version
```

</details>

---
<a id="community-product-interface-design"></a>

### プロダクト・UI・ポスターデザイン

ユースケース数: **4**.

<a id="community-usecase-4"></a>

### Community Use Case 4: [Trading terminal interface with market microstructure detail](https://x.com/MishikaAI/status/2074879603446026333) (by [@MishikaAI](https://x.com/MishikaAI))

Type: Demo | Date: 2026-07-08 | Category: Product, Interface & Poster Design

タグ: `prompt-available`

<img src="downloaded-media/media/004/01.jpg" width="520" alt="Trading terminal interface with market microstructure detail media">

> [!NOTE]
> The source post tests whether Seedream can produce a usable commercial visual, interface, product ad, or poster-style output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
a full trading terminal — K-lines, order book, bid/ask, volume, timestamps
```

</details>

---
<a id="community-usecase-5"></a>

### Community Use Case 5: [Cyberpunk android graphic poster](https://x.com/ComfyUI/status/2075027793491226677) (by [@ComfyUI](https://x.com/ComfyUI))

Type: Demo | Date: 2026-07-09 | Category: Product, Interface & Poster Design

タグ: `prompt-available`

<img src="downloaded-media/media/042/01.jpg" width="520" alt="Cyberpunk android graphic poster media">

> [!NOTE]
> The source post tests whether Seedream can produce a usable commercial visual, interface, product ad, or poster-style output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A sci-fi cyberpunk graphic design poster. In the center, a striking portrait of a female android with glossy, liquid chrome skin. A vivid swirling streak of neon orange, yellow, and pink liquid paint brush stroke horizontally covers her eyes, soft smudged color overlay with smooth flowing pigment texture, no cracks or broken facial surfaces. The background is a dark, textured charcoal gray. Behind the central figure, large bold white futuristic typography reads "Seedream 5.0 Pro" with a subtle…
```

</details>

---
<a id="community-usecase-6"></a>

### Community Use Case 6: [Premium sports footwear commercial ad set](https://x.com/iamrealsnow/status/2075063569486598281) (by [@iamrealsnow](https://x.com/iamrealsnow))

Type: Demo | Date: 2026-07-09 | Category: Product, Interface & Poster Design

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/047/01.jpg" width="240" alt="Premium sports footwear commercial ad set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/047/02.jpg" width="240" alt="Premium sports footwear commercial ad set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/047/03.jpg" width="240" alt="Premium sports footwear commercial ad set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/047/04.jpg" width="240" alt="Premium sports footwear commercial ad set media"></td>
</tr></table>

> [!NOTE]
> The source post tests whether Seedream can produce a usable commercial visual, interface, product ad, or poster-style output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
Ultra-realistic premium sports footwear commercial advertisement featuring a modern running shoe floating horizontally at the center of a futuristic cyan and deep blue gradient background. The sneaker is displayed in a clean side profile with ultra-detailed breathable knit mesh texture, glossy air-cushion sole, realistic stitching, premium materials, and crisp branding. Soft cinematic studio lighting creates realistic reflections, shadows, and depth. The composition is designed as a futuristic…
```

</details>

---
<a id="community-usecase-7"></a>

### Community Use Case 7: [Kids clay craft advertisement poster](https://x.com/Strength04_X/status/2075063250656621054) (by [@Strength04_X](https://x.com/Strength04_X))

Type: Demo | Date: 2026-07-09 | Category: Product, Interface & Poster Design

タグ: `prompt-available`

<img src="downloaded-media/media/050/01.jpg" width="520" alt="Kids clay craft advertisement poster media">

> [!NOTE]
> The source post tests whether Seedream can produce a usable commercial visual, interface, product ad, or poster-style output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A messy fun kids advertisement poster. A laughing young girl age 6 with clay all over her hands proudly shows a lumpy clay sculpture beside a giant colorful clay set box 3x her height overflowing with clay blocks in every color, "SQUISHCRAFT" written in big squishy letters on the box. Bright cheerful craft room background with clay sculptures tools and colorful handprints on the walls. Big squishy rounded typography "SQUISHCRAFT" in rainbow colors filling the background. Tagline bottom: "Get yo…
```

</details>

---
<a id="community-technical-structured-visuals"></a>

### 技術図・構造化ビジュアル

ユースケース数: **4**.

<a id="community-usecase-8"></a>

### Community Use Case 8: [Measurement-heavy technical blueprint rendering](https://x.com/LiamEtherson/status/2074862867442962667) (by [@LiamEtherson](https://x.com/LiamEtherson))

Type: Demo | Date: 2026-07-08 | Category: Technical, Diagram & Sequence Prompts

タグ: `prompt-available`

<img src="downloaded-media/media/003/01.jpg" width="520" alt="Measurement-heavy technical blueprint rendering media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
technical blueprint with abundant measurement values
```

</details>

---
<a id="community-usecase-9"></a>

### Community Use Case 9: [Concept car blueprint with exploded technical views](https://x.com/AiwithZohaib/status/2074880584107909602) (by [@AiwithZohaib](https://x.com/AiwithZohaib))

Type: Demo | Date: 2026-07-08 | Category: Technical, Diagram & Sequence Prompts

タグ: `prompt-available`

<img src="downloaded-media/media/005/01.jpg" width="520" alt="Concept car blueprint with exploded technical views media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
a blueprint-style technical drawing of a concept car: front/side/rear views, exploded parts, measurements everywhere
```

</details>

---
<a id="community-usecase-10"></a>

### Community Use Case 10: [Shot-list driven grayscale scene planning](https://x.com/munzxsdv/status/2074865454485483885) (by [@munzxsdv](https://x.com/munzxsdv))

Type: Demo | Date: 2026-07-08 | Category: Technical, Diagram & Sequence Prompts

タグ: `prompt-available`

<img src="downloaded-media/media/007/01.jpg" width="520" alt="Shot-list driven grayscale scene planning media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
a shot list — panel-by-panel direction, camera moves, grayscale spec
```

</details>

---
<a id="community-usecase-11"></a>

### Community Use Case 11: [Single-prompt 16-panel cavalry storyboard](https://x.com/sulekhat95/status/2074966196563431636) (by [@sulekhat95](https://x.com/sulekhat95))

Type: Demo | Date: 2026-07-08 | Category: Technical, Diagram & Sequence Prompts

タグ: `prompt-available`

<img src="downloaded-media/media/062/01.jpg" width="520" alt="Single-prompt 16-panel cavalry storyboard media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
16-panel storyboard from ONE prompt: numbered frames, consistent characters, coherent camera logic across a whole cavalry charge
```

</details>

---
<a id="community-cinematic-character-visuals"></a>

### 映画的・キャラクター・スタイル表現

ユースケース数: **10**.

<a id="community-usecase-12"></a>

### Community Use Case 12: [Fisheye editorial portraits with miniature clone motif](https://x.com/magnific/status/2074872903938846900) (by [@magnific](https://x.com/magnific))

Type: Demo | Date: 2026-07-08 | Category: Cinematic, Character & Style Visuals

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/008/01.jpg" width="240" alt="Fisheye editorial portraits with miniature clone motif media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/008/02.jpg" width="240" alt="Fisheye editorial portraits with miniature clone motif media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
Shot on cinema camera with subtle halation effect, 35mm film grain, fashion editorial photography in the style of Y2K revival magazine covers. Extreme fisheye lens, distorted wide perspective pulling the scene toward the curved edges, low camera angle from the street. A young man around 20 years old with messy dark hair with soft curtain bangs, smooth youthful skin with natural texture and a few freckles, wearing small oval sunglasses with pink tinted lenses, a colorful beaded necklace, silver…
```

</details>

---
<a id="community-usecase-13"></a>

### Community Use Case 13: [Melting-world-landmarks concept generation](https://x.com/magnific/status/2074918700709523881) (by [@magnific](https://x.com/magnific))

Type: Demo | Date: 2026-07-08 | Category: Cinematic, Character & Style Visuals

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/011/01.jpg" width="240" alt="Melting-world-landmarks concept generation media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/011/02.jpg" width="240" alt="Melting-world-landmarks concept generation media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
world's landmarks, melting like wax
```

</details>

---
<a id="community-usecase-14"></a>

### Community Use Case 14: [Photorealistic high-fashion portrait lighting](https://x.com/BubbleBrain/status/2074856963591290979) (by [@BubbleBrain](https://x.com/BubbleBrain))

Type: Demo | Date: 2026-07-08 | Category: Cinematic, Character & Style Visuals

タグ: `prompt-available`

<img src="downloaded-media/media/017/01.jpg" width="520" alt="Photorealistic high-fashion portrait lighting media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
This is a highly photorealistic, high-fashion full-body portrait with an overall dark-toned, dreamy, and hazy atmosphere, filled with the flowing beauty of light and shadow. The scene uses refined artificial lighting that is soft yet richly layered, with sparkling highlights, crystal-clear reflections, and a subtle lomo film texture in certain areas, creating a surreal and luxurious fashion mood that feels both realistic and dreamlike. The subject is a young adult Taiwanese woman with short pin…
```

</details>

---
<a id="community-usecase-15"></a>

### Community Use Case 15: [Natural phone-photo scene at San Francisco sunset](https://x.com/mattworkman/status/2074850550349222210) (by [@mattworkman](https://x.com/mattworkman))

Type: Demo | Date: 2026-07-08 | Category: Cinematic, Character & Style Visuals

タグ: `prompt-available`

<img src="downloaded-media/media/018/01.jpg" width="520" alt="Natural phone-photo scene at San Francisco sunset media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
a Korean girl in her twenties on her iPhone in San Francisco at sunset
```

</details>

---
<a id="community-usecase-16"></a>

### Community Use Case 16: [Fantasy fallen-angel warrior key visual](https://x.com/SimplyAnnisa/status/2074900816662774189) (by [@SimplyAnnisa](https://x.com/SimplyAnnisa))

Type: Demo | Date: 2026-07-08 | Category: Cinematic, Character & Style Visuals

タグ: `prompt-available`

<img src="downloaded-media/media/028/01.jpg" width="520" alt="Fantasy fallen-angel warrior key visual media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A divine fallen angel warrior kneeling in the center of an ancient celestial temple, thrusting a massive flaming holy sword into a cracked white marble floor, the impact creating glowing lava-like fractures and flying debris. Gigantic pure white feathered wings spread wide behind the warrior, wearing ornate gold and crimson medieval armor with intricate engravings, a flowing dark red cape, and ram-like curled white horns. Glowing crimson eyes stare downward with an intense, wrathful expression.…
```

</details>

---
<a id="community-usecase-17"></a>

### Community Use Case 17: [Japanese casual portrait styling set](https://x.com/Cia0_exe/status/2075033845032993261) (by [@Cia0_exe](https://x.com/Cia0_exe))

Type: Demo | Date: 2026-07-09 | Category: Cinematic, Character & Style Visuals

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/029/01.jpg" width="240" alt="Japanese casual portrait styling set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/029/02.jpg" width="240" alt="Japanese casual portrait styling set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/029/03.jpg" width="240" alt="Japanese casual portrait styling set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/029/04.jpg" width="240" alt="Japanese casual portrait styling set media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A beautiful young Japanese woman, natural and effortless beauty, soft glowing skin, wearing a fitted black tank top layered under an oversized cool white shirt worn open, casual chic styling. Cinematic movie-grade shot, anamorphic lens flare, shallow depth of field with creamy bokeh, slow dolly-in camera movement, dramatic rim lighting from golden hour sun, subtle film grain, volumetric light rays through window, color graded like a Denis Villeneuve film teal and warm amber tones, 35mm anamorph…
```

</details>

---
<a id="community-usecase-18"></a>

### Community Use Case 18: [ARRI-style cinematic city close-up](https://x.com/df_reno/status/2075055332452106476) (by [@df_reno](https://x.com/df_reno))

Type: Demo | Date: 2026-07-09 | Category: Cinematic, Character & Style Visuals

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/035/01.jpg" width="240" alt="ARRI-style cinematic city close-up media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/035/02.jpg" width="240" alt="ARRI-style cinematic city close-up media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/035/03.jpg" width="240" alt="ARRI-style cinematic city close-up media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/035/04.jpg" width="240" alt="ARRI-style cinematic city close-up media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
超写实电影剧照，一位女性在昏暗的都市环境中仰望天空，画面极具感染力。使用 ARRI Alexa Mini LF 摄影机和 Panavision C 系列 50mm 变形镜头拍摄，光圈 T2，加装 Black Pro-Mist 1/8 滤镜，采用 2.39:1 变形宽银幕构图。低角度特写镜头，镜头略低于女性面部，营造出亲密的电影视角。女性位于画面右侧，左侧留出大片空白。 右上角背景中存在强烈的人工光源，产生强烈的变形镜头水平光晕、蓝白色的光晕、镜头内部反射、电影光晕效果以及柔和的高光。 光源并非阳光，而是远处城市路灯或工业灯光，并因浅景深而呈现出模糊效果。柔和的青色环境光部分照亮了女性的脸庞，展现出逼真的肌肤纹理、自然的毛孔、细微的瑕疵，嘴唇微张，眼神充满情感地向上凝视。前景包含模糊的暗色调环境元素。中景是女性的脸部和头发。背景是高度虚化的城市建筑，点缀着抽象的光影。深邃的阴影、低对比度的黑色、冷色调的蓝色调、逼真的夜景电影感、柯达胶片质感、细腻的颗粒感、变形光晕、朦胧的氛围，以及真实的电影画面。 A vast grassy field filled with several larg…
```

</details>

---
<a id="community-usecase-19"></a>

### Community Use Case 19: [Fashion outfit editorial set in a parking structure](https://x.com/ChillaiKalan__/status/2075071088137208063) (by [@ChillaiKalan__](https://x.com/ChillaiKalan__))

Type: Demo | Date: 2026-07-09 | Category: Cinematic, Character & Style Visuals

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/038/01.jpg" width="240" alt="Fashion outfit editorial set in a parking structure media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/038/02.jpg" width="240" alt="Fashion outfit editorial set in a parking structure media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/038/03.jpg" width="240" alt="Fashion outfit editorial set in a parking structure media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/038/04.jpg" width="240" alt="Fashion outfit editorial set in a parking structure media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A stylish young woman with long layered black hair and soft curtain bangs, wearing sleek black rectangular sunglasses, an oversized chocolate-brown tailored blazer with matching wide-leg trousers, and a fitted mocha-brown camisole. She carries a large structured ivory leather tote bag with gold hardware over one shoulder. Standing confidently with one hand in her pocket, looking back over her shoulder. Shot in a modern open-air parking structure beneath a concrete overpass, with parked cars sof…
```

</details>

---
<a id="community-usecase-20"></a>

### Community Use Case 20: [Iridescent glass-flower editorial poster](https://x.com/ComfyUI/status/2075027810666914062) (by [@ComfyUI](https://x.com/ComfyUI))

Type: Demo | Date: 2026-07-09 | Category: Cinematic, Character & Style Visuals

タグ: `prompt-available`

<img src="downloaded-media/media/044/01.jpg" width="520" alt="Iridescent glass-flower editorial poster media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
An editorial graphic design poster on a solid black background. The central elements are exquisite, translucent 3D glass flowers with iridescent, holographic petals in shades of electric blue, violet, and soft purple. In the background, large, bold white sans-serif typography reads "Seedream 5.0 Pro", elegantly layered behind and interwoven with the glass petals. The layout is filled with clean blocks of small white placeholder body text and delicate thin white vector lines, creating a futurist…
```

</details>

---
<a id="community-usecase-21"></a>

### Community Use Case 21: [Anime skateboard sequence with multiple shot prompts](https://x.com/asatoucan/status/2075060881067769903) (by [@asatoucan](https://x.com/asatoucan))

Type: Demo | Date: 2026-07-09 | Category: Cinematic, Character & Style Visuals

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/069/01.jpg" width="240" alt="Anime skateboard sequence with multiple shot prompts media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/069/02.jpg" width="240" alt="Anime skateboard sequence with multiple shot prompts media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/069/03.jpg" width="240" alt="Anime skateboard sequence with multiple shot prompts media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/069/04.jpg" width="240" alt="Anime skateboard sequence with multiple shot prompts media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A girl with a sharp bob cut, purple hair with black accent strands, stylized layered hair flowing in the wind, wearing layered cloth with black accents, riding a skateboard through a vibrant concrete skate park, captured from a dramatic high angle looking down at the front profile, dynamic action pose, body leaning into a turn, skate park ramps, rails, and colorful graffiti walls sprawling below, cel shaded, toon shading, hard shadows, bold outlines, anime style, vibrant flat colors, crisp line…
```

</details>

---
<a id="community-concept-environment-worldbuilding"></a>

### コンセプトアート・環境・世界構築

ユースケース数: **3**.

<a id="community-usecase-22"></a>

### Community Use Case 22: [Solar-powered desert research station concept](https://x.com/ashen_one/status/2074915677815886071) (by [@ashen_one](https://x.com/ashen_one))

Type: Demo | Date: 2026-07-08 | Category: Concept Art, Environment & Worldbuilding

タグ: `prompt-available`

<img src="downloaded-media/media/021/01.jpg" width="520" alt="Solar-powered desert research station concept media">

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A solar-powered research station in a desert, featuring domed structures, solar panels, and various equipment for energy and research management.
```

</details>

---
<a id="community-usecase-23"></a>

### Community Use Case 23: [Impossible-scale cinematic sci-fi worldbuilding set](https://x.com/AllaAisling/status/2075036565147906511) (by [@AllaAisling](https://x.com/AllaAisling))

Type: Demo | Date: 2026-07-09 | Category: Concept Art, Environment & Worldbuilding

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/027/01.jpg" width="240" alt="Impossible-scale cinematic sci-fi worldbuilding set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/027/02.jpg" width="240" alt="Impossible-scale cinematic sci-fi worldbuilding set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/027/03.jpg" width="240" alt="Impossible-scale cinematic sci-fi worldbuilding set media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/027/04.jpg" width="240" alt="Impossible-scale cinematic sci-fi worldbuilding set media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
An industrial civilization is constructing an entire planet inside an enormous orbital shipyard. Giant robotic arms hold continents in place while molten oceans are poured into gigantic basins. Thousands of spacecraft weld mountain ranges together. The unfinished world glows from its molten core. Unreal scale, NASA realism, cinematic science fiction. Gigantic floating whales drift above endless wheat fields while enormous wind-powered harvesting machines extend hundreds of meters into the sky t…
```

</details>

---
<a id="community-usecase-24"></a>

### Community Use Case 24: [Bedroom design variations for MBTI types](https://x.com/FloraTechAI/status/2074866317484794131) (by [@FloraTechAI](https://x.com/FloraTechAI))

Type: Demo | Date: 2026-07-08 | Category: Concept Art, Environment & Worldbuilding

タグ: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/061/01.jpg" width="240" alt="Bedroom design variations for MBTI types media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/061/02.jpg" width="240" alt="Bedroom design variations for MBTI types media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/061/03.jpg" width="240" alt="Bedroom design variations for MBTI types media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/061/04.jpg" width="240" alt="Bedroom design variations for MBTI types media"></td>
</tr></table>

> [!NOTE]
> The source post tests cinematic, character, fashion, style, structured, or worldbuilding visual quality with visible media output.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
design a bedroom for each MBTI type
```

</details>

---
<a id="community-model-comparisons"></a>

### モデル比較と評価

ユースケース数: **11**.

<a id="community-usecase-25"></a>

### Community Use Case 25: [Multi-task Seedream capability sampling from four Chinese prompts](https://x.com/op7418/status/2074862226905948549) (by [@op7418](https://x.com/op7418))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `capability-sampling` `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/001/01.jpg" width="240" alt="Multi-task Seedream capability sampling from four Chinese prompts media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/001/02.jpg" width="240" alt="Multi-task Seedream capability sampling from four Chinese prompts media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/001/03.jpg" width="240" alt="Multi-task Seedream capability sampling from four Chinese prompts media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/001/04.jpg" width="240" alt="Multi-task Seedream capability sampling from four Chinese prompts media"></td>
</tr></table>

> [!NOTE]
> The source post samples several task types in one thread, so it works best as a broad capability check rather than a single-purpose case.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
1. 一句话让它生成《黑神话：水浒传》的一个游戏截图 2. 让他生成一张茶叶制作和品种的科普图 3. 给它一个参考图，让它基于这个参考图的组件生成一个 Web 的 UI 设计稿 4. 让他用一张图介绍《凡人修仙传：人界篇》的剧情
```

</details>

---
<a id="community-usecase-26"></a>

### Community Use Case 26: [Seedream vs GPT Image 2 in realistic car selfie framing](https://x.com/johnAGI168/status/2074870910469677387) (by [@johnAGI168](https://x.com/johnAGI168))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/006/01.jpg" width="240" alt="Seedream vs GPT Image 2 in realistic car selfie framing media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/006/02.jpg" width="240" alt="Seedream vs GPT Image 2 in realistic car selfie framing media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
生成一张真实感车内自拍视频首帧照片，横屏 16:9。画面像固定在副驾驶前方或中控台附近的小型广角相机拍摄，轻微广角，近距离车内第一视角，像社交媒体短视频截图。 主角是一位成年女性，气质清冷、安静、精致，整体像日常车内自拍视频里的主角。她脸型小巧偏鹅蛋脸，五官自然精致，鼻梁挺，嘴唇自然，表情平静、淡淡的，有一点冷感但不夸张。她正面面向镜头或略微看向前方，能清楚看到完整正脸，不低头，不侧脸。她戴细框透明或浅银色眼镜，长直发偏浅棕色，带轻微空气刘海，头发自然垂落在肩侧。穿简洁灰色无袖针织连衣裙或灰色无袖上衣搭配同色下装，造型干净日常、端庄自然。 她坐在驾驶位，安全带已经插好并固定完成：黑色安全带清楚地从肩膀斜跨过上身到腰侧，状态自然贴合身体，不是在拉安全带，也不是正在插卡扣。她一只手自然放在方向盘附近或轻扶方向盘，另一只手放低在座椅边或腿侧，姿态像准备开车前刚坐正的一瞬间。表情专注平静，眼神可以看向镜头，也可以略微看向前方道路。 车内是红棕色真皮座椅和红棕色门板，方向盘在画面右前方形成明显前景，仪表台、车窗边缘和后排座椅可见。车窗外是白天城市道路旁的绿化、树木和轻微模糊的街景，但车子此刻看…
```

</details>

---
<a id="community-usecase-27"></a>

### Community Use Case 27: [Seedream vs GPT Image 2 for clean lifestyle portrait styling](https://x.com/liyue_ai/status/2074890690686005590) (by [@liyue_ai](https://x.com/liyue_ai))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/012/01.jpg" width="240" alt="Seedream vs GPT Image 2 for clean lifestyle portrait styling media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/012/02.jpg" width="240" alt="Seedream vs GPT Image 2 for clean lifestyle portrait styling media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
摄影风格：冷白清透CCD生活照风 写真方向：轻熟生活照 场景方向：酒店泳池外步道 / 白色躺椅 / 浅蓝池水 / 简洁遮阳伞 服装方向：浅鼠尾草色修身无袖针织短裙 气质标签：温柔、清透、轻熟、安静、有吸引力 五官方向：真实清透自然脸，安静干净，不网红 五官细节：柔和鹅蛋脸，面部轮廓自然；清亮杏眼，眼神温柔安静；鼻型流畅小巧；唇形柔软克制，低饱和裸粉唇色；整体是安静、通透、舒服的生活感美人脸 发型方向：自然黑长发或低扎发，发丝顺滑，额前少量碎发，带一点微风感 身形方向：轻盈纤细，上围饱满自然 线条强调：强 镜头方向：大腿及上半身 姿态动作：站在泳池步道边，身体轻微侧向镜头，一只手自然垂落，另一只手轻扶裙侧 光线氛围：高色温晴天自然光 + 水面反射光 + 冷白极弱柔闪 滤镜效果：冷白高光 + 蓝白清透生活照色彩 + 轻颗粒 + 轻数码噪点 + 轻微过曝 画幅比例：9:16 补充要求：连衣裙贴身柔软，突出胸部轮廓、腰线和整体修长感，人物五官要安静耐看，整体要冷白清爽，不要商业泳池大片感
```

</details>

---
<a id="community-usecase-28"></a>

### Community Use Case 28: [Blueprint sports car comparison against GPT Image 2](https://x.com/marmaduke091/status/2074866077499105416) (by [@marmaduke091](https://x.com/marmaduke091))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/019/01.jpg" width="240" alt="Blueprint sports car comparison against GPT Image 2 media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/019/02.jpg" width="240" alt="Blueprint sports car comparison against GPT Image 2 media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A technical drawing of a futuristic sports car in blueprint style. Include line drawings of the sports car from the front, side, and rear views, exploded parts sketches, parts assembly diagrams, and structural diagrams of disassembled components. Use abundant lines and measurement values to indicate the dimensions of each part, with grayscale tones expressing the overall sketch relationship. In addition to the main design, also show scattered thumbnails from different angles.
```

</details>

---
<a id="community-usecase-29"></a>

### Community Use Case 29: [Reference-image camera-angle change comparison](https://x.com/hasamaru_studio/status/2075052934409375918) (by [@hasamaru_studio](https://x.com/hasamaru_studio))

Type: Evaluation | Date: 2026-07-09 | Category: Model Comparisons & Evaluations

タグ: `image-input` `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/022/01.jpg" width="240" alt="Reference-image camera-angle change comparison media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/022/02.jpg" width="240" alt="Reference-image camera-angle change comparison media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/022/03.jpg" width="240" alt="Reference-image camera-angle change comparison media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/022/04.jpg" width="240" alt="Reference-image camera-angle change comparison media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
リファレンス画像のスタイルを保ったまま、もう少し高い位置からの画角に変更してもらいました。
```

</details>

---
<a id="community-usecase-30"></a>

### Community Use Case 30: [Oversized beverage-can advertising composition comparison](https://x.com/emmanuel_2m/status/2075000101362131350) (by [@emmanuel_2m](https://x.com/emmanuel_2m))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/023/01.jpg" width="240" alt="Oversized beverage-can advertising composition comparison media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/023/02.jpg" width="240" alt="Oversized beverage-can advertising composition comparison media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A premium infographic-style advertisement featuring an oversized Pepsi can placed beside a young woman. The can is scaled to be nearly the same size as her entire seated body, creating a striking surreal proportion. The woman sits casually leaning against the giant can, one arm resting on it, interacting naturally. The Pepsi can is ultra-detailed with crisp branding, condensation droplets, realistic reflections, and metallic texture. The logo is clean, sharp, and properly proportioned. Composit…
```

</details>

---
<a id="community-usecase-31"></a>

### Community Use Case 31: [Chengdu travel scrapbook poster comparison](https://x.com/DeepBlueAIX/status/2074872447229419956) (by [@DeepBlueAIX](https://x.com/DeepBlueAIX))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/031/01.jpg" width="240" alt="Chengdu travel scrapbook poster comparison media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/031/02.jpg" width="240" alt="Chengdu travel scrapbook poster comparison media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
成都旅游 · 小红书手帐风海报 一张竖版 9:16 的小红书风格拼贴海报，主题为**「成都旅游城市漫游计划」**。整体采用手帐风设计，像旅行日记一样丰富、有生活感和轻松氛围。 画面以成都城市旅行为核心内容，包含宽窄巷子、锦里古街、春熙路、IFS熊猫、成都大熊猫繁育研究基地、东郊记忆、都江堰、青城山等真实场景照片，以拼贴方式散落在画面中，搭配撕纸边框与胶带装饰。画面中穿插熊猫元素、茶馆、人民公园、盖碗茶、街头巷尾、夜市、美食街、城市天际线等真实旅行场景，充分展现成都悠闲惬意的慢生活氛围。 整体视觉使用天蓝色作为主色调，并点缀粉色、浅黄色与柔和绿色，营造清新明亮又富有烟火气的城市旅行氛围。 画面中加入大量手帐元素，例如手绘箭头、涂鸦星星、对话气泡、便签标签、贴纸装饰、旅行地图、定位图标、拍立得照片、胶带、旅行印章、熊猫贴纸、相机、咖啡杯、小花、云朵、笑脸图标等，使画面具有强烈的小红书「种草笔记」视觉风格。 主标题为**「成都达人计划 / Chengdu City Guide」，采用手写感或涂鸦字体，具有明显的年轻化社交媒体风格。画面中穿插中英文混排文字，如「City Walk Cheng…
```

</details>

---
<a id="community-usecase-32"></a>

### Community Use Case 32: [Anime key-visual comparison](https://x.com/roco_kn_roco/status/2074890020260094137) (by [@roco_kn_roco](https://x.com/roco_kn_roco))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `prompt-available`

<img src="downloaded-media/media/034/01.jpg" width="520" alt="Anime key-visual comparison media">

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
新作アニメのキービジュアルを作って下さい
```

</details>

---
<a id="community-usecase-33"></a>

### Community Use Case 33: [Travel-poster comparison with signature constraint](https://x.com/Bic_Revelation/status/2074959714366922857) (by [@Bic_Revelation](https://x.com/Bic_Revelation))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/056/01.jpg" width="240" alt="Travel-poster comparison with signature constraint media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/056/02.jpg" width="240" alt="Travel-poster comparison with signature constraint media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
With its crystal-clear waters, white sandy beaches, and vibrant coral reefs, the Maldives is a tropical paradise perfect for exotic and tranquil visuals. SIGNATURE: 'BicRevelation' cursive script lower-left.
```

</details>

---
<a id="community-usecase-34"></a>

### Community Use Case 34: [Fantasy village watermill comparison against GPT Image 2](https://x.com/emmanuel_2m/status/2075000114427375742) (by [@emmanuel_2m](https://x.com/emmanuel_2m))

Type: Evaluation | Date: 2026-07-08 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/065/01.jpg" width="240" alt="Fantasy village watermill comparison against GPT Image 2 media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/065/02.jpg" width="240" alt="Fantasy village watermill comparison against GPT Image 2 media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
stylized stylized fantasy village watermill, two-story half-timbered red-clay tower w/ thatched conical roof, big wooden water-wheel, attached small thatched cottage, wooden walkways and stairs, lush green meadow w/ stones, painterly Genshin-Impact / Studio Ghibli env art, fluffy cumulus clouds, sunny midday
```

</details>

---
<a id="community-usecase-35"></a>

### Community Use Case 35: [Lake Como fashion scene comparison against Banana Pro](https://x.com/cso6709/status/2075046425277399261) (by [@cso6709](https://x.com/cso6709))

Type: Evaluation | Date: 2026-07-09 | Category: Model Comparisons & Evaluations

タグ: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="downloaded-media/media/066/01.jpg" width="240" alt="Lake Como fashion scene comparison against Banana Pro media"></td>
<td width="25%" valign="top"><img src="downloaded-media/media/066/02.jpg" width="240" alt="Lake Como fashion scene comparison against Banana Pro media"></td>
</tr></table>

> [!NOTE]
> The source post compares Seedream 5.0 Pro with another model on the same or closely related visual task.

<details>
<summary>プロンプト/入力の抜粋</summary>

```text
A straight-on medium-wide cinematic shot at eye-level, static locked frame, 4:5 vertical, captures a sun-bright late-morning inside a Lake Como villa courtyard room, camera perpendicular to the wall plane with no tilt, the atmosphere crisp and alive like the minute before heading out for gelato, the wall behind the scene a warm hand-troweled sable butter-yellow lime plaster slightly uneven with soft sun-bleach along the upper right edge, the floor matte burnt-terracotta chili tile grounding the…
```

</details>

---

<a id="prompt-library"></a>

## 🧾 プロンプトライブラリ

プロンプトと入力テキストは、ユースケース分類とは分けて掲載します。

Prompt-bearing community entries: **35**.

- [Community Use Case 1: Japanese no-makeup image edit instruction](#community-usecase-1)
  - Source: [post](https://x.com/renataro9/status/2075059699112652908) by [@renataro9](https://x.com/renataro9)

- [Community Use Case 2: Localized anime edit preserving composition while changing one subject](#community-usecase-2)
  - Source: [post](https://x.com/haruuraeadss/status/2075035201391255593) by [@haruuraeadss](https://x.com/haruuraeadss)

- [Community Use Case 3: Image-input cat-to-mecha transformation](#community-usecase-3)
  - Source: [post](https://x.com/JennyAITech/status/2074870477651398972) by [@JennyAITech](https://x.com/JennyAITech)

- [Community Use Case 4: Trading terminal interface with market microstructure detail](#community-usecase-4)
  - Source: [post](https://x.com/MishikaAI/status/2074879603446026333) by [@MishikaAI](https://x.com/MishikaAI)

- [Community Use Case 5: Cyberpunk android graphic poster](#community-usecase-5)
  - Source: [post](https://x.com/ComfyUI/status/2075027793491226677) by [@ComfyUI](https://x.com/ComfyUI)

- [Community Use Case 6: Premium sports footwear commercial ad set](#community-usecase-6)
  - Source: [post](https://x.com/iamrealsnow/status/2075063569486598281) by [@iamrealsnow](https://x.com/iamrealsnow)

- [Community Use Case 7: Kids clay craft advertisement poster](#community-usecase-7)
  - Source: [post](https://x.com/Strength04_X/status/2075063250656621054) by [@Strength04_X](https://x.com/Strength04_X)

- [Community Use Case 8: Measurement-heavy technical blueprint rendering](#community-usecase-8)
  - Source: [post](https://x.com/LiamEtherson/status/2074862867442962667) by [@LiamEtherson](https://x.com/LiamEtherson)

- [Community Use Case 9: Concept car blueprint with exploded technical views](#community-usecase-9)
  - Source: [post](https://x.com/AiwithZohaib/status/2074880584107909602) by [@AiwithZohaib](https://x.com/AiwithZohaib)

- [Community Use Case 10: Shot-list driven grayscale scene planning](#community-usecase-10)
  - Source: [post](https://x.com/munzxsdv/status/2074865454485483885) by [@munzxsdv](https://x.com/munzxsdv)

- [Community Use Case 11: Single-prompt 16-panel cavalry storyboard](#community-usecase-11)
  - Source: [post](https://x.com/sulekhat95/status/2074966196563431636) by [@sulekhat95](https://x.com/sulekhat95)

- [Community Use Case 12: Fisheye editorial portraits with miniature clone motif](#community-usecase-12)
  - Source: [post](https://x.com/magnific/status/2074872903938846900) by [@magnific](https://x.com/magnific)

- [Community Use Case 13: Melting-world-landmarks concept generation](#community-usecase-13)
  - Source: [post](https://x.com/magnific/status/2074918700709523881) by [@magnific](https://x.com/magnific)

- [Community Use Case 14: Photorealistic high-fashion portrait lighting](#community-usecase-14)
  - Source: [post](https://x.com/BubbleBrain/status/2074856963591290979) by [@BubbleBrain](https://x.com/BubbleBrain)

- [Community Use Case 15: Natural phone-photo scene at San Francisco sunset](#community-usecase-15)
  - Source: [post](https://x.com/mattworkman/status/2074850550349222210) by [@mattworkman](https://x.com/mattworkman)

- [Community Use Case 16: Fantasy fallen-angel warrior key visual](#community-usecase-16)
  - Source: [post](https://x.com/SimplyAnnisa/status/2074900816662774189) by [@SimplyAnnisa](https://x.com/SimplyAnnisa)

- [Community Use Case 17: Japanese casual portrait styling set](#community-usecase-17)
  - Source: [post](https://x.com/Cia0_exe/status/2075033845032993261) by [@Cia0_exe](https://x.com/Cia0_exe)

- [Community Use Case 18: ARRI-style cinematic city close-up](#community-usecase-18)
  - Source: [post](https://x.com/df_reno/status/2075055332452106476) by [@df_reno](https://x.com/df_reno)

- [Community Use Case 19: Fashion outfit editorial set in a parking structure](#community-usecase-19)
  - Source: [post](https://x.com/ChillaiKalan__/status/2075071088137208063) by [@ChillaiKalan__](https://x.com/ChillaiKalan__)

- [Community Use Case 20: Iridescent glass-flower editorial poster](#community-usecase-20)
  - Source: [post](https://x.com/ComfyUI/status/2075027810666914062) by [@ComfyUI](https://x.com/ComfyUI)

- [Community Use Case 21: Anime skateboard sequence with multiple shot prompts](#community-usecase-21)
  - Source: [post](https://x.com/asatoucan/status/2075060881067769903) by [@asatoucan](https://x.com/asatoucan)

- [Community Use Case 22: Solar-powered desert research station concept](#community-usecase-22)
  - Source: [post](https://x.com/ashen_one/status/2074915677815886071) by [@ashen_one](https://x.com/ashen_one)

- [Community Use Case 23: Impossible-scale cinematic sci-fi worldbuilding set](#community-usecase-23)
  - Source: [post](https://x.com/AllaAisling/status/2075036565147906511) by [@AllaAisling](https://x.com/AllaAisling)

- [Community Use Case 24: Bedroom design variations for MBTI types](#community-usecase-24)
  - Source: [post](https://x.com/FloraTechAI/status/2074866317484794131) by [@FloraTechAI](https://x.com/FloraTechAI)

- [Community Use Case 25: Multi-task Seedream capability sampling from four Chinese prompts](#community-usecase-25)
  - Source: [post](https://x.com/op7418/status/2074862226905948549) by [@op7418](https://x.com/op7418)

- [Community Use Case 26: Seedream vs GPT Image 2 in realistic car selfie framing](#community-usecase-26)
  - Source: [post](https://x.com/johnAGI168/status/2074870910469677387) by [@johnAGI168](https://x.com/johnAGI168)

- [Community Use Case 27: Seedream vs GPT Image 2 for clean lifestyle portrait styling](#community-usecase-27)
  - Source: [post](https://x.com/liyue_ai/status/2074890690686005590) by [@liyue_ai](https://x.com/liyue_ai)

- [Community Use Case 28: Blueprint sports car comparison against GPT Image 2](#community-usecase-28)
  - Source: [post](https://x.com/marmaduke091/status/2074866077499105416) by [@marmaduke091](https://x.com/marmaduke091)

- [Community Use Case 29: Reference-image camera-angle change comparison](#community-usecase-29)
  - Source: [post](https://x.com/hasamaru_studio/status/2075052934409375918) by [@hasamaru_studio](https://x.com/hasamaru_studio)

- [Community Use Case 30: Oversized beverage-can advertising composition comparison](#community-usecase-30)
  - Source: [post](https://x.com/emmanuel_2m/status/2075000101362131350) by [@emmanuel_2m](https://x.com/emmanuel_2m)

- [Community Use Case 31: Chengdu travel scrapbook poster comparison](#community-usecase-31)
  - Source: [post](https://x.com/DeepBlueAIX/status/2074872447229419956) by [@DeepBlueAIX](https://x.com/DeepBlueAIX)

- [Community Use Case 32: Anime key-visual comparison](#community-usecase-32)
  - Source: [post](https://x.com/roco_kn_roco/status/2074890020260094137) by [@roco_kn_roco](https://x.com/roco_kn_roco)

- [Community Use Case 33: Travel-poster comparison with signature constraint](#community-usecase-33)
  - Source: [post](https://x.com/Bic_Revelation/status/2074959714366922857) by [@Bic_Revelation](https://x.com/Bic_Revelation)

- [Community Use Case 34: Fantasy village watermill comparison against GPT Image 2](#community-usecase-34)
  - Source: [post](https://x.com/emmanuel_2m/status/2075000114427375742) by [@emmanuel_2m](https://x.com/emmanuel_2m)

- [Community Use Case 35: Lake Como fashion scene comparison against Banana Pro](#community-usecase-35)
  - Source: [post](https://x.com/cso6709/status/2075046425277399261) by [@cso6709](https://x.com/cso6709)

<a id="model-notes"></a>

## 🧩 モデルメモ

| 項目 | 出典に基づくメモ |
|---|---|
| モデルID | 公式資料は `dola-seedream-5-0-pro-260628` を記載しています。これを初回実行証拠とするには、EvoLink runtime 検証がまだ必要です。 |
| 入力画像 | 公式資料では Seedream 5.0 Pro が最大10枚の入力画像をサポートすると説明されています。 |
| 出力解像度 | Pro で 4K を主張しないでください。ソース資料は `<= 2.36M` ピクセルと `> 2.36M` ピクセル付近の出力階層を説明しています。 |
| ネイティブ prompt 言語 | 公式資料はアラビア語、英語、ロシア語、インドネシア語、スペイン語、ドイツ語、トルコ語、ポルトガル語、マレー語、ベトナム語、フランス語、日本語、韓国語、タガログ語、タイ語を挙げています。 |
| Seedream から Seedance への経路 | 公式資料では、Seedream 5.0 Pro/Lite の出力が、アカウントとモデレーション条件のもとで Seedance 系の画像から動画へのワークフローの信頼済み入力になり得ると説明されています。 |

<a id="acknowledge"></a>

## 🙏 謝辞

このリポジトリは、2026年7月8日にエクスポートされた Seedream 5.0 Pro の公式ローンチ資料と、ケース一覧に関する公式修正から作成されました。

- 公式の非公開ソース URL はローカル監査証拠にのみ保持します。
- prompt ブロックは、公式資料が prompt テキストを提供している場合にのみ含めます。
- メディアのみのケースはメディアのみのままにし、不足する prompt は作りません。

*公開ケースの境界に修正が必要な場合は、具体的なソース証拠を添えて issue または patch を送ってください。*
