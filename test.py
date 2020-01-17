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


