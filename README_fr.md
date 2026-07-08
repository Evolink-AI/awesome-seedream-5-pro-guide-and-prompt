<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Bannière EvoLink Awesome Seedream 5.0 Pro"></a>

# Guide et prompts Awesome Seedream 5.0 Pro

Guide appuyé par les sources, modèles de prompt et exemples visuels pour évaluer les workflows de génération et d’édition d’images avec Seedream 5.0 Pro.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Utiliser sur EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Obtenir une clé API](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Présentation

Seedream 5.0 Pro est présenté dans le matériel officiel de lancement comme un modèle contrôlable de génération et d’édition d’images. Ce guide aligne le README public sur le menu officiel des capacités : contrôle d’interaction, édition par croquis, édition de calques, positionnement par ancre, séparation de calques, fusion multi-image, exemples d’effets visuels et rendu de texte multilingue.

**Utilisez ce dépôt pour inspecter des exemples appuyés par la source, copier uniquement les prompts présents dans le matériel officiel et comprendre comment chaque catégorie correspond aux cas visibles.**

Essayez le point d’entrée du modèle sur EvoLink : [ouvrir Seedream 5.0 Pro sur EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Démarrage rapide:** Ce dépôt ne prétend pas qu’une route API de première exécution EvoLink pour Seedream 5.0 Pro a été vérifiée. Utilisez l’entrée publique du modèle, le tableau de bord des clés API et la référence technique officielle jusqu’à ce qu’une preuve runtime soit enregistrée.

1. [Ouvrir le parcours Seedream 5.0 Pro sur EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Obtenir votre clé API EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [Lire la référence technique officielle ModelArk](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> Politique de source : matériel officiel de lancement. Les URL privées Lark/Feishu restent uniquement dans les preuves locales de vérification et ne sont pas exposées comme pages sources publiques dans le README.

<a id="news"></a>

## 📰 Actualités

- **July 8, 2026:** Guide initial reconstruit autour du menu officiel et de l’inventaire de cas corrigé officiellement.

<a id="menu"></a>

## 📑 Menu

- [🍌 Présentation](#introduction)
- [📰 Actualités](#news)
- [📑 Menu](#menu)
- [🎛️ Contrôle d’interaction](#interaction-control)
  - [Case 1: Flèches et boîtes d’annotation pour l’intention spatiale](#case-1)
  - [Case 2: Description d’objets par zones encadrées pour une édition ciblée](#case-2)
- [✏️ Édition par croquis](#sketch-editing)
  - [Case 3: Génération d’objet guidée par un gribouillage](#case-3)
  - [Case 4: Édition guidée par blocs de couleur](#case-4)
  - [Case 5: Édition de détail guidée par des lignes](#case-5)
  - [Case 6: Du croquis simple à l’image affinée](#case-6)
- [🧱 Édition de calques](#layer-editing)
  - [Case 7: Édition des calques texte et graphique d’un poster : Avery Turns](#case-7)
  - [Case 8: Édition du calque d’offre d’un poster : Happy Hour](#case-8)
  - [Case 9: Édition d’un calque d’image mode dans une mise en page](#case-9)
  - [Case 10: Édition du calque graphique d’un poster sportif](#case-10)
  - [Case 11: Édition d’élément de poster : Public Joy](#case-11)
  - [Case 12: Remplacement de surface matière avec réponse de texture précise](#case-12)
- [📍 Édition par ancre / position](#anchor-position-editing)
  - [Case 13: Déplacement d’objet par position de grille](#case-13)
- [🧩 Séparation de calques](#layer-separation)
  - [Case 14: Séparation du premier plan / de la personne](#case-14)
- [🖼️ Édition par fusion multi-image](#multi-image-fusion-editing)
  - [Case 15: Composition de nature morte entrée/sortie avec sept références](#case-15)
- [🎬 Qualité visuelle et narration](#visual-quality-narrative)
  - [Case 16: Tennis cinématographique avec verre brisé](#case-16)
  - [Case 17: Action de boxe cinématographique](#case-17)
  - [Case 18: Scène en style animation 3D](#case-18)
  - [Case 19: Art conceptuel visuel](#case-19)
  - [Case 20: Visuel de scène de jeu](#case-20)
- [🌐 Rendu de texte multilingue](#multilingual-text-rendering)
  - [Case 21: Panneau de bienvenue en arabe et anglais](#case-21)
  - [Case 22: Panneau coréen ouvert 24 h/24](#case-22)
  - [Case 23: Panneau thaï de propreté](#case-23)
  - [Case 24: Poster français de création](#case-24)
  - [Case 25: Poster russe du futur](#case-25)
- [🧩 Notes du modèle](#model-notes)
- [🙏 Remerciements](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ Contrôle d’interaction

Utilisez des boîtes, points, flèches, marques d’annotation ou coordonnées pour spécifier la zone cible.

Nombre de cas : **2**.

<a id="case-1"></a>

### Case 1: Flèches et boîtes d’annotation pour l’intention spatiale

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif" width="720" alt="Flèches et boîtes d’annotation pour l’intention spatiale">

> [!NOTE]
> Utilisez flèches, boîtes et annotations pour rendre la zone cible explicite avant l’édition.

---

<a id="case-2"></a>

### Case 2: Description d’objets par zones encadrées pour une édition ciblée

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="Description d’objets par zones encadrées pour une édition ciblée">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ Édition par croquis

Utilisez des gribouillages, blocs de couleur, lignes ou croquis simples comme guidage visuel.

Nombre de cas : **4**.

<a id="case-3"></a>

### Case 3: Génération d’objet guidée par un gribouillage

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif" width="720" alt="Génération d’objet guidée par un gribouillage">

> [!NOTE]
> Utilisez des gribouillages libres comme signal de contrôle visuel et laissez le modèle rendre l’objet voulu.

---

<a id="case-4"></a>

### Case 4: Édition guidée par blocs de couleur

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif" width="720" alt="Édition guidée par blocs de couleur">

> [!NOTE]
> Utilisez de grands blocs de couleur pour préciser la composition générale, les zones de couleur ou le placement des objets.

---

<a id="case-5"></a>

### Case 5: Édition de détail guidée par des lignes

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif" width="720" alt="Édition de détail guidée par des lignes">

> [!NOTE]
> Utilisez un guidage par lignes simples lorsque la limite de forme compte plus qu’une longue description textuelle.

---

<a id="case-6"></a>

### Case 6: Du croquis simple à l’image affinée

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif" width="720" alt="Du croquis simple à l’image affinée">

> [!NOTE]
> Transformez un croquis minimal en image rendue plus complète tout en conservant son intention.

---

<a id="layer-editing"></a>

## 🧱 Édition de calques

Modifiez des calques de poster, graphique, texte, matière ou surface tout en préservant la composition globale.

Nombre de cas : **6**.

<a id="case-7"></a>

### Case 7: Édition des calques texte et graphique d’un poster : Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" width="720" alt="Édition des calques texte et graphique d’un poster : Avery Turns">

> [!NOTE]
> Modifiez les éléments visibles du poster tout en préservant la structure générale du design.

---

<a id="case-8"></a>

### Case 8: Édition du calque d’offre d’un poster : Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif" width="720" alt="Édition du calque d’offre d’un poster : Happy Hour">

> [!NOTE]
> Changez un badge promotionnel ou un élément graphique sans reconstruire tout le poster.

---

<a id="case-9"></a>

### Case 9: Édition d’un calque d’image mode dans une mise en page

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" width="720" alt="Édition d’un calque d’image mode dans une mise en page">

> [!NOTE]
> Ajustez un sujet en calque dans une mise en page visuelle composée.

---

<a id="case-10"></a>

### Case 10: Édition du calque graphique d’un poster sportif

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif" width="720" alt="Édition du calque graphique d’un poster sportif">

> [!NOTE]
> Modifiez le graphique d’un poster de course tout en gardant typographie et composition alignées.

---

<a id="case-11"></a>

### Case 11: Édition d’élément de poster : Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif" width="720" alt="Édition d’élément de poster : Public Joy">

> [!NOTE]
> Modifiez des éléments du poster tout en conservant le langage visuel source.

---

<a id="case-12"></a>

### Case 12: Remplacement de surface matière avec réponse de texture précise

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif" width="720" alt="Remplacement de surface matière avec réponse de texture précise">

> [!NOTE]
> Remplacez les cibles de matière et de couleur tout en conservant la structure de l’objet.

---

<a id="anchor-position-editing"></a>

## 📍 Édition par ancre / position

Utilisez des ancres de type grille ou des positions relatives pour déplacer précisément une cible donnée.

Nombre de cas : **1**.

<a id="case-13"></a>

### Case 13: Déplacement d’objet par position de grille

<table>
<tr>
<td width="50%" valign="top">

**Avant :**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" width="420" alt="Déplacement d’objet par position de grille avant">

</td>
<td width="50%" valign="top">

**Après :**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" width="420" alt="Déplacement d’objet par position de grille après">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 Séparation de calques

Séparez le premier plan, l’arrière-plan et les composants réutilisables pour l’édition en aval.

Nombre de cas : **1**.

<a id="case-14"></a>

### Case 14: Séparation du premier plan / de la personne

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" width="720" alt="Séparation du premier plan / de la personne">

> [!NOTE]
> Séparez un sujet de premier plan d’un arrière-plan de type poster pour le réutiliser ensuite.

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ Édition par fusion multi-image

Combinez plusieurs images de référence dans une composition cohérente sous une seule instruction.

Nombre de cas : **1**.

<a id="case-15"></a>

### Case 15: Composition de nature morte entrée/sortie avec sept références

<table>
<tr>
<td width="50%" valign="top">

**Entrée :**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" width="420" alt="Entrée de composition de nature morte avec sept références">

</td>
<td width="50%" valign="top">

**Sortie :**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" width="420" alt="Sortie de composition de nature morte avec sept références">

</td>
</tr>
</table>

> [!NOTE]
> Utilisez les sept références sur fond blanc comme groupe d’entrée et générez la sortie de photographie de nature morte dans un seul case apparié.


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 Qualité visuelle et narration

Regroupez les exemples d’effets par action cinématographique, 3D / animation, art conceptuel et sortie de scène de jeu.

Nombre de cas : **5**.

<a id="case-16"></a>

### Case 16: Tennis cinématographique avec verre brisé

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="Tennis cinématographique avec verre brisé">

> [!NOTE]
> Génération de scène très dynamique avec éclats de verre, timing d’action et éclairage cinématographique.

---

<a id="case-17"></a>

### Case 17: Action de boxe cinématographique

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="Action de boxe cinématographique">

> [!NOTE]
> Rendu de scène d’action avec une sensation plus forte de mouvement, d’impact et de profondeur.

---

<a id="case-18"></a>

### Case 18: Scène en style animation 3D

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="Scène en style animation 3D">

> [!NOTE]
> Sortie 3D / animation stylisée pour personnages ou visuels de divertissement.

---

<a id="case-19"></a>

### Case 19: Art conceptuel visuel

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="Art conceptuel visuel">

> [!NOTE]
> Génération en style art conceptuel pour explorer l’atmosphère, la direction visuelle et l’humeur.

---

<a id="case-20"></a>

### Case 20: Visuel de scène de jeu

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="Visuel de scène de jeu">

> [!NOTE]
> Génération de scène de type jeu pour explorer environnement, décor ou key art.

---

<a id="multilingual-text-rendering"></a>

## 🌐 Rendu de texte multilingue

Regroupez les exemples multilingues par langue rendue et cas d’usage de texte local.

Nombre de cas : **5**.

<a id="case-21"></a>

### Case 21: Panneau de bienvenue en arabe et anglais

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" width="720" alt="Panneau de bienvenue en arabe et anglais">

> [!NOTE]
> Rendu multilingue natif avec texte arabe et anglais dans le même visuel.

---

<a id="case-22"></a>

### Case 22: Panneau coréen ouvert 24 h/24

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" width="720" alt="Panneau coréen ouvert 24 h/24">

> [!NOTE]
> Rendu de texte coréen pour vitrines ou signalétique localisées.

---

<a id="case-23"></a>

### Case 23: Panneau thaï de propreté

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="Panneau thaï de propreté">

> [!NOTE]
> Rendu de texte thaï pour espaces publics locaux ou visuels de campagne.

---

<a id="case-24"></a>

### Case 24: Poster français de création

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="Poster français de création">

> [!NOTE]
> Rendu de texte français pour assets de produit, mode et campagne.

---

<a id="case-25"></a>

### Case 25: Poster russe du futur

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" width="720" alt="Poster russe du futur">

> [!NOTE]
> Rendu de texte russe avec structure de caractères claire pour concepts visuels localisés.

---

<a id="model-notes"></a>

## 🧩 Notes du modèle

| Élément | Note fondée sur la source |
|---|---|
| ID du modèle | Le matériel officiel mentionne `dola-seedream-5-0-pro-260628`; une vérification runtime EvoLink reste nécessaire avant d’en faire une preuve de première exécution. |
| Images d’entrée | Le matériel officiel indique que Seedream 5.0 Pro prend en charge jusqu’à 10 images d’entrée. |
| Résolution de sortie | Ne revendiquez pas la 4K pour Pro ; la source décrit des paliers de sortie autour de `<= 2.36M` pixels et `> 2.36M` pixels. |
| Langues natives de prompt | Le matériel officiel cite l’arabe, l’anglais, le russe, l’indonésien, l’espagnol, l’allemand, le turc, le portugais, le malais, le vietnamien, le français, le japonais, le coréen, le tagalog et le thaï. |
| Chemin Seedream vers Seedance | Le matériel officiel indique que les sorties Seedream 5.0 Pro/Lite peuvent devenir des entrées fiables pour les workflows image-vers-vidéo de la famille Seedance, sous conditions de compte et de modération. |

<a id="acknowledge"></a>

## 🙏 Remerciements

Ce dépôt a été créé à partir du matériel officiel de lancement Seedream 5.0 Pro exporté le 8 juillet 2026 et des corrections officielles concernant l’inventaire des cas.

- Les URL privées de source officielle sont conservées uniquement dans les preuves locales d’audit.
- Les blocs de prompt ne sont inclus que lorsque le matériel officiel fournit le texte du prompt.
- Les cas avec média uniquement restent média uniquement ; les prompts manquants ne sont pas inventés.

*Si une frontière de cas public doit être corrigée, ouvrez une issue ou envoyez un patch avec une preuve source concrète.*
