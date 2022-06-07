from ingredientes import carnes, vegetales, masas

# definiendo la clase y los atributos
class Pizza:
    tamano = "familiar"
    precio = 10000

    @staticmethod
    def validando_elemento(elemento, posibles):
        elemento.lower()
        if elemento in posibles:
            return True
        return False

    def pedido(self):
        # ingredientes carnes
        self.carnes = input("\nSeleccione qué carne desea agregar:"
                              "Elija entre:\n"
                            "- Pollo\n"
                            "- Carne\n"
                            "- Pavo\n")

        # Define atributo vegetales como lista
        self.vegetales = []

        # elegir primer vegetal
        self.vegetales.append(input("\nSeleccione qué vegetal quiere agregar:"
                                    " Elija entre:\n"
                                    "-Cebolla\n"
                                    "-Choclo\n"
                                    "-Tomate\n"
                                    "-Aceitunas\n"))

        # elegir segundo vegetal
        self.vegetales.append(input("\nSeleccione qué otro vegetal quiere agregar:"
                                    " Elija entre:\n"
                                    "-Cebolla\n"
                                    "-Choclo\n"
                                    "-Tomate\n"
                                    "-Aceitunas\n"))

        # elegir masa
        self.tipo_de_masa = input("\nSeleccione qué tipo de masa quiere para su pizza:"
                                    " Elija entre:\n"
                                    "-Tradicional\n"
                                    "-Delgada\n"
                                    "-Borde Queso\n")

        # validar si todos los ingredientes corresponden a los de la lista, para saber si la pizza es válida
        self.pizza_valida = self.validando_elemento(self.carnes, carnes) and \
                                   self.validando_elemento(self.vegetales[0], vegetales) and \
                                   self.validando_elemento(self.vegetales[1], vegetales) and \
                                   self.validando_elemento(self.tipo_de_masa, masas)


