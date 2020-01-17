#Ejercicio 1

def valida_Dni(strDNI):
    #1.strDNI es una cadena de 8 caracteres
    #2.la longitud debe ser de 8
    if(len(strDNI))!= 8:
        return False
    else:
        return True
#fin_valida_Dni

#Ejercicio 2

def valida_Vocal(strVocal):
    #1.strVocal es un caracter
    #2.Se validara si es vocal
    if(strVocal=='a' or strVocal== 'e' or strVocal=='i' or strVocal=='o' or strVocal=='u' ):
        return True
    else:
        return False
#fin_valida_Vocal

#Ejercicio 3

def valida_NroPar(Par):
    #1.strPar es un numero
    #2.Se validara solo si es un numero par

    if(Par%2==0):
        return True
    else:
        return False
#fin_valida_NroPar

#Ejercicio 4

def es_Moneda_valido(strMoneda):
    #1. Convertir strMoneda es Mayuscula
    #2. Convertir si moneda es igual a EUROS SOLES DOLARES
       #retornar True
       #caso contrario False

    strMoneda= strMoneda.upper()
    if (strMoneda == "EUROS" or strMoneda=="SOLES" or strMoneda=="DOLARES"):
        return True
    else:
        return False
#fin_es_Moneda_valido


