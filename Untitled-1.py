import pubchempy as pcp # type: ignore
from collections import Counter
import math

#serve a trovare il cid, cioè il codice dell aspirina dal nome
#sostanza1 = pcp.get_compounds("H2SO4", 'formula')
#print(sostanza1[0].cid)

#dal cid al nome IUPAC
#sostanza2 = pcp.Compound.from_cid(sostanza1)

#print(sostanza2.iupac_name)

#ti butta il primo sinonimo, in genere il nome comune
#print(sostanza2.synonyms[0])

#ti butta il seconodo sinonimo
#print(sostanza2.synonyms[1])

#print(sostanza2.molecular_formula) #stampa la formula molecolare
#print(sostanza2.molecular_weight) #stampa il peso molecolare
#print(sostanza2.charge) #stampa la carica
#print(sostanza2.elements) # stampa tutti gli elementi
#print(list(set(sostanza2.elements))) #stampa tutti gli elementi una sola volta
#print(dict(Counter(sostanza2.elements))) #stampa le quantità di ogni elemento
#print(sostanza2._atoms) #stampa le quantità di ogni elemento e le posizioni
composto = pcp.get_properties("HCl", "cid")
'''
scelta = input("digita \"A\" per un acido forte, \"B\" per una base forte, " \
"a\" per un acido debole, \"b\" per una base debole : ")

if scelta == "A":
    dissociazioni = int(input("quanto vale \"Z\"?"))
    concentrazione_acido = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
    concentrazione_idronio = concentrazione_acido * dissociazioni
    pH = round(-math.log10(concentrazione_idronio), 2)
    print(pH)
elif scelta == "B":
    associazioni = int(input("quanto vale \"Z\"?"))
    concentrazione_base = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
    concentrazione_idrossido = concentrazione_base * associazioni
    pH = round(14 + math.log10(concentrazione_idrossido), 2)
    print(pH)
elif scelta == "a":
    dissociazioni = int(input("quanto vale \"Z\"?"))
    concentrazione_acido = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
    composto = pcp.get_properties("HCl", "cid")
'''
pippo