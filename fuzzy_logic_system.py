import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# === Girdiler ===
hava = ctrl.Antecedent(np.arange(0, 101, 1), 'hava')
ruzgar = ctrl.Antecedent(np.arange(0, 101, 1), 'ruzgar')
yogunluk = ctrl.Antecedent(np.arange(0, 101, 1), 'yogunluk')
yorgunluk = ctrl.Antecedent(np.arange(0, 101, 1), 'yorgunluk')
agirlik = ctrl.Antecedent(np.arange(0, 101, 1), 'agirlik')

# === Çıktılar ===
guvenlik = ctrl.Consequent(np.arange(0, 101, 1), 'guvenlik')
onay = ctrl.Consequent(np.arange(0, 101, 1), 'onay')

# === Üyelik fonksiyonları ===

for girdi in [hava, ruzgar, yogunluk, yorgunluk, agirlik]:
    girdi['dusuk'] = fuzz.trimf(girdi.universe, [0, 0, 50])
    girdi['orta'] = fuzz.trimf(girdi.universe, [25, 50, 75])
    girdi['yuksek'] = fuzz.trimf(girdi.universe, [50, 100, 100])

guvenlik['kotu'] = fuzz.trimf(guvenlik.universe, [0, 0, 50])
guvenlik['orta'] = fuzz.trimf(guvenlik.universe, [25, 50, 75])
guvenlik['iyi'] = fuzz.trimf(guvenlik.universe, [50, 100, 100])

onay['iptal'] = fuzz.trimf(onay.universe, [0, 0, 50])
onay['bekle'] = fuzz.trimf(onay.universe, [25, 50, 75])
onay['devam'] = fuzz.trimf(onay.universe, [50, 100, 100])

# === Kurallar ===

kurallar = [
    ctrl.Rule(hava['dusuk'] & ruzgar['dusuk'] & yorgunluk['dusuk'] & yogunluk['dusuk'] & agirlik['dusuk'], guvenlik['iyi']),
    ctrl.Rule(hava['orta'] | ruzgar['orta'] | yorgunluk['orta'] | yogunluk['orta'], guvenlik['orta']),
    ctrl.Rule(hava['yuksek'] | ruzgar['yuksek'] | yorgunluk['yuksek'] | yogunluk['yuksek'] | agirlik['yuksek'], guvenlik['kotu']),

    ctrl.Rule(guvenlik['iyi'], onay['devam']),
    ctrl.Rule(guvenlik['orta'], onay['bekle']),
    ctrl.Rule(guvenlik['kotu'], onay['iptal']),
]

# === Kontrol sistemi tanımlama ===
guvenlik_sistemi = ctrl.ControlSystem(kurallar)
guvenlik_simulasyon = ctrl.ControlSystemSimulation(guvenlik_sistemi)

# === Değerlendirme fonksiyonu ===
def evaluate(h, r, y, yk, a):
    guvenlik_simulasyon.input['hava'] = h
    guvenlik_simulasyon.input['ruzgar'] = r
    guvenlik_simulasyon.input['yogunluk'] = y
    guvenlik_simulasyon.input['yorgunluk'] = yk
    guvenlik_simulasyon.input['agirlik'] = a

    try:
        guvenlik_simulasyon.compute()
        return guvenlik_simulasyon.output['guvenlik'], guvenlik_simulasyon.output['onay']
    except Exception as e:
        print("[HATA]:", e)
        return 0, 0

# === Terminal test fonksiyonu ===
if __name__ == "__main__":
    g, o = evaluate(30, 25, 60, 40, 50)
    print(f"Güvenlik Skoru: {g:.2f}")
    print(f"Uçuş Onay Durumu: {o:.2f}")
