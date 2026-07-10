<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Banner do Awesome Seedream 5.0 Pro no EvoLink"></a>

# Guia e prompts do Awesome Seedream 5.0 Pro

Guia com base em fontes, padrões de prompt e exemplos visuais para avaliar fluxos de geração e edição de imagens com Seedream 5.0 Pro.

[![Licença: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Usar no EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Obter chave API](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Introdução

Seedream 5.0 Pro é apresentado no material oficial de lançamento como um modelo controlável de geração e edição de imagens. Este guia mantém o README público alinhado ao menu oficial de capacidades: controle de interação, edição por esboço, edição em camadas, posicionamento por âncora, separação de camadas, fusão de múltiplas imagens, amostras visuais e renderização de texto multilíngue.

**Use este repositório para inspecionar exemplos com fonte, copiar apenas prompts presentes no material oficial e entender como cada categoria se conecta a casos visíveis.**

Experimente o ponto de entrada do modelo no EvoLink: [abrir Seedream 5.0 Pro no EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Início rápido:** Este repositório não afirma que uma rota API de primeira execução do Seedream 5.0 Pro na EvoLink já foi verificada. Use a entrada pública do modelo, o painel de chaves API e a referência técnica oficial até que a evidência de runtime seja registrada.

1. [Abrir a rota do Seedream 5.0 Pro no EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Obter sua chave API da EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [Ler a referência técnica oficial do ModelArk](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> Política de fonte: material oficial de lançamento. URLs privadas do Lark/Feishu ficam apenas na evidência local de auditoria e não são expostas como páginas públicas de fonte no README.

<a id="news"></a>

## 📰 Novidades

- **10 de julho de 2026:** Foram adicionados 4 casos com fontes públicas, localizados os títulos e aprendizados dos 39 casos e incluído um pôster de vídeo clicável.
- **July 8, 2026:** Guia inicial reconstruído em torno do menu oficial e do inventário de casos corrigido oficialmente.

<a id="menu"></a>

## 📑 Menu

- [🍌 Introdução](#introduction)
- [📰 Novidades](#news)
- [📑 Menu](#menu)
- [🎛️ Controle de interação](#interaction-control)
  - [Case 1: Setas e caixas de anotação para intenção espacial](#case-1)
  - [Case 2: Descrição de objetos por caixa de região para edição direcionada](#case-2)
- [✏️ Edição por esboço](#sketch-editing)
  - [Case 3: Geração de objetos guiada por rabiscos](#case-3)
  - [Case 4: Edição guiada por blocos de cor](#case-4)
  - [Case 5: Edição de detalhes guiada por linhas](#case-5)
  - [Case 6: De esboço simples a imagem refinada](#case-6)
- [🧱 Edição em camadas](#layer-editing)
  - [Case 7: Edição de texto e camada gráfica de pôster: Avery Turns](#case-7)
  - [Case 8: Edição de camada de oferta em pôster: Happy Hour](#case-8)
  - [Case 9: Edição de camada de imagem de moda dentro de um layout](#case-9)
  - [Case 10: Edição de camada gráfica em pôster esportivo](#case-10)
  - [Case 11: Edição de elemento de pôster: Public Joy](#case-11)
  - [Case 12: Troca de superfície material com resposta precisa de textura](#case-12)
- [📍 Edição por âncora / posição](#anchor-position-editing)
  - [Case 13: Movimento de objeto por posição em grade](#case-13)
- [🧩 Separação de camadas](#layer-separation)
  - [Case 14: Separação de camada de primeiro plano / pessoa](#case-14)
- [🖼️ Edição por fusão de múltiplas imagens](#multi-image-fusion-editing)
  - [Case 15: Composição de natureza-morta de entrada/saída com sete referências](#case-15)
- [🎬 Qualidade visual e narrativa](#visual-quality-narrative)
  - [Case 16: Tênis cinematográfico com vidro estilhaçado](#case-16)
  - [Case 17: Ação cinematográfica de boxe](#case-17)
  - [Case 18: Cena em estilo de animação 3D](#case-18)
  - [Case 19: Arte conceitual visual](#case-19)
  - [Case 20: Visual de cena de jogo](#case-20)
- [🌐 Renderização de texto multilíngue](#multilingual-text-rendering)
  - [Case 21: Placa de boas-vindas em árabe e inglês](#case-21)
  - [Case 22: Placa coreana de aberto 24 horas](#case-22)
  - [Case 23: Placa tailandesa de limpeza](#case-23)
  - [Case 24: Pôster francês de criação](#case-24)
  - [Case 25: Pôster russo de futuro](#case-25)
- [🧾 Galeria oficial de capacidades](#official-capability-gallery)
- [🧪 Casos de uso da comunidade](#community-use-cases)
  - [Fluxos de edição e controle de entrada](#community-editing-control)
  - [Design de produto, interface e pôster](#community-product-interface-design)
  - [Prompts técnicos, diagramas e sequências](#community-technical-structured-visuals)
  - [Visuais cinematográficos, personagens e estilo](#community-cinematic-character-visuals)
  - [Arte conceitual, ambiente e worldbuilding](#community-concept-environment-worldbuilding)
  - [Comparações e avaliações de modelos](#community-model-comparisons)
- [🙏 Agradecimentos](#acknowledge)

<a id="official-capability-gallery"></a>

## 🧾 Galeria oficial de capacidades

A galeria oficial mantém juntos os exemplos de lançamento fornecidos pelo proprietário como referência base de capacidades.

<a id="interaction-control"></a>

## 🎛️ Controle de interação

Use caixas, pontos, setas, marcações de anotação ou coordenadas para especificar a região-alvo.

Número de casos: **2**.

<a id="case-1"></a>

### Case 1: Setas e caixas de anotação para intenção espacial

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif?v=20260709-camo" height="420" alt="Setas e caixas de anotação para intenção espacial">

---

<a id="case-2"></a>

### Case 2: Descrição de objetos por caixa de região para edição direcionada

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" height="420" alt="Descrição de objetos por caixa de região para edição direcionada">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ Edição por esboço

Use rabiscos, blocos de cor, linhas ou esboços simples como guia visual.

Número de casos: **4**.

<a id="case-3"></a>

### Case 3: Geração de objetos guiada por rabiscos

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif?v=20260709-camo" height="420" alt="Geração de objetos guiada por rabiscos">

---

<a id="case-4"></a>

### Case 4: Edição guiada por blocos de cor

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif?v=20260709-camo" height="420" alt="Edição guiada por blocos de cor">

---

<a id="case-5"></a>

### Case 5: Edição de detalhes guiada por linhas

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif?v=20260709-camo" height="420" alt="Edição de detalhes guiada por linhas">

---

<a id="case-6"></a>

### Case 6: De esboço simples a imagem refinada

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif?v=20260709-camo" height="420" alt="De esboço simples a imagem refinada">

---

<a id="layer-editing"></a>

## 🧱 Edição em camadas

Edite camadas de pôster, gráfico, texto, material ou superfície preservando a composição geral.

Número de casos: **6**.

<a id="case-7"></a>

### Case 7: Edição de texto e camada gráfica de pôster: Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" height="420" alt="Edição de texto e camada gráfica de pôster: Avery Turns">

---

<a id="case-8"></a>

### Case 8: Edição de camada de oferta em pôster: Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="Edição de camada de oferta em pôster: Happy Hour">

---

<a id="case-9"></a>

### Case 9: Edição de camada de imagem de moda dentro de um layout

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" height="420" alt="Edição de camada de imagem de moda dentro de um layout">

---

<a id="case-10"></a>

### Case 10: Edição de camada gráfica em pôster esportivo

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="Edição de camada gráfica em pôster esportivo">

---

<a id="case-11"></a>

### Case 11: Edição de elemento de pôster: Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="Edição de elemento de pôster: Public Joy">

---

<a id="case-12"></a>

### Case 12: Troca de superfície material com resposta precisa de textura

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif?v=20260709-camo2" height="420" alt="Troca de superfície material com resposta precisa de textura">

---

<a id="anchor-position-editing"></a>

## 📍 Edição por âncora / posição

Use âncoras em grade ou posições relativas para mover um alvo específico com precisão.

Número de casos: **1**.

<a id="case-13"></a>

### Case 13: Movimento de objeto por posição em grade

<table>
<tr>
<td width="50%" valign="top">

**Antes:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" height="300" alt="Movimento de objeto por posição em grade antes">

</td>
<td width="50%" valign="top">

**Depois:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" height="300" alt="Movimento de objeto por posição em grade depois">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 Separação de camadas

Separe primeiro plano, fundo e componentes reutilizáveis para edição posterior.

Número de casos: **1**.

<a id="case-14"></a>

### Case 14: Separação de camada de primeiro plano / pessoa

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" height="420" alt="Separação de camada de primeiro plano / pessoa">

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ Edição por fusão de múltiplas imagens

Combine várias imagens de referência em uma composição coerente seguindo uma única instrução.

Número de casos: **1**.

<a id="case-15"></a>

### Case 15: Composição de natureza-morta de entrada/saída com sete referências

<table>
<tr>
<td width="50%" valign="top">

**Entrada:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" height="300" alt="Entrada de composição de natureza-morta com sete referências">

</td>
<td width="50%" valign="top">

**Saída:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" height="300" alt="Saída de composição de natureza-morta com sete referências">

</td>
</tr>
</table>


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 Qualidade visual e narrativa

Agrupe as amostras de efeito por ação cinematográfica, 3D / animação, arte conceitual e saída de cena de jogo.

Número de casos: **5**.

<a id="case-16"></a>

### Case 16: Tênis cinematográfico com vidro estilhaçado

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" height="420" alt="Tênis cinematográfico com vidro estilhaçado">

---

<a id="case-17"></a>

### Case 17: Ação cinematográfica de boxe

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" height="420" alt="Ação cinematográfica de boxe">

---

<a id="case-18"></a>

### Case 18: Cena em estilo de animação 3D

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" height="420" alt="Cena em estilo de animação 3D">

---

<a id="case-19"></a>

### Case 19: Arte conceitual visual

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" height="420" alt="Arte conceitual visual">

---

<a id="case-20"></a>

### Case 20: Visual de cena de jogo

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" height="420" alt="Visual de cena de jogo">

---

<a id="multilingual-text-rendering"></a>

## 🌐 Renderização de texto multilíngue

Agrupe as amostras multilíngues por idioma renderizado e caso de uso de texto local.

Número de casos: **5**.

<a id="case-21"></a>

### Case 21: Placa de boas-vindas em árabe e inglês

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" height="420" alt="Placa de boas-vindas em árabe e inglês">

---

<a id="case-22"></a>

### Case 22: Placa coreana de aberto 24 horas

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" height="420" alt="Placa coreana de aberto 24 horas">

---

<a id="case-23"></a>

### Case 23: Placa tailandesa de limpeza

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" height="420" alt="Placa tailandesa de limpeza">

---

<a id="case-24"></a>

### Case 24: Pôster francês de criação

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" height="420" alt="Pôster francês de criação">

---

<a id="case-25"></a>

### Case 25: Pôster russo de futuro

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" height="420" alt="Pôster russo de futuro">

---

<a id="community-use-cases"></a>

## 🧪 Casos de uso da comunidade

Estes 39 casos da comunidade com fontes públicas estão agrupados por tarefa e objetivo de saída. As tags indicam atributos secundários como comparação de modelos, disponibilidade do prompt, entrada de imagem e saída com várias imagens.

<a id="community-editing-control"></a>

### Fluxos de edição e controle de entrada

<a id="community-usecase-1"></a>

### Community Use Case 1: [Instrução em japonês para edição de imagem sem maquiagem](https://x.com/renataro9/status/2075059699112652908) (by [@renataro9](https://x.com/renataro9))

**A publicação de origem mostra um fluxo de edição ou controle de entrada em que a relação entre as entradas importa tanto quanto a imagem final.**

Type: Tutorial | Date: 2026-07-09 | Category: Fluxos de edição e controle de entrada

Tags: `image-input` `multi-image` `prompt-available` `tutorial`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/043/01.jpg" height="180" alt="Instrução em japonês para edição de imagem sem maquiagem mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/043/02.jpg" height="180" alt="Instrução em japonês para edição de imagem sem maquiagem mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
すっぴんメイクにして
```

</details>

---

<a id="community-usecase-2"></a>

### Community Use Case 2: [Edição de anime localizada que preserva a composição e altera um único sujeito](https://x.com/haruuraeadss/status/2075035201391255593) (by [@haruuraeadss](https://x.com/haruuraeadss))

**A publicação de origem mostra um fluxo de edição ou controle de entrada em que a relação entre as entradas importa tanto quanto a imagem final.**

Type: Tutorial | Date: 2026-07-09 | Category: Fluxos de edição e controle de entrada

Tags: `multi-image` `prompt-available` `tutorial`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/052/01.jpg" height="180" alt="Edição de anime localizada que preserva a composição e altera um único sujeito mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/052/02.jpg" height="180" alt="Edição de anime localizada que preserva a composição e altera um único sujeito mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
元画像の構図、人物の横顔、顔の輪郭、髪型、花飾り、白いドレス、藤の花の背景、全体の淡いピンクとラベンダーの幻想的な雰囲気はそのまま維持してください。 局所的に、少女の視線の先にいる紫の蝶を、より美しく印象的な「光をまとった宝石のような蝶」に変更してください。蝶の羽は透明感のある紫、水晶、ラベンダー、淡いピンクのグラデーションで、細かな発光粒子と繊細な羽脈を持たせてください。 蝶から少女の瞳へ向かって、細い光の粒子と柔らかな魔法の軌跡を追加してください。光は強すぎず、白飛びさせず、既存の明るく儚い花園の空気感に自然に溶け込ませてください。 少女の紫色の瞳には、蝶の光が小さく反射しているような宝石風のハイライトを少しだけ追加してください。瞳の形、顔立ち、表情、年齢感は変えないでください。 前髪の一部にも、蝶の淡い紫光がわずかに反射しているようにしてください。ただし髪色全体は変えず、ピンクブロンドの柔らかさを維持してください。 全体は高品質な日本アニメイラスト、幻想的、透明感、春の花園、上品、繊細、儚い美しさ。過度な発光、派手な魔法陣、強いコントラスト、顔の変形、衣装変更、背景変更は避けて…
```

</details>

---

<a id="community-usecase-3"></a>

### Community Use Case 3: [Transformação de gato em mecha por entrada de imagem](https://x.com/JennyAITech/status/2074870477651398972) (by [@JennyAITech](https://x.com/JennyAITech))

**A publicação de origem mostra um fluxo de edição ou controle de entrada em que a relação entre as entradas importa tanto quanto a imagem final.**

Type: Demo | Date: 2026-07-08 | Category: Fluxos de edição e controle de entrada

Tags: `image-input` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/058/01.jpg" height="180" alt="Transformação de gato em mecha por entrada de imagem mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/058/02.jpg" height="180" alt="Transformação de gato em mecha por entrada de imagem mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
a pic of my cat, asked for a mecha version
```

</details>

---

<a id="community-usecase-36"></a>

### Community Use Case 36: [Variação de imagem de referência a partir de uma fonte Niji7](https://x.com/Naonekozamurai/status/2075407158129353026) (by [@Naonekozamurai](https://x.com/Naonekozamurai))

**Use uma ilustração existente como base visual e gere no Seedream uma variação controlada.**

Type: Demo | Date: 2026-07-10 | Category: Fluxos de edição e controle de entrada

Tags: `image-input` `multi-image` `reference-variation`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/071/01.jpg" height="180" alt="Variação de imagem de referência a partir de uma fonte Niji7 mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/071/02.jpg" height="180" alt="Variação de imagem de referência a partir de uma fonte Niji7 mídia"></td>
</tr></table>

---

<a id="community-usecase-38"></a>

### Community Use Case 38: [Transferência de maquiagem preservando a identidade](https://x.com/YaZoraiz/status/2075189150127726801) (by [@YaZoraiz](https://x.com/YaZoraiz))

**Transfira a maquiagem de uma referência mantendo intacta a identidade da pessoa de destino.**

Type: Evaluation | Date: 2026-07-09 | Category: Fluxos de edição e controle de entrada

Tags: `identity-preservation` `image-input` `model-comparison` `multi-image`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/01.jpg" height="180" alt="Transferência de maquiagem preservando a identidade mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/02.jpg" height="180" alt="Transferência de maquiagem preservando a identidade mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/03.jpg" height="180" alt="Transferência de maquiagem preservando a identidade mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/073/04.jpg" height="180" alt="Transferência de maquiagem preservando a identidade mídia"></td>
</tr></table>

---


<a id="community-product-interface-design"></a>

### Design de produto, interface e pôster

<a id="community-usecase-4"></a>

### Community Use Case 4: [Interface de terminal de trading com detalhes da microestrutura do mercado](https://x.com/MishikaAI/status/2074879603446026333) (by [@MishikaAI](https://x.com/MishikaAI))

**A publicação de origem testa se o Seedream produz um visual comercial, uma interface, um anúncio de produto ou uma saída em formato de pôster que seja utilizável.**

Type: Demo | Date: 2026-07-08 | Category: Design de produto, interface e pôster

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/004/01.jpg" height="340" alt="Interface de terminal de trading com detalhes da microestrutura do mercado mídia">

<details open>
<summary>Prompt</summary>

```
a full trading terminal — K-lines, order book, bid/ask, volume, timestamps
```

</details>

---

<a id="community-usecase-5"></a>

### Community Use Case 5: [Pôster gráfico de androide cyberpunk](https://x.com/ComfyUI/status/2075027793491226677) (by [@ComfyUI](https://x.com/ComfyUI))

**A publicação de origem testa se o Seedream produz um visual comercial, uma interface, um anúncio de produto ou uma saída em formato de pôster que seja utilizável.**

Type: Demo | Date: 2026-07-09 | Category: Design de produto, interface e pôster

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/042/01.jpg" height="340" alt="Pôster gráfico de androide cyberpunk mídia">

<details open>
<summary>Prompt</summary>

```
A sci-fi cyberpunk graphic design poster. In the center, a striking portrait of a female android with glossy, liquid chrome skin. A vivid swirling streak of neon orange, yellow, and pink liquid paint brush stroke horizontally covers her eyes, soft smudged color overlay with smooth flowing pigment texture, no cracks or broken facial surfaces. The background is a dark, textured charcoal gray. Behind the central figure, large bold white futuristic typography reads "Seedream 5.0 Pro" with a subtle…
```

</details>

---

<a id="community-usecase-6"></a>

### Community Use Case 6: [Conjunto de anúncios para calçados esportivos premium](https://x.com/iamrealsnow/status/2075063569486598281) (by [@iamrealsnow](https://x.com/iamrealsnow))

**A publicação de origem testa se o Seedream produz um visual comercial, uma interface, um anúncio de produto ou uma saída em formato de pôster que seja utilizável.**

Type: Demo | Date: 2026-07-09 | Category: Design de produto, interface e pôster

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/01.jpg" height="180" alt="Conjunto de anúncios para calçados esportivos premium mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/02.jpg" height="180" alt="Conjunto de anúncios para calçados esportivos premium mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/03.jpg" height="180" alt="Conjunto de anúncios para calçados esportivos premium mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/047/04.jpg" height="180" alt="Conjunto de anúncios para calçados esportivos premium mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
Ultra-realistic premium sports footwear commercial advertisement featuring a modern running shoe floating horizontally at the center of a futuristic cyan and deep blue gradient background. The sneaker is displayed in a clean side profile with ultra-detailed breathable knit mesh texture, glossy air-cushion sole, realistic stitching, premium materials, and crisp branding. Soft cinematic studio lighting creates realistic reflections, shadows, and depth. The composition is designed as a futuristic…
```

</details>

---

<a id="community-usecase-7"></a>

### Community Use Case 7: [Pôster publicitário de artesanato infantil com argila](https://x.com/Strength04_X/status/2075063250656621054) (by [@Strength04_X](https://x.com/Strength04_X))

**A publicação de origem testa se o Seedream produz um visual comercial, uma interface, um anúncio de produto ou uma saída em formato de pôster que seja utilizável.**

Type: Demo | Date: 2026-07-09 | Category: Design de produto, interface e pôster

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/050/01.jpg" height="340" alt="Pôster publicitário de artesanato infantil com argila mídia">

<details open>
<summary>Prompt</summary>

```
A messy fun kids advertisement poster. A laughing young girl age 6 with clay all over her hands proudly shows a lumpy clay sculpture beside a giant colorful clay set box 3x her height overflowing with clay blocks in every color, "SQUISHCRAFT" written in big squishy letters on the box. Bright cheerful craft room background with clay sculptures tools and colorful handprints on the walls. Big squishy rounded typography "SQUISHCRAFT" in rainbow colors filling the background. Tagline bottom: "Get yo…
```

</details>

---


<a id="community-technical-structured-visuals"></a>

### Prompts técnicos, diagramas e sequências

<a id="community-usecase-8"></a>

### Community Use Case 8: [Renderização de planta técnica com muitas medidas](https://x.com/LiamEtherson/status/2074862867442962667) (by [@LiamEtherson](https://x.com/LiamEtherson))

**A publicação de origem testa o seguimento de prompts estruturados, incluindo diagramas, layouts técnicos, listas de planos e lógica de sequência com vários quadros.**

Type: Demo | Date: 2026-07-08 | Category: Prompts técnicos, diagramas e sequências

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/003/01.jpg" height="340" alt="Renderização de planta técnica com muitas medidas mídia">

<details open>
<summary>Prompt</summary>

```
technical blueprint with abundant measurement values
```

</details>

---

<a id="community-usecase-9"></a>

### Community Use Case 9: [Planta de carro conceitual com vistas técnicas explodidas](https://x.com/AiwithZohaib/status/2074880584107909602) (by [@AiwithZohaib](https://x.com/AiwithZohaib))

**A publicação de origem testa o seguimento de prompts estruturados, incluindo diagramas, layouts técnicos, listas de planos e lógica de sequência com vários quadros.**

Type: Demo | Date: 2026-07-08 | Category: Prompts técnicos, diagramas e sequências

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/005/01.jpg" height="340" alt="Planta de carro conceitual com vistas técnicas explodidas mídia">

<details open>
<summary>Prompt</summary>

```
a blueprint-style technical drawing of a concept car: front/side/rear views, exploded parts, measurements everywhere
```

</details>

---

<a id="community-usecase-10"></a>

### Community Use Case 10: [Planejamento de cena em tons de cinza orientado por lista de planos](https://x.com/munzxsdv/status/2074865454485483885) (by [@munzxsdv](https://x.com/munzxsdv))

**A publicação de origem testa o seguimento de prompts estruturados, incluindo diagramas, layouts técnicos, listas de planos e lógica de sequência com vários quadros.**

Type: Demo | Date: 2026-07-08 | Category: Prompts técnicos, diagramas e sequências

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/007/01.jpg" height="340" alt="Planejamento de cena em tons de cinza orientado por lista de planos mídia">

<details open>
<summary>Prompt</summary>

```
a shot list — panel-by-panel direction, camera moves, grayscale spec
```

</details>

---

<a id="community-usecase-11"></a>

### Community Use Case 11: [Storyboard de cavalaria com 16 quadros a partir de um único prompt](https://x.com/sulekhat95/status/2074966196563431636) (by [@sulekhat95](https://x.com/sulekhat95))

**A publicação de origem testa o seguimento de prompts estruturados, incluindo diagramas, layouts técnicos, listas de planos e lógica de sequência com vários quadros.**

Type: Demo | Date: 2026-07-08 | Category: Prompts técnicos, diagramas e sequências

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/062/01.jpg" height="340" alt="Storyboard de cavalaria com 16 quadros a partir de um único prompt mídia">

<details open>
<summary>Prompt</summary>

```
16-panel storyboard from ONE prompt: numbered frames, consistent characters, coherent camera logic across a whole cavalry charge
```

</details>

---

<a id="community-usecase-37"></a>

### Community Use Case 37: [Diagrama técnico explodido a partir de um único prompt](https://x.com/Ciri_ai/status/2075248022515294567) (by [@Ciri_ai](https://x.com/Ciri_ai))

**Use o Seedream para transformar uma instrução em uma composição técnica explodida e rotulada.**

Type: Demo | Date: 2026-07-09 | Category: Prompts técnicos, diagramas e sequências

Tags: `diagram` `multi-image` `structured-layout`

<table><tr>
<td width="33%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/072/01.jpg" height="180" alt="Diagrama técnico explodido a partir de um único prompt mídia"></td>
<td width="33%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/072/02.jpg" height="180" alt="Diagrama técnico explodido a partir de um único prompt mídia"></td>
<td width="33%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/072/03.jpg" height="180" alt="Diagrama técnico explodido a partir de um único prompt mídia"></td>
</tr></table>

---


<a id="community-cinematic-character-visuals"></a>

### Visuais cinematográficos, de personagens e de estilo

<a id="community-usecase-12"></a>

### Community Use Case 12: [Retratos editoriais olho de peixe com motivo de clones em miniatura](https://x.com/magnific/status/2074872903938846900) (by [@magnific](https://x.com/magnific))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-08 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/008/01.jpg" height="180" alt="Retratos editoriais olho de peixe com motivo de clones em miniatura mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/008/02.jpg" height="180" alt="Retratos editoriais olho de peixe com motivo de clones em miniatura mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
Shot on cinema camera with subtle halation effect, 35mm film grain, fashion editorial photography in the style of Y2K revival magazine covers. Extreme fisheye lens, distorted wide perspective pulling the scene toward the curved edges, low camera angle from the street. A young man around 20 years old with messy dark hair with soft curtain bangs, smooth youthful skin with natural texture and a few freckles, wearing small oval sunglasses with pink tinted lenses, a colorful beaded necklace, silver…
```

</details>

---

<a id="community-usecase-13"></a>

### Community Use Case 13: [Geração conceitual de marcos mundiais derretendo](https://x.com/magnific/status/2074918700709523881) (by [@magnific](https://x.com/magnific))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-08 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/011/01.jpg" height="180" alt="Geração conceitual de marcos mundiais derretendo mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/011/02.jpg" height="180" alt="Geração conceitual de marcos mundiais derretendo mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
world's landmarks, melting like wax
```

</details>

---

<a id="community-usecase-14"></a>

### Community Use Case 14: [Iluminação fotorrealista para retrato de alta moda](https://x.com/BubbleBrain/status/2074856963591290979) (by [@BubbleBrain](https://x.com/BubbleBrain))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-08 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/017/01.jpg" height="340" alt="Iluminação fotorrealista para retrato de alta moda mídia">

<details open>
<summary>Prompt</summary>

```
This is a highly photorealistic, high-fashion full-body portrait with an overall dark-toned, dreamy, and hazy atmosphere, filled with the flowing beauty of light and shadow. The scene uses refined artificial lighting that is soft yet richly layered, with sparkling highlights, crystal-clear reflections, and a subtle lomo film texture in certain areas, creating a surreal and luxurious fashion mood that feels both realistic and dreamlike. The subject is a young adult Taiwanese woman with short pin…
```

</details>

---

<a id="community-usecase-15"></a>

### Community Use Case 15: [Cena natural de foto no celular ao pôr do sol em São Francisco](https://x.com/mattworkman/status/2074850550349222210) (by [@mattworkman](https://x.com/mattworkman))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-08 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/018/01.jpg" height="340" alt="Cena natural de foto no celular ao pôr do sol em São Francisco mídia">

<details open>
<summary>Prompt</summary>

```
a Korean girl in her twenties on her iPhone in San Francisco at sunset
```

</details>

---

<a id="community-usecase-16"></a>

### Community Use Case 16: [Visual principal de guerreiro anjo caído de fantasia](https://x.com/SimplyAnnisa/status/2074900816662774189) (by [@SimplyAnnisa](https://x.com/SimplyAnnisa))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-08 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/028/01.jpg" height="340" alt="Visual principal de guerreiro anjo caído de fantasia mídia">

<details open>
<summary>Prompt</summary>

```
A divine fallen angel warrior kneeling in the center of an ancient celestial temple, thrusting a massive flaming holy sword into a cracked white marble floor, the impact creating glowing lava-like fractures and flying debris. Gigantic pure white feathered wings spread wide behind the warrior, wearing ornate gold and crimson medieval armor with intricate engravings, a flowing dark red cape, and ram-like curled white horns. Glowing crimson eyes stare downward with an intense, wrathful expression.…
```

</details>

---

<a id="community-usecase-17"></a>

### Community Use Case 17: [Conjunto de estilos para retrato casual japonês](https://x.com/Cia0_exe/status/2075033845032993261) (by [@Cia0_exe](https://x.com/Cia0_exe))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-09 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/01.jpg" height="180" alt="Conjunto de estilos para retrato casual japonês mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/02.jpg" height="180" alt="Conjunto de estilos para retrato casual japonês mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/03.jpg" height="180" alt="Conjunto de estilos para retrato casual japonês mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/029/04.jpg" height="180" alt="Conjunto de estilos para retrato casual japonês mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A beautiful young Japanese woman, natural and effortless beauty, soft glowing skin, wearing a fitted black tank top layered under an oversized cool white shirt worn open, casual chic styling. Cinematic movie-grade shot, anamorphic lens flare, shallow depth of field with creamy bokeh, slow dolly-in camera movement, dramatic rim lighting from golden hour sun, subtle film grain, volumetric light rays through window, color graded like a Denis Villeneuve film teal and warm amber tones, 35mm anamorph…
```

</details>

---

<a id="community-usecase-18"></a>

### Community Use Case 18: [Close urbano cinematográfico no estilo ARRI](https://x.com/df_reno/status/2075055332452106476) (by [@df_reno](https://x.com/df_reno))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-09 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/01.jpg" height="180" alt="Close urbano cinematográfico no estilo ARRI mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/02.jpg" height="180" alt="Close urbano cinematográfico no estilo ARRI mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/03.jpg" height="180" alt="Close urbano cinematográfico no estilo ARRI mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/035/04.jpg" height="180" alt="Close urbano cinematográfico no estilo ARRI mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
超写实电影剧照，一位女性在昏暗的都市环境中仰望天空，画面极具感染力。使用 ARRI Alexa Mini LF 摄影机和 Panavision C 系列 50mm 变形镜头拍摄，光圈 T2，加装 Black Pro-Mist 1/8 滤镜，采用 2.39:1 变形宽银幕构图。低角度特写镜头，镜头略低于女性面部，营造出亲密的电影视角。女性位于画面右侧，左侧留出大片空白。 右上角背景中存在强烈的人工光源，产生强烈的变形镜头水平光晕、蓝白色的光晕、镜头内部反射、电影光晕效果以及柔和的高光。 光源并非阳光，而是远处城市路灯或工业灯光，并因浅景深而呈现出模糊效果。柔和的青色环境光部分照亮了女性的脸庞，展现出逼真的肌肤纹理、自然的毛孔、细微的瑕疵，嘴唇微张，眼神充满情感地向上凝视。前景包含模糊的暗色调环境元素。中景是女性的脸部和头发。背景是高度虚化的城市建筑，点缀着抽象的光影。深邃的阴影、低对比度的黑色、冷色调的蓝色调、逼真的夜景电影感、柯达胶片质感、细腻的颗粒感、变形光晕、朦胧的氛围，以及真实的电影画面。 A vast grassy field filled with several larg…
```

</details>

---

<a id="community-usecase-19"></a>

### Community Use Case 19: [Editorial de looks de moda em um estacionamento](https://x.com/ChillaiKalan__/status/2075071088137208063) (by [@ChillaiKalan__](https://x.com/ChillaiKalan__))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-09 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/01.jpg" height="180" alt="Editorial de looks de moda em um estacionamento mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/02.jpg" height="180" alt="Editorial de looks de moda em um estacionamento mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/03.jpg" height="180" alt="Editorial de looks de moda em um estacionamento mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/038/04.jpg" height="180" alt="Editorial de looks de moda em um estacionamento mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A stylish young woman with long layered black hair and soft curtain bangs, wearing sleek black rectangular sunglasses, an oversized chocolate-brown tailored blazer with matching wide-leg trousers, and a fitted mocha-brown camisole. She carries a large structured ivory leather tote bag with gold hardware over one shoulder. Standing confidently with one hand in her pocket, looking back over her shoulder. Shot in a modern open-air parking structure beneath a concrete overpass, with parked cars sof…
```

</details>

---

<a id="community-usecase-20"></a>

### Community Use Case 20: [Pôster editorial de flor de vidro iridescente](https://x.com/ComfyUI/status/2075027810666914062) (by [@ComfyUI](https://x.com/ComfyUI))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-09 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/044/01.jpg" height="340" alt="Pôster editorial de flor de vidro iridescente mídia">

<details open>
<summary>Prompt</summary>

```
An editorial graphic design poster on a solid black background. The central elements are exquisite, translucent 3D glass flowers with iridescent, holographic petals in shades of electric blue, violet, and soft purple. In the background, large, bold white sans-serif typography reads "Seedream 5.0 Pro", elegantly layered behind and interwoven with the glass petals. The layout is filled with clean blocks of small white placeholder body text and delicate thin white vector lines, creating a futurist…
```

</details>

---

<a id="community-usecase-21"></a>

### Community Use Case 21: [Sequência de skate em anime com vários prompts de plano](https://x.com/asatoucan/status/2075060881067769903) (by [@asatoucan](https://x.com/asatoucan))

**A publicação de origem testa a qualidade cinematográfica, de personagens, moda ou estilo por meio dos resultados visuais publicados.**

Type: Demo | Date: 2026-07-09 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/01.jpg" height="180" alt="Sequência de skate em anime com vários prompts de plano mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/02.jpg" height="180" alt="Sequência de skate em anime com vários prompts de plano mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/03.jpg" height="180" alt="Sequência de skate em anime com vários prompts de plano mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/069/04.jpg" height="180" alt="Sequência de skate em anime com vários prompts de plano mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A girl with a sharp bob cut, purple hair with black accent strands, stylized layered hair flowing in the wind, wearing layered cloth with black accents, riding a skateboard through a vibrant concrete skate park, captured from a dramatic high angle looking down at the front profile, dynamic action pose, body leaning into a turn, skate park ramps, rails, and colorful graffiti walls sprawling below, cel shaded, toon shading, hard shadows, bold outlines, anime style, vibrant flat colors, crisp line…
```

</details>

---

<a id="community-usecase-39"></a>

### Community Use Case 39: [Quadros-chave do Seedream em um vídeo explicativo de ponta a ponta](https://x.com/alisaqqt/status/2075241584615108812) (by [@alisaqqt](https://x.com/alisaqqt))

**Use o Seedream para criar quadros-chave em um pipeline multimodelo que produz um vídeo explicativo finalizado.**

Type: Integration | Date: 2026-07-09 | Category: Visuais cinematográficos, de personagens e de estilo

Tags: `integration` `keyframes` `video`

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/074/demo.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/074/poster.jpg" height="340" alt="Quadros-chave do Seedream em um vídeo explicativo de ponta a ponta mídia"></a>

[Reproduzir vídeo de demonstração](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/074/demo.mp4)

---


<a id="community-concept-environment-worldbuilding"></a>

### Arte conceitual, ambientes e construção de mundos

<a id="community-usecase-22"></a>

### Community Use Case 22: [Conceito de estação de pesquisa no deserto movida a energia solar](https://x.com/ashen_one/status/2074915677815886071) (by [@ashen_one](https://x.com/ashen_one))

**A publicação de origem testa composições de ambientes, interiores, ficção científica ou construção de mundos, e não a edição de um único objeto.**

Type: Demo | Date: 2026-07-08 | Category: Arte conceitual, ambientes e construção de mundos

Tags: `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/021/01.jpg" height="340" alt="Conceito de estação de pesquisa no deserto movida a energia solar mídia">

<details open>
<summary>Prompt</summary>

```
A solar-powered research station in a desert, featuring domed structures, solar panels, and various equipment for energy and research management.
```

</details>

---

<a id="community-usecase-23"></a>

### Community Use Case 23: [Construção de mundo sci-fi cinematográfico em escala impossível](https://x.com/AllaAisling/status/2075036565147906511) (by [@AllaAisling](https://x.com/AllaAisling))

**A publicação de origem testa composições de ambientes, interiores, ficção científica ou construção de mundos, e não a edição de um único objeto.**

Type: Demo | Date: 2026-07-09 | Category: Arte conceitual, ambientes e construção de mundos

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/01.jpg" height="180" alt="Construção de mundo sci-fi cinematográfico em escala impossível mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/02.jpg" height="180" alt="Construção de mundo sci-fi cinematográfico em escala impossível mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/03.jpg" height="180" alt="Construção de mundo sci-fi cinematográfico em escala impossível mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/027/04.jpg" height="180" alt="Construção de mundo sci-fi cinematográfico em escala impossível mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
An industrial civilization is constructing an entire planet inside an enormous orbital shipyard. Giant robotic arms hold continents in place while molten oceans are poured into gigantic basins. Thousands of spacecraft weld mountain ranges together. The unfinished world glows from its molten core. Unreal scale, NASA realism, cinematic science fiction. Gigantic floating whales drift above endless wheat fields while enormous wind-powered harvesting machines extend hundreds of meters into the sky t…
```

</details>

---

<a id="community-usecase-24"></a>

### Community Use Case 24: [Variações de design de quarto para tipos MBTI](https://x.com/FloraTechAI/status/2074866317484794131) (by [@FloraTechAI](https://x.com/FloraTechAI))

**A publicação de origem testa composições de ambientes, interiores, ficção científica ou construção de mundos, e não a edição de um único objeto.**

Type: Demo | Date: 2026-07-08 | Category: Arte conceitual, ambientes e construção de mundos

Tags: `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/01.jpg" height="180" alt="Variações de design de quarto para tipos MBTI mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/02.jpg" height="180" alt="Variações de design de quarto para tipos MBTI mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/03.jpg" height="180" alt="Variações de design de quarto para tipos MBTI mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/061/04.jpg" height="180" alt="Variações de design de quarto para tipos MBTI mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
design a bedroom for each MBTI type
```

</details>

---


<a id="community-model-comparisons"></a>

### Comparações e avaliações de modelos

<a id="community-usecase-25"></a>

### Community Use Case 25: [Amostragem multitarefa das capacidades do Seedream com quatro prompts em chinês](https://x.com/op7418/status/2074862226905948549) (by [@op7418](https://x.com/op7418))

**A publicação de origem reúne várias tarefas em uma thread e funciona melhor como avaliação ampla de capacidades do que como caso de finalidade única.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `capability-sampling` `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/01.jpg" height="180" alt="Amostragem multitarefa das capacidades do Seedream com quatro prompts em chinês mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/02.jpg" height="180" alt="Amostragem multitarefa das capacidades do Seedream com quatro prompts em chinês mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/03.jpg" height="180" alt="Amostragem multitarefa das capacidades do Seedream com quatro prompts em chinês mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/001/04.jpg" height="180" alt="Amostragem multitarefa das capacidades do Seedream com quatro prompts em chinês mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
1. 一句话让它生成《黑神话：水浒传》的一个游戏截图 2. 让他生成一张茶叶制作和品种的科普图 3. 给它一个参考图，让它基于这个参考图的组件生成一个 Web 的 UI 设计稿 4. 让他用一张图介绍《凡人修仙传：人界篇》的剧情
```

</details>

---

<a id="community-usecase-26"></a>

### Community Use Case 26: [Seedream contra GPT Image 2 em enquadramento realista de selfie no carro](https://x.com/johnAGI168/status/2074870910469677387) (by [@johnAGI168](https://x.com/johnAGI168))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/006/01.jpg" height="180" alt="Seedream contra GPT Image 2 em enquadramento realista de selfie no carro mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/006/02.jpg" height="180" alt="Seedream contra GPT Image 2 em enquadramento realista de selfie no carro mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
生成一张真实感车内自拍视频首帧照片，横屏 16:9。画面像固定在副驾驶前方或中控台附近的小型广角相机拍摄，轻微广角，近距离车内第一视角，像社交媒体短视频截图。 主角是一位成年女性，气质清冷、安静、精致，整体像日常车内自拍视频里的主角。她脸型小巧偏鹅蛋脸，五官自然精致，鼻梁挺，嘴唇自然，表情平静、淡淡的，有一点冷感但不夸张。她正面面向镜头或略微看向前方，能清楚看到完整正脸，不低头，不侧脸。她戴细框透明或浅银色眼镜，长直发偏浅棕色，带轻微空气刘海，头发自然垂落在肩侧。穿简洁灰色无袖针织连衣裙或灰色无袖上衣搭配同色下装，造型干净日常、端庄自然。 她坐在驾驶位，安全带已经插好并固定完成：黑色安全带清楚地从肩膀斜跨过上身到腰侧，状态自然贴合身体，不是在拉安全带，也不是正在插卡扣。她一只手自然放在方向盘附近或轻扶方向盘，另一只手放低在座椅边或腿侧，姿态像准备开车前刚坐正的一瞬间。表情专注平静，眼神可以看向镜头，也可以略微看向前方道路。 车内是红棕色真皮座椅和红棕色门板，方向盘在画面右前方形成明显前景，仪表台、车窗边缘和后排座椅可见。车窗外是白天城市道路旁的绿化、树木和轻微模糊的街景，但车子此刻看…
```

</details>

---

<a id="community-usecase-27"></a>

### Community Use Case 27: [Seedream contra GPT Image 2 em retrato clean de estilo de vida](https://x.com/liyue_ai/status/2074890690686005590) (by [@liyue_ai](https://x.com/liyue_ai))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/012/01.jpg" height="180" alt="Seedream contra GPT Image 2 em retrato clean de estilo de vida mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/012/02.jpg" height="180" alt="Seedream contra GPT Image 2 em retrato clean de estilo de vida mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
摄影风格：冷白清透CCD生活照风 写真方向：轻熟生活照 场景方向：酒店泳池外步道 / 白色躺椅 / 浅蓝池水 / 简洁遮阳伞 服装方向：浅鼠尾草色修身无袖针织短裙 气质标签：温柔、清透、轻熟、安静、有吸引力 五官方向：真实清透自然脸，安静干净，不网红 五官细节：柔和鹅蛋脸，面部轮廓自然；清亮杏眼，眼神温柔安静；鼻型流畅小巧；唇形柔软克制，低饱和裸粉唇色；整体是安静、通透、舒服的生活感美人脸 发型方向：自然黑长发或低扎发，发丝顺滑，额前少量碎发，带一点微风感 身形方向：轻盈纤细，上围饱满自然 线条强调：强 镜头方向：大腿及上半身 姿态动作：站在泳池步道边，身体轻微侧向镜头，一只手自然垂落，另一只手轻扶裙侧 光线氛围：高色温晴天自然光 + 水面反射光 + 冷白极弱柔闪 滤镜效果：冷白高光 + 蓝白清透生活照色彩 + 轻颗粒 + 轻数码噪点 + 轻微过曝 画幅比例：9:16 补充要求：连衣裙贴身柔软，突出胸部轮廓、腰线和整体修长感，人物五官要安静耐看，整体要冷白清爽，不要商业泳池大片感
```

</details>

---

<a id="community-usecase-28"></a>

### Community Use Case 28: [Comparação de carro esportivo em planta técnica com GPT Image 2](https://x.com/marmaduke091/status/2074866077499105416) (by [@marmaduke091](https://x.com/marmaduke091))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/019/01.jpg" height="180" alt="Comparação de carro esportivo em planta técnica com GPT Image 2 mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/019/02.jpg" height="180" alt="Comparação de carro esportivo em planta técnica com GPT Image 2 mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A technical drawing of a futuristic sports car in blueprint style. Include line drawings of the sports car from the front, side, and rear views, exploded parts sketches, parts assembly diagrams, and structural diagrams of disassembled components. Use abundant lines and measurement values to indicate the dimensions of each part, with grayscale tones expressing the overall sketch relationship. In addition to the main design, also show scattered thumbnails from different angles.
```

</details>

---

<a id="community-usecase-29"></a>

### Community Use Case 29: [Comparação de mudança de ângulo de câmera com imagem de referência](https://x.com/hasamaru_studio/status/2075052934409375918) (by [@hasamaru_studio](https://x.com/hasamaru_studio))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-09 | Category: Comparações e avaliações de modelos

Tags: `image-input` `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/01.jpg" height="180" alt="Comparação de mudança de ângulo de câmera com imagem de referência mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/02.jpg" height="180" alt="Comparação de mudança de ângulo de câmera com imagem de referência mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/03.jpg" height="180" alt="Comparação de mudança de ângulo de câmera com imagem de referência mídia"></td>
<td width="25%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/022/04.jpg" height="180" alt="Comparação de mudança de ângulo de câmera com imagem de referência mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
リファレンス画像のスタイルを保ったまま、もう少し高い位置からの画角に変更してもらいました。
```

</details>

---

<a id="community-usecase-30"></a>

### Community Use Case 30: [Comparação de composição publicitária com lata de bebida gigante](https://x.com/emmanuel_2m/status/2075000101362131350) (by [@emmanuel_2m](https://x.com/emmanuel_2m))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/023/01.jpg" height="180" alt="Comparação de composição publicitária com lata de bebida gigante mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/023/02.jpg" height="180" alt="Comparação de composição publicitária com lata de bebida gigante mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A premium infographic-style advertisement featuring an oversized Pepsi can placed beside a young woman. The can is scaled to be nearly the same size as her entire seated body, creating a striking surreal proportion. The woman sits casually leaning against the giant can, one arm resting on it, interacting naturally. The Pepsi can is ultra-detailed with crisp branding, condensation droplets, realistic reflections, and metallic texture. The logo is clean, sharp, and properly proportioned. Composit…
```

</details>

---

<a id="community-usecase-31"></a>

### Community Use Case 31: [Comparação de pôster de viagem em scrapbook de Chengdu](https://x.com/DeepBlueAIX/status/2074872447229419956) (by [@DeepBlueAIX](https://x.com/DeepBlueAIX))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/031/01.jpg" height="180" alt="Comparação de pôster de viagem em scrapbook de Chengdu mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/031/02.jpg" height="180" alt="Comparação de pôster de viagem em scrapbook de Chengdu mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
成都旅游 · 小红书手帐风海报 一张竖版 9:16 的小红书风格拼贴海报，主题为**「成都旅游城市漫游计划」**。整体采用手帐风设计，像旅行日记一样丰富、有生活感和轻松氛围。 画面以成都城市旅行为核心内容，包含宽窄巷子、锦里古街、春熙路、IFS熊猫、成都大熊猫繁育研究基地、东郊记忆、都江堰、青城山等真实场景照片，以拼贴方式散落在画面中，搭配撕纸边框与胶带装饰。画面中穿插熊猫元素、茶馆、人民公园、盖碗茶、街头巷尾、夜市、美食街、城市天际线等真实旅行场景，充分展现成都悠闲惬意的慢生活氛围。 整体视觉使用天蓝色作为主色调，并点缀粉色、浅黄色与柔和绿色，营造清新明亮又富有烟火气的城市旅行氛围。 画面中加入大量手帐元素，例如手绘箭头、涂鸦星星、对话气泡、便签标签、贴纸装饰、旅行地图、定位图标、拍立得照片、胶带、旅行印章、熊猫贴纸、相机、咖啡杯、小花、云朵、笑脸图标等，使画面具有强烈的小红书「种草笔记」视觉风格。 主标题为**「成都达人计划 / Chengdu City Guide」，采用手写感或涂鸦字体，具有明显的年轻化社交媒体风格。画面中穿插中英文混排文字，如「City Walk Cheng…
```

</details>

---

<a id="community-usecase-32"></a>

### Community Use Case 32: [Comparação de visual principal de anime](https://x.com/roco_kn_roco/status/2074890020260094137) (by [@roco_kn_roco](https://x.com/roco_kn_roco))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `prompt-available`

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/034/01.jpg" height="340" alt="Comparação de visual principal de anime mídia">

<details open>
<summary>Prompt</summary>

```
新作アニメのキービジュアルを作って下さい
```

</details>

---

<a id="community-usecase-33"></a>

### Community Use Case 33: [Comparação de pôster de viagem com restrição de assinatura](https://x.com/Bic_Revelation/status/2074959714366922857) (by [@Bic_Revelation](https://x.com/Bic_Revelation))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/056/01.jpg" height="180" alt="Comparação de pôster de viagem com restrição de assinatura mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/056/02.jpg" height="180" alt="Comparação de pôster de viagem com restrição de assinatura mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
With its crystal-clear waters, white sandy beaches, and vibrant coral reefs, the Maldives is a tropical paradise perfect for exotic and tranquil visuals. SIGNATURE: 'BicRevelation' cursive script lower-left.
```

</details>

---

<a id="community-usecase-34"></a>

### Community Use Case 34: [Moinho d’água de vila fantástica contra GPT Image 2](https://x.com/emmanuel_2m/status/2075000114427375742) (by [@emmanuel_2m](https://x.com/emmanuel_2m))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-08 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/065/01.jpg" height="180" alt="Moinho d’água de vila fantástica contra GPT Image 2 mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/065/02.jpg" height="180" alt="Moinho d’água de vila fantástica contra GPT Image 2 mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
stylized stylized fantasy village watermill, two-story half-timbered red-clay tower w/ thatched conical roof, big wooden water-wheel, attached small thatched cottage, wooden walkways and stairs, lush green meadow w/ stones, painterly Genshin-Impact / Studio Ghibli env art, fluffy cumulus clouds, sunny midday
```

</details>

---

<a id="community-usecase-35"></a>

### Community Use Case 35: [Cena de moda no Lago de Como contra Banana Pro](https://x.com/cso6709/status/2075046425277399261) (by [@cso6709](https://x.com/cso6709))

**A publicação de origem compara o Seedream 5.0 Pro com outro modelo na mesma tarefa visual ou em uma tarefa muito próxima.**

Type: Evaluation | Date: 2026-07-09 | Category: Comparações e avaliações de modelos

Tags: `model-comparison` `multi-image` `prompt-available`

<table><tr>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/066/01.jpg" height="180" alt="Cena de moda no Lago de Como contra Banana Pro mídia"></td>
<td width="50%" valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/066/02.jpg" height="180" alt="Cena de moda no Lago de Como contra Banana Pro mídia"></td>
</tr></table>

<details open>
<summary>Prompt</summary>

```
A straight-on medium-wide cinematic shot at eye-level, static locked frame, 4:5 vertical, captures a sun-bright late-morning inside a Lake Como villa courtyard room, camera perpendicular to the wall plane with no tilt, the atmosphere crisp and alive like the minute before heading out for gelato, the wall behind the scene a warm hand-troweled sable butter-yellow lime plaster slightly uneven with soft sun-bleach along the upper right edge, the floor matte burnt-terracotta chili tile grounding the…
```

</details>

---

<a id="acknowledge"></a>

## 🙏 Agradecimentos

Este repositório se baseia no material oficial de lançamento do Seedream 5.0 Pro exportado em 8 de julho de 2026 e nas publicações públicas da comunidade citadas na galeria de casos de uso.

Obrigado à equipe Seedream pelos exemplos oficiais, materiais de produto e referências técnicas.

Obrigado aos autores da comunidade cujas publicações públicas são citadas neste repositório:

- [@renataro9](https://x.com/renataro9), [@haruuraeadss](https://x.com/haruuraeadss), [@JennyAITech](https://x.com/JennyAITech), [@MishikaAI](https://x.com/MishikaAI), [@ComfyUI](https://x.com/ComfyUI), [@iamrealsnow](https://x.com/iamrealsnow), [@Strength04_X](https://x.com/Strength04_X), [@LiamEtherson](https://x.com/LiamEtherson)
- [@AiwithZohaib](https://x.com/AiwithZohaib), [@munzxsdv](https://x.com/munzxsdv), [@sulekhat95](https://x.com/sulekhat95), [@magnific](https://x.com/magnific), [@BubbleBrain](https://x.com/BubbleBrain), [@mattworkman](https://x.com/mattworkman), [@SimplyAnnisa](https://x.com/SimplyAnnisa), [@Cia0_exe](https://x.com/Cia0_exe)
- [@df_reno](https://x.com/df_reno), [@ChillaiKalan__](https://x.com/ChillaiKalan__), [@asatoucan](https://x.com/asatoucan), [@ashen_one](https://x.com/ashen_one), [@AllaAisling](https://x.com/AllaAisling), [@FloraTechAI](https://x.com/FloraTechAI), [@op7418](https://x.com/op7418), [@johnAGI168](https://x.com/johnAGI168)
- [@liyue_ai](https://x.com/liyue_ai), [@marmaduke091](https://x.com/marmaduke091), [@hasamaru_studio](https://x.com/hasamaru_studio), [@emmanuel_2m](https://x.com/emmanuel_2m), [@DeepBlueAIX](https://x.com/DeepBlueAIX), [@roco_kn_roco](https://x.com/roco_kn_roco), [@Bic_Revelation](https://x.com/Bic_Revelation), [@cso6709](https://x.com/cso6709)
- [@Naonekozamurai](https://x.com/Naonekozamurai), [@Ciri_ai](https://x.com/Ciri_ai), [@YaZoraiz](https://x.com/YaZoraiz), [@alisaqqt](https://x.com/alisaqqt)

Se algum autor quiser alterar ou remover a atribuição, abra uma issue com o link da publicação pública correspondente.
