import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QSpinBox, QLabel, QPushButton,
    QMessageBox, QVBoxLayout, QHBoxLayout, QGroupBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from fuzzy_logic_system import evaluate


class FlightApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✈️ Uçuş Güvenlik Değerlendirme Sistemi")
        self.setGeometry(200, 200, 500, 400)
        self.setStyleSheet("background-color: #f0f4f7;")
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()

        # === Başlık ===
        title = QLabel("Uçuş Öncesi Risk ve Onay Değerlendirmesi")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(title)

        # === Giriş Formları ===
        formBox = QGroupBox("Girdi Değerleri")
        formLayout = QFormLayout()

        self.inputs = {}
        input_labels = [
            'Hava Durumu Şiddeti',
            'Rüzgar Hızı',
            'Yolcu Yoğunluğu',
            'Ekip Yorgunluğu',
            'Uçak Ağırlığı'
        ]

        for label in input_labels:
            spin = QSpinBox()
            spin.setRange(0, 100)
            spin.setStyleSheet("background-color: white;")
            formLayout.addRow(label, spin)
            self.inputs[label] = spin

        formBox.setLayout(formLayout)
        mainLayout.addWidget(formBox)

        # === Sonuç Etiketi ===
        self.resultLabel = QLabel("🔍 Sonuç: Henüz hesaplama yapılmadı.")
        self.resultLabel.setFont(QFont("Arial", 11))
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setStyleSheet("padding: 8px; color: #333333; background-color: #e6f0fa; border: 1px solid #cccccc;")
        mainLayout.addWidget(self.resultLabel)

        # === Butonlar ===
        buttonLayout = QHBoxLayout()

        hesaplaBtn = QPushButton("Hesapla")
        hesaplaBtn.clicked.connect(self.calculate)
        hesaplaBtn.setStyleSheet("background-color: #2e86de; color: white; padding: 8px;")
        buttonLayout.addWidget(hesaplaBtn)

        gosterBtn = QPushButton("Sonuçları Görselleştir")
        gosterBtn.clicked.connect(self.plot_results)
        gosterBtn.setStyleSheet("background-color: #28b463; color: white; padding: 8px;")
        buttonLayout.addWidget(gosterBtn)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

    def calculate(self):
        try:
            values = [spin.value() for spin in self.inputs.values()]
            self.g, self.o = evaluate(*values)
            self.resultLabel.setText(
                f"✅ Güvenlik Skoru: {self.g:.2f} | Uçuş Onay Durumu: {self.o:.2f}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Hesaplama Hatası", str(e))

    def plot_results(self):
        try:
            if hasattr(self, 'g') and hasattr(self, 'o'):
                labels = ['Güvenlik Skoru', 'Uçuş Onay Durumu']
                values = [self.g, self.o]
                plt.figure(figsize=(5, 4))
                plt.bar(labels, values, color=['#3498db', '#27ae60'])
                plt.ylim(0, 100)
                plt.title("Değerlendirme Sonuçları")
                plt.ylabel("Skor (0-100)")
                plt.grid(axis='y')
                plt.tight_layout()
                plt.show()
            else:
                QMessageBox.warning(self, "Uyarı", "Lütfen önce 'Hesapla' butonuna basın.")
        except Exception as e:
            QMessageBox.critical(self, "Görselleştirme Hatası", str(e))


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = FlightApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("Bir hata oluştu:", e)
        input("Devam etmek için Enter'a bas...")
