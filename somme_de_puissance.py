n= int(input("saissisez la naleur de n :"))
S= 0
for i in range(0,n+1) :
    S= S + 10**i 
    print("la somme de 1 a 10^",i,"=",format(S,".2f"))
    
