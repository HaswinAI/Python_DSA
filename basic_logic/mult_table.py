def multiplication_table(n,i=1):
    
    #recursive
    if (i == 11):
        return
    print(n,"*",i,"=",n*i)
    i+=1
    multiplication_table(n,i)
    
    #for i in range(1,11):
     #   print("%d * %d = %d" %(n,i,n*1))

if __name__=="__main__":
    n=9
    multiplication_table(n)