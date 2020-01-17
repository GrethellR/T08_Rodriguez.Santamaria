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


