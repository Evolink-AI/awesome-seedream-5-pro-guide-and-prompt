<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Banner de Awesome Seedream 5.0 Pro en EvoLink"></a>

# Guía y prompts de Awesome Seedream 5.0 Pro

Guía con respaldo de fuentes, patrones de prompt y ejemplos visuales para evaluar flujos de generación y edición de imágenes con Seedream 5.0 Pro.

[![Licencia: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Usar en EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Obtener clave API](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Introducción

Seedream 5.0 Pro se presenta en el material oficial de lanzamiento como un modelo controlable de generación y edición de imágenes. Esta guía mantiene el README público alineado con el menú oficial de capacidades: control de interacción, edición con bocetos, edición por capas, posicionamiento por anclas, separación de capas, fusión de múltiples imágenes, muestras visuales y renderizado de texto multilingüe.

**Usa este repositorio para revisar ejemplos respaldados por la fuente, copiar solo los prompts que aparecen en el material oficial y entender cómo cada categoría se vincula con casos visibles.**

Prueba el punto de entrada del modelo en EvoLink: [abrir Seedream 5.0 Pro en EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Inicio rápido:** Este repositorio no afirma que ya exista una ruta API de primera ejecución verificada en EvoLink para Seedream 5.0 Pro. Usa la entrada pública del modelo, el panel de claves API y la referencia técnica oficial hasta que haya evidencia de runtime.

1. [Abrir la ruta de Seedream 5.0 Pro en EvoLink](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [Obtener tu clave API de EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [Leer la referencia técnica oficial de ModelArk](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> Política de fuente: material oficial de lanzamiento. Las URL privadas de Lark/Feishu se conservan solo en evidencia local de auditoría y no se exponen como páginas públicas de fuente en el README.

<a id="news"></a>

## 📰 Novedades

- **July 8, 2026:** Guía inicial reorganizada según el menú oficial y el inventario de casos corregido oficialmente.

<a id="menu"></a>

## 📑 Menú

- [🍌 Introducción](#introduction)
- [📰 Novedades](#news)
- [📑 Menú](#menu)
- [🎛️ Control de interacción](#interaction-control)
  - [Case 1: Flechas y cuadros de anotación para intención espacial](#case-1)
  - [Case 2: Descripción de objetos por cuadro de región para edición dirigida](#case-2)
- [✏️ Edición con bocetos](#sketch-editing)
  - [Case 3: Generación de objetos guiada por garabatos](#case-3)
  - [Case 4: Edición guiada por bloques de color](#case-4)
  - [Case 5: Edición de detalles guiada por líneas](#case-5)
  - [Case 6: De boceto simple a imagen refinada](#case-6)
- [🧱 Edición por capas](#layer-editing)
  - [Case 7: Edición de texto y capa gráfica de póster: Avery Turns](#case-7)
  - [Case 8: Edición de capa de oferta de póster: Happy Hour](#case-8)
  - [Case 9: Edición de capa de imagen de moda dentro de un diseño](#case-9)
  - [Case 10: Edición de capa gráfica de póster deportivo](#case-10)
  - [Case 11: Edición de elemento de póster: Public Joy](#case-11)
  - [Case 12: Cambio de superficie material con respuesta de textura precisa](#case-12)
- [📍 Edición por ancla / posición](#anchor-position-editing)
  - [Case 13: Movimiento de objeto por posición de cuadrícula](#case-13)
- [🧩 Separación de capas](#layer-separation)
  - [Case 14: Separación de capa de primer plano / persona](#case-14)
- [🖼️ Edición por fusión de múltiples imágenes](#multi-image-fusion-editing)
  - [Case 15: Composición de bodegón de entrada/salida con siete referencias](#case-15)
- [🎬 Calidad visual y narrativa](#visual-quality-narrative)
  - [Case 16: Tenis cinematográfico con cristal quebrado](#case-16)
  - [Case 17: Acción cinematográfica de boxeo](#case-17)
  - [Case 18: Escena con estilo de animación 3D](#case-18)
  - [Case 19: Arte conceptual visual](#case-19)
  - [Case 20: Visual de escena de juego](#case-20)
- [🌐 Renderizado de texto multilingüe](#multilingual-text-rendering)
  - [Case 21: Cartel de bienvenida en árabe e inglés](#case-21)
  - [Case 22: Cartel coreano de abierto 24 horas](#case-22)
  - [Case 23: Cartel tailandés de limpieza](#case-23)
  - [Case 24: Póster francés de creación](#case-24)
  - [Case 25: Póster ruso de futuro](#case-25)
- [🧩 Notas del modelo](#model-notes)
- [🙏 Agradecimientos](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ Control de interacción

Usa cuadros, puntos, flechas, marcas de anotación o coordenadas para especificar la región objetivo.

Número de casos: **2**.

<a id="case-1"></a>

### Case 1: Flechas y cuadros de anotación para intención espacial

<img src="assets/media/003-arrows-annotation-boxes.gif" width="720" alt="Flechas y cuadros de anotación para intención espacial">

> [!NOTE]
> Usa flechas, cuadros y anotaciones para hacer explícita la zona objetivo antes de editar.

---

<a id="case-2"></a>

### Case 2: Descripción de objetos por cuadro de región para edición dirigida

<img src="assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="Descripción de objetos por cuadro de región para edición dirigida">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ Edición con bocetos

Usa garabatos, bloques de color, líneas o bocetos simples como guía visual.

Número de casos: **4**.

<a id="case-3"></a>

### Case 3: Generación de objetos guiada por garabatos

<img src="assets/media/005-doodles.gif" width="720" alt="Generación de objetos guiada por garabatos">

> [!NOTE]
> Usa garabatos sueltos como señal de control visual y deja que el modelo renderice el objeto previsto.

---

<a id="case-4"></a>

### Case 4: Edición guiada por bloques de color

<img src="assets/media/006-color-block.gif" width="720" alt="Edición guiada por bloques de color">

> [!NOTE]
> Usa bloques de color amplios para indicar composición aproximada, zonas de color o ubicación de objetos.

---

<a id="case-5"></a>

### Case 5: Edición de detalles guiada por líneas

<img src="assets/media/007-lines.gif" width="720" alt="Edición de detalles guiada por líneas">

> [!NOTE]
> Usa guía de líneas simples cuando el contorno de la forma importa más que una descripción larga.

---

<a id="case-6"></a>

### Case 6: De boceto simple a imagen refinada

<img src="assets/media/008-simple-sketches.gif" width="720" alt="De boceto simple a imagen refinada">

> [!NOTE]
> Convierte un boceto mínimo en una imagen renderizada más completa sin perder la intención del boceto.

---

<a id="layer-editing"></a>

## 🧱 Edición por capas

Edita capas de póster, gráficos, texto, material o superficie sin romper la composición general.

Número de casos: **6**.

<a id="case-7"></a>

### Case 7: Edición de texto y capa gráfica de póster: Avery Turns

<img src="assets/media/009-Feishu-Docs-Image.gif" width="720" alt="Edición de texto y capa gráfica de póster: Avery Turns">

> [!NOTE]
> Edita elementos visibles del póster preservando la estructura general del diseño.

---

<a id="case-8"></a>

### Case 8: Edición de capa de oferta de póster: Happy Hour

<img src="assets/media/010-Feishu-Docs-Image.gif" width="720" alt="Edición de capa de oferta de póster: Happy Hour">

> [!NOTE]
> Cambia una insignia promocional o un elemento gráfico sin reconstruir todo el póster.

---

<a id="case-9"></a>

### Case 9: Edición de capa de imagen de moda dentro de un diseño

<img src="assets/media/011-Feishu-Docs-Image.gif" width="720" alt="Edición de capa de imagen de moda dentro de un diseño">

> [!NOTE]
> Ajusta un sujeto por capas dentro de una composición visual ya diseñada.

---

<a id="case-10"></a>

### Case 10: Edición de capa gráfica de póster deportivo

<img src="assets/media/012-Feishu-Docs-Image.gif" width="720" alt="Edición de capa gráfica de póster deportivo">

> [!NOTE]
> Edita un gráfico de carreras manteniendo alineadas la tipografía y la composición.

---

<a id="case-11"></a>

### Case 11: Edición de elemento de póster: Public Joy

<img src="assets/media/013-Feishu-Docs-Image.gif" width="720" alt="Edición de elemento de póster: Public Joy">

> [!NOTE]
> Modifica elementos del póster preservando el lenguaje visual de origen.

---

<a id="case-12"></a>

### Case 12: Cambio de superficie material con respuesta de textura precisa

<img src="assets/media/014-Feishu-Docs-Image.gif" width="720" alt="Cambio de superficie material con respuesta de textura precisa">

> [!NOTE]
> Cambia objetivos de material y color manteniendo intacta la estructura del objeto.

---

<a id="anchor-position-editing"></a>

## 📍 Edición por ancla / posición

Usa anclas en forma de cuadrícula o posiciones relativas para mover un objetivo específico con precisión.

Número de casos: **1**.

<a id="case-13"></a>

### Case 13: Movimiento de objeto por posición de cuadrícula

<table>
<tr>
<td width="50%" valign="top">

**Antes:**

<img src="assets/media/015-Feishu-Docs-Image.png" width="420" alt="Movimiento de objeto por posición de cuadrícula antes">

</td>
<td width="50%" valign="top">

**Después:**

<img src="assets/media/016-Feishu-Docs-Image.png" width="420" alt="Movimiento de objeto por posición de cuadrícula después">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 Separación de capas

Separa primer plano, fondo y componentes reutilizables para edición posterior.

Número de casos: **1**.

<a id="case-14"></a>

### Case 14: Separación de capa de primer plano / persona

<img src="assets/media/017-Feishu-Docs-Image.png" width="720" alt="Separación de capa de primer plano / persona">

> [!NOTE]
> Separa un sujeto en primer plano de un fondo tipo póster para reutilizarlo después.

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ Edición por fusión de múltiples imágenes

Combina varias imágenes de referencia en una composición coherente siguiendo una sola instrucción.

Número de casos: **1**.

<a id="case-15"></a>

### Case 15: Composición de bodegón de entrada/salida con siete referencias

<table>
<tr>
<td width="50%" valign="top">

**Entrada:**

<img src="assets/media/018-Feishu-Docs-Image.png" width="420" alt="Entrada de composición de bodegón con siete referencias">

</td>
<td width="50%" valign="top">

**Salida:**

<img src="assets/media/019-Feishu-Docs-Image.png" width="420" alt="Salida de composición de bodegón con siete referencias">

</td>
</tr>
</table>

> [!NOTE]
> Usa las siete referencias con fondo blanco como grupo de entrada y genera la salida de fotografía de bodegón en un único case emparejado.


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 Calidad visual y narrativa

Agrupa las muestras de efecto por acción cinematográfica, 3D / animación, arte conceptual y salida de escena de juego.

Número de casos: **5**.

<a id="case-16"></a>

### Case 16: Tenis cinematográfico con cristal quebrado

<img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="Tenis cinematográfico con cristal quebrado">

> [!NOTE]
> Generación de escenas de alto movimiento con fragmentos de vidrio, timing de acción e iluminación cinematográfica.

---

<a id="case-17"></a>

### Case 17: Acción cinematográfica de boxeo

<img src="assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="Acción cinematográfica de boxeo">

> [!NOTE]
> Renderizado de escena de acción con mayor sensación de movimiento, impacto y profundidad.

---

<a id="case-18"></a>

### Case 18: Escena con estilo de animación 3D

<img src="assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="Escena con estilo de animación 3D">

> [!NOTE]
> Salida 3D / animada estilizada para personajes o visuales de entretenimiento.

---

<a id="case-19"></a>

### Case 19: Arte conceptual visual

<img src="assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="Arte conceptual visual">

> [!NOTE]
> Generación con estilo de arte conceptual para explorar atmósfera, dirección visual y mood.

---

<a id="case-20"></a>

### Case 20: Visual de escena de juego

<img src="assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="Visual de escena de juego">

> [!NOTE]
> Generación de escena tipo juego para explorar entorno, set o key art.

---

<a id="multilingual-text-rendering"></a>

## 🌐 Renderizado de texto multilingüe

Agrupa las muestras multilingües por idioma renderizado y caso de uso de texto local.

Número de casos: **5**.

<a id="case-21"></a>

### Case 21: Cartel de bienvenida en árabe e inglés

<img src="assets/media/025-Welcome.png" width="720" alt="Cartel de bienvenida en árabe e inglés">

> [!NOTE]
> Renderizado multilingüe nativo con texto árabe e inglés en la misma imagen.

---

<a id="case-22"></a>

### Case 22: Cartel coreano de abierto 24 horas

<img src="assets/media/026-24-Open-24-hours.png" width="720" alt="Cartel coreano de abierto 24 horas">

> [!NOTE]
> Renderizado de texto coreano para escaparates o señalética localizada.

---

<a id="case-23"></a>

### Case 23: Cartel tailandés de limpieza

<img src="assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="Cartel tailandés de limpieza">

> [!NOTE]
> Renderizado de texto tailandés para espacios públicos locales o visuales de campaña.

---

<a id="case-24"></a>

### Case 24: Póster francés de creación

<img src="assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="Póster francés de creación">

> [!NOTE]
> Renderizado de texto francés para productos, moda y recursos de campaña.

---

<a id="case-25"></a>

### Case 25: Póster ruso de futuro

<img src="assets/media/029-Future.png" width="720" alt="Póster ruso de futuro">

> [!NOTE]
> Renderizado de texto ruso con estructura de caracteres clara para conceptos visuales localizados.

---

<a id="model-notes"></a>

## 🧩 Notas del modelo

| Área | Nota respaldada por fuente |
|---|---|
| ID del modelo | El material oficial lista `dola-seedream-5-0-pro-260628`; todavía se requiere verificación de runtime en EvoLink antes de usarlo como evidencia de primera ejecución. |
| Imágenes de entrada | El material oficial indica que Seedream 5.0 Pro admite hasta 10 imágenes de entrada. |
| Resolución de salida | No afirmes que Pro ofrece 4K; el material fuente describe niveles de salida alrededor de `<= 2.36M` píxeles y `> 2.36M` píxeles. |
| Idiomas nativos de prompt | El material oficial lista árabe, inglés, ruso, indonesio, español, alemán, turco, portugués, malayo, vietnamita, francés, japonés, coreano, tagalo y tailandés. |
| Ruta de Seedream a Seedance | El material oficial indica que las salidas de Seedream 5.0 Pro/Lite pueden convertirse en entradas confiables para flujos de imagen a video de la familia Seedance, con condiciones de cuenta y moderación. |

<a id="acknowledge"></a>

## 🙏 Agradecimientos

Este repositorio se creó a partir del material oficial de lanzamiento de Seedream 5.0 Pro exportado el 8 de julio de 2026 y de las correcciones oficiales sobre el inventario de casos.

- Las URL privadas de la fuente oficial se conservan solo en evidencia local de auditoría.
- Los bloques de prompt se incluyen solo cuando el material oficial proporciona texto de prompt.
- Los casos solo con medios permanecen solo con medios; no se inventan prompts faltantes.

*Si algún límite de caso público necesita corrección, abre un issue o envía un patch con evidencia concreta de la fuente.*
