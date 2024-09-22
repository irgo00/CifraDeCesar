frase = input("Informe a frase: ")

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

for i in range(len(alfabeto)):
    print(f"{i} - ", end="")
    for caracter in frase:
        if caracter.islower():
            caracter = caracter.upper()
        if caracter in alfabeto:
            caracter = alfabeto[(alfabeto.index(caracter) + i) % 26]
            print(caracter, end="")
        else:
            print(" ", end="")
    print("\n")
