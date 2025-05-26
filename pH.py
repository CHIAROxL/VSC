def main():
    import pubchempy as pcp # type: ignore
    from collections import Counter
    import math


    class if_non_soddisfatto(Exception):
        pass

    scelta = input("digita \"A\" per un acido forte, \"B\" per una base forte, " \
    "a\" per un acido debole, \"b\" per una base debole : ")

    if scelta == "A":
        dissociazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_acido = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
        concentrazione_idronio = concentrazione_acido * dissociazioni
        pH = round(-math.log10(concentrazione_idronio), 2)
        print(pH)
    elif scelta == "B":
        associazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_base = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
        concentrazione_idrossido = concentrazione_base * associazioni
        pH = round(14 + math.log10(concentrazione_idrossido), 2)
        print(pH)
    elif scelta == "a":
        dissociazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_acido = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
        costante = input("hai la constante acida o basica? ")
        if costante != "acida" or "Acida" or "basica" or "Basica":
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
        if costante == "acida" or "Acida":
            costante_acida = float(input("inserisci la costante acida (es: 1.8e-5): "))
            concentrazione_idronio = math.sqrt(concentrazione_acido * costante_acida)
            pH = round(-math.log10(concentrazione_idronio), 2)
            print(pH)
        elif costante == "basica" or "Basica":
            costante_basica = float(input("inserisci la costante basica (es: 1.8e-5): "))
            concentrazione_idronio = math.sqrt(concentrazione_acido * ((10^-14) / costante_basica))
            pH = round(-math.log10(concentrazione_idronio), 2)
            print(pH)
        else:
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
    elif scelta == "b":
        dissociazioni = int(input("quanto vale \"Z\"? "))
        concentrazione_base = float(input("digita la concentrazione molare (separando i decimali con il punto): "))
        costante = input("hai la constante acida o basica? ")
        if costante != "acida" or "Acida" or "basica" or "Basica":
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
        if costante == "basica" or "Basica":
            costante_basica = float(input("inserisci la costante basica (es: 1.8e-5): "))
            concentrazione_idrossido = math.sqrt(concentrazione_base * costante_basica)
            pH = round(14 + math.log10(concentrazione_idrossido), 2)
            print(pH)
        elif costante == "acida" or "Acida":
            costante_acida = float(input("inserisci la costante acida (es: 1.8e-5): "))
            concentrazione_idrossido = math.sqrt(concentrazione_base * ((10^-14) / costante_acida))
            pH = round(14 + math.log10(concentrazione_idrossido), 2)
            print(pH)
        else:
            raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
    else:
        raise if_non_soddisfatto("la condizione non è stata soddisfatta; interruzione del programma")
    
if __name__ == "__main__":
    main()