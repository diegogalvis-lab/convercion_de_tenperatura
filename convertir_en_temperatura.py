# programar para convertir grados °C a °F, °K, °Ra y Re

#Librerias
import math

#-----
#input
#-----

print("                                               ")
print("------convertir °c a °F, °K, °Ra y °Re------")
print("                                             ")


C=int(input(" digite el valor de grados centrigados: "))

#----------
#processing
#----------

F=C*1.8+32
K=C+273.15

#----------
#output
#----------
print("grados fahrenheit: " +str(F))
print("grados kelvin   "  +str(K))