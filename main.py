import sys
from PyQt5.QtWidgets import QApplication
from model import CalculatorModel
from view import SalaryView
from controller import SalaryController

def main():
    app = QApplication(sys.argv)

    # Instanciamos las 3 partes del MVC
    model = CalculatorModel()
    view = SalaryView()
    
    # El controlador conecta el modelo y la vista
    controller = SalaryController(model, view)

    # Mostramos la ventana
    view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()