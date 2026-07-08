<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink 배너"></a>

# Awesome Seedream 5.0 Pro 가이드와 프롬프트

Seedream 5.0 Pro 이미지 생성 및 편집 워크플로를 평가하기 위한 출처 기반 가이드, 프롬프트 패턴, 시각 예시입니다.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![EvoLink에서 사용](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![API 키 받기](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 소개

Seedream 5.0 Pro는 공식 출시 자료에서 제어 가능한 이미지 생성 및 편집 모델로 설명됩니다. 이 가이드는 상호작용 제어, 스케치 편집, 레이어 편집, 앵커 위치 편집, 레이어 분리, 다중 이미지 융합, 시각 효과 샘플, 다국어 텍스트 렌더링이라는 공식 능력 메뉴에 README를 맞춥니다.

**이 저장소에서 공식 자료 기반 예시를 확인하고, 공식 자료에 실제로 있는 prompt만 복사하며, 각 능력 범주가 어떤 공개 case와 연결되는지 볼 수 있습니다.**

EvoLink 모델 진입점 사용해 보기: [EvoLink에서 Seedream 5.0 Pro 열기](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**빠른 시작:** 이 저장소는 EvoLink에서 Seedream 5.0 Pro 첫 실행 API 경로가 검증되었다고 주장하지 않습니다. 실행 증거가 기록되기 전까지는 공개 모델 진입점, API 키 대시보드, 공식 기술 레퍼런스를 사용하세요.

1. [Seedream 5.0 Pro EvoLink 경로 열기](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [공식 ModelArk 기술 레퍼런스 읽기](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> 출처 정책: 공식 출시 자료를 사용합니다. 비공개 Lark/Feishu URL은 로컬 감사 증거에만 보관하며 README의 공개 출처 페이지로 노출하지 않습니다.

<a id="news"></a>

## 📰 업데이트

- **July 8, 2026:** 공식 메뉴와 공식 수정된 case 목록을 기준으로 초기 가이드를 다시 구성했습니다.

<a id="menu"></a>

## 📑 메뉴

- [🍌 소개](#introduction)
- [📰 업데이트](#news)
- [📑 메뉴](#menu)
- [🎛️ 상호작용 제어](#interaction-control)
  - [Case 1: 공간 의도를 나타내는 화살표와 주석 박스](#case-1)
  - [Case 2: 대상 편집을 위한 영역 박스별 객체 설명](#case-2)
- [✏️ 스케치 편집](#sketch-editing)
  - [Case 3: 낙서 가이드 기반 객체 생성](#case-3)
  - [Case 4: 색 블록으로 가이드하는 편집](#case-4)
  - [Case 5: 선으로 가이드하는 디테일 편집](#case-5)
  - [Case 6: 간단한 스케치에서 정교한 이미지로](#case-6)
- [🧱 레이어 편집](#layer-editing)
  - [Case 7: 포스터 텍스트와 그래픽 레이어 편집: Avery Turns](#case-7)
  - [Case 8: 포스터 오퍼 레이어 편집: Happy Hour](#case-8)
  - [Case 9: 디자인 레이아웃 안의 패션 이미지 레이어 편집](#case-9)
  - [Case 10: 스포츠 포스터 그래픽 레이어 편집](#case-10)
  - [Case 11: 포스터 요소 편집: Public Joy](#case-11)
  - [Case 12: 정확한 텍스처 반응을 통한 소재 표면 교체](#case-12)
- [📍 앵커 / 위치 편집](#anchor-position-editing)
  - [Case 13: 그리드 위치 기반 객체 이동](#case-13)
- [🧩 레이어 분리](#layer-separation)
  - [Case 14: 전경 / 인물 레이어 분리](#case-14)
- [🖼️ 다중 이미지 융합 편집](#multi-image-fusion-editing)
  - [Case 15: 7장 참조 이미지 입력/출력 정물 구성](#case-15)
- [🎬 시각 품질과 내러티브](#visual-quality-narrative)
  - [Case 16: 유리가 깨지는 시네마틱 테니스 장면](#case-16)
  - [Case 17: 시네마틱 복싱 액션](#case-17)
  - [Case 18: 3D 애니메이션 스타일 장면](#case-18)
  - [Case 19: 시각 콘셉트 아트](#case-19)
  - [Case 20: 게임 장면 비주얼](#case-20)
- [🌐 다국어 텍스트 렌더링](#multilingual-text-rendering)
  - [Case 21: 아랍어와 영어 환영 표지](#case-21)
  - [Case 22: 한국어 24시간 영업 표지](#case-22)
  - [Case 23: 태국어 청결 유지 표지](#case-23)
  - [Case 24: 프랑스어 창작 포스터](#case-24)
  - [Case 25: 러시아어 미래 포스터](#case-25)
- [🧩 모델 노트](#model-notes)
- [🙏 감사의 말](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ 상호작용 제어

박스, 점, 화살표, 주석 표시, 좌표를 사용해 대상 영역을 지정합니다.

케이스 수: **2**.

<a id="case-1"></a>

### Case 1: 공간 의도를 나타내는 화살표와 주석 박스

<img src="assets/media/003-arrows-annotation-boxes.gif" width="720" alt="공간 의도를 나타내는 화살표와 주석 박스">

> [!NOTE]
> 편집 전에 화살표, 박스, 주석으로 대상 영역을 명확히 표시합니다.

---

<a id="case-2"></a>

### Case 2: 대상 편집을 위한 영역 박스별 객체 설명

<img src="assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="대상 편집을 위한 영역 박스별 객체 설명">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ 스케치 편집

낙서, 색 블록, 선, 간단한 스케치를 시각 가이드로 사용합니다.

케이스 수: **4**.

<a id="case-3"></a>

### Case 3: 낙서 가이드 기반 객체 생성

<img src="assets/media/005-doodles.gif" width="720" alt="낙서 가이드 기반 객체 생성">

> [!NOTE]
> 느슨한 낙서를 시각 제어 신호로 사용해 모델이 의도한 객체를 렌더링하게 합니다.

---

<a id="case-4"></a>

### Case 4: 색 블록으로 가이드하는 편집

<img src="assets/media/006-color-block.gif" width="720" alt="색 블록으로 가이드하는 편집">

> [!NOTE]
> 넓은 색 블록으로 대략적인 구성, 색 영역, 객체 배치를 지정합니다.

---

<a id="case-5"></a>

### Case 5: 선으로 가이드하는 디테일 편집

<img src="assets/media/007-lines.gif" width="720" alt="선으로 가이드하는 디테일 편집">

> [!NOTE]
> 긴 텍스트 설명보다 형태 경계가 중요할 때 간단한 선 가이드를 사용합니다.

---

<a id="case-6"></a>

### Case 6: 간단한 스케치에서 정교한 이미지로

<img src="assets/media/008-simple-sketches.gif" width="720" alt="간단한 스케치에서 정교한 이미지로">

> [!NOTE]
> 스케치의 의도를 유지하면서 최소한의 스케치를 더 완성도 높은 렌더링 이미지로 바꿉니다.

---

<a id="layer-editing"></a>

## 🧱 레이어 편집

포스터, 그래픽, 텍스트, 소재, 표면 레이어를 전체 구성을 유지한 채 편집합니다.

케이스 수: **6**.

<a id="case-7"></a>

### Case 7: 포스터 텍스트와 그래픽 레이어 편집: Avery Turns

<img src="assets/media/009-Feishu-Docs-Image.gif" width="720" alt="포스터 텍스트와 그래픽 레이어 편집: Avery Turns">

> [!NOTE]
> 전체 디자인 구조를 유지하면서 포스터의 보이는 요소를 편집합니다.

---

<a id="case-8"></a>

### Case 8: 포스터 오퍼 레이어 편집: Happy Hour

<img src="assets/media/010-Feishu-Docs-Image.gif" width="720" alt="포스터 오퍼 레이어 편집: Happy Hour">

> [!NOTE]
> 포스터 전체를 다시 만들지 않고 프로모션 배지나 그래픽 요소를 변경합니다.

---

<a id="case-9"></a>

### Case 9: 디자인 레이아웃 안의 패션 이미지 레이어 편집

<img src="assets/media/011-Feishu-Docs-Image.gif" width="720" alt="디자인 레이아웃 안의 패션 이미지 레이어 편집">

> [!NOTE]
> 구성된 시각 레이아웃 안의 레이어화된 피사체를 조정합니다.

---

<a id="case-10"></a>

### Case 10: 스포츠 포스터 그래픽 레이어 편집

<img src="assets/media/012-Feishu-Docs-Image.gif" width="720" alt="스포츠 포스터 그래픽 레이어 편집">

> [!NOTE]
> 타이포그래피와 구성을 맞춘 상태로 레이싱 포스터 그래픽을 편집합니다.

---

<a id="case-11"></a>

### Case 11: 포스터 요소 편집: Public Joy

<img src="assets/media/013-Feishu-Docs-Image.gif" width="720" alt="포스터 요소 편집: Public Joy">

> [!NOTE]
> 원본 디자인 언어를 유지하면서 포스터 요소를 수정합니다.

---

<a id="case-12"></a>

### Case 12: 정확한 텍스처 반응을 통한 소재 표면 교체

<img src="assets/media/014-Feishu-Docs-Image.gif" width="720" alt="정확한 텍스처 반응을 통한 소재 표면 교체">

> [!NOTE]
> 객체 구조를 유지한 채 소재와 색상 대상을 교체합니다.

---

<a id="anchor-position-editing"></a>

## 📍 앵커 / 위치 편집

그리드형 앵커나 상대 위치를 사용해 특정 대상을 정확히 이동합니다.

케이스 수: **1**.

<a id="case-13"></a>

### Case 13: 그리드 위치 기반 객체 이동

<table>
<tr>
<td width="50%" valign="top">

**변경 전:**

<img src="assets/media/015-Feishu-Docs-Image.png" width="420" alt="그리드 위치 기반 객체 이동 변경 전">

</td>
<td width="50%" valign="top">

**변경 후:**

<img src="assets/media/016-Feishu-Docs-Image.png" width="420" alt="그리드 위치 기반 객체 이동 변경 후">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 레이어 분리

전경, 배경, 재사용 가능한 구성 요소를 분리해 후속 편집에 사용합니다.

케이스 수: **1**.

<a id="case-14"></a>

### Case 14: 전경 / 인물 레이어 분리

<img src="assets/media/017-Feishu-Docs-Image.png" width="720" alt="전경 / 인물 레이어 분리">

> [!NOTE]
> 나중에 재사용할 수 있도록 포스터형 배경에서 전경 피사체를 분리합니다.

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ 다중 이미지 융합 편집

여러 참조 이미지를 하나의 지시에 따라 일관된 구성으로 결합합니다.

케이스 수: **1**.

<a id="case-15"></a>

### Case 15: 7장 참조 이미지 입력/출력 정물 구성

<table>
<tr>
<td width="50%" valign="top">

**입력:**

<img src="assets/media/018-Feishu-Docs-Image.png" width="420" alt="7장 참조 이미지 정물 구성 입력">

</td>
<td width="50%" valign="top">

**출력:**

<img src="assets/media/019-Feishu-Docs-Image.png" width="420" alt="7장 참조 이미지 정물 구성 출력">

</td>
</tr>
</table>

> [!NOTE]
> 흰 배경의 7장 참조 이미지를 입력 그룹으로 사용하고, 같은 짝지어진 case 안에서 정물 사진 출력을 생성합니다.


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 시각 품질과 내러티브

효과 샘플을 시네마틱 액션, 3D / 애니메이션, 콘셉트 아트, 게임 장면 출력으로 분류합니다.

케이스 수: **5**.

<a id="case-16"></a>

### Case 16: 유리가 깨지는 시네마틱 테니스 장면

<img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="유리가 깨지는 시네마틱 테니스 장면">

> [!NOTE]
> 유리 파편, 액션 타이밍, 영화적 조명을 포함한 고동작 장면 생성.

---

<a id="case-17"></a>

### Case 17: 시네마틱 복싱 액션

<img src="assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="시네마틱 복싱 액션">

> [!NOTE]
> 움직임, 충격감, 장면 깊이가 더 강한 액션 장면 렌더링.

---

<a id="case-18"></a>

### Case 18: 3D 애니메이션 스타일 장면

<img src="assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="3D 애니메이션 스타일 장면">

> [!NOTE]
> 캐릭터나 엔터테인먼트 비주얼을 위한 스타일화된 3D / 애니메이션 출력.

---

<a id="case-19"></a>

### Case 19: 시각 콘셉트 아트

<img src="assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="시각 콘셉트 아트">

> [!NOTE]
> 분위기, 시각 방향성, 무드 탐색을 위한 콘셉트 아트 스타일 생성.

---

<a id="case-20"></a>

### Case 20: 게임 장면 비주얼

<img src="assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="게임 장면 비주얼">

> [!NOTE]
> 환경, 세트, 키아트 탐색을 위한 게임형 장면 생성.

---

<a id="multilingual-text-rendering"></a>

## 🌐 다국어 텍스트 렌더링

다국어 샘플을 렌더링 언어와 로컬 텍스트 사용 사례별로 분류합니다.

케이스 수: **5**.

<a id="case-21"></a>

### Case 21: 아랍어와 영어 환영 표지

<img src="assets/media/025-Welcome.png" width="720" alt="아랍어와 영어 환영 표지">

> [!NOTE]
> 같은 비주얼 안에서 아랍어와 영어 텍스트를 네이티브하게 다국어 렌더링합니다.

---

<a id="case-22"></a>

### Case 22: 한국어 24시간 영업 표지

<img src="assets/media/026-24-Open-24-hours.png" width="720" alt="한국어 24시간 영업 표지">

> [!NOTE]
> 현지화된 매장이나 표지 콘텐츠를 위한 한국어 텍스트 렌더링.

---

<a id="case-23"></a>

### Case 23: 태국어 청결 유지 표지

<img src="assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="태국어 청결 유지 표지">

> [!NOTE]
> 지역 공공 공간이나 캠페인 비주얼을 위한 태국어 텍스트 렌더링.

---

<a id="case-24"></a>

### Case 24: 프랑스어 창작 포스터

<img src="assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="프랑스어 창작 포스터">

> [!NOTE]
> 제품, 패션, 캠페인 자산을 위한 프랑스어 텍스트 렌더링.

---

<a id="case-25"></a>

### Case 25: 러시아어 미래 포스터

<img src="assets/media/029-Future.png" width="720" alt="러시아어 미래 포스터">

> [!NOTE]
> 현지화된 비주얼 콘셉트를 위해 명확한 문자 구조로 러시아어를 렌더링합니다.

---

<a id="model-notes"></a>

## 🧩 모델 노트

| 항목 | 출처 기반 메모 |
|---|---|
| 모델 ID | 공식 자료에는 `dola-seedream-5-0-pro-260628`가 기재되어 있습니다. 이것이 첫 실행 증거가 되려면 EvoLink runtime 검증이 아직 필요합니다. |
| 입력 이미지 | 공식 자료에 따르면 Seedream 5.0 Pro는 최대 10장의 입력 이미지를 지원합니다. |
| 출력 해상도 | Pro에 대해 4K를 주장하지 마세요. 소스 자료는 `<= 2.36M` 픽셀 및 `> 2.36M` 픽셀 부근의 출력 티어를 설명합니다. |
| 네이티브 prompt 언어 | 공식 자료는 아랍어, 영어, 러시아어, 인도네시아어, 스페인어, 독일어, 터키어, 포르투갈어, 말레이어, 베트남어, 프랑스어, 일본어, 한국어, 타갈로그어, 태국어를 나열합니다. |
| Seedream에서 Seedance로의 경로 | 공식 자료에 따르면 Seedream 5.0 Pro/Lite 출력은 계정 및 모더레이션 조건하에서 Seedance 계열 이미지-투-비디오 워크플로의 신뢰 입력이 될 수 있습니다. |

<a id="acknowledge"></a>

## 🙏 감사의 말

이 저장소는 2026년 7월 8일에 내보낸 Seedream 5.0 Pro 공식 출시 자료와 case 목록에 대한 공식 수정 사항을 기반으로 만들어졌습니다.

- 공식 비공개 출처 URL은 로컬 감사 증거에만 보관합니다.
- prompt 블록은 공식 자료가 prompt 텍스트를 제공하는 경우에만 포함합니다.
- 미디어만 있는 case는 그대로 미디어만 유지하며, 누락된 prompt를 만들어내지 않습니다.

*공개 case 경계를 수정해야 한다면 구체적인 소스 증거와 함께 issue를 열거나 patch를 보내 주세요.*
