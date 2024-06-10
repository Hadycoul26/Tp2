n= int(input("entrez un putain de nombre :"))
while n<=0 :
    n= int(input("entrez un putain de nombre :"))
print("les divisuer de",n,"sont {" )
for i in range(1,n+1) :
    if n % i ==0 :
        print(i,end=" ")
        
    
      
    
