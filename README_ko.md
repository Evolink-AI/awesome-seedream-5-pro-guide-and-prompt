<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Seedream 5.0 Pro 이미지 생성 및 편집 워크플로를 평가하기 위한 출처 기반 가이드, 프롬프트 패턴, 시각 예시입니다.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 소개

Seedream 5.0 Pro는 공식 출시 자료에서 제어 가능한 시각 제작을 위한 이미지 생성 및 편집 모델로 소개됩니다. 자료는 영역 기반 편집, 스케치 기반 편집, 앵커 위치 지정, 레이어 분리, 재질과 색상 제어, 다중 참조 합성, 영화적 이미지, 다국어 텍스트 렌더링을 강조합니다.

이 저장소는 **가이드 및 프롬프트** 표면입니다. 출처 기반 프롬프트 패턴과 미디어 예시를 한곳에 모아, 빌더가 무엇을 테스트할지 검토하고 원본 자료에 등장하는 프롬프트만 복사하며 접근 가능 시 EvoLink 전환 경로로 이동할 수 있게 합니다.

EvoLink에서 모델 진입점 사용해 보기: [EvoLink Seedream 5.0 Pro 경로 열기](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**빠른 시작:** 이 저장소는 EvoLink Seedream 5.0 Pro의 첫 API 실행 경로가 검증되었다고 주장하지 않습니다. 현재 모델의 런타임 증거가 기록될 때까지 이 경로를 공개 전환 경로로 사용하세요:

1. [Seedream 5.0 Pro 접근을 위해 EvoLink 열기](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. 공식 ModelArk 레퍼런스를 기술 배경으로 보기: [Seedream 5.0 Pro ModelArk 문서 읽기](https://docs.byteplus.com/en/docs/ModelArk/1541523).

런타임 상태: 공식 자료는 `dola-seedream-5-0-pro-260628`을 Seedream 5.0 Pro 모델 ID로 명시하지만, 이 저장소는 크레딧을 소비하는 EvoLink API 스모크 테스트를 완료하지 않았습니다. 인접 이미지 모델 예시를 Seedream 5.0 Pro의 검증된 첫 실행 증거로 보지 마세요.

<a id="news"></a>

## 📰 뉴스

- **2026-07-08:** Seedream 5.0 Pro 공식 출시 자료와 미디어 내보내기를 바탕으로 초기 로컬 scaffold를 만들었습니다.

<a id="menu"></a>

## 📑 메뉴

- [🍌 소개](#introduction)
- [📰 뉴스](#news)
- [📑 메뉴](#menu)
- [🎛️ 제어 편집 프롬프트 패턴](#controlled-editing-prompt-patterns)
  - [Case 1: 대상 편집을 위한 영역 박스 객체 설명](#case-1)
  - [Case 2: 격자형 장면의 앵커 위치 편집](#case-2)
  - [Case 3: 다중 참조 정물 구성](#case-3)
- [🎬 시각 기능 갤러리](#visual-capability-gallery)
- [🧩 모델 노트](#model-notes)
- [🙏 감사의 말](#acknowledge)

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ 제어 편집 프롬프트 패턴

아래 case는 만들어낸 예시가 아닙니다. `docs/source-notes.md`에 요약된 공식 Seedream 5.0 Pro 원본 자료에서 복사하거나 번역한 것입니다.

<a id="case-1"></a>

### Case 1: [대상 편집을 위한 영역 박스 객체 설명](docs/source-notes.md#included-public-cases) (by [@官方](docs/source-notes.md))

![Region-box annotation example](assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.png)

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: 官方.

<a id="case-2"></a>

### Case 2: [격자형 장면의 앵커 위치 편집](docs/source-notes.md#included-public-cases) (by [@官方](docs/source-notes.md))

<table>
  <tr>
    <td width="50%" valign="top"><strong>이전</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>이후</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: 官方.

<a id="case-3"></a>

### Case 3: [다중 참조 정물 구성](docs/source-notes.md#included-public-cases) (by [@官方](docs/source-notes.md))

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.png)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: 官方.

<a id="visual-capability-gallery"></a>

## 🎬 시각 기능 갤러리

공식 자료에는 스케치 기반 편집, 레이어 분리, 영화적 내러티브 이미지, 다국어 텍스트 렌더링을 위한 추가 시각 샘플이 포함되어 있습니다.

<table>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">스케치 기반 낙서</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/005-doodles.png" alt="스케치 기반 낙서 example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">스케치 기반 색상 블록</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/006-color-block.png" alt="스케치 기반 색상 블록 example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">스케치 기반 선</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/007-lines.png" alt="스케치 기반 선 example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">간단한 스케치 제어</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/008-simple-sketches.png" alt="간단한 스케치 제어 example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">레이어 분리 예시</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="레이어 분리 예시"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">레이어 분리 변형</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="레이어 분리 변형"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">영화적 테니스 유리 파편</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="영화적 테니스 유리 파편"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">영화적 복싱 액션</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="영화적 복싱 액션"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">아랍어와 영어 텍스트 렌더링</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">한국어 텍스트 렌더링</a></strong> - by <a href="docs/source-notes.md">@官方</a><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 모델 노트

| 영역 | 출처 기반 노트 |
|---|---|
| 모델 ID | 공식 자료에는 `dola-seedream-5-0-pro-260628`이 명시되어 있으며, 이것이 첫 실행 증거가 되려면 EvoLink 런타임 검증이 여전히 필요합니다. |
| 입력 이미지 | 원본 자료는 Seedream 5.0 Pro가 최대 10개의 입력 이미지를 지원한다고 말합니다. |
| 출력 해상도 | 원본 자료는 Pro의 공개 포지셔닝에서 4K를 주장하지 말아야 한다고 하며, <= 2.36M 픽셀과 > 2.36M 픽셀 수준의 출력 구간을 설명합니다. |
| 기본 프롬프트 언어 | 원본 자료는 아랍어, 영어, 러시아어, 인도네시아어, 스페인어, 독일어, 터키어, 포르투갈어, 말레이어, 베트남어, 프랑스어, 일본어, 한국어, 타갈로그어, 태국어를 나열합니다. |
| Seedream에서 Seedance로의 경로 | 원본 자료는 계정 및 moderation 조건하에서 Seedream 5.0 Pro/Lite 출력이 Seedance 계열 image-to-video 워크플로의 신뢰 입력이 될 수 있다고 말합니다. |

<a id="acknowledge"></a>

## 🙏 감사의 말

이 저장소는 2026-07-08에 내보낸 Seedream 5.0 Pro 공식 출시 자료에서 만들어졌습니다.

- 공개 출처 노트: `docs/source-notes.md`
- 비공개 소스 URL: 로컬 감사 증거에 기록되며 README 공개 링크로 노출하지 않습니다.
- 실행 노트: 이 저장소 감사에서는 크레딧을 소비하는 EvoLink API 스모크 테스트를 실행하지 않았습니다.
