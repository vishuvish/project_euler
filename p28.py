T=int(input())
for i in range(T):
    n=int(input())
    sum1=(n*(n+1)*(2*n+1))//3
    sum2=((n-1)*(n-1))//2
    sum=sum1-sum2-1
    print(sum%1000000007)  
