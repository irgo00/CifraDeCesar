frase = input("Informe a frase: ")

desloc = int(input("Informe o deslocamento: "))

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

for caracter in frase:
    if caracter.isupper():
        caracter = caracter.lower()
    if caracter in alfabeto:
        caracter = alfabeto[(alfabeto.index(caracter) + desloc) % 26]
        print(caracter, end="")
    else:
        print(" ", end="")
