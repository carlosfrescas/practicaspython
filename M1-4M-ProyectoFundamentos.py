nombre = input("introduce tu nombre: ")
apellidoPaterno = input("introduce tu apellido paterno: ")
apellidoMaterno = input("introduce tu apellido materno: ")
edad = int(input("introduce tu edad: "))
estatura = float(input("introduce tu estatura en metros: "))
peso = float(input("introduce tu peso en kilogramos: "))
#se le solicita nombre, apellido paterno, materno, edad(int), estatura en metros(float), peso en kilogramos(float) 

IMC = peso/ estatura**2
#formula para conseguir el indice de masa corporal

if (edad < 18):
    print("usted es menor de edad")
else:
    print("usted es mayor de edad")
#aclaración de mayoría de edad 

print("usted "+ nombre +" "+ apellidoPaterno +" "+ apellidoMaterno +
       " tiene un IMC de: " + str(IMC))
print("lo que se traduce como: ")


if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
elif IMC >= 40.00:
        print ("obesidad morbida")  
#con las diferentes resultados posibles se crea un parametro para medir el nivel de delgadez u obesidad en el que se encuentra el usuario 
