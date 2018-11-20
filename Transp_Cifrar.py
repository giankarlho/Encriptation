
def main():
    #mensaje a cifrar
    myMessage = 'a quien druga dios le ayuda'
    #la llave que utilizaremos
    myKey = 5
    #llamando a la funcion que se encarga de cifrar
    ciphertext = encryptMessage(myKey, myMessage)
 
    # Imprime la cedena cifrada y usando  '|' para indicar el fin
    #del mensaje cifrado
    print(ciphertext + '|')
 
#funcion para cifrar el mensaje
def encryptMessage(key, message):
#Cada cadena de texto en el mensaje cifrado representa una columna en la matriz
    ciphertext = [''] * key
 
    # recorremos las colimnas
    for col in range(key):
        pointer = col
 
        #Lee cada elemento de la columna
        while pointer < len(message):
            # Pone el caracter que encuentra en el indice de la matriz
            ciphertext[col] += message[pointer]
 
            #mueve el puntero al siguiente elemento de la columna
            pointer += key
 
    # Convertimos la lista en una cadena de texto y  lo retornamos
    return ''.join(ciphertext)
 
# si el nombre de la funcion es main la manda a ejecutar
if __name__ == '__main__':
    main()