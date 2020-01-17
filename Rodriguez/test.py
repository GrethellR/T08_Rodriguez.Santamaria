from Rodriguez import libreria

assert (libreria.valida_Dni("7288342") == False)
assert (libreria.valida_Dni("12345") == False)
assert (libreria.valida_Dni("123456789") == False)
assert (libreria.valida_Dni("123456") == False)
assert (libreria.valida_Dni("12345678") == True)
print("valida_Dni OK")

assert (libreria.valida_Vocal("a") == True)
assert (libreria.valida_Vocal("r") == False)
assert (libreria.valida_Vocal("i") == True)
assert (libreria.valida_Vocal("u") == True)
assert (libreria.valida_Vocal("f") == False)
print("valida_Vocal OK")

assert (libreria.valida_NroPar(5) == False)
assert (libreria.valida_NroPar(4) == True)
assert (libreria.valida_NroPar(21) == False)
assert (libreria.valida_NroPar(20) == True)
assert (libreria.valida_NroPar(1) == False)
print("valida_NroPar OK")

assert (libreria.es_Moneda_valido("EUROS") == True)
assert (libreria.es_Moneda_valido("INTI") == False)
assert (libreria.es_Moneda_valido("REAL") == False)
assert (libreria.es_Moneda_valido("YEN") == False)
assert (libreria.es_Moneda_valido("SOLES") == True)
print("es_Moneda_valido OK")

assert (libreria.es_EstadoCivil_valido("SOLTERO") == True)
assert (libreria.es_EstadoCivil_valido("ENAMORADO") == False)
assert (libreria.es_EstadoCivil_valido("COMPROMETIDO") == False)
assert (libreria.es_EstadoCivil_valido("CASADO") == True)
assert (libreria.es_EstadoCivil_valido("VIUDO") == True)
print("es_EstadoCivil_valido OK")

assert (libreria.validamayorEdad(18) == True)
assert (libreria.validamayorEdad(30) == True)
assert (libreria.validamayorEdad(12) == False)
assert (libreria.validamayorEdad(76) == True)
assert (libreria.validamayorEdad(1) == False)
print("validamayorEdad OK")

assert (libreria.validaNroTelefono("984645040") == True)
assert (libreria.validaNroTelefono("984123") == False)
assert (libreria.validaNroTelefono("963875424") == True)
assert (libreria.validaNroTelefono("98464504032") == False)
assert (libreria.validaNroTelefono("984876635423") == False)
print("validaNroTelefono OK")

assert (libreria.validarAñoNacimiento(1958) == True)
assert (libreria.validarAñoNacimiento(1950) == True)
assert (libreria.validarAñoNacimiento(1935) == False)
assert (libreria.validarAñoNacimiento(1905) == False)
assert (libreria.validarAñoNacimiento(1998) == True)
print("validarAñoNacimiento OK")



