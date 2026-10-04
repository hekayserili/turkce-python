# tpy/motor.py - TPY v0.4.0 Çekirdek Motoru
import sys
import tokenize
import io
import traceback
from .sozluk import (
    TPY_SOZLUK, GORUNMEZ_KELIMELER, MODUL_HARITASI, 
    METOT_HARITASI, TPY_HATALAR, TPY_ACIKLAMALAR
)
from . import __version__

def tpy_cozumle(kod_metni):
    """
    Türkçe TPY token'larını okur ve standart Python AST/Kod yapısına dönüştürür.
    """
    girdi_stream = io.StringIO(kod_metni)
    
    try:
        tokens = tokenize.generate_tokens(girdi_stream.readline)
        yeni_tokens = []

        for toknum, tokval, start, end, line in tokens:
            if toknum == tokenize.NAME:
                if tokval in GORUNMEZ_KELIMELER:
                    continue
                elif tokval in TPY_SOZLUK:
                    yeni_tokens.append((toknum, TPY_SOZLUK[tokval]))
                elif tokval in MODUL_HARITASI:
                    yeni_tokens.append((toknum, MODUL_HARITASI[tokval]))
                elif tokval in METOT_HARITASI:
                    yeni_tokens.append((toknum, METOT_HARITASI[tokval]))
                else:
                    yeni_tokens.append((toknum, tokval))
            else:
                yeni_tokens.append((toknum, tokval))

        return tokenize.untokenize(yeni_tokens)
    except tokenize.TokenError as e:
        # Kapatılmamış tırnak veya parantez hatalarını düzgün yakalamak için
        raise SyntaxError("Sözdizimi tamamlanmadı (kapatılmamış tırnak veya parantez var).")

def calistir(dosya_yolu):
    """
    .tpy uzantılı Türkçe Python kod dosyasını okur ve çalıştırır.
    """
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            turkce_kod = f.read()

        python_kodu = tpy_cozumle(turkce_kod)
        
        # Çalıştırma kapsamına __file__ ve __name__ bilgilerini doğru aktaralım
        kapsam = {
            "__name__": "__main__",
            "__file__": dosya_yolu
        }
        exec(python_kodu, kapsam)

    except FileNotFoundError:
        print(f"Hata [DosyaBulunamadıHatası]: '{dosya_yolu}' dosyası bulunamadı.")
    except Exception as e:
        hata_bas(e)

def canli_kod_modu():
    """
    İnteraktif REPL (Canlı Terminal) Modu
    """
    print(f"Türkçe Python (TPY) Sürüm {__version__} [v0.4.0]")
    print("Çıkmak için 'çıkış()', 'çık' veya 'kapat' yazabilirsiniz.\n")

    yerel_hafiza = {"__name__": "__main__"}
    coklu_satir_blok = []

    while True:
        try:
            prompt = "... " if coklu_satir_blok else "tpy> "
            girdi = input(prompt)

            # Çıkış komutları denetimi
            if not coklu_satir_blok and girdi.strip() in ["çıkış()", "çık", "kapat", "exit()", "exit"]:
                print("TPY oturumu sonlandırıldı.")
                break

            # Blok başlama denetimi (eğer:, için:, tanımla: vb.)
            if girdi.endswith(":") or (coklu_satir_blok and girdi.strip() != ""):
                coklu_satir_blok.append(girdi)
                continue

            # Blok bitirme (boş satır girildiğinde bloğu çalıştır)
            if coklu_satir_blok and girdi.strip() == "":
                tam_kod = "\n".join(coklu_satir_blok)
                coklu_satir_blok = []
            else:
                tam_kod = girdi

            if not tam_kod.strip():
                continue

            python_kodu = tpy_cozumle(tam_kod)

            # Önce tek satırlık ifade (expression) olarak eval et, olmuyorsa exec çalıştır
            try:
                sonuc = eval(python_kodu, yerel_hafiza)
                if sonuc is not None:
                    print(sonuc)
            except SyntaxError:
                exec(python_kodu, yerel_hafiza)

        except KeyboardInterrupt:
            print("\nOturum kapatıldı.")
            break
        except Exception as e:
            coklu_satir_blok = []
            hata_bas(e)

def hata_bas(e):
    """
    Python hatalarını TPY_HATALAR ve TPY_ACIKLAMALAR haritalarını kullanarak Türkçeleştirir.
    """
    hata_turu = type(e).__name__
    turkce_hata = TPY_HATALAR.get(hata_turu, hata_turu)
    aciklama = str(e)

    # Açıklamalardaki İngilizce kalıpları Türkçeleriyle değiştir
    for ing, tr in TPY_ACIKLAMALAR.items():
        if ing in aciklama:
            aciklama = aciklama.replace(ing, tr)

    print(f"Hata [{turkce_hata}]: {aciklama}")