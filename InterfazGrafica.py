import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QGridLayout

class Inicio(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QGridLayout()  # Usar QGridLayout para organizar el título y los botones
        
        self.setWindowTitle("Interfaz Hombre-Máquina")
        
        font = QFont("Arial", 20)
        font.setBold(True)
        
        titulo_label = QLabel("ESTACIÓN SOLAR FOTOVOLTAICA")
        titulo_label.setFont(font)  # Establecer la fuente
        layout.addWidget(titulo_label, 7, 7, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)  # Centrar el título

        button_width = 400
        button_height = 45

        panel_button = QPushButton("PANEL SOLAR")
        panel_button.setFixedSize(button_width, button_height)

        bateria_button = QPushButton("BATERÍA")
        bateria_button.setFixedSize(button_width, button_height)

        inversor_button = QPushButton("SALIDA DEL INVERSOR")
        inversor_button.setFixedSize(button_width, button_height)

        diagrama_button = QPushButton("DIAGRAMA ESQUEMÁTICO")
        diagrama_button.setFixedSize(button_width, button_height)

        # Cambiar el color de los botones a verde
        button_style = "background-color: green; color: white; font-size: 16px;"
        panel_button.setStyleSheet(button_style)
        bateria_button.setStyleSheet(button_style)
        inversor_button.setStyleSheet(button_style)
        diagrama_button.setStyleSheet(button_style)

        # Agregar botones al diseño y moverlos un poco a la derecha
        layout.addWidget(panel_button, 10, 6, 2, 2)
        layout.addWidget(bateria_button, 11, 6, 3, 2)
        layout.addWidget(inversor_button, 12, 6, 4, 2)
        layout.addWidget(diagrama_button, 13, 6, 5, 2)
        self.setLayout(layout)
        escudo_label = QLabel()
        cargar_escudo = QPixmap("ESCUDO.png")
        cargar_escudo = cargar_escudo.scaledToWidth(cargar_escudo.width() // 2)
        escudo_label.setPixmap(cargar_escudo)
        layout.addWidget(escudo_label, 16, 5, 7, 5, alignment=Qt.AlignmentFlag.AlignRight)  # Mover el escudo a la derecha
     
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    inicio_widget = Inicio()
    ventana.setCentralWidget(inicio_widget)
    ventana.show()
    sys.exit(app.exec())


'''
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QGridLayout, QGroupBox


class Inicio(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.setWindowTitle("Interfaz Hombre-Máquina")
        
        font = QFont("Arial", 20)
        font.setBold(True)
        
        titulo_label = QLabel("ESTACIÓN SOLAR FOTOVOLTAICA")
        titulo_label.setFont(font)  # Establecer la fuente
        layout.addWidget(titulo_label)
        layout.addStretch(1)  # Agregar espacio elástico para empujar el escudo hacia arriba
        button_width = 320
        button_height = 34

        panel_button = QPushButton("PANEL SOLAR")
        panel_button.setFixedSize(button_width, button_height)

        bateria_button = QPushButton("BATERÍA")
        bateria_button.setFixedSize(button_width, button_height)

        inversor_button = QPushButton("SALIDA DEL INVERSOR")
        inversor_button.setFixedSize(button_width, button_height)

        diagrama_button = QPushButton("DIAGRAMA ESQUEMÁTICO")
        diagrama_button.setFixedSize(button_width, button_height)

        # Cambiar el color de los botones a verde
        button_style = "background-color: green; color: white; font-size: 16px;"
        panel_button.setStyleSheet(button_style)
        bateria_button.setStyleSheet(button_style)
        inversor_button.setStyleSheet(button_style)
        diagrama_button.setStyleSheet(button_style)

        # Agregar botones al diseño
        layout.addWidget(panel_button)
        layout.addWidget(bateria_button)
        layout.addWidget(inversor_button)
        layout.addWidget(diagrama_button)

        escudo_label = QLabel()
        cargar_escudo = QPixmap("ESCUDO.png")
        cargar_escudo = cargar_escudo.scaledToWidth(cargar_escudo.width() // 2)
        #cargar_escudo = cargar_escudo.scaledToHeight(cargar_escudo.height() // 2)
        escudo_label.setPixmap(cargar_escudo)
        layout.addWidget(escudo_label, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addStretch(1)  # Agregar espacio elástico para empujar el escudo hacia arriba

        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    inicio_widget = Inicio()
    ventana.setCentralWidget(inicio_widget)
    ventana.show()
    sys.exit(app.exec())

'''