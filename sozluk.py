# tpy/sozluk.py - TPY v0.3.0 Sözlük ve Modül Haritası

TPY_SOZLUK = {
    # Karar ve Kontrol Yapıları
    "eğer": "if",
    "değilse": "else",
    "yoksa": "elif",
    "ise": "",
    
    # Döngüler
    "için": "for",
    "sürece": "while",
    "içinde": "in",
    "döngü": "",
    "kır": "break",
    "devam": "continue",
    
    # Fonksiyon ve Sınıf
    "tanımla": "def",
    "döndür": "return",
    "sınıf": "class",
    
    # Mantıksal ve Bağlaçlar
    "ve": "and",
    "veya": "or",
    "değil": "not",
    "doğru": "True",
    "yanlış": "False",
    "boş": "None",
    
    # Modül İşlemleri
    "içe_aktar": "import",
    "olarak": "as",

    # Gömülü Fonksiyonlar
    "yazdır": "print",
    "giriş": "input",
    "oku": "input",
    "uzunluk": "len",
    "toplam": "sum",
    "en_büyük": "max",
    "en_küçük": "min",
    "aralık": "range",
    "tür": "type",
    "sırala": "sorted",
    "mutlak": "abs",
    "tam_sayı": "int",
    "metin": "str",
    "ondalık": "float",
    "liste": "list",
    "sözlük": "dict",
    "küme": "set",
    "demet": "tuple"
}

GORUNMEZ_KELIMELER = {"ise", "durumunda", "döngü"}

# Modül ve Metot Dönüşüm Haritası (Kütüphaneler için)
MODUL_HARITASI = {
    "matematik": "math",
    "rastgele": "random",
    "zaman": "time"
}

METOT_HARITASI = {
    # matematik
    "karekök": "sqrt",
    "üs": "pow",
    "mutlak": "fabs",
    "taban": "floor",
    "tavan": "ceil",
    "pi": "pi",
    # rastgele
    "rastgele_sayı": "randint",  # 'tam_sayı' yerine 'rastgele_sayı' kullandık
    "seç": "choice",
    "karıştır": "shuffle",
    "rastgele": "random",
    # zaman
    "bekle": "sleep",
    "zaman": "time"
}

TPY_HATALAR = {
    "SyntaxError": "SözdizimiHatası",
    "NameError": "TanımsızİsimHatası",
    "TypeError": "TipHatası",
    "ValueError": "DeğerHatası",
    "ZeroDivisionError": "SıfıraBölmeHatası",
    "IndexError": "IndeksHatası",
    "KeyError": "AnahtarHatası",
    "FileNotFoundError": "DosyaBulunamadıHatası",
    "IndentationError": "GirintiHatası"
}

TPY_ACIKLAMALAR = {
    "is not defined": "tanımlanmamış",
    "division by zero": "bir sayı sıfıra bölünemez",
    "list index out of range": "liste indeks sınırları aşıldı",
    "invalid syntax": "geçersiz sözdizimi"
}