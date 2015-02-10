#!/bin/usr/python
# -*- coding: utf-8 -*-

"""
Script para multiplicar, dividir, sumar o restar dos números.

Para ejecutarlo, desde la shell:
$ python calculadora.py funcion operando1 operando2

"""

import sys
import os


def suma(sumando1, sumando2):
    """Suma de dos reales"""

    return sumando1 + sumando2


def resta(minuendo, sustraendo):
    """Resta de dos reales"""

    return minuendo - sustraendo


def multi(factor1, factor2):
    """Multiplicacion de dos reales"""

    return factor1 * factor2


def division(dividendo, divisor):
    """Division de dos reales"""

    try:
        return dividendo / divisor
    except ZeroDivisionError:
        sys.exit("\nERROR: Dividido por zero");


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("\nUsage: $ python calculadora.py" +
                 " funcion operando1 operando2")

    funcion = sys.argv[1]
    try:
        operando1 = float(sys.argv[2])
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("\nERROR: Algún número es incorrecto");
    
    if funcion == "sumar":
        resultado = suma(operando1,	operando2)
    elif funcion == "restar":
        resultado = resta(operando1, operando2)
    elif funcion == "multiplicar":
        resultado = multi(operando1, operando2)
    elif funcion == "dividir":
        resultado = division(operando1, operando2)
    else:
        sys.exit("\nLas operaciones validas son:" +
                 " sumar, restar, multiplicar y dividir")
    print "\nEl resultado es " + str(resultado)
