#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:38:52 2018

@author: Paulo Andrade
"""

from include.LinearRegression import LinearRegression

# Metodo principal del programa
def main ():
    x = [] # valores para x
    t = [] # valores para t
    
    print "Algorithm of Linear Regression\n\n"
    
    # Ingresamos el valor de n
    n = input("Ingrese el numero de pares ordenados: ");
    
    # Obtenemos los pares ordenados
    for i in range(0, n):
        x.append(input("X"+str(i)+": "))
        t.append(input("t"+str(i)+": "))
        
    # Instanciamos
    lr = LinearRegression(x, t)
        
    # Ingresamos el dato para la prediccion
    xi = input("Ingrese el dato a predecir: ")
    
    # Obtenemos el resultado
    res = lr.prediction(xi)
    
    # Mostramos el resultado
    print "Resultado: "+str(xi)+" = "+str(res)
    
# Indicamos cual es el metodo principal
if __name__ == "__main__":
    main()