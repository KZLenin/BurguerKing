valid_input = True
print("**********Bienvenido a Burger King************")
print("")
print("inserte los datos para la factura electronica")
print("")
name = input("Ingrese su nombre: ")
id = input("Ingrese su numero de cedula: ")
email = input("Ingrese su correo: ")
n = int(input("Ingrese el número de hamburguesas a adquirir: "))
print("")
print("Ingrese uno de los siguientes tipos de hamburgesas: ")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
typeH = int(input("Ingrese la opcion: "))
match typeH:
    case 1:
        cpayment = n * 1.50
    case 2:
        cpayment = n * 2.50
    case 3:
        cpayment = n * 3.25
    case _:
        print("Este tipo de hamburguesa no existe")
        valid_input = False

if valid_input:
    print("")
    print("Ingrese su forma de pago: ")
    print("1) Tarjeta de crédito")
    print("2) Efectivo")
    print("")

    typeP = int(input("Ingrese la opción: "))

    match typeP:
        case 1:
            cpayment = cpayment * 1.05
        case 2:
            pass
        case _:
            print("No existe este método de pago")
            valid_input = False

if valid_input:
    print(f"Genial, {name}, el precio final a pagar es: ${round(cpayment, 2)}")
    print(f"La factura se enviará a su correo {email}")
else:
    print("No se pudo completar la transacción debido a una entrada inválida.")