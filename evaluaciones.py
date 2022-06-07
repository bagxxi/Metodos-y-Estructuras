from pizza import Pizza

# a:
print("Todas las pizzas tienen un tamaño {} y un valor de {}".format(
    Pizza.tamano, Pizza.precio
))

# b:
print(Pizza.validando_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c:
pizza = Pizza()
pizza.pedido()

# d:
print("\nVegetales: {}\nCarne: {}\nTipo de masa: {}\n¿Es una pizza válida?: {}\n".format(
    pizza.vegetales, pizza.carnes, pizza.tipo_de_masa, pizza.pizza_valida
))

# e:
print("¿La clase es una pizza válida?: {}".format(pizza.pizza_valida))