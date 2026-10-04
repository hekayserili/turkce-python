# tpy/__main__.py
import sys
from . import motor, __version__

def main():
    args = sys.argv[1:]
    
    if not args:
        # Parametre verilmediyse canlı terminali aç
        motor.canli_kod_modu()
    elif args[0] in ["-v", "--version", "sürüm"]:
        print(f"TPY Sürümü: {__version__}")
    elif args[0] in ["-h", "--help", "yardım"]:
        print("Kullanım:")
        print("  python -m tpy              Canlı etkileşimli terminali açar.")
        print("  python -m tpy <dosya.tpy>  Belirtilen Türkçe Python dosyasını çalıştırır.")
    else:
        # Verilen .tpy dosyasını çalıştır
        dosya_yolu = args[0]
        motor.calistir(dosya_yolu)

if __name__ == "__main__":
    main()