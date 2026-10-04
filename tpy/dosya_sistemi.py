# tpy/dosya_sistemi.py - TPY v0.4.0 Dosya Sistemi Modülü
import os
import shutil

def mevcut_dizin():
    """Çalışılan mevcut dizin yolunu döndürür."""
    return os.getcwd()

def dizin_listele(yol="."):
    """Belirtilen dizindeki dosya ve klasörleri liste olarak döndürür."""
    try:
        return os.listdir(yol)
    except FileNotFoundError:
        print(f"Hata [DosyaBulunamadıHatası]: '{yol}' dizini bulunamadı.")
    except PermissionError:
        print(f"Hata [ErişimİzniHatası]: '{yol}' dizinine erişim izni yok.")

def klasör_oluştur(ad):
    """Yeni bir klasör oluşturur."""
    try:
        os.mkdir(ad)
    except FileExistsError:
        print(f"Hata [Hata]: '{ad}' adında bir klasör zaten var.")
    except Exception as e:
        print(f"Hata [KlasörOluşturmaHatası]: {e}")

def klasör_sil(ad, zorla=False):
    """
    Belirtilen klasörü siler. 
    Eğer zorla=True yapılırsa içi dolu klasörleri de siler (shutil kullanır).
    """
    try:
        if zorla:
            shutil.rmtree(ad)
        else:
            os.rmdir(ad)
    except FileNotFoundError:
        print(f"Hata [DosyaBulunamadıHatası]: '{ad}' klasörü bulunamadı.")
    except OSError:
        print(f"Hata [KlasörDoluHatası]: '{ad}' klasörü boş değil. Silmek için 'zorla=Doğru' parametresini kullanın.")

def dosya_sil(yol):
    """Belirtilen dosyayı siler."""
    try:
        os.remove(yol)
    except FileNotFoundError:
        print(f"Hata [DosyaBulunamadıHatası]: '{yol}' dosyası bulunamadı.")
    except IsADirectoryError:
        print(f"Hata [TipHatası]: '{yol}' bir dosya değil, klasör. Klasör silmek için 'klasör_sil()' kullanın.")

def değiştir(eski_ad, yeni_ad):
    """Dosya veya klasör adını/yolunu değiştirir."""
    try:
        os.rename(eski_ad, yeni_ad)
    except FileNotFoundError:
        print(f"Hata [DosyaBulunamadıHatası]: '{eski_ad}' bulunamadı.")

def var_mı(yol):
    """Dosya veya klasörün var olup olmadığını kontrol eder (Doğru/Yanlış)."""
    return os.path.exists(yol)

def dosya_mı(yol):
    """Verilen yolun bir dosya olup olmadığını kontrol eder."""
    return os.path.isfile(yol)

def klasör_mü(yol):
    """Verilen yolun bir klasör olup olmadığını kontrol eder."""
    return os.path.isdir(yol)

def yol_birleştir(*yollar):
    """İşletim sistemine uygun şekilde dosya yollarını birleştirir."""
    return os.path.join(*yollar)