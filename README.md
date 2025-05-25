#  Uçuş Güvenlik ve Onay Değerlendirme Sistemi (Fuzzy Logic)

Bu proje, uçuş öncesi çeşitli operasyonel ve çevresel verileri kullanarak uçuşun güvenli olup olmadığını değerlendiren ve uçuş için onay durumu veren bir **bulanık mantık (fuzzy logic)** kontrol sistemidir. Sistem, kullanıcıdan alınan beş farklı girdiye göre iki farklı çıktı üretir: **Güvenlik Skoru** ve **Uçuş Onay Durumu**.

---

##  Amaç

Uçuş öncesinde belirsizlik içeren çevresel ve operasyonel verileri değerlendirerek, güvenlik skoru ve onay durumu tahmini yapmak.

---

##  Kullanılan Teknolojiler

- Python 3
- PyQt5 (Grafiksel Arayüz)
- Scikit-Fuzzy (Bulanık Mantık Motoru)
- Matplotlib (Sonuçların Görselleştirilmesi)

---

##  Uygulama Özellikleri

-  Kullanıcı dostu arayüz (PyQt5 ile geliştirilmiştir)
-  Girdiler değiştirildikçe tekrar tekrar hesaplama yapılabilir
-  Çıktılar grafiksel olarak görselleştirilebilir (bar grafik)
-  5 adet giriş parametresi ve 2 adet bağımsız çıktı üretimi

---

##  Girdi/Çıktı Parametre Tablosu

| Tür     | Parametre Adı           | Açıklama                                 | Değer Aralığı |
|---------|--------------------------|-------------------------------------------|---------------|
| Girdi   | Hava Durumu Şiddeti      | Uçuş sırasındaki potansiyel hava riski   | 0 – 100       |
| Girdi   | Rüzgar Hızı              | Anlık rüzgar kuvveti                     | 0 – 100       |
| Girdi   | Yolcu Yoğunluğu          | Kabin içi doluluk oranı                  | 0 – 100       |
| Girdi   | Ekip Yorgunluğu          | Uçuş ekibinin yorgunluk seviyesi         | 0 – 100       |
| Girdi   | Uçak Ağırlığı            | Yük ve yolcu dengesine bağlı ağırlık     | 0 – 100       |
| Çıktı   | Güvenlik Skoru           | Genel güvenlik değerlendirmesi (fuzzy)   | 0 – 100       |
| Çıktı   | Uçuş Onay Durumu         | Uçuşun devam edip etmeyeceği kararı      | 0 – 100       |

---

##  Kurulum

Proje klasörünü klonladıktan sonra, aşağıdaki adımları izleyin:

```bash
git clone https://github.com/kullaniciadi/ucus-fuzzy.git
cd ucus-fuzzy
pip install -r requirements.txt
python gui_main.py
