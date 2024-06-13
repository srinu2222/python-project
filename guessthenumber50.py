import random
def guess(j):
    num=random.randint(1,51)
    i=j
    while (i<=j):
        x=int(input("guess the number : "))
        if x<num:
            print("your guess is too low")
            i-=1
            print("left u have",i," chances")
        elif x>num:
            print("your guess is too high")
            i-=1
            print("left u have",i," chances")
        elif x==num:
            print("your guess is correct")
            print("left u have",i,"chances")
            break
        if i==0:
            print("loose")
            break
opinion=input("choose your level in hard or easy : ")
if opinion=="hard":
    print("u have 5 chances only.....")
    guess(5)
elif opinion=="easy":
    print("u have 10 chances....")
    guess(10)

        
        
            
