print("Hvor meget vejer dit brev i kg?")

brevvægt = input()

if float(brevvægt) <= 0.05 :
    print("Dit brev koster 12 DKK at sende i Danmark")
elif float(brevvægt) <= 1 :
    print("Dit brev koster 50 DKK at sende i Danmark")
elif float(brevvægt) <= 2 :
    print("Dit brev koster 60 DKK at sende i Danmark")
elif float(brevvægt) > 2 :
    print("Det er en pakke og kan derfor ikke sendes med brev. Det er en pakke")