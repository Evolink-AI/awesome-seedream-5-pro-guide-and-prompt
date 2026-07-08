<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Руководство с источниками, шаблоны промптов и визуальные примеры для оценки рабочих процессов генерации и редактирования изображений Seedream 5.0 Pro.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Введение

В официальных материалах запуска Seedream 5.0 Pro представлен как модель генерации и редактирования изображений для управляемого визуального производства. Материалы подчеркивают редактирование по областям, редактирование по эскизам, позиционирование по якорям, разделение слоев, контроль материалов и цвета, композицию по нескольким референсам, кинематографичные изображения и многоязычный рендеринг текста.

Этот репозиторий является поверхностью **руководства и промптов**. Он собирает подтвержденные источниками шаблоны промптов и медиа-примеры в одном месте, чтобы разработчики могли понять, что тестировать, копировать только промпты из исходного материала и переходить к маршруту конверсии EvoLink при наличии доступа.

Открыть точку входа модели на EvoLink: [Открыть путь Seedream 5.0 Pro на EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Быстрый старт:** этот репозиторий не утверждает, что маршрут первого API-запуска EvoLink для Seedream 5.0 Pro был проверен. Используйте этот путь как публичный маршрут конверсии, пока не будет зафиксировано доказательство выполнения текущей модели:

1. [Открыть EvoLink для доступа к Seedream 5.0 Pro](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Получить API-ключ EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. Использовать официальную справку ModelArk как технический контекст: [Прочитать документацию ModelArk для Seedream 5.0 Pro](https://docs.byteplus.com/en/docs/ModelArk/1541523).

Статус выполнения: официальные материалы называют `dola-seedream-5-0-pro-260628` ID модели Seedream 5.0 Pro, но этот репозиторий не проходил EvoLink API smoke test с расходом кредитов. Не считайте примеры соседних моделей изображений проверенным доказательством первого запуска Seedream 5.0 Pro.

<a id="news"></a>

## 📰 Новости

- **2026-07-08:** Первоначальный локальный scaffold создан на основе официальных материалов запуска Seedream 5.0 Pro и экспорта медиа.

<a id="menu"></a>

## 📑 Меню

- [🍌 Введение](#introduction)
- [📰 Новости](#news)
- [📑 Меню](#menu)
- [🎛️ Шаблоны промптов для управляемого редактирования](#controlled-editing-prompt-patterns)
  - [Case 1: Описание объектов по региональным рамкам для целевого редактирования](#case-1)
  - [Case 2: Редактирование позиции якоря в сцене, похожей на сетку](#case-2)
  - [Case 3: Натюрмортная композиция с несколькими референсами](#case-3)
- [🎬 Визуальная галерея возможностей](#visual-capability-gallery)
- [🧩 Заметки о модели](#model-notes)
- [🙏 Благодарности](#acknowledge)

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ Шаблоны промптов для управляемого редактирования

Приведенные ниже кейсы не являются выдуманными примерами. Они скопированы или переведены из официальных исходных материалов Seedream 5.0 Pro, кратко описанных в `docs/source-notes.md`.

<a id="case-1"></a>

### Case 1: [Описание объектов по региональным рамкам для целевого редактирования](docs/source-notes.md#included-public-cases)

<table>
  <tr>
    <td width="50%" valign="top"><img src="assets/media/003-arrows-annotation-boxes.gif" alt="Interaction arrows and annotation boxes"></td>
    <td width="50%" valign="top"><img src="assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" alt="Region-box annotation example"></td>
  </tr>
</table>

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: Official.

<a id="case-2"></a>

### Case 2: [Редактирование позиции якоря в сцене, похожей на сетку](docs/source-notes.md#included-public-cases)

<table>
  <tr>
    <td width="50%" valign="top"><strong>До</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>После</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: Official.

<a id="case-3"></a>

### Case 3: [Натюрмортная композиция с несколькими референсами](docs/source-notes.md#included-public-cases)

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.gif)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: Official.

<a id="visual-capability-gallery"></a>

## 🎬 Визуальная галерея возможностей

Официальные материалы включают дополнительные визуальные образцы для редактирования по эскизам, разделения слоев, кинематографичных сюжетных изображений и многоязычного рендеринга текста.

<table>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Каракули по эскизу</a></strong><br><img src="assets/media/005-doodles.gif" alt="Каракули по эскизу example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Цветовой блок по эскизу</a></strong><br><img src="assets/media/006-color-block.gif" alt="Цветовой блок по эскизу example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Линии по эскизу</a></strong><br><img src="assets/media/007-lines.gif" alt="Линии по эскизу example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Управление простым эскизом</a></strong><br><img src="assets/media/008-simple-sketches.gif" alt="Управление простым эскизом example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Пример разделения слоев</a></strong><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Пример разделения слоев"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Вариант разделения слоев</a></strong><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Вариант разделения слоев"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Кинематографичный теннис с разбитым стеклом</a></strong><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Кинематографичный теннис с разбитым стеклом"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Кинематографичный боксерский экшен</a></strong><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Кинематографичный боксерский экшен"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Рендеринг арабского и английского текста</a></strong><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Рендеринг корейского текста</a></strong><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 Заметки о модели

| Раздел | Заметка с источником |
|---|---|
| ID модели | В официальных материалах указан `dola-seedream-5-0-pro-260628`; перед тем как считать это доказательством первого запуска, все еще требуется проверка выполнения в EvoLink. |
| Входные изображения | Исходный материал говорит, что Seedream 5.0 Pro поддерживает до 10 входных изображений. |
| Разрешение вывода | Исходный материал говорит, что публичное позиционирование не должно заявлять 4K для Pro; оно описывает уровни вывода около <= 2,36 млн пикселей и > 2,36 млн пикселей. |
| Нативные языки промптов | Исходный материал перечисляет арабский, английский, русский, индонезийский, испанский, немецкий, турецкий, португальский, малайский, вьетнамский, французский, японский, корейский, тагальский и тайский языки. |
| Путь от Seedream к Seedance | Исходный материал говорит, что выходы Seedream 5.0 Pro/Lite могут стать доверенными входами для image-to-video workflows семейства Seedance при соблюдении условий аккаунта и модерации. |

<a id="acknowledge"></a>

## 🙏 Благодарности

Этот репозиторий создан на основе официальных материалов запуска Seedream 5.0 Pro, экспортированных 2026-07-08.

- Публичная заметка о происхождении: `docs/source-notes.md`
- Приватный URL источника: записан в локальных аудиторских доказательствах и не раскрыт как публичная ссылка README.
- Заметка о запуске: в этом аудите репозитория не выполнялся EvoLink API smoke test с расходом кредитов.
