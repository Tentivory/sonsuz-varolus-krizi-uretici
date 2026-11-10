#!/usr/bin/env python3
# Sonsuz Varoluş Krizi Üretici
# Bu kod gerçekten çalışır ve gerçekten saçmadır.

import random
import time

krizler = [
    "Ya eğer düşündüğüm şey aslında düşünmüyorsam?",
    "Var olmak zorunda mıyım yoksa var olmak zorunda olan şey miyim?",
    "Eğer hiçbir şey anlamsızsa, anlamsızlığın anlamı nedir?",
    "Kahve içmeden önce var mıydım yoksa kahve mi beni var etti?",
    "Bu cümleyi okurken aslında bu cümleyi yazan kişiyi mi okuyorsun?",
    "Zaman gerçekten geçiyor mu yoksa biz mi zamanın içinde duruyoruz?",
    "Eğer her şey bir rüyaysa, rüyayı gören kim?",
    "Neden buradayım? Neden sen oradasın? Neden bu soru var?"
]

def uret_kriz():
    print("\n" + "="*50)
    print("YENİ BİR VAROLUŞSAL KRİZ ÜRETİLDİ:")
    print(random.choice(krizler))
    print("="*50 + "\n")
    print("Lütfen 3 saniye düşün...")
    time.sleep(3)

if __name__ == "__main__":
    print("Sonsuz Varoluş Krizi Üretici başlatıldı. Durdurmak için Ctrl+C")
    try:
        while True:
            uret_kriz()
    except KeyboardInterrupt:
        print("\nKriz üretimi durduruldu. Ama krizler durmaz...")

# gizli_mesaj = 'ZGVtb2tyYXNpIGVuIGl5aSBzaXN0ZW1kaXIgYW1hIGVuIGtvdMO8c8O8ZMO8cg=='  # base64 of something mild
