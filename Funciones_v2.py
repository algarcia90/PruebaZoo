import Screen_v2 as scr

def validacion(age):
    try:
        if int(age) >= 0:
            return True
        else:
            return False
    except:
        return False

#////////////////////////////////////////////////////////////////////////
def pediredad():
    age = scr.pregunta('Que edad tienes? ',line = 1,column = 1)
    while validacion(age) == False:
        scr.formato(0,33,41)
        scr.imprime('Debes introducir un numero entero positivo.',line = 25,column = 1, color = 'yellow', back = 'red')
        scr.quitaformato()
        age = scr.pregunta('Que edad tienes? ',line = 1,column = 1)
    scr.clearline(25,1)
    return int(age)
#////////////////////////////////////////////////////////////////////////
def tipoEntrada(edad):
    if edad <= 2:
         Tipo = 'baby'
    elif edad <= 12:
        Tipo = 'menores'
    elif edad < 65:
        Tipo = 'normales'
    else:
        Tipo = 'jubilado'
    return Tipo
#////////////////////////////////////////////////////////////////////////
def printScreen():
    scr.clear()
    scr.imprime('Bebe....:   -',line = 4,column = 5)
    scr.imprime('Niño....:   -',line = 5,column = 5)
    scr.imprime('Adulto..:   -',line = 6,column = 5)
    scr.imprime('Jubilado:   -',line = 7,column = 5)
    scr.imprime('Total....:',line = 9,column = 8)
