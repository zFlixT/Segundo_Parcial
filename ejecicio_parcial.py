print("----------------")
print("---Bienvenido---")
print("----------------")


num = -1

while num <= 0:

    try:
        num = int(input("\nIngresa un numero para empezar la serie. -> "))

        if num > 0:
            break
        
        print("\033[1m"+"\nEl numero es incorrecto, por favor vuelva a intentarlo."+"\033[0m")

    except ValueError:
        print("\033[1m"+"\nSe ingresó un valor que no es un número entero. Por favor ingrese uno correcto."+"\033[0m")

suma = 1
suma2 = 1

while suma2 < num:
    suma += 1/(1+suma2)
    suma2 +=1
    
print("El resultado de la suma es ", suma)