import math
 
def main():
    myMessage = 'hello soy de peru'
    myKey = 8
 
    plaintext = decryptMessage(myKey, myMessage)
 
    # imprime con un  | después de los espacios y el fin del mensaje
    # des cifrado
    print(plaintext + '|')
 
def decryptMessage(key, message):
    # La función decrypt transposition simula las columnas y filas 
    # de nuestra tabla como el texto plano es escrito usando una lista 
    # de cadenas de texto, primero , necesitamos calcular unos cantos
    # valores
 
    # El numero de columnas en nuestra tabla
    numOfColumns = math.ceil(len(message) / key)
    # El numero de filas que nuestra tabla necesitara
    numOfRows = key
    # El numero de cajas sombreadas en la ultima columna de nuestra tabla
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
 
    # Cada cadena de texto in texto plano representa una columna dentro
    # de nuestra tabla
    plaintext = [''] * numOfColumns
 
    # Las variables col y row señalan el punto en la tabla donde ira el
    # próximo carácter del mensaje enciptado
    col = 0
    row = 0
 
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # señala la siguiente columna
 
        # si no hay mas columas  o estamos en un lugar sombreado,volver a 
        # la primera columna y la siguiente fila
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
 
    return ''.join(plaintext)
 
if __name__ == '__main__':
    main()