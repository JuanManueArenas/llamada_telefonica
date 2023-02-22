# Programa para saber el valor de la llamada

print("------------------------------------------")
print("---El resultado de las operaciones son:---")
print("------------------------------------------")


# input

minutos = int(input("ingrese los minutos de la llamada: "))

# procesing

if minutos < 3:
    costo = 300

else: 
    costo = (minutos * 50 ) + 300 - 150




# output
print("-----------------------------------------")
print("---------------RESULTADOS----------------")
print("-----------------------------------------")
print("El costo de la llamada es de: " + str (costo))