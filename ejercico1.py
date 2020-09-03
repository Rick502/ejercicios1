#proyecto: calcular distancia 
#autor: ricardo nistch 
#carnet: 1618720
# clacular la distancia de cualquier objeto 
print('bienvendio el vamos a calcular la distancia de cualquier objeto')

velosidad_inicial = input('ingrese la velocidad en km: ')
velosidad_inicial = int(velosidad_inicial)

tiempo = input('ingrese el tiempo en Hr: ')  
tiempo = int(tiempo)

aceleracion = input('ingrese la aceleracio: ')
aceleracion = int(aceleracion)

distancia = print(velosidad_inicial * tiempo + 1/2 * aceleracion ** tiempo)
