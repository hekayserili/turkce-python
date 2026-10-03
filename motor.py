# tpy/motor.py - TPY v0.3.0 Çekirdek Motoru
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
    girdi_stream = io.StringIO(kod_metni)
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

def calistir(dosya_yolu):
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            turkce_kod = f.read()

        python_kodu = tpy_cozumle(turkce_kod)
        exec(python_kodu, {"__name__": "__main__"})

    except FileNotFoundError:
        print(f"Hata: '{dosya_yolu}' dosyası bulunamadı.")
    except Exception as e:
        hata_bas(e)

def canli_kod_modu():
    print(f"Türkçe Python (TPY) Sürüm {__version__} [LİG SÜRÜMÜ]")
    print("Çıkmak için 'çıkış()' veya 'çık' yazabilirsiniz.\n")

    yerel_hafiza = {"__name__": "__main__"}
    coklu_satir_blok = []

    while True:
        try:
            prompt = "... " if coklu_satir_blok else "tpy> "
            girdi = input(prompt)

            if not coklu_satir_blok and girdi.strip() in ["çıkış()", "çık", "exit()", "exit"]:
                break

            if girdi.endswith(":") or (coklu_satir_blok and girdi.strip() != ""):
                coklu_satir_blok.append(girdi)
                continue

            if coklu_satir_blok and girdi.strip() == "":
                tam_kod = "\n".join(coklu_satir_blok)
                coklu_satir_blok = []
            else:
                tam_kod = girdi

            if not tam_kod.strip():
                continue

            python_kodu = tpy_cozumle(tam_kod)

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
    hata_turu = type(e).__name__
    turkce_hata = TPY_HATALAR.get(hata_turu, hata_turu)
    aciklama = str(e)
    for ing, tr in TPY_ACIKLAMALAR.items():
        if ing in aciklama:
            aciklama = aciklama.replace(ing, tr)

    print(f"Hata [{turkce_hata}]: {aciklama}")