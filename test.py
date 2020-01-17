import libreria

assert (libreria.valida_Dni("7288342")== False)
assert (libreria.valida_Dni("12345")== False)
assert (libreria.valida_Dni("123456789")== False)
assert (libreria.valida_Dni("123456")== False)
assert (libreria.valida_Dni("12345678")== True)
print("valida_Dni OK")

assert (libreria.valida_Vocal("a")== True)
assert (libreria.valida_Vocal("r")== False)
assert (libreria.valida_Vocal("i")== True)
assert (libreria.valida_Vocal("u")== True)
assert (libreria.valida_Vocal("f")== False)
print("valida_Vocal OK")

assert (libreria.valida_NroPar(5)== False)
assert (libreria.valida_NroPar(4)== True)
assert (libreria.valida_NroPar(21)== False)
assert (libreria.valida_NroPar(20)== True)
assert (libreria.valida_NroPar(1)== False)
print("valida_NroPar OK")
