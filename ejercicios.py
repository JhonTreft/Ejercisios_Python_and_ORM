# 1. Escribe una función que tome una lista de números y devuelva una lista de los cuadrados de esos
# números utilizando la funcion map.

cuadrado_num = lambda lista: list(map(lambda item: item**3, lista))

# 2. Escribe una función que tome una lista de cadenas y devuelva una lista de las mismas cadenas en orden inverso
# utilizando map

reverse = lambda cadena: list(map(lambda item: cadena[::-1], cadena))

# 3. Escribe una función que tome una lista de números y devuelva una lista de los números pares utilizando
# la funcotn filter().

pares = lambda list_num: list(filter(lambda item: item % 2 == 0, list_num))

# 4. Escribe una función que tome una lista de cadenas y devuelva una lista de las cadenas que contienen
# la letra (s) utilizando filter()

cadena_s = lambda lista_cadena: list(
  filter(lambda item: item in "s", lista_cadena))

# 5. Escribe una función que tome una lista de números y devuelva la suma de los
# cuadrados de esos números utilizando reduce()
from functools import reduce

suma_cuadrados = lambda list_num: reduce(lambda x, y: x + y,
                                         map(lambda x: x**2, list_num))

# 6. Escribe una función que tome una lista de cadenas y devuelva la cadena más larga utilizando reduce()

max_len = lambda lista_cadenas: reduce(
  lambda x, y: x if len(x) > len(y) else y, lista_cadenas)

# 7. Escribe una función que tome una lista de números y devuelva la lista ordenada utilizando sorted()

order_list = lambda list_number: sorted(list_number)

# 8. Escribe una función que tome una lista de cadenas y devuelva la lista ordenada por longitud de cadena utilizando sorted() y una función lambda:

order_len_chain = lambda lista_cadenas: sorted(lista_cadenas,
                                               key=lambda item: len(item))

# 9. Escribe una función que tome una lista de números y devuelva la lista ordenada de forma descendente utilizando sorted() y el argumento reverse=True

reverse = lambda list_num: sorted(list_num, reverse=True)

# 10. Escribe una función que tome una lista de cadenas y devuelva la lista ordenada alfabéticamente pero ignorando las mayúsculas utilizando sorted() y la función str.lower()

order_chain = lambda lista_cadenas: sorted(lista_cadenas,
                                           key=lambda item: item.lower())

# 11. Dada una lista de listas, devuelve una lista con el número máximo en cada lista
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_each_list = [max(l) for l in list]

# 12. Dada una lista de diccionarios, devuelve una lista con los valores únicos de una determinada clave

lista = [
  {
    "planet": "Jupyter",
    "star": 11
  },
  {
    "planet": "Marte",
    "star": 3
  },
  {
    "planet": "Pluton",
    "star": 9
  },
]

unique_value = lambda lista, value: set(dic[value] for dic in lista)

print(unique_value(lista, "star"))
# 13. Dada una lista de números, devuelve una lista con los números que aparecen más de una vez

count_more_one = lambda list_number: list(
  set(number for number in list_number if list_number.count(number) > 1))

# 14. Dada una lista de números, devuelve una lista con los números que son la suma de dos números en la lista
from itertools import combinations

nums = [1, 2, 4, 5, 6, 7]

target = 5

sum_of_two = [pair for pair in combinations(nums, 2) if sum(pair) == target]

# 15. Dada una lista de cadenas, devuelve una lista con las palabras que empiezan y terminan con la misma letra

chains_list = ["hola", "si", "epa"]

end_and_start = [x for x in chains_list if x[0] == x[-1]]

# 16. Dada una lista de números, devuelve una lista con los números que son divisibles por todos los números de otra lista
numeros_ = [40, 20, 30, 60, 10]
divisores = [2, 5, 10]

all_divisibles = lambda num: all(num % divisor == 0 for divisor in divisores)

#print(list(filter(all_divisibles, numeros_)))

# 17. Dada una lista de diccionarios, devuelve una lista con los diccionarios ordenados por una determinada clave

lista = [
  {
    "planet": "Jupyter",
    "star": 11
  },
  {
    "planet": "Pluton",
    "star": 3
  },
  {
    "planet": "Marte",
    "star": 9
  },
]
clave = "planet"
order_dict = sorted(lista, key=lambda x: x[clave])

# 18. Dada una lista de números, devuelve la lista ordenada de forma ascendente pero con los números pares primero y los impares después

list_num = [3, 5, 1, 4, 2, 6, 7, 8, 9]

order = sorted(list_num, key=lambda x: (x % 2 == 0, x))

# 19. Dada una lista de diccionarios, devuelve una lista con los diccionarios que contienen una determinada clave

lista_diccionarios = [{
  'nombre': 'Juan',
  'edad': 25
}, {
  'nombre': 'María',
  'email': 'maria@example.com'
}, {
  'nombre': 'Pedro',
  'edad': 30,
  'email': 'pedro@example.com'
}, {
  'nombre': 'Luisa',
  'email': 'luisa@example.com'
}]

clave_buscada = 'email'

filtrados = list(filter(lambda d: clave_buscada in d, lista_diccionarios))

# 20. Dada una lista de cadenas, devuelve una lista con las palabras que contienen todas las vocales

words = [
  'programacion', 'planeta', 'gamer', 'low', 'computadora', 'peliculota'
]

filter_vocals = list(filter(lambda word: set('aeiou') <= set(word), words))

# 21. Crea tu primer proyecto.

#Projecto De Como es la gestion en memoria(basico)

# definir funciones lambda para la gestión de memoria

"""
inicializar_memoria = lambda size: [0]*size
escribir_en_memoria = lambda mem, addr, val: list(map(lambda i: val if i == addr else mem[i], range(len(mem))))
leer_de_memoria = lambda mem, addr: mem[addr]
imprimir_memoria = lambda mem: print(mem)

# inicializar la memoria
memoria = inicializar_memoria(10)

# escribir algunos valores en la memoria utilizando map
memoria = list(map(lambda x: escribir_en_memoria(memoria, x[0], x[1]), [(2, 5), (4, 10), (8, 20)]))

# leer algunos valores de la memoria utilizando map
valores_leidos = list(map(lambda x: leer_de_memoria(memoria, x), [2, 4, 8]))
print(valores_leidos)

# mostrar la memoria actual utilizando la función lambda imprimir_memoria
imprimir_memoria(memoria)





En el código, se definen cuatro funciones que se utilizan para inicializar, escribir y leer valores en una lista que simula la memoria. La función inicializar_memoria toma un argumento que representa el tamaño de la memoria y devuelve una lista de ceros del tamaño especificado. La función escribir_en_memoria toma tres argumentos: la lista de memoria, la dirección de memoria donde se desea escribir el valor y el valor que se desea escribir en la memoria. Esta función devuelve una nueva lista con el valor actualizado en la dirección de memoria especificada. La función leer_de_memoria toma dos argumentos: la lista de memoria y la dirección de memoria donde se desea leer el valor. Esta función devuelve el valor en la dirección de memoria especificada. La función imprimir_memoria toma la lista de memoria y muestra su contenido en la consola.

Luego, se inicializa la memoria con la función inicializar_memoria, se escriben algunos valores en ella con la función escribir_en_memoria y se leen algunos valores con la función leer_de_memoria. Finalmente, se muestra el contenido actual de la memoria en la consola con la función imprimir_memoria.
"""

# 22. Subelo a tu repositorio explicado cada punto

#Okey Bro

# 23. Escribe un articulo sobre las funiones mas usadas en python y cuales usarioas tu, cita varios ejemplos, puedes usar linkedin y medium

#Okey Bro
