print("Hvor mange DKK vil du væksle til dollars?")

penge = input() # spørg om mængde af penge

if int(penge) <= 5 :
    print("Så får du " + str(int(penge) / 7.44 - 0.5) + " dollar tilbage efter kommision")
else :
    print("så får du " + str(int(penge) / 7.44 * 0.98) + " dollar tilbage efter kommision")
