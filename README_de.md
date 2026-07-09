<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink-Banner"></a>

# Awesome Seedream 5.0 Pro Guide und Prompts

Quellengestützter Guide, Prompt-Muster und visuelle Beispiele zur Bewertung von Seedream 5.0 Pro Workflows für Bildgenerierung und Bildbearbeitung.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Auf EvoLink nutzen](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![API-Key abrufen](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Einführung

Seedream 5.0 Pro wird im offiziellen Launch-Material als steuerbares Modell für Bildgenerierung und Bildbearbeitung beschrieben. Dieser Guide richtet das öffentliche README am offiziellen Fähigkeitsmenü aus: Interaktionssteuerung, Skizzenbearbeitung, Ebenenbearbeitung, Anker-/Positionsbearbeitung, Ebenentrennung, Multi-Image-Fusion, visuelle Effektbeispiele und mehrsprachiges Textrendering.

**Nutze dieses Repository, um quellengestützte Beispiele zu prüfen, nur die im offiziellen Material vorhandenen Prompts zu kopieren und die Zuordnung von Kategorien zu sichtbaren Cases zu verstehen.**

Teste den Modelleinstieg auf EvoLink: [Seedream 5.0 Pro auf EvoLink öffnen](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Schnellstart:** Dieses Repository behauptet nicht, dass eine EvoLink-First-Run-API-Route für Seedream 5.0 Pro verifiziert wurde. Nutze bis zum Runtime-Nachweis den öffentlichen Modelleinstieg, das API-Key-Dashboard und die offizielle technische Referenz.

1. [Seedream 5.0 Pro EvoLink-Pfad öffnen](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API-Key abrufen](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [Offizielle ModelArk-Technikreferenz lesen](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> Quellenrichtlinie: offizielles Einführungsmaterial. Private Lark/Feishu-URLs bleiben nur in lokalen Prüfnachweisen und werden nicht als öffentliche README-Quellseiten veröffentlicht.

<a id="news"></a>

## 📰 Neuigkeiten

- **July 8, 2026:** Erster Guide anhand des offiziellen Menüs und des offiziell korrigierten Case-Inventars neu aufgebaut.

<a id="menu"></a>

## 📑 Menü

- [🍌 Einführung](#introduction)
- [📰 Neuigkeiten](#news)
- [📑 Menü](#menu)
- [🎛️ Interaktionssteuerung](#interaction-control)
  - [Case 1: Pfeile und Anmerkungsboxen für räumliche Absicht](#case-1)
  - [Case 2: Objektbeschreibung nach Bereichsboxen für gezielte Bearbeitung](#case-2)
- [✏️ Skizzenbearbeitung](#sketch-editing)
  - [Case 3: Objektgenerierung mit Doodle-Vorgabe](#case-3)
  - [Case 4: Bearbeitung mit Farbblock-Vorgabe](#case-4)
  - [Case 5: Detailbearbeitung mit Linienvorgabe](#case-5)
  - [Case 6: Von einfacher Skizze zu verfeinertem Bild](#case-6)
- [🧱 Ebenenbearbeitung](#layer-editing)
  - [Case 7: Text- und Grafikebenen im Poster bearbeiten: Avery Turns](#case-7)
  - [Case 8: Angebots-Ebene im Poster bearbeiten: Happy Hour](#case-8)
  - [Case 9: Modebild-Ebene innerhalb eines Designlayouts bearbeiten](#case-9)
  - [Case 10: Grafikebene eines Sportposters bearbeiten](#case-10)
  - [Case 11: Posterelement bearbeiten: Public Joy](#case-11)
  - [Case 12: Materialoberfläche mit präziser Texturreaktion austauschen](#case-12)
- [📍 Anker- / Positionsbearbeitung](#anchor-position-editing)
  - [Case 13: Objektbewegung anhand einer Rasterposition](#case-13)
- [🧩 Ebenentrennung](#layer-separation)
  - [Case 14: Vordergrund-/Personenebene trennen](#case-14)
- [🖼️ Multi-Image-Fusion-Bearbeitung](#multi-image-fusion-editing)
  - [Case 15: Stillleben-Komposition mit sieben Referenzen als Input/Output](#case-15)
- [🎬 Visuelle Qualität und Narrativ](#visual-quality-narrative)
  - [Case 16: Filmische Tennisszene mit splitterndem Glas](#case-16)
  - [Case 17: Filmische Boxaktion](#case-17)
  - [Case 18: Szene im 3D-Animationsstil](#case-18)
  - [Case 19: Visuelle Concept Art](#case-19)
  - [Case 20: Game-Scene-Visual](#case-20)
- [🌐 Mehrsprachiges Textrendering](#multilingual-text-rendering)
  - [Case 21: Willkommensschild auf Arabisch und Englisch](#case-21)
  - [Case 22: Koreanisches 24-Stunden-geöffnet-Schild](#case-22)
  - [Case 23: Thailändisches Sauberkeitsschild](#case-23)
  - [Case 24: Französisches Creation-Poster](#case-24)
  - [Case 25: Russisches Zukunftsposter](#case-25)
- [🧩 Modellnotizen](#model-notes)
- [🙏 Danksagung](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ Interaktionssteuerung

Verwende Boxen, Punkte, Pfeile, Anmerkungsmarkierungen oder Koordinaten, um den Zielbereich festzulegen.

Case-Anzahl: **2**.

<a id="case-1"></a>

### Case 1: Pfeile und Anmerkungsboxen für räumliche Absicht

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif?v=20260709-camo" width="720" alt="Pfeile und Anmerkungsboxen für räumliche Absicht">

> [!NOTE]
> Markiere den Zielbereich vor der Bearbeitung explizit mit Pfeilen, Boxen und Anmerkungen.

---

<a id="case-2"></a>

### Case 2: Objektbeschreibung nach Bereichsboxen für gezielte Bearbeitung

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="Objektbeschreibung nach Bereichsboxen für gezielte Bearbeitung">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ Skizzenbearbeitung

Nutze Doodles, Farbblöcke, Linien oder einfache Skizzen als visuelle Vorgabe.

Case-Anzahl: **4**.

<a id="case-3"></a>

### Case 3: Objektgenerierung mit Doodle-Vorgabe

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif?v=20260709-camo" width="720" alt="Objektgenerierung mit Doodle-Vorgabe">

> [!NOTE]
> Verwende grobe Doodles als visuelles Steuersignal und lasse das Modell das beabsichtigte Objekt rendern.

---

<a id="case-4"></a>

### Case 4: Bearbeitung mit Farbblock-Vorgabe

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif?v=20260709-camo" width="720" alt="Bearbeitung mit Farbblock-Vorgabe">

> [!NOTE]
> Nutze breite Farbblöcke, um grobe Komposition, Farbzonen oder Objektplatzierung festzulegen.

---

<a id="case-5"></a>

### Case 5: Detailbearbeitung mit Linienvorgabe

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif?v=20260709-camo" width="720" alt="Detailbearbeitung mit Linienvorgabe">

> [!NOTE]
> Verwende einfache Linienvorgaben, wenn die Formgrenze wichtiger ist als eine lange Textbeschreibung.

---

<a id="case-6"></a>

### Case 6: Von einfacher Skizze zu verfeinertem Bild

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif?v=20260709-camo" width="720" alt="Von einfacher Skizze zu verfeinertem Bild">

> [!NOTE]
> Wandle eine minimale Skizze in ein vollständiger gerendertes Bild um, ohne die Skizzenabsicht zu verlieren.

---

<a id="layer-editing"></a>

## 🧱 Ebenenbearbeitung

Bearbeite Poster-, Grafik-, Text-, Material- oder Oberflächenebenen, während die größere Komposition erhalten bleibt.

Case-Anzahl: **6**.

<a id="case-7"></a>

### Case 7: Text- und Grafikebenen im Poster bearbeiten: Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" width="720" alt="Text- und Grafikebenen im Poster bearbeiten: Avery Turns">

> [!NOTE]
> Bearbeite sichtbare Posterelemente, während die gesamte Designstruktur erhalten bleibt.

---

<a id="case-8"></a>

### Case 8: Angebots-Ebene im Poster bearbeiten: Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="Angebots-Ebene im Poster bearbeiten: Happy Hour">

> [!NOTE]
> Ändere ein Promotion-Badge oder Grafikelement, ohne das ganze Poster neu aufzubauen.

---

<a id="case-9"></a>

### Case 9: Modebild-Ebene innerhalb eines Designlayouts bearbeiten

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" width="720" alt="Modebild-Ebene innerhalb eines Designlayouts bearbeiten">

> [!NOTE]
> Passe ein geschichtetes Motiv innerhalb eines komponierten visuellen Layouts an.

---

<a id="case-10"></a>

### Case 10: Grafikebene eines Sportposters bearbeiten

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="Grafikebene eines Sportposters bearbeiten">

> [!NOTE]
> Bearbeite eine Racing-Poster-Grafik, während Typografie und Komposition ausgerichtet bleiben.

---

<a id="case-11"></a>

### Case 11: Posterelement bearbeiten: Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="Posterelement bearbeiten: Public Joy">

> [!NOTE]
> Ändere Posterelemente, während die ursprüngliche Designsprache erhalten bleibt.

---

<a id="case-12"></a>

### Case 12: Materialoberfläche mit präziser Texturreaktion austauschen

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif?v=20260709-camo2" width="720" alt="Materialoberfläche mit präziser Texturreaktion austauschen">

> [!NOTE]
> Tausche Material- und Farbziele aus, während die Objektstruktur intakt bleibt.

---

<a id="anchor-position-editing"></a>

## 📍 Anker- / Positionsbearbeitung

Nutze rasterartige Anker oder relative Positionen, um ein bestimmtes Ziel präzise zu verschieben.

Case-Anzahl: **1**.

<a id="case-13"></a>

### Case 13: Objektbewegung anhand einer Rasterposition

<table>
<tr>
<td width="50%" valign="top">

**Vorher:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" width="420" alt="Objektbewegung anhand einer Rasterposition vorher">

</td>
<td width="50%" valign="top">

**Nachher:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" width="420" alt="Objektbewegung anhand einer Rasterposition nachher">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 Ebenentrennung

Trenne Vordergrund, Hintergrund und wiederverwendbare Komponenten für nachgelagerte Bearbeitung.

Case-Anzahl: **1**.

<a id="case-14"></a>

### Case 14: Vordergrund-/Personenebene trennen

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" width="720" alt="Vordergrund-/Personenebene trennen">

> [!NOTE]
> Trenne ein Vordergrundmotiv von einem posterartigen Hintergrund, damit es später wiederverwendet werden kann.

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ Multi-Image-Fusion-Bearbeitung

Kombiniere mehrere Referenzbilder unter einer einzigen Anweisung zu einer kohärenten Komposition.

Case-Anzahl: **1**.

<a id="case-15"></a>

### Case 15: Stillleben-Komposition mit sieben Referenzen als Input/Output

<table>
<tr>
<td width="50%" valign="top">

**Input:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" width="420" alt="Stillleben-Komposition mit sieben Referenzen als Input">

</td>
<td width="50%" valign="top">

**Output:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" width="420" alt="Stillleben-Komposition mit sieben Referenzen als Output">

</td>
</tr>
</table>

> [!NOTE]
> Verwende die sieben Referenzen mit weißem Hintergrund als Input-Gruppe und generiere den Stillleben-Foto-Output in einem gepaarten Case.


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 Visuelle Qualität und Narrativ

Gruppiere die Effektbeispiele nach filmischer Action, 3D / Animation, Concept Art und Game-Scene-Output.

Case-Anzahl: **5**.

<a id="case-16"></a>

### Case 16: Filmische Tennisszene mit splitterndem Glas

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="Filmische Tennisszene mit splitterndem Glas">

> [!NOTE]
> High-Motion-Szenengenerierung mit Glassplittern, Action-Timing und filmischem Licht.

---

<a id="case-17"></a>

### Case 17: Filmische Boxaktion

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="Filmische Boxaktion">

> [!NOTE]
> Action-Szenen-Rendering mit stärkerem Bewegungsgefühl, Impact und Szenentiefe.

---

<a id="case-18"></a>

### Case 18: Szene im 3D-Animationsstil

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="Szene im 3D-Animationsstil">

> [!NOTE]
> Stilisierter 3D-/Animations-Output für Charaktere oder Entertainment-Visuals.

---

<a id="case-19"></a>

### Case 19: Visuelle Concept Art

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="Visuelle Concept Art">

> [!NOTE]
> Concept-Art-Generierung zur Erkundung von Atmosphäre, visueller Richtung und Stimmung.

---

<a id="case-20"></a>

### Case 20: Game-Scene-Visual

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="Game-Scene-Visual">

> [!NOTE]
> Spielartige Szenengenerierung für Umgebung, Set oder Key-Art-Erkundung.

---

<a id="multilingual-text-rendering"></a>

## 🌐 Mehrsprachiges Textrendering

Gruppiere mehrsprachige Beispiele nach gerenderter Sprache und lokalem Texteinsatz.

Case-Anzahl: **5**.

<a id="case-21"></a>

### Case 21: Willkommensschild auf Arabisch und Englisch

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" width="720" alt="Willkommensschild auf Arabisch und Englisch">

> [!NOTE]
> Natives mehrsprachiges Rendering mit arabischem und englischem Text im selben Visual.

---

<a id="case-22"></a>

### Case 22: Koreanisches 24-Stunden-geöffnet-Schild

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" width="720" alt="Koreanisches 24-Stunden-geöffnet-Schild">

> [!NOTE]
> Koreanisches Textrendering für lokalisierte Ladenfronten oder Beschilderung.

---

<a id="case-23"></a>

### Case 23: Thailändisches Sauberkeitsschild

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="Thailändisches Sauberkeitsschild">

> [!NOTE]
> Thailändisches Textrendering für lokale öffentliche Räume oder Kampagnenvisuals.

---

<a id="case-24"></a>

### Case 24: Französisches Creation-Poster

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="Französisches Creation-Poster">

> [!NOTE]
> Französisches Textrendering für Produkt-, Fashion- und Kampagnenassets.

---

<a id="case-25"></a>

### Case 25: Russisches Zukunftsposter

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" width="720" alt="Russisches Zukunftsposter">

> [!NOTE]
> Russisches Textrendering mit klarer Zeichenstruktur für lokalisierte visuelle Konzepte.

---

<a id="model-notes"></a>

## 🧩 Modellnotizen

| Bereich | Quellenbasierte Notiz |
|---|---|
| Modell-ID | Das offizielle Material nennt `dola-seedream-5-0-pro-260628`; eine EvoLink Runtime-Verifizierung ist noch erforderlich, bevor dies als First-Run-Evidenz gilt. |
| Eingabebilder | Laut offiziellem Material unterstützt Seedream 5.0 Pro bis zu 10 Eingabebilder. |
| Ausgabeauflösung | Für Pro nicht 4K behaupten; das Quellmaterial beschreibt Ausgabe-Tiers um `<= 2.36M` Pixel und `> 2.36M` Pixel. |
| Native Prompt-Sprachen | Das offizielle Material nennt Arabisch, Englisch, Russisch, Indonesisch, Spanisch, Deutsch, Türkisch, Portugiesisch, Malaiisch, Vietnamesisch, Französisch, Japanisch, Koreanisch, Tagalog und Thai. |
| Seedream-zu-Seedance-Pfad | Laut offiziellem Material können Ausgaben von Seedream 5.0 Pro/Lite unter Account- und Moderationsbedingungen zu vertrauenswürdigen Inputs für Seedance-Image-to-Video-Workflows werden. |

<a id="acknowledge"></a>

## 🙏 Danksagung

Dieses Repository wurde aus offiziellem Seedream 5.0 Pro Einführungsmaterial, exportiert am 8. Juli 2026, sowie aus offiziellen Korrekturen zum Case-Inventar erstellt.

- Offizielle private Quell-URLs werden nur in lokalen Prüfnachweisen aufbewahrt.
- Prompt-Blöcke werden nur dort aufgenommen, wo das offizielle Material Prompt-Text liefert.
- Nur-Media-Cases bleiben Nur-Media-Cases; fehlende Prompts werden nicht erfunden.

*Wenn eine öffentliche Case-Grenze korrigiert werden muss, öffne ein Issue oder sende einen Patch mit konkreter Quellen-Evidenz.*
