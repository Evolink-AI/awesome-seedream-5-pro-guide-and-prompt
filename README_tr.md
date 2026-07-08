<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink banner"></a>

# Awesome Seedream 5.0 Pro Guide and Prompt

Seedream 5.0 Pro görüntü üretme ve düzenleme iş akışlarını değerlendirmek için kaynaklı rehber, prompt kalıpları ve görsel örnekler.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![Use on EvoLink](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![Get API Key](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Giriş

Seedream 5.0 Pro, resmi lansman materyalinde kontrol edilebilir görsel üretim için bir görüntü üretme ve düzenleme modeli olarak sunulur. Kaynak materyal; bölge odaklı düzenlemeleri, eskiz rehberli düzenlemeleri, çapa konumlandırmayı, katman ayrımını, malzeme ve renk kontrolünü, çok referanslı kompozisyonu, sinematik görüntüleri ve çok dilli metin işlemeyi vurgular.

Bu depo bir **rehber ve prompt** yüzeyidir. Kaynak destekli prompt kalıplarını ve medya örneklerini tek yerde tutar; böylece geliştiriciler neyi test edeceklerini inceleyebilir, yalnızca kaynak materyalde görünen promptları kopyalayabilir ve erişim hazır olduğunda EvoLink dönüşüm yoluna ilerleyebilir.

Model giriş noktasını EvoLink üzerinde dene: [EvoLink Seedream 5.0 Pro yolunu aç](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Hızlı başlangıç:** bu depo, EvoLink Seedream 5.0 Pro için ilk API çalıştırma yolunun doğrulandığını iddia etmez. Güncel model çalışma kanıtı kaydedilene kadar bu yolu herkese açık dönüşüm rotası olarak kullanın:

1. [Seedream 5.0 Pro erişimi için EvoLink’i aç](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API anahtarını al](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. Resmi ModelArk referansını teknik arka plan olarak kullan: [Seedream 5.0 Pro ModelArk belgelerini oku](https://docs.byteplus.com/en/docs/ModelArk/1541523).

Çalışma durumu: resmi materyal `dola-seedream-5-0-pro-260628` değerini Seedream 5.0 Pro model ID’si olarak adlandırır, ancak bu depo kredi tüketen bir EvoLink API smoke testini tamamlamamıştır. Yakın model örneklerini Seedream 5.0 Pro için doğrulanmış ilk çalıştırma kanıtı olarak değerlendirmeyin.

<a id="news"></a>

## 📰 Haberler

- **2026-07-08:** İlk yerel scaffold, resmi Seedream 5.0 Pro lansman materyali ve medya dışa aktarımından oluşturuldu.

<a id="menu"></a>

## 📑 Menü

- [🍌 Giriş](#introduction)
- [📰 Haberler](#news)
- [📑 Menü](#menu)
- [🎛️ Kontrollü düzenleme prompt kalıpları](#controlled-editing-prompt-patterns)
  - [Case 1: Hedefli düzenleme için bölge kutusu nesne açıklaması](#case-1)
  - [Case 2: Izgara benzeri sahnede çapa konumu düzenleme](#case-2)
  - [Case 3: Çok referanslı natürmort kompozisyonu](#case-3)
- [🎬 Görsel yetenek galerisi](#visual-capability-gallery)
- [🧩 Model notları](#model-notes)
- [🙏 Teşekkür](#acknowledge)

<a id="controlled-editing-prompt-patterns"></a>

## 🎛️ Kontrollü düzenleme prompt kalıpları

Aşağıdaki case’ler uydurulmuş örnekler değildir. `docs/source-notes.md` içinde özetlenen resmi Seedream 5.0 Pro kaynak materyalinden kopyalanmış veya çevrilmiştir.

<a id="case-1"></a>

### Case 1: [Hedefli düzenleme için bölge kutusu nesne açıklaması](docs/source-notes.md#included-public-cases)

![Region-box annotation example](assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.png)

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

Source: Official.

<a id="case-2"></a>

### Case 2: [Izgara benzeri sahnede çapa konumu düzenleme](docs/source-notes.md#included-public-cases)

<table>
  <tr>
    <td width="50%" valign="top"><strong>Önce</strong><br><img src="assets/media/015-Feishu-Docs-Image.png" alt="Anchor positioning example before edit"></td>
    <td width="50%" valign="top"><strong>Sonra</strong><br><img src="assets/media/016-Feishu-Docs-Image.png" alt="Anchor positioning example after edit"></td>
  </tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

Source: Official.

<a id="case-3"></a>

### Case 3: [Çok referanslı natürmort kompozisyonu](docs/source-notes.md#included-public-cases)

![Multi-reference material example](assets/media/014-Feishu-Docs-Image.png)

**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

Source: Official.

<a id="visual-capability-gallery"></a>

## 🎬 Görsel yetenek galerisi

Resmi materyal; eskiz rehberli düzenleme, katman ayrımı, sinematik anlatı görüntüleri ve çok dilli metin işleme için ek görsel örnekler içerir.

<table>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Eskiz rehberli karalamalar</a></strong><br><img src="assets/media/005-doodles.png" alt="Eskiz rehberli karalamalar example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Eskiz rehberli renk bloğu</a></strong><br><img src="assets/media/006-color-block.png" alt="Eskiz rehberli renk bloğu example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Eskiz rehberli çizgiler</a></strong><br><img src="assets/media/007-lines.png" alt="Eskiz rehberli çizgiler example"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Basit eskiz kontrolü</a></strong><br><img src="assets/media/008-simple-sketches.png" alt="Basit eskiz kontrolü example"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Katman ayrımı örneği</a></strong><br><img src="assets/media/017-Feishu-Docs-Image.png" alt="Katman ayrımı örneği"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Katman ayrımı varyantı</a></strong><br><img src="assets/media/018-Feishu-Docs-Image.png" alt="Katman ayrımı varyantı"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Sinematik tenis cam kırılması</a></strong><br><img src="assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" alt="Sinematik tenis cam kırılması"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Sinematik boks aksiyonu</a></strong><br><img src="assets/media/021-Cinematic-narrative-action-boxing.png" alt="Sinematik boks aksiyonu"></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Arapça ve İngilizce metin işleme</a></strong><br><img src="assets/media/025-Welcome.png" alt="Arabic and English welcome text rendering"></td>
    <td width="50%" valign="top"><strong><a href="docs/source-notes.md#included-public-cases">Korece metin işleme</a></strong><br><img src="assets/media/026-24-Open-24-hours.png" alt="Korean open 24 hours text rendering"></td>
  </tr>
</table>

<a id="model-notes"></a>

## 🧩 Model notları

| Alan | Kaynak destekli not |
|---|---|
| Model ID | Resmi materyal `dola-seedream-5-0-pro-260628` değerini listeler; bunun ilk çalıştırma kanıtı sayılabilmesi için EvoLink çalışma doğrulaması hâlâ gerekir. |
| Giriş görüntüleri | Kaynak materyal, Seedream 5.0 Pro’nun 10 adede kadar giriş görüntüsünü desteklediğini söyler. |
| Çıktı çözünürlüğü | Kaynak materyal, Pro için herkese açık konumlandırmada 4K iddiası yapılmaması gerektiğini söyler; <= 2,36M piksel ve > 2,36M piksel civarında çıktı katmanları açıklar. |
| Yerel prompt dilleri | Kaynak materyal Arapça, İngilizce, Rusça, Endonezce, İspanyolca, Almanca, Türkçe, Portekizce, Malayca, Vietnamca, Fransızca, Japonca, Korece, Tagalogca ve Taycayı listeler. |
| Seedream’den Seedance’e yol | Kaynak materyal, Seedream 5.0 Pro/Lite çıktılarının hesap ve moderasyon koşullarıyla Seedance ailesi image-to-video iş akışları için güvenilir girdilere dönüşebileceğini söyler. |

<a id="acknowledge"></a>

## 🙏 Teşekkür

Bu depo, 2026-07-08 tarihinde dışa aktarılan resmi Seedream 5.0 Pro lansman materyalinden oluşturuldu.

- Herkese açık kaynak notu: `docs/source-notes.md`
- Özel kaynak URL: yerel denetim kanıtında kayıtlıdır, README içinde herkese açık bağlantı olarak gösterilmez.
- Çalışma notu: Bu depo denetiminde kredi tüketen bir EvoLink API smoke testi çalıştırılmadı.
