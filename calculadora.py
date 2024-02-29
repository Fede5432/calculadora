def calculadora(num1, num2, operador):

    if num1.isdigit() and num2.isdigit():    

        if num2 == "0" and operador == "/":
            print("No se puede dividir por 0")
            return ingreso_datos()

        else:

            if operador == "+": texto1 = "El resultado de la suma de {} y {} es = {}"
            elif operador == "-": texto1 = "El resultado de la resta de {} y {} es = {}"
            elif operador == "*": texto1 = "El resultado de la multiplicación de {} y {} es = {}"
            elif operador == "/": texto1 = "El resultado de la división de {} y {} es = {}"
            else: return print("El operador no es valido")

            num1 = int(num1)
            num2 = int(num2)

            diccionario = {
                "+": texto1.format(num1, num2, num1 + num2),
                "-": texto1.format(num1, num2, num1 - num2),
                "*": texto1.format(num1, num2, num1 * num2),
                "/": texto1.format(num1, num2, num1 / num2)
                }

            for i in diccionario:
                if operador == i:
                    return print(diccionario[i])
    else:
        return print("Los dos datos ingresados necesitan ser si o si un numero")
    
def ingreso_datos():

    global num1, num2, operador

    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    operador = input("Ingrese el operador: ")

    return calculadora(num1, num2, operador)
    
ingreso_datos()