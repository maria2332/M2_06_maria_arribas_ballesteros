def imc():
    peso = int(input("Introduce tu peso: "))
    talla = round(float(input("Introduce tu altura: ")),2)
    IMC = peso / (talla * talla)
    print("Tu imc es de ", IMC)

    if IMC < 18.50:
        print("Bajo peso")
    elif 25.00 > IMC >=18.50 :
        print("Peso normal")
    elif IMC >= 25.00 :
        print("Sobrepeso")
    elif IMC >= 30.00 :
        print("Obesidad")
    return imc

imc()