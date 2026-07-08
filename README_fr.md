<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Guide sourcé, modèles de prompts et exemples visuels pour évaluer les workflows de génération et d’édition d’images avec Seedream 5.0 Pro.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Introduction

Seedream 5.0 Pro est présenté dans le matériel officiel de lancement comme un modèle de génération et d’édition d’images pour une production visuelle contrôlable. Le matériel met en avant les éditions dirigées par régions, l’édition guidée par croquis, le positionnement par ancres, la séparation de calques, le contrôle des matériaux et des couleurs, la composition multi-références, l’imagerie cinématographique et le rendu de texte multilingue.

Ce dépôt est une surface **guide et prompts**. Il réunit des modèles de prompts et des exemples média sourcés afin que les builders puissent inspecter quoi tester, copier uniquement les prompts présents dans le matériau source et avancer vers le parcours de conversion EvoLink lorsque l’accès est disponible.

Essayer le point d’entrée du modèle sur EvoLink: [Ouvrir le chemin Seedream 5.0 Pro sur EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Démarrage rapide:** ce dépôt ne prétend pas qu’une route API EvoLink de première exécution pour Seedream 5.0 Pro a été vérifiée. Utilisez ce chemin comme parcours public de conversion jusqu’à l’enregistrement d’une preuve d’exécution du modèle actuel:

1. [Ouvrir EvoLink pour accéder à Seedream 5.0 Pro](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Obtenir votre clé API EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. Utiliser la référence officielle ModelArk comme contexte technique: [Lire la documentation ModelArk de Seedream 5.0 Pro](https://docs.byteplus.com/en/docs/ModelArk/1541523).

État d’exécution : le matériel officiel nomme `dola-seedream-5-0-pro-260628` comme ID du modèle Seedream 5.0 Pro, mais ce dépôt n’a pas effectué de smoke test API EvoLink consommant des crédits. Ne considérez pas les exemples de modèles d’image adjacents comme une preuve vérifiée de première exécution pour Seedream 5.0 Pro.

<a id="news"></a>

## 📰 Actualités

- **2026-07-08:** Scaffold local initial créé à partir du matériel officiel de lancement de Seedream 5.0 Pro et de l’export média.

<a id="menu"></a>

## 📑 Menu

- [🍌 Introduction](#introduction)
- [📰 Actualités](#news)
- [📑 Menu](#menu)
- [🎛️ Modèles de prompts pour édition contrôlée](#controlled-editing-prompt-patterns)
  - [Case 1: Description d’objets par cadres de région pour édition ciblée](#case-1)
  - [Case 2: Édition par position d’ancre dans une scène en grille](#case-2)
  - [Case 3: Composition de nature morte multi-références](#case-3)
- [🎬 Galerie visuelle des capacités](#visual-capability-gallery)
- [🧩 Notes du modèle](#model-notes)
- [🙏 Remerciements](#acknowledge)

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ Modèles de prompts pour édition contrôlée


<a id="case-1"></a>

### Case 1: Description d’objets par cadres de région pour édition ciblée

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

### Case 2: Édition par position d’ancre dans une scène en grille

<table>
  <tr>
    <td width="50%" valign="top"><strong>Avant</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>Après</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: Official.

<a id="case-3"></a>

### Case 3: Composition de nature morte multi-références

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.gif)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: Official.

<a id="visual-capability-gallery"></a>

## 🎬 Galerie visuelle des capacités

Le matériel officiel inclut des échantillons visuels supplémentaires pour l’édition guidée par croquis, la séparation de calques, l’imagerie narrative cinématographique et le rendu de texte multilingue.

<table>
  <tr>
    <td width="50%" valign="top"><strong>Gribouillages guidés par croquis</strong><br><img src="assets/media/005-doodles.gif" alt="Gribouillages guidés par croquis example"></td>
    <td width="50%" valign="top"><strong>Bloc de couleur guidé par croquis</strong><br><img src="assets/media/006-color-block.gif" alt="Bloc de couleur guidé par croquis example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Lignes guidées par croquis</strong><br><img src="assets/media/007-lines.gif" alt="Lignes guidées par croquis example"></td>
    <td width="50%" valign="top"><strong>Contrôle par croquis simple</strong><br><img src="assets/media/008-simple-sketches.gif" alt="Contrôle par croquis simple example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Exemple de séparation de calques</strong><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Exemple de séparation de calques"></td>
    <td width="50%" valign="top"><strong>Variante de séparation de calques</strong><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Variante de séparation de calques"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Tennis cinématographique avec verre brisé</strong><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Tennis cinématographique avec verre brisé"></td>
    <td width="50%" valign="top"><strong>Action de boxe cinématographique</strong><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Action de boxe cinématographique"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Rendu de texte arabe et anglais</strong><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong>Rendu de texte coréen</strong><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 Notes du modèle

| Domaine | Note sourcée |
|---|---|
| ID du modèle | Le matériel officiel liste `dola-seedream-5-0-pro-260628`; une vérification d’exécution EvoLink reste nécessaire avant que cela devienne une preuve de première exécution. |
| Images d’entrée | Le matériel source indique que Seedream 5.0 Pro prend en charge jusqu’à 10 images d’entrée. |
| Résolution de sortie | Le matériel source indique que le positionnement public ne doit pas revendiquer la 4K pour Pro ; il décrit des niveaux de sortie autour de <= 2,36 M pixels et > 2,36 M pixels. |
| Langues natives des prompts | Le matériel source liste l’arabe, l’anglais, le russe, l’indonésien, l’espagnol, l’allemand, le turc, le portugais, le malais, le vietnamien, le français, le japonais, le coréen, le tagalog et le thaï. |
| Parcours de Seedream vers Seedance | Le matériel source indique que les sorties Seedream 5.0 Pro/Lite peuvent devenir des entrées fiables pour les workflows image-vers-vidéo de la famille Seedance, sous conditions de compte et de modération. |

<a id="acknowledge"></a>

## 🙏 Remerciements

Ce dépôt a été créé à partir du matériel officiel de lancement Seedream 5.0 Pro exporté le 2026-07-08.

- URL source privée : enregistrée dans les preuves d’audit locales, non exposée comme lien public du README.
- Note d’exécution : aucun test API EvoLink consommant des crédits n’a été exécuté dans cet audit du dépôt.
