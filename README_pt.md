<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Guia com fontes, padrões de prompts e exemplos visuais para avaliar fluxos de geração e edição de imagens com Seedream 5.0 Pro.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Introdução

Seedream 5.0 Pro é apresentado no material oficial de lançamento como um modelo de geração e edição de imagens para produção visual controlável. O material destaca edições direcionadas por região, edições guiadas por esboços, posicionamento por âncoras, separação em camadas, controle de materiais e cores, composição com múltiplas referências, imagens cinematográficas e renderização de texto multilíngue.

Este repositório é uma superfície de **guia e prompts**. Ele reúne padrões de prompts e exemplos de mídia respaldados por fontes para que builders possam inspecionar o que testar, copiar apenas os prompts presentes no material de origem e avançar para uma rota de conversão no EvoLink quando o acesso estiver disponível.

Experimente o ponto de entrada do modelo no EvoLink: [Abrir a rota do Seedream 5.0 Pro no EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Início rápido:** este repositório não afirma que uma rota de primeira execução da API EvoLink para Seedream 5.0 Pro foi verificada. Use esta rota pública até que a evidência de execução do modelo atual seja registrada:

1. [Abrir o EvoLink para acessar o Seedream 5.0 Pro](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Obter sua chave API do EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. Tratar a referência oficial do ModelArk como contexto técnico: [Ler a documentação do Seedream 5.0 Pro no ModelArk](https://docs.byteplus.com/en/docs/ModelArk/1541523).

Estado de execução: o material oficial nomeia `dola-seedream-5-0-pro-260628` como o ID do modelo Seedream 5.0 Pro, mas este repositório não concluiu um smoke test da API EvoLink com consumo de créditos. Não trate exemplos de modelos de imagem adjacentes como evidência verificada de primeira execução para Seedream 5.0 Pro.

<a id="news"></a>

## 📰 Notícias

- **2026-07-08:** Scaffold local inicial criado a partir do material oficial de lançamento do Seedream 5.0 Pro e da exportação de mídia.

<a id="menu"></a>

## 📑 Menu

- [🍌 Introdução](#introduction)
- [📰 Notícias](#news)
- [📑 Menu](#menu)
- [🧭 Categorias de edição interativa](#interactive-editing-categories)
- [🎛️ Padrões de prompts para edição controlada](#controlled-editing-prompt-patterns)
  - [Case 1: Descrição de objetos por caixas de região para edição direcionada](#case-1)
  - [Case 2: Edição por posição de âncora em uma cena em grade](#case-2)
  - [Case 3: Composição de natureza-morta com múltiplas referências](#case-3)
- [🎬 Galeria visual de capacidades](#visual-capability-gallery)
- [🧩 Notas do modelo](#model-notes)
- [🙏 Agradecimentos](#acknowledge)

<a id="interactive-editing-categories"></a>

## 🧭 Categorias de edição interativa

O material oficial do Seedream 5.0 Pro agrupa a edição controlável em seis modos práticos. Use este mapa antes de escolher um padrão de prompt, porque o sinal de controle muda o que o prompt deve especificar.

| Categoria | O que o usuário fornece | Melhor para |
|---|---|---|
| Controle interativo | Seleções, pontos, setas, caixas de anotação ou coordenadas que apontam para a região alvo. | Geração ou modificação local com intenção espacial explícita. |
| Edição por esboço | Rabiscos, blocos de cor, linhas ou esboços simples com instruções em linguagem natural. | Transformar intenção visual aproximada em objetos ou detalhes renderizados. |
| Edição por âncora / posição | Âncoras textuais em uma cena em grade ou claramente organizada. | Mover ou reposicionar objetos específicos evitando regiões não alvo. |
| Separação em camadas | Um prompt que pede dividir primeiro plano, fundo e componentes em camadas editáveis. | Arrastar, escalar, recompor e reutilizar ativos em fluxos posteriores. |
| Resposta precisa de cor e material | Códigos hex / de cor e descrições de materiais. | Variantes de produto, correspondência de cor de marca e troca de materiais. |
| Edição por fusão multiimagem | Várias imagens de referência com uma instrução de layout, estilo ou material. | Combinar produtos, estilos, texturas ou objetos em uma imagem coerente. |

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ Padrões de prompts para edição controlada


<a id="case-1"></a>

### Case 1: Descrição de objetos por caixas de região para edição direcionada

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

### Case 2: Edição por posição de âncora em uma cena em grade

<table>
  <tr>
    <td width="50%" valign="top"><strong>Antes</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>Depois</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: Official.

<a id="case-3"></a>

### Case 3: Composição de natureza-morta com múltiplas referências

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.gif)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: Official.

<a id="visual-capability-gallery"></a>

## 🎬 Galeria visual de capacidades

O material oficial inclui amostras visuais adicionais de edição guiada por esboços, separação em camadas, imagens narrativas cinematográficas e renderização de texto multilíngue.

<table>
  <tr>
    <td width="50%" valign="top"><strong>Rabiscos guiados por esboço</strong><br><img src="assets/media/005-doodles.gif" alt="Rabiscos guiados por esboço example"></td>
    <td width="50%" valign="top"><strong>Bloco de cor guiado por esboço</strong><br><img src="assets/media/006-color-block.gif" alt="Bloco de cor guiado por esboço example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Linhas guiadas por esboço</strong><br><img src="assets/media/007-lines.gif" alt="Linhas guiadas por esboço example"></td>
    <td width="50%" valign="top"><strong>Controle por esboço simples</strong><br><img src="assets/media/008-simple-sketches.gif" alt="Controle por esboço simples example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Exemplo de separação em camadas</strong><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Exemplo de separação em camadas"></td>
    <td width="50%" valign="top"><strong>Variante de separação em camadas</strong><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Variante de separação em camadas"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Tênis cinematográfico com vidro estilhaçado</strong><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Tênis cinematográfico com vidro estilhaçado"></td>
    <td width="50%" valign="top"><strong>Ação cinematográfica de boxe</strong><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Ação cinematográfica de boxe"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong>Renderização de texto em árabe e inglês</strong><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong>Renderização de texto em coreano</strong><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 Notas do modelo

| Área | Nota respaldada por fonte |
|---|---|
| ID do modelo | O material oficial lista `dola-seedream-5-0-pro-260628`; ainda é necessária verificação de execução no EvoLink antes que isso se torne evidência de primeira execução. |
| Imagens de entrada | O material de origem informa que Seedream 5.0 Pro aceita até 10 imagens de entrada. |
| Resolução de saída | O material de origem diz que o posicionamento público não deve prometer 4K para o Pro; ele descreve faixas de saída em torno de <= 2,36M pixels e > 2,36M pixels. |
| Idiomas nativos de prompt | O material de origem lista árabe, inglês, russo, indonésio, espanhol, alemão, turco, português, malaio, vietnamita, francês, japonês, coreano, tagalo e tailandês. |
| Caminho de Seedream para Seedance | O material de origem diz que saídas do Seedream 5.0 Pro/Lite podem se tornar entradas confiáveis para fluxos de imagem para vídeo da família Seedance, com condições de conta e moderação. |

<a id="acknowledge"></a>

## 🙏 Agradecimentos

Este repositório foi criado a partir do material oficial de lançamento do Seedream 5.0 Pro exportado em 2026-07-08.

- URL fonte privada: registrada na evidência local de auditoria, não exposta como link público do README.
- Nota de execução: uma prova de API do EvoLink que consome créditos ainda não foi executada nesta auditoria do repositório.
