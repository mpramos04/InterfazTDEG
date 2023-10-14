import sys
import random
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QGridLayout

class Inicio(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected_button = None  # Para rastrear el botón seleccionado

    def initUI(self):
        layout = QGridLayout()
        
        self.setWindowTitle("Interfaz Hombre-Máquina")
        self.setGeometry(200, 100, 1250, 650)  # Establecer tamaño fijo de la ventana
        
        font = QFont("Arial", 30)
        font.setBold(True)
        
        titulo_label = QLabel("ESTACIÓN SOLAR FOTOVOLTAICA")
        titulo_label.setFont(font)
        layout.addWidget(titulo_label, 0, 1, 1, 5, alignment=Qt.AlignmentFlag.AlignCenter)

        button_width = 400
        button_height = 100

        self.panel_button = QPushButton("PANEL SOLAR\nV: ## A: ##")
        self.panel_button.setFixedSize(button_width, button_height)
        button_font = QFont("Arial", 12)
        button_font.setBold(True)
        self.panel_button.setFont(button_font)
        self.panel_button.setStyleSheet("background-color: green;")

        self.bateria_button = QPushButton("BATERÍA\nV: ## A: ##")
        self.bateria_button.setFixedSize(button_width, button_height)
        self.bateria_button.setFont(button_font)
        self.bateria_button.setStyleSheet("background-color: green;")

        self.inversor_button = QPushButton("SALIDA DEL INVERSOR\nV: ## A: ##")
        self.inversor_button.setFixedSize(button_width, button_height)
        self.inversor_button.setFont(button_font)
        self.inversor_button.setStyleSheet("background-color: green;")

        diagrama_button = QPushButton("DIAGRAMA ESQUEMÁTICO")
        diagrama_button.setFixedSize(button_width, button_height)
        diagrama_button.setFont(button_font)
        diagrama_button.setStyleSheet("background-color: green;")

        layout.addWidget(self.panel_button, 2, 0, 1, 1)
        layout.addWidget(self.bateria_button, 3, 0, 1, 1)
        layout.addWidget(self.inversor_button, 4, 0, 1, 1)
        layout.addWidget(diagrama_button, 5, 0, 1, 1)

        self.setLayout(layout)
        
        self.energia_values = {
            "PANEL SOLAR": (0, 0),
            "BATERÍA": (0, 0),
            "SALIDA DEL INVERSOR": (0, 0)
        }

        self.plot_label = QLabel()
        layout.addWidget(self.plot_label, 2, 3, 4, 2)

        int_frame_width = 200
        int_frame_height = 50
        self.int_frame = QLabel()
        self.int_frame.setStyleSheet("background-color: yellow;")
        self.int_frame.setFixedSize(int_frame_width, int_frame_height)
        layout.addWidget(self.int_frame, 3, 6, 1, 1)
        self.int_label = QLabel("INT: ##")
        self.int_label.setFont(button_font)
        layout.addWidget(self.int_label, 3, 6, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        
        out_frame_width = 200
        out_frame_height = 50
        self.out_frame = QLabel()
        self.out_frame.setStyleSheet("background-color: yellow;")
        self.out_frame.setFixedSize(out_frame_width, out_frame_height)
        layout.addWidget(self.out_frame, 4, 6, 1, 1)
        self.out_label = QLabel("OUT: ##")
        self.out_label.setFont(button_font)
        layout.addWidget(self.out_label, 4, 6, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        
        escudo_label = QLabel()
        cargar_escudo = QPixmap("ESCUDO.png")
        cargar_escudo = cargar_escudo.scaledToWidth(cargar_escudo.width() // 2)
        escudo_label.setPixmap(cargar_escudo)
        layout.addWidget(escudo_label, 6, 5, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        self.panel_button.clicked.connect(lambda: self.show_values("PANEL SOLAR"))
        self.bateria_button.clicked.connect(lambda: self.show_values("BATERÍA"))
        self.inversor_button.clicked.connect(lambda: self.show_values("SALIDA DEL INVERSOR"))
        diagrama_button.clicked.connect(self.show_diagrama)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_energy)
        self.timer.start(1000)  # Actualiza la energía cada segundo

    def show_values(self, key):
        self.selected_button = key
        voltaje, corriente = self.energia_values[key]
        self.int_label.setText(f"INT: {voltaje}V")
        self.out_label.setText(f"OUT: {corriente}A")
        self.int_frame.setStyleSheet("background-color: yellow;")
        self.out_frame.setStyleSheet("background-color: yellow")
        if key == "PANEL SOLAR":
            self.panel_button.setText(f"PANEL SOLAR\n ( {voltaje} )V \n ( {corriente} )A")
        elif key == "BATERÍA":
            self.bateria_button.setText(f"BATERÍA\n ( {voltaje} )V \n ( {corriente} )A")
        elif key == "SALIDA DEL INVERSOR":
            self.inversor_button.setText(f"SALIDA DEL INVERSOR\n ( {voltaje} )V \n ( {corriente} )A")
        self.plot_graph(voltaje, corriente, key)  # Pasa el nombre del componente

    def show_diagrama(self):
        if self.selected_button:
            self.plot_label.clear()
            diagrama_label = QLabel()
            diagrama = QPixmap("diagrama.png")
            diagrama_label.setPixmap(diagrama)
            self.plot_label.addWidget(diagrama_label)

    def update_energy(self):
        for key in self.energia_values:
            voltaje = random.randint(0, 100)
            corriente = random.randint(0, 50)
            self.energia_values[key] = (voltaje, corriente)
        if self.selected_button:
            self.show_values(self.selected_button)
            if self.selected_button == "DIAGRAMA ESQUEMÁTICO":
                self.show_diagrama()

    def plot_graph(self, voltaje, corriente, componente):
        plt.figure(figsize=(5, 4))
        plt.plot(range(10), [random.randint(0, voltaje) for _ in range(10)], label='Voltaje (V)')
        plt.plot(range(10), [random.randint(0, corriente) for _ in range(10)], label='Corriente (A)')
        plt.xlabel('Tiempo')
        plt.ylabel('Magnitud')
        plt.title(f'{componente}')
        plt.legend()
        plt.savefig("graph.png")
        image = QPixmap("graph.png")
        self.plot_label.setPixmap(image)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    inicio_widget = Inicio()
    ventana.setCentralWidget(inicio_widget)
    ventana.show()
    sys.exit(app.exec())
