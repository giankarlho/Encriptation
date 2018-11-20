# Cadena de texto que deseamos cifrar
message = 'ESTE ES MI MENSAJE SECRETO'
 
# La llave de cifrado o descifrado
key = 13
 
# Le decimos al programa que queremos realizar
mode = 'encrypt' # 'encrypt' o 'decrypt'
 
# Todos los posibles simbolos 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
#Aqui se almacena el mensaje final
translated = ''
 
# Ponemos en mayúsculas el mensaje
message = message.upper()
 
# Recorremos el mensaje
for symbol in message:
    if symbol in LETTERS:
        # Obtenemos el indice del simbolo
        num = LETTERS.find(symbol) 
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
 
        # si num es mayor que el largo de
        # LETTERS o es menor que  0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
 
        # Agregamos el simbolo al mensaje final
        translated = translated + LETTERS[num]
 
    else:
        # Agregamos el simbolo
        translated = translated + symbol
 
# Imprimimos el mensaje cifrado/descifrado
print(translated)
