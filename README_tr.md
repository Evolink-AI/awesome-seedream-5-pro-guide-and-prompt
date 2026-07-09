<div align="center">

<a href="https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=readme_banner"><img src="assets/banner.png" alt="Awesome Seedream 5.0 Pro EvoLink bannerı"></a>

# Awesome Seedream 5.0 Pro rehberi ve promptları

Seedream 5.0 Pro görüntü üretim ve düzenleme iş akışlarını değerlendirmek için kaynak destekli rehber, prompt kalıpları ve görsel örnekler.

[![License: MIT](assets/badges/license-mit.svg)](LICENSE)
[![EvoLink’te kullan](assets/badges/use-on-evolink.svg)](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_badge)
[![API anahtarı al](assets/badges/get-api-key.svg)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key)

[🇺🇸 English](README.md) · [🇪🇸 Español](README_es.md) · [🇵🇹 Português](README_pt.md) · [🇯🇵 日本語](README_ja.md) · [🇰🇷 한국어](README_ko.md) · [🇩🇪 Deutsch](README_de.md) · [🇫🇷 Français](README_fr.md) · [🇹🇷 Türkçe](README_tr.md) · [🇹🇼 繁體中文](README_zh-TW.md) · [🇨🇳 简体中文](README_zh-CN.md) · [🇷🇺 Русский](README_ru.md)

</div>

<a id="introduction"></a>

## 🍌 Giriş

Seedream 5.0 Pro, resmi lansman materyalinde kontrol edilebilir bir görüntü üretim ve düzenleme modeli olarak sunulur. Bu rehber, README içeriğini resmi yetenek menüsüyle hizalar: etkileşim kontrolü, eskizle düzenleme, katman düzenleme, çapa/konum düzenleme, katman ayırma, çoklu görüntü füzyonu, görsel efekt örnekleri ve çok dilli metin işleme.

**Bu depoyu kaynak destekli örnekleri incelemek, yalnızca resmi materyalde bulunan promptları kopyalamak ve her kategorinin görünen case’lerle nasıl eşleştiğini anlamak için kullanın.**

EvoLink model girişini deneyin: [Seedream 5.0 Pro’yu EvoLink’te açın](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=top_text_cta).

**Hızlı başlangıç:** Bu depo, EvoLink üzerinde Seedream 5.0 Pro için doğrulanmış bir ilk API çalıştırma rotası olduğunu iddia etmez. Çalıştırma kanıtı kaydedilene kadar herkese açık model girişini, API anahtarı panelini ve resmi teknik referansı kullanın.

