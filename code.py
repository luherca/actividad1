p_raras = { "ARREBOL" : "color rojo de las nubes iluminadas por el sol" , 
           "ABUHADO" : 'dícese de aquellas personas quienes tienen una apariencia similar a un búho o ave similar' }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in p_raras.keys():
    print(p_raras[word])
else:
    print('esa palabra no está en el diccionario')
