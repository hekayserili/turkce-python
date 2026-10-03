# tpy.py - TPY Çalıştırıcı
import sys
from tpy.motor import calistir, canli_kod_modu
from tpy import __version__

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Parametre verilmezse CANLI KOD MODU açılır
        canli_kod_modu()
    elif sys.argv[1] in ["--surum", "-v", "--version"]:
        print(f"TPY Sürümü: v{__version__}")
    else:
        calistir(sys.argv[1])