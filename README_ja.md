<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Seedream 5.0 Pro の画像生成と編集ワークフローを評価するための、出典付きガイド、プロンプトパターン、ビジュアル例です。

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 紹介

Seedream 5.0 Pro は、公式ローンチ資料で制御可能なビジュアル制作向けの画像生成・編集モデルとして紹介されています。資料では、領域指定編集、スケッチ誘導編集、アンカー配置、レイヤー分離、素材と色の制御、複数参照の合成、映画的な画像、多言語テキスト描画が強調されています。

このリポジトリは **guide and prompt** サーフェスです。出典に基づくプロンプトパターンとメディア例をまとめ、ビルダーが検証対象を確認し、ソース資料に存在するプロンプトだけをコピーし、アクセス可能になったときに EvoLink の変換経路へ進めるようにします。

EvoLink のモデル入口を試す: [EvoLink の Seedream 5.0 Pro パスを開く](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**クイックスタート:** このリポジトリは、EvoLink Seedream 5.0 Pro の初回 API 実行ルートが検証済みだとは主張しません。現行モデルの実行証拠が記録されるまで、この公開変換ルートを使用してください:

1. [Seedream 5.0 Pro へのアクセスのため EvoLink を開く](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API キーを取得する](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. 公式 ModelArk リファレンスを技術的背景として扱う: [Seedream 5.0 Pro の ModelArk ドキュメントを読む](https://docs.byteplus.com/en/docs/ModelArk/1541523).

実行状態: 公式資料では Seedream 5.0 Pro のモデル ID として `dola-seedream-5-0-pro-260628` が示されていますが、このリポジトリではクレジットを消費する EvoLink API スモークテストは完了していません。隣接する画像モデル例を Seedream 5.0 Pro の検証済み初回実行証拠として扱わないでください。

<a id="news"></a>

## 📰 ニュース

- **2026-07-08:** Seedream 5.0 Pro の公式ローンチ資料とメディアエクスポートから初期ローカル scaffold を作成しました。

<a id="menu"></a>

## 📑 メニュー

- [🍌 紹介](#introduction)
- [📰 ニュース](#news)
- [📑 メニュー](#menu)
- [🎛️ 制御編集プロンプトパターン](#controlled-editing-prompt-patterns)
  - [Case 1: 領域ボックスのオブジェクト説明によるターゲット編集](#case-1)
  - [Case 2: グリッド状シーンでのアンカー位置編集](#case-2)
  - [Case 3: 複数参照による静物構成](#case-3)
- [🎬 視覚機能ギャラリー](#visual-capability-gallery)
- [🧩 モデルノート](#model-notes)
- [🙏 謝辞](#acknowledge)

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ 制御編集プロンプトパターン

以下のケースは作成された架空例ではありません。`docs/source-notes.md` に要約された Seedream 5.0 Pro 公式ソース資料からコピーまたは翻訳されています。

<a id="case-1"></a>

### Case 1: [領域ボックスのオブジェクト説明によるターゲット編集](docs/source-notes.md#included-public-cases)

![Region-box annotation example](assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.png)

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: Official.

<a id="case-2"></a>

### Case 2: [グリッド状シーンでのアンカー位置編集](docs/source-notes.md#included-public-cases)

<table>
  <tr>
    <td width="50%" valign="top"><strong>前</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>後</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: Official.

<a id="case-3"></a>

### Case 3: [複数参照による静物構成](docs/source-notes.md#included-public-cases)

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.png)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: Official.

<a id="visual-capability-gallery"></a>

## 🎬 視覚機能ギャラリー

公式資料には、スケッチ誘導編集、レイヤー分離、映画的な物語画像、多言語テキスト描画の追加ビジュアルサンプルが含まれています。

<table>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">スケッチ誘導の落書き</a></strong><br><img src="assets/media/005-doodles.png" alt="Sketch-guided doodles example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">スケッチ誘導の色ブロック</a></strong><br><img src="assets/media/006-color-block.png" alt="Sketch-guided color block example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">スケッチ誘導の線</a></strong><br><img src="assets/media/007-lines.png" alt="Sketch-guided lines example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">シンプルスケッチ制御</a></strong><br><img src="assets/media/008-simple-sketches.png" alt="Simple sketch control example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">レイヤー分離の例</a></strong><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Layer separation example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">レイヤー分離のバリエーション</a></strong><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Layer separation variant"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">映画的なテニスとガラス破砕</a></strong><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Cinematic tennis glass shatter"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">映画的なボクシングアクション</a></strong><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Cinematic action boxing"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">アラビア語と英語のテキスト描画</a></strong><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">韓国語テキスト描画</a></strong><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 モデルノート

| 領域 | 出典に基づくノート |
|---|---|
| モデル ID | 公式資料には `dola-seedream-5-0-pro-260628` が記載されています。これを初回実行証拠とする前に、EvoLink の実行検証がまだ必要です。 |
| 入力画像 | ソース資料では、Seedream 5.0 Pro は最大 10 枚の入力画像をサポートするとされています。 |
| 出力解像度 | ソース資料では、Pro の公開ポジショニングで 4K を主張すべきではなく、出力段階は <= 2.36M ピクセルと > 2.36M ピクセル付近として説明されています。 |
| ネイティブプロンプト言語 | Source material lists Arabic, English, Russian, Indonesian, Spanish, German, Turkish, Portuguese, Malay, Vietnamese, French, Japanese, Korean, Tagalog, and Thai. |
| Seedream から Seedance への経路 | ソース資料では、アカウントとモデレーション条件のもとで、Seedream 5.0 Pro/Lite の出力が Seedance ファミリーの image-to-video ワークフローの信頼できる入力になり得るとされています。 |

<a id="acknowledge"></a>

## 🙏 謝辞

このリポジトリは、2026-07-08 にエクスポートされた Seedream 5.0 Pro の公式ローンチ資料から作成されました。

- 公開来歴ノート: `docs/source-notes.md`
- 非公開ソース URL: ローカル監査証拠に記録し、README の公開リンクとしては露出しません。
- 実行ノート: このリポジトリ監査では、クレジットを消費する EvoLink API スモークテストは実行されていません。
