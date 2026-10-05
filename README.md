# 🇹🇷 TPY - Türkçe Python Programlama Çeviricisi & Canlı Terminal

**TPY (v0.4.0)**, Python programlama dilini Türkçe sözdizimi ile yazmanızı ve çalıştırmanızı sağlayan bağımsız bir transpiler ve canlı terminal (REPL) ortamıdır.

---

## ✨ Öne Çıkan Özellikler

* 🚀 **Bağımsız CLI:** Sisteminizde Python kurulu olmasa dahi `.exe` üzerinden doğrudan çalışır.
* 💻 **Canlı Terminal (REPL):** Komut satırında `tpy` yazarak anlık Türkçe kod çalıştırma ve çok satırlı blok desteği.
* 📦 **Türkçe Standart Kütüphaneler:** `matematik`, `rastgele` ve `zaman` modüllerine tam Türkçe erişim.
* 🔍 **Türkçe Hata Ayıklayıcı:** Karşılaşılan hataların Türkçe açıklamaları.

```python
içe_aktar matematik
içe_aktar rastgele

yazdır("Karekök Hesabı:", matematik.karekök(16))
yazdır("Rastgele Sayı:", rastgele.rastgele_sayı(1, 100))

için i içinde aralık(5):
    eğer i % 2 == 0 ise:
        yazdır(f"{i} çift sayıdır")
    değilse:
        yazdır(f"{i} tek sayıdır")
