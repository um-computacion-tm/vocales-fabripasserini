def contar_vocales(my_string):
    vocales =("a", "e", "i", "o", "u")
    resultado = {}
    my_string = my_string.lower()
    for letra in my_string:
        if letra in vocales:
            if letra not in resultado:
                 resultado[letra] = 0
            resultado[letra] += 1
    return resultado
            
