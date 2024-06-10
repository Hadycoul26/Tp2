while  True :
    print("------CALUCULATRICE:Menu:-----")
    print("1 -addition.")
    print("2 -Soustraction.")
    print("3 -multiplication.")
    print("4 -Division.")
    print("5 -reste d'unr division entiere.")
    print("6 -puissance.")
    O= int(input("quel calcul veux tu effectuer :"))
    if O== 1 :
        a= float(input("saisir le premier terme :"))
        b= float(input("saisir le deuxieme terme :"))
        S= a + b
        print("le resultat est :",S)
    elif O== 2 :
        a= float(input("saisir le premier terme :"))
        b= float(input("saisir le deuxieme terme :"))
        S= a - b
        print("le resultat est :",S)
    elif O== 3 :
        a= float(input("saisir le premier terme :"))
        b= float(input("saisir le deuxieme terme :"))
        S= a * b
        print("le resultat est :",S)
    elif O== 4 :
        a= float(input("saisir le premier terme :"))
        b= float(input("saisir le deuxieme terme :"))
        if b != 0 :
           S= a / b
           print("le resultat est :",S)
        else :
            print("la division de 0 est non defini")
    elif O== 5 :
        a= int(input("saisir le premier terme :"))
        b= int(input("saisir le deuxieme terme :"))
        S= a%b
        print("le resultat est :",S)
    elif O== 6 :
        a= float(input("saisir le premier terme :"))
        b= float(input("saisir le deuxieme terme :"))
        S= a**b
        print("le resultat est :",S)                
    else :
        print("le resultat est incorrect")
    reponse = input("veux tu faire un aotre calcul (O/N) : ")
    if reponse == "N" :
        break   
               
        
