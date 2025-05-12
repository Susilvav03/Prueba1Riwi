# Add colors to apply.
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

flag = True

# Create the inventory with the initial products.
inventory = {
    "Arepa blanca" : {"Precio": 5000, "Cantidad": 14},
    "Leche" : {"Precio": 3500, "Cantidad": 21},
    "Canasta de Huevos" : {"Precio": 21000, "Cantidad": 27},
    "Arepa de mote" : {"Precio": 5500, "Cantidad": 0},
    "Tostadas" : {"Precio": 13000, "Cantidad": 6}
}

def options():
    """ Show the options """
    print(MAGENTA + "\n _________________________________________________" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "|  Bienvenido al sistema de gestión de inventario |" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "|---------------------- Menú ---------------------|" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "| 1. Añadir productos                             |" + RESET)
    print(MAGENTA + "| 2. Consultar productos                          |" + RESET)
    print(MAGENTA + "| 3. Actualizar productos                         |" + RESET)
    print(MAGENTA + "| 4. Eliminar productos                           |" + RESET)
    print(MAGENTA + "| 5. Calcular el valor total del inventario       |" + RESET)
    print(MAGENTA + "| 6. Salir                                        |" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)

def errorMessage():
    """ Show error message once the attempt counter reaches its limit """
    print(RED + "\n ___________________________________________________ " + RESET)
    print(RED + "|                                                   |" + RESET)
    print(RED + "|  Demasiados intentos fallidos. Volviendo al menú. |" + RESET)
    print(RED + "|___________________________________________________|" + RESET)

def validatePositivePrice(value):
    """ Validate that the number entered is positive and multiple of 50"""
    if ((value.isdigit()) and (int(value) > 0) and (int(value) % 50 == 0)):
        return True, None
    return False, "El valor ingresado debe ser un número positivo y multiplo de 50."

def validatePositiveQuantity(value):
    """ Validate that the number entered is positive and integer"""
    if ((value.isdigit()) and (int(value) >= 0)):
        return True, None
    return False, "El valor ingresado debe ser un número positivo y entero."

def validateInventory(name):
    """ Validate that the product exists in the inventory """
    if (name in inventory):
        return True, f"El producto '{name}' existe en el inventario." 
    return False, f"El producto '{name}' no existe en el inventario." 

def addProduct(name, price, quantity):
    """ Add product to the inventory """
    inventory[name] = {"Precio": price, "Cantidad": quantity}
    return f"\nProducto '{name}' ha sido añadido al inventario exitosamente."

def searchProduct(name):
    """ Search a product in the inventory and return the name, price and quantity """
    price = inventory[name]["Precio"]
    quantity = inventory[name]["Cantidad"]
    return f"""
Producto '{name}' encontrado: 
Precio: ${int(price):.2f} 
Cantidad: {quantity}"""

def updateProduct(name, price, quantity):
    """ Update the price and quantity of a product """
    prevPrice, prevQuantity = inventory[name]["Precio"], inventory[name]["Cantidad"]
    inventory[name] = {"Precio": price, "Cantidad": quantity}
    return f"\nEl precio del producto '{name}' ha sido actualizado de ${int(prevPrice):.2f} a ${int(price):.2f} y la cantidad pasó de {prevQuantity} a {quantity}."

def deleteProduct(name):
    """ Delete a product from the inventory only if there is no disponibility (Disponibilidad = False) """
    if (int(inventory[name]["Cantidad"]) == 0):
        del inventory[name]
        return GREEN + f"\nProducto '{name}' ha sido eliminado del inventario." + RESET
    return RED + f"Para poder eliminar '{name}' del sistema, no debe haber disponibilidad, por favor primero actualiza '{name}' en caso de ser así." + RESET

def calculateTotalValue():
    """ Calculate the total value of the inventory (the sum of the multiplication of price by quantity of each product) """
    total = 0
    for x in inventory:
        price, quantity = inventory[x]["Precio"], inventory[x]["Cantidad"]
        total += int(price) * int(quantity)
    return f"\nEl valor total del inventario es ${total:.2f}"

# Main program.
while flag:
    options()
    # Choose the option.
    option = input("\nSeleeccione una opción (1-6): ")
    match option:
        # Add product.
        case "1":
            # Attempt counter can reach up to 3 attempts.
            # Possible errors: The price or quantity are not positive, the product already exists, the price is not multiple of 50.
            i=0
            while i < 3:
                name = input("\nIngrese el nombre del producto: ")
                val, msg = validateInventory(name)
                if (val):
                    print(YELLOW + msg + RESET)
                    i += 1
                    continue
                price = input(f"\nIngrese el precio de '{name}': ")
                val, msg = validatePositivePrice(price)
                if (not val):
                    print(YELLOW + msg + RESET)
                    i += 1
                    continue
                quantity = input(f"\nIngrese la cantidad de '{name}': ")
                val, msg = validatePositiveQuantity(quantity)
                if (not val):
                    print(YELLOW + msg + RESET)
                    i += 1
                    continue
                print(GREEN + addProduct(name, price, quantity) + RESET)
                break
            else:
                errorMessage()

        # Search for a product.
        case "2":
            name = input("\nIngrese el nombre del producto a consultar: ")
            val, msg = validateInventory(name)
            if (val):
                print (GREEN + searchProduct(name) + RESET)
            else:
                print(RED + msg + RESET)
        
        # Update product.
        case "3":
            name = input("\nIngrese el nombre del producto a actualizar: ")
            val, msg = validateInventory(name)
            # If the product doesn't exist in the inventory will appear an error.
            if (not val):
                print(RED + msg + RESET)
            else:
                # If the product does exist the user has to enter the new price and new quantity, if they want one of these characteristics to stay the same, they would have to enter the same
                # Attempt counter can reach up to 3 attempts.
                # Possible errors: The price or quantity are not positive, he price is not multiple of 50, the quantity is not an integer.
                i=0
                while i < 3:
                    newPrice = input(f"\nIngrese el nuevo precio de '{name}': ")
                    val, msg = validatePositivePrice(newPrice)
                    if (val):
                        newQuantity = input(f"\nIngrese la cantidad actual de '{name}': ")
                        val, msg = validatePositiveQuantity(newQuantity)
                        if (val):
                            print (GREEN + updateProduct(name, newPrice, newQuantity) + RESET)
                            break
                        else: 
                            print(YELLOW + msg + RESET)
                            i += 1
                            continue
                    else: 
                        print(YELLOW + msg + RESET)
                        i += 1
                        continue
                else:
                    errorMessage()

        # Delete product.
        case "4": 
            name = input("\nIngrese el nombre del producto a eliminar: ")
            val, msg = validateInventory(name)
            # If the product doesn't exist the syste will print an error and it'll go back to the menu
            if (not val):
                print(RED + msg + RESET)
            else:
                print(deleteProduct(name))
        
        # Calculate total value of the inventory
        case "5":
            print(GREEN + calculateTotalValue() + RESET)
        
        # Exit the system
        case "6":
            print(GREEN + "\nGracias por usar el sistema de gestión de inventario. ¡Hasta luego!" + RESET)
            flag = False

        # For any other option besides the ones on the menu: error
        case _:
            print(RED + "\nOpción no válida. Por favor, seleccione una opción del menú." + RESET)

