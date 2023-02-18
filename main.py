from multiprocessing import Pool # importa la clase Pool del módulo multiprocessing
from time import sleep # importa la función sleep del módulo time
import random # importa el módulo random

# define una función llamada scrape que toma un argumento url
def scrape(url):
    print("starting", url) # imprime un mensaje indicando que se está iniciando el raspado con una URL específica
    duration = round(random.random(), 3) # genera un número aleatorio entre 0 y 1 y lo redondea a tres decimales. Este número se utiliza como la duración del raspado simulado.
    sleep(duration) # espera por la cantidad de tiempo especificada por la duración simulada del raspado
    print("finished", url, "time taken:", duration, "seconds") # imprime un mensaje indicando que se ha completado el raspado con una URL específica y cuánto tiempo tomó.
    return url, duration # devuelve la URL y la duración del raspado

# define una lista de URLs para raspar
urls = ["a.com", "b.com", "c.com", "d.com"]

# comprueba si el archivo se está ejecutando directamente y no se está importando
if __name__ == "__main__":
    pool = Pool(processes=4) # crea una instancia de la clase Pool con un tamaño de grupo de procesos de 4
    data = pool.map(scrape, urls) # ejecuta la función scrape para cada URL en la lista usando el grupo de procesos de la piscina y devuelve los resultados como una lista de tuplas
    pool.close() # cierra la piscina de procesos
    
    print() # imprime una línea en blanco
    for row in data: # para cada tupla en la lista de resultados de raspado
        print(row) # imprime la tupla que contiene la URL y la duración del raspado
