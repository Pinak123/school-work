num=int(input("enter the amounth :-"))
def minimum_coins(N):
    coins=[1000,500,100,50,20,10,5,2,1]
    count=0
    num=N
    length=len(coins)
    i=0
    while i<length:
            if coins[i]<=num:
                num=num-coins[i]
                count+=1
            else:
                i+=1
    return count
print ("Minimum coins required is %d"%minimum_coins(num))

        
   
