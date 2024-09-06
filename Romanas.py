print(" 🎀 Design by Berenice Hernandez 🎀")
print("Student of Institute of Technology Ensenada")

#------Definimos las letras romanas en un conjunto y le asignamos valor------
def son_letras_romanas(letra):
    letras_romanas = {'I', 'V', 'X', 'L', 'C', 'D', 'M', 'i', 'v', 'x', 'l', 'c', 'd', 'm'}
    return letra in letras_romanas #regresa true si la letra es parte del conjunto

#-----Toma como argumento a @letra y regresa su valor numerico-----
def valores_romanos(letra):
    asignacion_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                          'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    return asignacion_romanos.get(letra, 0) #sino esta dentro del conjunto regresa 0



#----- Funcion para Realizar la suma de cada letra en @palabra -----#
def suma_letra(palabra):  #agregamos @palabra como atributo
    suma = 0 #acumulador
    long = len(palabra) #longitud de cada palabra
    
    for i in range(long): #ciclo para recorrer la palabra
        actual = palabra[i] #definimos actual para la letra actual
        if not son_letras_romanas(actual): 
            continue 
        valor_actual = valores_romanos(actual)
    
        #Verifica la sig letra    
        if i < long - 1 and valores_romanos(palabra[i+1]) > valor_actual:
            #si la letra anterior es menor que la sig y la que sig es romana
            continue 
        suma += valor_actual
    
    return suma

def suma_palabra(arreglo):
        return{palabra:suma_letra(palabra) for palabra in arreglo}
    #funcionamiento
    # resultados = {}
    # for palabra in arreglo:
    #     suma_palabra_actual = suma_letra(palabra)
    #     resultados[palabra] = suma_palabra_actual
    # return resultados

arreglo = ["Pixel", "Civil", "Hijo", "Toxico", "Camion", "Clave", "Ximena", "Damian", "Lili", "Claudia", "Berenice"]

#
resultados_palabras = suma_palabra(arreglo)

print("---Resultados de las palabras ingresadas y su valores en Romano, mientras sea un valor valido-----")
for palabra, suma in resultados_palabras.items():
    print(f"La suma de {palabra} es: {suma}")
print("Gracias por usar mi codigo........🥰")