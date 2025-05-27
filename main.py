def main():
    import pH, info

    scelta = input("1 - informazioni di un composto\n2 - calcoli del pH\ncosa vuoi fare? ")
    print("---")
    scelta = scelta.lower()
    scelta_1 = ["1", "informazioni", "informazioni di un composto"]
    scelta_2 = ["2", "ph", "calcoli del ph"]
    if scelta in scelta_1:
        info.main()
    elif scelta in scelta_2:
        pH.main()

if __name__ == "__main__":
    main()
    