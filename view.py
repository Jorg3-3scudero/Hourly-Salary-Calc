from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QFormLayout, 
    QComboBox, QDoubleSpinBox, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SalaryView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pro Salary Calculator MVC")
        self.setFixedSize(400, 450)
        self.init_ui()

    def init_ui(self):
        #CSS-like
        self.setStyleSheet("""
            QWidget { font-family: 'Segoe UI', sans-serif; background-color: #f4f4f4; }
            QLabel { font-size: 14px; color: #333; }
            QPushButton { 
                background-color: #0078d7; color: white; border-radius: 5px; 
                padding: 10px; font-weight: bold; font-size: 14px;
            }
            QPushButton:hover { background-color: #005a9e; }
            QComboBox, QDoubleSpinBox { 
                padding: 5px; border: 1px solid #ccc; border-radius: 3px; background: white;
            }
        """)

        layout = QVBoxLayout()

        # Título
        title = QLabel("Monthly Salary Calculator")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        layout.addSpacing(20)

        # Formulario
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        # Inputs
        self.country_combo = QComboBox()
        self.hours_input = QDoubleSpinBox()
        self.hours_input.setRange(0, 750)
        self.hours_input.setDecimals(1)
        
        self.rate_input = QDoubleSpinBox()
        self.rate_input.setRange(0, 100000000)
        self.rate_input.setDecimals(2)
        # Valor por defecto inicial (dado el caso de mi trabajo actual)
        self.rate_input.setValue(13000) 

        form_layout.addRow("Select Country:", self.country_combo)
        form_layout.addRow("Hours Worked:", self.hours_input)
        form_layout.addRow("Hourly Rate:", self.rate_input)

        layout.addLayout(form_layout)
        layout.addSpacing(25)

        # Botón
        self.calculate_btn = QPushButton("Calculate Salary")
        layout.addWidget(self.calculate_btn)

        # Resultado
        self.result_frame = QFrame()
        self.result_frame.setStyleSheet("background-color: white; border-radius: 5px; border: 1px solid #ddd;")
        result_layout = QVBoxLayout(self.result_frame)
        
        self.result_label = QLabel("Enter data to calculate")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Segoe UI", 12))
        
        result_layout.addWidget(self.result_label)
        layout.addSpacing(20)
        layout.addWidget(self.result_frame)
        
        layout.addStretch()
        self.setLayout(layout)


    
    def set_countries(self, countries):
        self.country_combo.addItems(countries)

    def get_inputs(self):
        return {
            "country": self.country_combo.currentText(),
            "hours": self.hours_input.value(),
            "rate": self.rate_input.value()
        }

    def update_result(self, text, is_error=False):
        self.result_label.setText(text)
        if is_error:
            self.result_label.setStyleSheet("color: red; font-weight: bold;")
        else:
            self.result_label.setStyleSheet("color: green; font-weight: bold; font-size: 16px;")