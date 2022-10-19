peso = int(input("ingresa peso kg : "))
estatura = int(input("ingresa estatura centimetros : "))

estatura_metros = estatura/100
# El índice de masa corporal (IMC) es el peso de una persona en kilogramos dividido por el cuadrado de la estatura en metros.
masa_corporal = peso/estatura_metros**2

print("la estaura en metros es {} metros".format(estatura_metros))

print(f"la masa corporal es: {masa_corporal:.2f} metros cuadrados ")
