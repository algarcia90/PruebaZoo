import Funciones_v2 as fn
import Screen_v2 as scr
#////////////////////////////////////////////////////////////////////////
fn.printScreen()
#precios esta en el archivo principal y en la funcion calcularentrada
negocio = {
        'baby': {'precio': 0, 'cantidad':0, 'acumulado':0},
        'menores': {'precio': 14, 'cantidad':0, 'acumulado':0},
        'normales': {'precio': 23, 'cantidad':0, 'acumulado':0},
        'jubilado': {'precio': 18, 'cantidad':0, 'acumulado':0}
    }

coordenadas = {
        'baby': {'cantidad':(4,15),'acumulado':(4,22)},
        'menores': {'cantidad':(5,15),'acumulado':(5,22)},
        'normales': {'cantidad':(6,15),'acumulado':(6,22)},
        'jubilado': {'cantidad':(7,15),'acumulado':(7,22)}
    }
edad = fn.pediredad()
preciototal = 0
#OJO A ESTO RESPECTO A LA BETA
#Al cambiar el condicionante precio, por el tipo, que es lo que realmente condiciona,
#Podemos eliminar todos los bucles que estabamos haciendo a lo tonto, y hacer solo el bucle para encontrar el tipo correcto
while edad != 0:
    Tipo = fn.tipoEntrada(edad)
    negocio[Tipo]['cantidad'] += 1
    negocio[Tipo]['acumulado'] = negocio[Tipo]['cantidad']*negocio[Tipo]['precio']
    scr.imprime(negocio[Tipo]['cantidad'],\
    line = coordenadas[Tipo]['cantidad'][0],\
    column = coordenadas[Tipo]['cantidad'][1])
    scr.imprime('{:7.2f} €'.format(negocio[Tipo]['acumulado']),\
    line = coordenadas[Tipo]['acumulado'][0],\
    column = coordenadas[Tipo]['acumulado'][1])

    preciototal = preciototal + negocio[Tipo]['precio']
    scr.imprime('{:7.2f} €'.format(preciototal),line = 9,column = 22, style = 'bold')
    edad = fn.pediredad()

#comando para que la siguiente instruccion de linux no me tape el programa
scr.locate(11,1)
