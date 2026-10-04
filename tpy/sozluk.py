# tpy/sozluk.py - TPY v0.4.0 Sözlük ve Modül Haritası (Dev Sürüm)

TPY_SOZLUK = {
    # Karar ve Kontrol Yapıları
    "eğer": "if",
    "değilse": "else",
    "yoksa": "elif",
    "ise": "",
    "durumunda": "",
    
    # Döngüler
    "için": "for",
    "sürece": "while",
    "içinde": "in",
    "döngü": "",
    "kır": "break",
    "devam": "continue",
    "pas": "pass",
    
    # Fonksiyon, Sınıf ve Hata Yakalama
    "tanımla": "def",
    "fonksiyon": "def",
    "fonk": "def",
    "döndür": "return",
    "sınıf": "class",
    "dene": "try",
    "yakala": "except",
    "sonunda": "finally",
    "yükselt": "raise",
    "doğrula": "assert",
    
    # Mantıksal, Bağlaçlar ve Varlık Kontrolleri
    "ve": "and",
    "veya": "or",
    "değil": "not",
    "Doğru": "True",
    "Yanlış": "False",
    "Boş": "None",
    "eşittir": "==",
    "farklıdır": "!=",
    "aynı": "is",
    
    # Modulate ve Kapsam İşlemleri
    "içe_aktar": "import",
    "olarak": "as",
    "küresel": "global",
    "yerel_değil": "nonlocal",
    "sil": "del",

    # Gömülü Fonksiyonlar - Giriş / Çıkış ve Dosya
    "yazdır": "print",
    "giriş": "input",
    "oku": "input",
    "dosya_aç": "open",
    
    # Gömülü Fonksiyonlar - Veri Tipleri ve Dönüştürücüler
    "tam_sayı": "int",
    "metin": "str",
    "ondalık": "float",
    "mantıksal": "bool",
    "liste": "list",
    "sözlük": "dict",
    "küme": "set",
    "demet": "tuple",
    "dondurulmuş_küme": "frozenset",
    "karmaşık": "complex",
    "bayt": "bytes",
    "bayt_dizisi": "bytearray",
    
    # Gömülü Fonksiyonlar - Matematiksel ve Dizi İşlemleri
    "uzunluk": "len",
    "toplam": "sum",
    "en_büyük": "max",
    "en_küçük": "min",
    "aralık": "range",
    "tür": "type",
    "sırala": "sorted",
    "mutlak": "abs",
    "yuvarla": "round",
    "üslü": "pow",
    "bölüm_kalan": "divmod",
    "ters_çevir": "reversed",
    "numaralandır": "enumerate",
    "birleştir": "zip",
    "filtrele": "filter",
    "harita": "map",
    
    # Gömülü Fonksiyonlar - Denetim ve Sistem Metotları
    "hepsi": "all",
    "herhangi_biri": "any",
    "çağrılabilir": "callable",
    "özellik_var_mı": "hasattr",
    "özellik_al": "getattr",
    "özellik_ata": "setattr",
    "özellik_sil": "delattr",
    "kimlik": "id",
    "örneği_mi": "isinstance",
    "alt_sınıfı_mı": "issubclass",
    "dizin": "dir",
    "yardım": "help"
}

GORUNMEZ_KELIMELER = {"ise", "durumunda", "döngü"}

# Modül ve Metot Dönüşüm Haritası (Kütüphaneler için)
MODUL_HARITASI = {
    "matematik": "math",
    "rastgele": "random",
    "zaman": "time",
    "dosya_sistemi": "os",
    "sistem": "sys"
}

METOT_HARITASI = {
    # matematik
    "karekök": "sqrt",
    "üs": "pow",
    "mutlak": "fabs",
    "taban": "floor",
    "tavan": "ceil",
    "faktöriyel": "factorial",
    "ebob": "gcd",
    "ekok": "lcm",
    "pi": "pi",
    "e_sayısı": "e",
    
    # rastgele
    "rastgele_sayı": "randint",
    "seç": "choice",
    "karıştır": "shuffle",
    "rastgele": "random",
    "örneklem": "sample",
    
    # zaman
    "bekle": "sleep",
    "zaman": "time",
    "yerel_zaman": "ctime",
    
    # dosya_sistemi (os)
    "mevcut_dizin": "getcwd",
    "dizin_listele": "listdir",
    "klasör_oluştur": "mkdir",
    "klasör_sil": "rmdir",
    "dosya_sil": "remove",
    "değiştir": "rename",
    
    # sistem (sys)
    "çıkış": "exit",
    "argümanlar": "argv",
    "platform": "platform"
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
    "IndentationError": "GirintiHatası",
    "AttributeError": "ÖzellikHatası",
    "ImportError": "İçeAktarmaHatası",
    "ModuleNotFoundError": "ModülBulunamadıHatası",
    "KeyboardInterrupt": "KullanıcıİptaliHatası",
    "PermissionError": "ErişimİzniHatası"
}

TPY_ACIKLAMALAR = {
    "is not defined": "tanımlanmamış",
    "division by zero": "bir sayı sıfıra bölünemez",
    "list index out of range": "liste indeks sınırları aşıldı",
    "invalid syntax": "geçersiz sözdizimi",
    "unexpected indent": "beklenmeyen girinti",
    "unindent does not match any outer indentation level": "girinti seviyesi eşleşmiyor",
    "file not found": "belirtilen dosya bulunamadı",
    "permission denied": "dosya erişim izni reddedildi"
}