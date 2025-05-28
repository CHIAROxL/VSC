def main():
    import pubchempy as pcp
    from collections import Counter
    import math

    def pH_acido_forte(concentrazione_idronio):
        pH = -math.log10(concentrazione_idronio)
        return pH

    def pH_base_forte(concentrazione_idrossido):
        pH = 14 + math.log10(concentrazione_idrossido)
        return pH

    def pH_acido_debole(concentrazione_acido, Ka):
        pH = 0.5*-math.log10(Ka*concentrazione_acido)
        return pH

    def pH_base_debole(concentrazione_base, Kb):
        pH = 14 + 0.5*math.log10(Kb*concentrazione_base)
        return pH

    def pH_tampone_acido(concentrazione_acido, concentrazione_base, Ka):
        pH = -math.log10(Ka) - math.log10(concentrazione_acido/concentrazione_base)
        return pH

    def pH_tampone_basico(concentrazione_acido, concentrazione_base, Kb):
        pOH = -math.log10(Kb) - math.log10(concentrazione_base/concentrazione_acido)
        pH = 14 - pOH
        return pH

    def c_idronio_ac(concentrazione_sale_acido, Ka):
        concentrazione_idronio = math.sqrt(concentrazione_sale_acido*Ka)
        return concentrazione_idronio

    def c_idrossido_bc(concentrazione_sale_basico, Kb):
        concentrazione_idrossido = math.sqrt(concentrazione_sale_basico*Kb)
        return concentrazione_idrossido

    class if_non_soddisfatto(Exception):
        pass

    print("---")
    scelta = input("1 - acido forte\n2 - base forte\n3 - acido debole\n4 - base debole\n5 - titolazione\n---\n cosa scegli? ")
    print("---")
    scelta = scelta.lower()

    scelta_1 = ["1", "acido forte"]
    scelta_2 = ["2", "base forte"]
    scelta_3 = ["3", "acido debole"]
    scelta_4 = ["4", "base debole"]
    scelta_5 = ["5", "titolazione"]

    if scelta in scelta_1:
        dissociazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_acido = float(input("digita la concentrazione molare (separa i decimali con il punto): "))
        concentrazione_idronio = concentrazione_acido * dissociazioni
        pH = round(-math.log10(concentrazione_idronio), 2)
        print(pH)
        print("---")

    elif scelta in scelta_2:
        associazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_base = float(input("digita la concentrazione molare (separa i decimali con il punto): "))
        concentrazione_idrossido = concentrazione_base * associazioni
        pH = round(14 + math.log10(concentrazione_idrossido), 2)
        print(pH)
        print("---")

    
    elif scelta in scelta_3:
        dissociazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_acido = float(input("digita la concentrazione molare (separa i decimali con il punto): "))
        costante = input("hai la constante acida o basica? ")

        if costante != "acida" or "Acida" or "basica" or "Basica":
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
        
        if costante == "acida" or "Acida":
            Ka = float(input("inserisci la costante acida (es: 1.8e-5): "))
            concentrazione_idronio = math.sqrt(concentrazione_acido * Ka)
            pH = round(-math.log10(concentrazione_idronio), 2)
            print(pH)
            print("---")

        elif costante == "basica" or "Basica":
            Kb = float(input("inserisci la costante basica (es: 1.8e-5): "))
            concentrazione_idronio = math.sqrt(concentrazione_acido * ((10^-14) / Kb))
            pH = round(-math.log10(concentrazione_idronio), 2)
            print(pH)
            print("---")

        else:
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
        
    elif scelta in scelta_4:
        dissociazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_base = float(input("digita la concentrazione molare (separa i decimali con il punto): "))
        costante = input("hai la constante acida o basica? ")

        if costante != "acida" or "Acida" or "basica" or "Basica":
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
        
        if costante == "basica" or "Basica":
            Kb = float(input("inserisci la costante basica (es: 1.8e-5): "))
            concentrazione_idrossido = math.sqrt(concentrazione_base * Kb)
            pH = round(14 + math.log10(concentrazione_idrossido), 2)
            print(pH)
            print("---")

        elif costante == "acida" or "Acida":
            Ka = float(input("inserisci la costante acida (es: 1.8e-5): "))
            concentrazione_idrossido = math.sqrt(concentrazione_base * ((10^-14) / Ka))
            pH = round(14 + math.log10(concentrazione_idrossido), 2)
            print(pH)
            print("---")
            
        else:
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
        
    elif scelta in scelta_5:

        carattere_analita = str(input("l'analita è un acido o una base? "))
        potenza_analita = str(input("l'analita è forte o debole? "))
        concentrazione_analita = float(input("quant'è la normalità di analita (separa i decimali con il punto)? "))
        volume_analita = float(input("quant'è il volume di analita in litri (separa i decimali con il punto)? "))
        potenza_titolante = str(input("il titolante è forte o debole? "))
        concentrazione_titolante = float(input("quant'è la normalità del titolante (separa i decimali con il punto)? "))
        numero_titolanti = int(input("con quanti volumi vuoi titolare? "))

        carattere_analita = carattere_analita.lower()
        potenza_analita = potenza_analita.lower()
        potenza_titolante = potenza_titolante.lower()
        
        volumi_titolante = []
        for i in range(numero_titolanti):
            volumi_titolante.append(float(input("inserisci il #" + str(i+1) + " volume di titolante (separa i decimali con il punto): ")))

        
        if carattere_analita == "acido":

            
            if potenza_analita == "forte":

                
                if potenza_titolante == "forte":
                    moli_analita = concentrazione_analita*volume_analita

                    #analita acido forte, titolante base forte
                    for i in range(numero_titolanti):

                        moli_titolante = concentrazione_titolante*volumi_titolante[i]
                        moli_analita_residue = moli_analita-moli_titolante

                        if moli_analita_residue > 0:
                            concentrazione_analita = moli_analita_residue/(volume_analita + volumi_titolante[i])
                            pH = pH_acido_forte(concentrazione_analita)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        elif moli_analita_residue < 0:
                            concentrazione_base = -moli_analita_residue/(volume_analita + volumi_titolante[i])
                            pH = pH_base_forte(concentrazione_base)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        else:
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è 7")

                elif potenza_titolante == "debole":
                    moli_analita = concentrazione_analita*volume_analita

                    #analita acido forte, titolante base debole
                    Kb = float(input("quanto vale la Kb1 del titolante (es. 1.8e-5)? "))
                    Ka = 10e-14/Kb

                    for i in range(numero_titolanti):
                        moli_titolante = concentrazione_titolante*volumi_titolante[i]
                        moli_analita_residue = moli_analita-moli_titolante

                        if moli_analita_residue > 0:
                            concentrazione_acido = moli_analita_residue/(volume_analita + volumi_titolante[i])
                            concentrazione_sale_acido = moli_titolante/(volume_analita + volumi_titolante[i])
                            idronio_totale = concentrazione_acido + c_idronio_ac(concentrazione_sale_acido, Ka)
                            pH = pH_acido_forte(idronio_totale)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))
                            
                        elif moli_analita_residue < 0:
                            concentrazione_base = -moli_analita_residue/(volume_analita + volumi_titolante[i])
                            concentrazione_sale_acido = moli_analita/(volume_analita + volumi_titolante[i])
                            pH = pH_tampone_basico(concentrazione_sale_acido, concentrazione_base, Kb)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        else:
                            concentrazione_sale_acido = moli_analita/(volume_analita + volumi_titolante[i])
                            pH = pH_acido_debole(concentrazione_sale_acido, Ka)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

            elif potenza_analita == "debole":

                if potenza_titolante == "forte":
                    Ka = float(input("quanto vale la Ka1 dell'analita (es. 1.8e-5)? "))
                    Kb = 10e-14/Ka
                    moli_analita = concentrazione_analita*volume_analita

                    #analita acido debole, titolante base forte
                    for i in range(numero_titolanti):

                        moli_titolante = concentrazione_titolante*volumi_titolante[i]
                        moli_analita_residue = moli_analita-moli_titolante

                        if moli_analita_residue > 0:
                            concentrazione_acido = moli_analita_residue/(volume_analita + volumi_titolante[i])
                            concentrazione_sale_basico = moli_titolante/(volume_analita + volumi_titolante[i])
                            pH = pH_tampone_acido(concentrazione_acido, concentrazione_sale_basico, Ka)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        elif moli_analita_residue < 0:
                            concentrazione_base = -moli_analita_residue/(volume_analita + volumi_titolante[i])
                            concentrazione_sale_basico = moli_analita/(volume_analita + volumi_titolante[i])
                            concentrazione_idrossido = concentrazione_base + float(c_idrossido_bc(concentrazione_sale_basico, Kb))
                            pH = pH_base_forte(concentrazione_idrossido)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        else:
                            concentrazione_sale_basico = moli_analita/(volume_analita + volumi_titolante[i])
                            pH = pH_base_debole(concentrazione_sale_basico, Kb)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                elif potenza_titolante == "debole":

                    #analita acido debole, titolante basico debole
                    for i in range(numero_titolanti):

                        moli_titolante = concentrazione_titolante*volumi_titolante[i]
                        moli_analita_residue = moli_analita-moli_titolante

                        if moli_analita_residue > 0:
                            concentrazione_analita = moli_analita_residue/(volume_analita + volumi_titolante[i])
                            concentrazione_sale = moli_titolante/(volume_analita + volumi_titolante[i])
                            concentrazione_base_prodotta, concentrazione_acido_prodotto = concentrazione_sale
                            concentrazione_idronio = c_idronio_ac(concentrazione_acido_prodotto, Ka)
                            pH = pH_tampone_acido(concentrazione_analita + concentrazione_idronio, concentrazione_base_prodotta - concentrazione_idronio, Ka)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        elif moli_analita_residue < 0:
                            concentrazione_titolante = -moli_analita_residue/(volume_analita + volumi_titolante[i])
                            concentrazione_sale = moli_analita/(volume_analita + volumi_titolante[i])
                            concentrazione_base_prodotta, concentrazione_acido_prodotto = concentrazione_sale
                            concentrazione_idrossido = c_idrossido_bc(concentrazione_base_prodotta, Kb)
                            pH = pH_tampone_basico(concentrazione_acido_prodotto, concentrazione_titolante, Kb)
                            print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                        else:
                            concentrazione_sale = moli_analita/(volume_analita + volumi_titolante[i])
                            concentrazione_acido_prodotto, concentrazione_base_prodotta = concentrazione_sale
                            concentrazione_idronio = c_idronio_ac(concentrazione_acido_prodotto, Ka)
                            concentrazione_idrossido = c_idrossido_bc(concentrazione_base_prodotta, Kb)
                            idronio_rimanente = concentrazione_idronio - concentrazione_idrossido

                            if idronio_rimanente > 0:
                                pH = pH_acido_forte(idronio_rimanente)
                                print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))

                            elif idronio_rimanente < 0:
                                pH = pH_base_forte(-idronio_rimanente)
                                print("il pH con " + str(volumi_titolante[i]) + "L di titolante è " + str(round(pH, 1)))
                            
                            else:
                                print("il pH con " + str(volumi_titolante[i]) + "L di titolante è 7")

    else:
        raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
    
if __name__ == "__main__":
    main()