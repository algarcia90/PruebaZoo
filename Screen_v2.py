#modulo para trabajar con la pantalla de consola y presentar resultados. Codigos ANSI
#version mejorada desde el zoo_v1
styles = {
'bold' : '1',
'underline' : '4',
'blink' : '5',
'reversed' : '7'
}
colors = {
'black' : '30',
'red' : '31',
'green' : '32',
'yellow' : '33',
'blue' : '34',
'magenta' : '35',
'cyan' : '36',
'white' : '37',
'reset' : '39'
}
background = {
'black' : '40',
'red' : '41',
'green' : '42',
'yellow' : '43',
'blue' : '44',
'magenta' : '45',
'cyan' : '46',
'white' : '47',
'reset' : '49'
}

def clear():
    print('\033[2J')

def locate(linea, columna):
    print('\033[{};{}H'.format(linea, columna), end = "")

def clearline(linea = None, columna = None):
    #cuidado con el print, porque incluye un salto de línea y descuadra todo, meter siempmre el end para estas cosas
    if linea is not None and columna is not None:
        locate(linea, columna)
    elif linea is not None:
        locate(linea,1)
    print('\033[K', end = '')
#meter este clearline cada vez que tenemos que hacer un input o imprimir algo y además reposicionarnos es engorroso

#creamos una función que nos modifique el estilo de pantalla en función de los inputs que tenga del diccionario
def procesaparams(params):
    if 'line' in params:
        line = params['line']
        column = 1
        if 'column' in params:
            column = params['column']
        locate(26,1)
        print(line)
        print(column)
        wait = input('press enter')
        locate(line, column)
    if 'color' in params and params['color'] in colors:
        print('\033[{}m'.format(colors[params['color']]))
    if 'back' in params and params['back'] in background:
        print('\033[{}m'.format(background[params['back']]))
    if 'style' in params and params['style'] in styles:
        print('\033[{}m'.format(styles[params['style']]))
#creamos nuestros propios input y print para facilitarnos la vida
#recordamos los dos tipos de argumento de las funciones

# es un print, aparte del texto, podemos definir line, column, color, background y style que usará el diccionario params
#también incluye el parámetro booleano newline y el también booleano nr(noreset)
def imprime(cadena, **params):
    procesaparams(params)
    if 'newline' in params and params['newline']:
        print(cadena)
    else:
        print(cadena, end = '')
    if 'nr' not in params:
        quitaformato()
#el poner delend por defecto o no depende de que queramos con la funcion, los input nos interesa que se vean claros
#por otra parte, cuando estamos imprimiendo texto, a veces queremos respetar lo que ya hay

# es un input, aparte del texto, podemos definir line, column, color, background y style que usará el diccionario params
#también incluye el booleano de key 'dirty' por si queremos no borrar lo que había escrito previamente en la localizacion
def pregunta(msg, **params):
    procesaparams(params)
    if 'dirty' not in params:
        clearline()
    return input(msg)

def formato(estilo, color = None, fondo = None):
    if color is None and fondo is None:
        print('\033[{}m'.format(estilo), end='')
    else:
        print('\033[{};{};{}m'.format(estilo, color, fondo), end='')

def quitaformato():
    print('\033[0m', end='')
