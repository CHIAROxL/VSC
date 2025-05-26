def main():
    import pubchempy as pcp

    tipo = input("1 - CID\n2 - Formula bruta\n3 - Nome IUPAC\n4 - Sinonimo\ncome vuoi cercare il composto? ")

    tipo_1 = ["1", "CID", "Cid", "cid", "compound identifier",]
    if tipo in tipo_1:
        composto = pcp.Compound.from_cid(input("inserisci il CID del composto: "))
        print("nome IUPAC: \"" + composto.iupac_name + "\"")
        print("ecco i primi tre sinonimi secondo PubChem: " + str(composto.synonyms[:3]))
        print("la formula del composto è " + composto.molecular_formula)
        print("il peso molecolare del composto è di " + composto.molecular_weight + " g/mol")
        print("il composto ha carica " + str(composto.charge))

if __name__ == "__main__":
    main()