1. [Seedream 5.0 Pro EvoLink yolunu açın](https://evolink.ai/seedream-5-0-pro?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=model_link).
2. [EvoLink API anahtarınızı alın](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedream-5-pro-guide-and-prompt&utm_content=api_key).
3. [Resmi ModelArk teknik referansını okuyun](https://docs.byteplus.com/en/docs/ModelArk/1541523).

> [!NOTE]
> Kaynak politikası: resmi lansman materyali. Özel Lark/Feishu URL’leri yalnızca yerel denetim kanıtında tutulur ve README’de herkese açık kaynak sayfaları olarak gösterilmez.

<a id="news"></a>

## 📰 Haberler

- **July 8, 2026:** İlk rehber resmi menü ve resmi olarak düzeltilen case envanteri etrafında yeniden kuruldu.

<a id="menu"></a>

## 📑 Menü

- [🍌 Giriş](#introduction)
- [📰 Haberler](#news)
- [📑 Menü](#menu)
- [🎛️ Etkileşim kontrolü](#interaction-control)
  - [Case 1: Mekânsal niyet için oklar ve açıklama kutuları](#case-1)
  - [Case 2: Hedefli düzenleme için bölge kutusu nesne açıklaması](#case-2)
- [✏️ Eskizle düzenleme](#sketch-editing)
  - [Case 3: Karalama rehberli nesne üretimi](#case-3)
  - [Case 4: Renk bloğu rehberli düzenleme](#case-4)
  - [Case 5: Çizgi rehberli detay düzenleme](#case-5)
  - [Case 6: Basit eskizden rafine görüntüye](#case-6)
- [🧱 Katman düzenleme](#layer-editing)
  - [Case 7: Poster metni ve grafik katmanı düzenleme: Avery Turns](#case-7)
  - [Case 8: Poster teklif katmanı düzenleme: Happy Hour](#case-8)
  - [Case 9: Tasarım düzeni içinde moda görseli katmanı düzenleme](#case-9)
  - [Case 10: Spor posteri grafik katmanı düzenleme](#case-10)
  - [Case 11: Poster öğesi düzenleme: Public Joy](#case-11)
  - [Case 12: Hassas doku yanıtıyla malzeme yüzeyi değiştirme](#case-12)
- [📍 Çapa / konum düzenleme](#anchor-position-editing)
  - [Case 13: Izgara konumuna göre nesne hareketi](#case-13)
- [🧩 Katman ayırma](#layer-separation)
  - [Case 14: Ön plan / kişi katmanı ayırma](#case-14)
- [🖼️ Çoklu görüntü füzyon düzenleme](#multi-image-fusion-editing)
  - [Case 15: Yedi referanslı giriş/çıkış natürmort kompozisyonu](#case-15)
- [🎬 Görsel kalite ve anlatı](#visual-quality-narrative)
  - [Case 16: Cam kırılmalı sinematik tenis sahnesi](#case-16)
  - [Case 17: Sinematik boks aksiyonu](#case-17)
  - [Case 18: 3D animasyon tarzı sahne](#case-18)
  - [Case 19: Görsel konsept sanatı](#case-19)
  - [Case 20: Oyun sahnesi görseli](#case-20)
- [🌐 Çok dilli metin işleme](#multilingual-text-rendering)
  - [Case 21: Arapça ve İngilizce karşılama tabelası](#case-21)
  - [Case 22: Korece 24 saat açık tabelası](#case-22)
  - [Case 23: Tayca temizlik tabelası](#case-23)
  - [Case 24: Fransızca yaratım posteri](#case-24)
  - [Case 25: Rusça gelecek posteri](#case-25)
- [🧩 Model notları](#model-notes)
- [🙏 Teşekkür](#acknowledge)

<a id="interaction-control"></a>

## 🎛️ Etkileşim kontrolü

Hedef bölgeyi belirtmek için kutular, noktalar, oklar, açıklama işaretleri veya koordinatlar kullanın.

Case sayısı: **2**.

<a id="case-1"></a>

### Case 1: Mekânsal niyet için oklar ve açıklama kutuları

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/003-arrows-annotation-boxes.gif?v=20260709-camo" width="720" alt="Mekânsal niyet için oklar ve açıklama kutuları">

> [!NOTE]
> Düzenlemeden önce hedef alanı açık hale getirmek için oklar, kutular ve açıklamalar kullanın.

---

<a id="case-2"></a>

### Case 2: Hedefli düzenleme için bölge kutusu nesne açıklaması

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex.gif" width="720" alt="Hedefli düzenleme için bölge kutusu nesne açıklaması">

**Prompt:**

```
Red box: A huge blue-furred head with a ferocious squished expression, gazing at the bubble ahead. Green box: A transparent bubble reflecting the indoor lights. Yellow box: A large warm gray-beige yarn ball. Blue box: A stack of building blocks including a warm dark gray arch, a warm light gray half-cylinder, a lake blue cylinder, a deep lake blue ramp, and a cobalt blue half-disc. Purple box: A grass green tasseled blanket draped over the sofa.
```

---

<a id="sketch-editing"></a>

## ✏️ Eskizle düzenleme

Görsel rehberlik olarak karalamalar, renk blokları, çizgiler veya basit eskizler kullanın.

Case sayısı: **4**.

<a id="case-3"></a>

### Case 3: Karalama rehberli nesne üretimi

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/005-doodles.gif?v=20260709-camo" width="720" alt="Karalama rehberli nesne üretimi">

> [!NOTE]
> Gevşek karalamaları görsel kontrol sinyali olarak kullanın ve modelin amaçlanan nesneyi işlemesini sağlayın.

---

<a id="case-4"></a>

### Case 4: Renk bloğu rehberli düzenleme

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/006-color-block.gif?v=20260709-camo" width="720" alt="Renk bloğu rehberli düzenleme">

> [!NOTE]
> Kabaca kompozisyonu, renk bölgelerini veya nesne yerleşimini belirtmek için geniş renk blokları kullanın.

---

<a id="case-5"></a>

### Case 5: Çizgi rehberli detay düzenleme

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/007-lines.gif?v=20260709-camo" width="720" alt="Çizgi rehberli detay düzenleme">

> [!NOTE]
> Şekil sınırı uzun metin açıklamasından daha önemli olduğunda basit çizgi rehberliği kullanın.

---

<a id="case-6"></a>

### Case 6: Basit eskizden rafine görüntüye

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/008-simple-sketches.gif?v=20260709-camo" width="720" alt="Basit eskizden rafine görüntüye">

> [!NOTE]
> Eskizin niyetini korurken minimal bir eskizi daha tamamlanmış bir render görüntüsüne dönüştürün.

---

<a id="layer-editing"></a>

## 🧱 Katman düzenleme

Daha geniş kompozisyonu koruyarak poster, grafik, metin, malzeme veya yüzey katmanlarını düzenleyin.

Case sayısı: **6**.

<a id="case-7"></a>

### Case 7: Poster metni ve grafik katmanı düzenleme: Avery Turns

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/009-Feishu-Docs-Image.gif" width="720" alt="Poster metni ve grafik katmanı düzenleme: Avery Turns">

> [!NOTE]
> Genel tasarım yapısını koruyarak posterin görünen öğelerini düzenleyin.

---

<a id="case-8"></a>

### Case 8: Poster teklif katmanı düzenleme: Happy Hour

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/010-Feishu-Docs-Image.gif" width="720" alt="Poster teklif katmanı düzenleme: Happy Hour">

> [!NOTE]
> Tüm posteri yeniden oluşturmadan promosyon rozeti veya grafik öğesini değiştirin.

---

<a id="case-9"></a>

### Case 9: Tasarım düzeni içinde moda görseli katmanı düzenleme

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/011-Feishu-Docs-Image.gif" width="720" alt="Tasarım düzeni içinde moda görseli katmanı düzenleme">

> [!NOTE]
> Oluşturulmuş görsel düzen içinde katmanlı bir özneyi ayarlayın.

---

<a id="case-10"></a>

### Case 10: Spor posteri grafik katmanı düzenleme

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/012-Feishu-Docs-Image.gif" width="720" alt="Spor posteri grafik katmanı düzenleme">

> [!NOTE]
> Tipografi ve kompozisyon hizasını koruyarak yarış posteri grafiğini düzenleyin.

---

<a id="case-11"></a>

### Case 11: Poster öğesi düzenleme: Public Joy

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/013-Feishu-Docs-Image.gif" width="720" alt="Poster öğesi düzenleme: Public Joy">

> [!NOTE]
> Kaynak tasarım dilini koruyarak poster öğelerini değiştirin.

---

<a id="case-12"></a>

### Case 12: Hassas doku yanıtıyla malzeme yüzeyi değiştirme

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/014-Feishu-Docs-Image.gif" width="720" alt="Hassas doku yanıtıyla malzeme yüzeyi değiştirme">

> [!NOTE]
> Nesne yapısını bozmadan malzeme ve renk hedeflerini değiştirin.

---

<a id="anchor-position-editing"></a>

## 📍 Çapa / konum düzenleme

Belirli bir hedefi hassas biçimde taşımak için ızgara benzeri çapalar veya göreli konumlar kullanın.

Case sayısı: **1**.

<a id="case-13"></a>

### Case 13: Izgara konumuna göre nesne hareketi

<table>
<tr>
<td width="50%" valign="top">

**Önce:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/015-Feishu-Docs-Image.png" width="420" alt="Izgara konumuna göre nesne hareketi önce">

</td>
<td width="50%" valign="top">

**Sonra:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/016-Feishu-Docs-Image.png" width="420" alt="Izgara konumuna göre nesne hareketi sonra">

</td>
</tr>
</table>

**Prompt:**

```
Move the red car in the lower-left corner one grid cell to the right, and move the black pawn in the second column from the left of the black-square position one grid cell downward.
```

---

<a id="layer-separation"></a>

## 🧩 Katman ayırma

Sonraki düzenleme için ön planı, arka planı ve yeniden kullanılabilir bileşenleri ayırın.

Case sayısı: **1**.

<a id="case-14"></a>

### Case 14: Ön plan / kişi katmanı ayırma

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/017-Feishu-Docs-Image.png" width="720" alt="Ön plan / kişi katmanı ayırma">

> [!NOTE]
> Daha sonra yeniden kullanmak için ön plan öznesini poster benzeri bir arka plandan ayırın.

---

<a id="multi-image-fusion-editing"></a>

## 🖼️ Çoklu görüntü füzyon düzenleme

Tek bir talimat altında birden fazla referans görüntüyü tutarlı bir kompozisyonda birleştirin.

Case sayısı: **1**.

<a id="case-15"></a>

### Case 15: Yedi referanslı giriş/çıkış natürmort kompozisyonu

<table>
<tr>
<td width="50%" valign="top">

**Giriş:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/018-Feishu-Docs-Image.png" width="420" alt="Yedi referanslı natürmort kompozisyonu girişi">

</td>
<td width="50%" valign="top">

**Çıkış:**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/019-Feishu-Docs-Image.png" width="420" alt="Yedi referanslı natürmort kompozisyonu çıkışı">

</td>
</tr>
</table>

> [!NOTE]
> Yedi beyaz arka planlı referansı giriş grubu olarak kullanın ve aynı eşleştirilmiş case içinde natürmort fotoğraf çıktısını üretin.


**Prompt:**

```
Precisely cut out the objects from my seven white-background reference photos and arrange them into a realistic still-life photography image according to the specified layout. Make sure the perspective, lighting, and spatial relationships are correct. Faithfully preserve material details such as wood grain, leather, lace, jelly glass, and feathers, creating a high-quality image that feels realistic and playful, with a blend of vintage and modern aesthetics.
```

---

<a id="visual-quality-narrative"></a>

## 🎬 Görsel kalite ve anlatı

Efekt örneklerini sinematik aksiyon, 3D / animasyon, konsept sanat ve oyun sahnesi çıktısı olarak gruplayın.

Case sayısı: **5**.

<a id="case-16"></a>

### Case 16: Cam kırılmalı sinematik tenis sahnesi

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/020-Cinematic-narrative-tennis-glass-shatter.png" width="720" alt="Cam kırılmalı sinematik tenis sahnesi">

> [!NOTE]
> Cam parçaları, aksiyon zamanlaması ve sinematik ışık içeren yüksek hareketli sahne üretimi.

---

<a id="case-17"></a>

### Case 17: Sinematik boks aksiyonu

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/021-Cinematic-narrative-action-boxing.png" width="720" alt="Sinematik boks aksiyonu">

> [!NOTE]
> Daha güçlü hareket, darbe ve sahne derinliği hissi veren aksiyon sahnesi render’ı.

---

<a id="case-18"></a>

### Case 18: 3D animasyon tarzı sahne

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/022-Cinematic-narrative-3D-animation.png" width="720" alt="3D animasyon tarzı sahne">

> [!NOTE]
> Karakter veya eğlence görselleri için stilize 3D / animasyon çıktısı.

---

<a id="case-19"></a>

### Case 19: Görsel konsept sanatı

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/023-Cinematic-narrative-visual-concept.png" width="720" alt="Görsel konsept sanatı">

> [!NOTE]
> Atmosfer, görsel yön ve duygu keşfi için konsept sanat tarzı üretim.

---

<a id="case-20"></a>

### Case 20: Oyun sahnesi görseli

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/024-Cinematic-narrative-game-scene.png" width="720" alt="Oyun sahnesi görseli">

> [!NOTE]
> Ortam, set veya key art keşfi için oyun benzeri sahne üretimi.

---

<a id="multilingual-text-rendering"></a>

## 🌐 Çok dilli metin işleme

Çok dilli örnekleri işlenen dile ve yerel metin kullanım durumuna göre gruplayın.

Case sayısı: **5**.

<a id="case-21"></a>

### Case 21: Arapça ve İngilizce karşılama tabelası

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/025-Welcome.png" width="720" alt="Arapça ve İngilizce karşılama tabelası">

> [!NOTE]
> Aynı görselde Arapça ve İngilizce metinle yerel çok dilli render.

---

<a id="case-22"></a>

### Case 22: Korece 24 saat açık tabelası

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/026-24-Open-24-hours.png" width="720" alt="Korece 24 saat açık tabelası">

> [!NOTE]
> Yerelleştirilmiş vitrin veya tabela içeriği için Korece metin render’ı.

---

<a id="case-23"></a>

### Case 23: Tayca temizlik tabelası

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/027-Please-help-keep-the-place-clean-together.png" width="720" alt="Tayca temizlik tabelası">

> [!NOTE]
> Yerel kamusal alanlar veya kampanya görselleri için Tayca metin render’ı.

---

<a id="case-24"></a>

### Case 24: Fransızca yaratım posteri

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/028-CREATION-FRANCAISE-Made-in-France.png" width="720" alt="Fransızca yaratım posteri">

> [!NOTE]
> Ürün, moda ve kampanya varlıkları için Fransızca metin render’ı.

---

<a id="case-25"></a>

### Case 25: Rusça gelecek posteri

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedream-5-pro-guide-and-prompt/assets/media/029-Future.png" width="720" alt="Rusça gelecek posteri">

> [!NOTE]
> Yerelleştirilmiş görsel konseptler için net karakter yapısıyla Rusça metin render’ı.

---

<a id="model-notes"></a>

## 🧩 Model notları

| Alan | Kaynak destekli not |
|---|---|
| Model ID | Resmi materyalde `dola-seedream-5-0-pro-260628` listelenir; bunun ilk çalıştırma kanıtı olabilmesi için EvoLink runtime doğrulaması hâlâ gereklidir. |
| Giriş görüntüleri | Resmi materyal, Seedream 5.0 Pro’nun en fazla 10 giriş görüntüsünü desteklediğini belirtir. |
| Çıkış çözünürlüğü | Pro için 4K iddia etmeyin; kaynak materyal `<= 2.36M` piksel ve `> 2.36M` piksel civarında çıkış katmanlarını açıklar. |
| Yerel prompt dilleri | Resmi materyal Arapça, İngilizce, Rusça, Endonezce, İspanyolca, Almanca, Türkçe, Portekizce, Malayca, Vietnamca, Fransızca, Japonca, Korece, Tagalogca ve Taycayı listeler. |
| Seedream’den Seedance’e yol | Resmi materyal, Seedream 5.0 Pro/Lite çıktılarının hesap ve moderasyon koşulları altında Seedance ailesi image-to-video iş akışları için güvenilir girdiler olabileceğini belirtir. |

<a id="acknowledge"></a>

## 🙏 Teşekkür

Bu depo, 8 Temmuz 2026’da dışa aktarılan resmi Seedream 5.0 Pro lansman materyalinden ve case envanteri hakkındaki resmi düzeltmelerden oluşturuldu.

- Resmi özel kaynak URL’leri yalnızca yerel denetim kanıtlarında saklanır.
- Prompt blokları yalnızca resmi materyalin prompt metni sağladığı yerlerde eklenir.
- Yalnızca medya içeren case’ler yalnızca medya olarak kalır; eksik promptlar uydurulmaz.

*Herhangi bir public case sınırının düzeltilmesi gerekiyorsa, somut kaynak kanıtıyla bir issue açın veya patch gönderin.*
