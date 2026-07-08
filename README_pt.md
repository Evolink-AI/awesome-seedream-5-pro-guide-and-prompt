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
- [🧩 Notas do modelo](#model-notes)
- [🙏 Agradecimentos](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ Controle de interação

Use caixas, pontos, setas, marcações de anotação ou coordenadas para especificar a região-alvo.

Número de casos: **2**.

<a id="case-1"></a>

### Case 1: Setas e caixas de anotação para intenção espacial

<img src="assets/media/003-arrows-annotation-boxes.gif" width="720" alt="Setas e caixas de anotação para intenção espacial">

> [!NOTE]
> Use setas, caixas e anotações para explicitar a área-alvo antes da edição.

---

<a id="case-2"></a>

### Case 2: Descrição de objetos por caixa de região para edição direcionada

<img src="assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="Descrição de objetos por caixa de região para edição direcionada">

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

<img src="assets/media/005-doodles.gif" width="720" alt="Geração de objetos guiada por rabiscos">

> [!NOTE]
> Use rabiscos soltos como sinal de controle visual e deixe o modelo renderizar o objeto pretendido.

---

<a id="case-4"></a>

### Case 4: Edição guiada por blocos de cor

<img src="assets/media/006-color-block.gif" width="720" alt="Edição guiada por blocos de cor">

> [!NOTE]
> Use blocos amplos de cor para indicar composição aproximada, zonas de cor ou posicionamento de objetos.

---

<a id="case-5"></a>

### Case 5: Edição de detalhes guiada por linhas

<img src="assets/media/007-lines.gif" width="720" alt="Edição de detalhes guiada por linhas">

> [!NOTE]
> Use linhas simples quando o contorno da forma importar mais que uma descrição longa.

---

<a id="case-6"></a>

### Case 6: De esboço simples a imagem refinada

<img src="assets/media/008-simple-sketches.gif" width="720" alt="De esboço simples a imagem refinada">

> [!NOTE]
> Transforme um esboço mínimo em uma imagem renderizada mais completa preservando a intenção do esboço.

---

<a id="layer-editing"></a>

## 🧱 Edição em camadas

Edite camadas de pôster, gráfico, texto, material ou superfície preservando a composição geral.

Número de casos: **6**.

<a id="case-7"></a>

### Case 7: Edição de texto e camada gráfica de pôster: Avery Turns

<img src="assets/media/009-Feishu-Docs-Image.gif" width="720" alt="Edição de texto e camada gráfica de pôster: Avery Turns">

> [!NOTE]
> Edite elementos visíveis do pôster preservando a estrutura geral do design.

---

<a id="case-8"></a>

### Case 8: Edição de camada de oferta em pôster: Happy Hour

<img src="assets/media/010-Feishu-Docs-Image.gif" width="720" alt="Edição de camada de oferta em pôster: Happy Hour">

> [!NOTE]
> Altere um selo promocional ou elemento gráfico sem reconstruir todo o pôster.

---

<a id="case-9"></a>

### Case 9: Edição de camada de imagem de moda dentro de um layout

<img src="assets/media/011-Feishu-Docs-Image.gif" width="720" alt="Edição de camada de imagem de moda dentro de um layout">

> [!NOTE]
> Ajuste um sujeito em camadas dentro de uma composição visual.

---

<a id="case-10"></a>

### Case 10: Edição de camada gráfica em pôster esportivo

<img src="assets/media/012-Feishu-Docs-Image.gif" width="720" alt="Edição de camada gráfica em pôster esportivo">

> [!NOTE]
> Edite um gráfico de corrida mantendo tipografia e composição alinhadas.

---

<a id="case-11"></a>

### Case 11: Edição de elemento de pôster: Public Joy

<img src="assets/media/013-Feishu-Docs-Image.gif" width="720" alt="Edição de elemento de pôster: Public Joy">

> [!NOTE]
> Modifique elementos do pôster preservando a linguagem de design original.

---

<a id="case-12"></a>

### Case 12: Troca de superfície material com resposta precisa de textura

<img src="assets/media/014-Feishu-Docs-Image.gif" width="720" alt="Troca de superfície material com resposta precisa de textura">

> [!NOTE]
> Troque alvos de material e cor mantendo intacta a estrutura do objeto.

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

<img src="assets/media/015-Feishu-Docs-Image.png" width="420" alt="Movimento de objeto por posição em grade antes">

</td>
<td width="50%" valign="top">

**Depois:**

<img src="assets/media/016-Feishu-Docs-Image.png" width="420" alt="Movimento de objeto por posição em grade depois">

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

<img src="assets/media/017-Feishu-Docs-Image.png" width="720" alt="Separação de camada de primeiro plano / pessoa">

> [!NOTE]
> Separe um sujeito em primeiro plano de um fundo parecido com pôster para reutilização posterior.

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

<img src="assets/media/018-Feishu-Docs-Image.png" width="420" alt="Entrada de composição de natureza-morta com sete referências">

</td>
<td width="50%" valign="top">

**Saída:**

<img src="assets/media/019-Feishu-Docs-Image.png" width="420" alt="Saída de composição de natureza-morta com sete referências">

</td>
</tr>
</table>

> [!NOTE]
> Use as sete referências com fundo branco como grupo de entrada e gere a saída de fotografia de natureza-morta em um único case emparelhado.


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

<img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="Tênis cinematográfico com vidro estilhaçado">

> [!NOTE]
> Geração de cena de alto movimento com fragmentos de vidro, timing de ação e iluminação cinematográfica.

---

<a id="case-17"></a>

### Case 17: Ação cinematográfica de boxe

<img src="assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="Ação cinematográfica de boxe">

> [!NOTE]
> Renderização de cena de ação com maior sensação de movimento, impacto e profundidade.

---

<a id="case-18"></a>

### Case 18: Cena em estilo de animação 3D

<img src="assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="Cena em estilo de animação 3D">

> [!NOTE]
> Saída 3D / animação estilizada para personagens ou visuais de entretenimento.

---

<a id="case-19"></a>

### Case 19: Arte conceitual visual

<img src="assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="Arte conceitual visual">

> [!NOTE]
> Geração em estilo de arte conceitual para explorar atmosfera, direção visual e mood.

---

<a id="case-20"></a>

### Case 20: Visual de cena de jogo

<img src="assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="Visual de cena de jogo">

> [!NOTE]
> Geração de cena tipo jogo para explorar ambiente, set ou key art.

---

<a id="multilingual-text-rendering"></a>

## 🌐 Renderização de texto multilíngue

Agrupe as amostras multilíngues por idioma renderizado e caso de uso de texto local.

Número de casos: **5**.

<a id="case-21"></a>

### Case 21: Placa de boas-vindas em árabe e inglês

<img src="assets/media/025-Welcome.png" width="720" alt="Placa de boas-vindas em árabe e inglês">

> [!NOTE]
> Renderização multilíngue nativa com texto árabe e inglês no mesmo visual.

---

<a id="case-22"></a>

### Case 22: Placa coreana de aberto 24 horas

<img src="assets/media/026-24-Open-24-hours.png" width="720" alt="Placa coreana de aberto 24 horas">

> [!NOTE]
> Renderização de texto coreano para vitrines ou sinalização localizada.

---

<a id="case-23"></a>

### Case 23: Placa tailandesa de limpeza

<img src="assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="Placa tailandesa de limpeza">

> [!NOTE]
> Renderização de texto tailandês para espaços públicos locais ou visuais de campanha.

---

<a id="case-24"></a>

### Case 24: Pôster francês de criação

<img src="assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="Pôster francês de criação">

> [!NOTE]
> Renderização de texto francês para produtos, moda e recursos de campanha.

---

<a id="case-25"></a>

### Case 25: Pôster russo de futuro

<img src="assets/media/029-Future.png" width="720" alt="Pôster russo de futuro">

> [!NOTE]
> Renderização de texto russo com estrutura clara de caracteres para conceitos visuais localizados.

---

<a id="model-notes"></a>

## 🧩 Notas do modelo

| Área | Nota com base na fonte |
|---|---|
| ID do modelo | O material oficial lista `dola-seedream-5-0-pro-260628`; a verificação de runtime na EvoLink ainda é necessária antes que isso se torne evidência de primeira execução. |
| Imagens de entrada | O material oficial diz que Seedream 5.0 Pro suporta até 10 imagens de entrada. |
| Resolução de saída | Não afirme que o Pro oferece 4K; o material fonte descreve níveis de saída em torno de `<= 2.36M` pixels e `> 2.36M` pixels. |
| Idiomas nativos de prompt | O material oficial lista árabe, inglês, russo, indonésio, espanhol, alemão, turco, português, malaio, vietnamita, francês, japonês, coreano, tagalo e tailandês. |
| Caminho de Seedream para Seedance | O material oficial diz que saídas do Seedream 5.0 Pro/Lite podem se tornar entradas confiáveis para fluxos imagem-para-vídeo da família Seedance, com condições de conta e moderação. |

<a id="acknowledge"></a>

## 🙏 Agradecimentos

Este repositório foi criado a partir do material oficial de lançamento do Seedream 5.0 Pro exportado em 8 de julho de 2026 e de correções oficiais sobre o inventário de casos.

- URLs privadas da fonte oficial são mantidas apenas em evidência local de auditoria.
- Blocos de prompt são incluídos apenas quando o material oficial fornece texto de prompt.
- Casos somente com mídia permanecem somente com mídia; prompts ausentes não são inventados.

*Se algum limite de case público precisar de correção, abra uma issue ou envie um patch com evidência concreta da fonte.*
