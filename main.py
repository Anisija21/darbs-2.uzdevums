import math 

def gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums) :
  telpas_izmers = math.ceil(telpas_garums) * math.ceil(telpas_platums)
  izmaksa = telpas_izmers / linoleja_platums

  return izmaksa

cena1 = 2.50
linoleja_platums1 = 3.0
platums1 = 5.50
garums1 = 6.0


print("izklājot garumā:")
print(gridas_izmaksa(cena1, linoleja_platums1, platums1, garums1))
print("izklājot platumā")
print(gridas_izmaksa(cena1, linoleja_platums1, garums1, platums1))
