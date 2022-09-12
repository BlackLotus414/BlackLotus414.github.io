print("Hvor mange DKK vil du væksle til dollars?")

penge = input() # spørg om mængde af penge

if int(penge) <= 5 :
    print("No can do, det er for lidt")
else :
    print("så får du " + str(int(penge) / 7.44 * 0.98) + " dollar tilbage efter kommision")
