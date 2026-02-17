class SalaryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # 1. Configuración Inicial: Llenar la lista de países desde el modelo
        countries = self.model.get_country_list()
        self.view.set_countries(countries)

        # 2. Conectar señales (Eventos)
        # Cuando toquen el botón, llamar a self.calculate
        self.view.calculate_btn.clicked.connect(self.handle_calculation)
        
        # Opcional: Actualizar símbolo moneda cuando cambie país en tiempo real
        self.view.country_combo.currentTextChanged.connect(self.update_currency_display)

    def update_currency_display(self, country_name):
        """Pequeño detalle UX: Cambiar prefijo del input de tarifa"""
        code = self.model.get_currency_code(country_name)
        self.view.rate_input.setPrefix(f"{code} $ ")

    def handle_calculation(self):
        data = self.view.get_inputs()
        
        # Validaciones básicas
        if data['hours'] <= 0:
            self.view.update_result("Hours must be greater than 0", is_error=True)
            return

        # Pedir al modelo que calcule
        total = self.model.calculate_payment(data['hours'], data['rate'])
        
        # Pedir al modelo el código de moneda (COP, USD, etc.)
        currency_code = self.model.get_currency_code(data['country'])

        # Formatear el texto (Tu truco de los puntos para miles)
        # {:,.2f} pone comas en miles y 2 decimales. Luego reemplazamos.
        formatted_total = f"{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        final_text = f"Total: {currency_code} $ {formatted_total}"

        # Mandar el resultado a la vista
        self.view.update_result(final_text)