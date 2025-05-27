def main():
    import pubchempy as pcp

    tipo = input("1 - CID\n2 - Formula\n3 - Nome\ncome vuoi cercare il composto? ")
    print("---")
    tipo = tipo.lower()

    tipo_1 = ["1", "cid", "compound identifier"]
    tipo_2 = ["2", "formula"]
    tipo_3 = ["3", "nome"]

    if tipo in tipo_1:
        composto = pcp.Compound.from_cid(input("inserisci il CID del composto: "))
        print("---")
        print("nome: \"" + composto.iupac_name + "\"")
        print("ecco i primi tre sinonimi secondo PubChem: " + str(composto.synonyms[:3]))
        print("la formula del composto è " + composto.molecular_formula)
        print("il peso molecolare del composto è di " + composto.molecular_weight + " g/mol")
        print("il composto ha carica " + str(composto.charge))
        print("---")

    elif tipo in tipo_2:
        composto = pcp.get_compounds(input("inserisci la formula: "), "formula")[0]
        print("---")
        print("nome: \"" + composto.iupac_name + "\"")
        print("ecco i primi tre sinonimi secondo PubChem: " + str(composto.synonyms[:3]))
        print(f"il CID del composto è {composto.cid}")
        print("il peso molecolare del composto è di " + composto.molecular_weight + " g/mol")
        print("il composto ha carica " + str(composto.charge))
        print("---")
    
    elif tipo in tipo_3:
        composto = pcp.get_compounds(input("inserisci nome: "), "name")[0]
        print("---")
        print("ecco i primi tre sinonimi secondo PubChem: " + str(composto.synonyms[:3]))
        print(f"il CID del composto è {composto.cid}")
        print("la formula del composto è " + composto.molecular_formula)
        print("il peso molecolare del composto è di " + composto.molecular_weight + " g/mol")
        print("il composto ha carica " + str(composto.charge))
        print("---")

    else:
        print(f"\"{tipo}\" non è un valore adeguato, riprova.")
        main()

if __name__ == "__main__":
    main()