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
- [🧩 モデルメモ](#model-notes)
- [🙏 謝辞](#acknowledge)

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
