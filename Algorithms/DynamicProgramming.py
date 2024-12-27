# Longest Common Subsequence, 0-1 Knapsack

    
# 1) Longest Common Subsequence

def LCS_recursion(a:str,b:str) -> int :

    if(len(a)==0 or len(b)==0):
        return 0
    
    if(a[0]==b[0]):
        return 1+LCS_recursion(a[1:],b[1:])

    return max(LCS_recursion(a[1:],b),LCS_recursion(a,b[1:]))

def LCS_memoisation(a:str,b:str,m:int,n:int, memo:list[list[int]]) -> int :

    if(m==0 or n==0):
        memo[m][n]=0
    if(memo[m][n]!=-1):
        return memo[m][n]
    elif(a[m-1]==b[n-1]):
        memo[m][n]=1+LCS_memoisation(a,b,m-1,n-1,memo)
    else:
        memo[m][n]=max(LCS_memoisation(a,b,m-1,n,memo),LCS_memoisation(a,b,m,n-1,memo))

    return memo[m][n]

def LCS_dp(a:str,b:str) -> int:


    m=len(a)
    n=len(b)
    dp=[[0 for i in range (n+1)] for j in range (m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(a[i-1]==b[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[m][n]

def LCS(a:str , b:str) -> None:

    m=len(a)
    n=len(b)

    memo =[]
    for _ in range(m+1):
        ele = []
        for i in range(n+1):
            ele.append(-1)
        memo.append(ele)

    R = LCS_recursion(a,b)
    M = LCS_memoisation(a,b,m,n,memo)
    D = LCS_dp(a,b)

    print(f"LCS : ({R},{M},{D})")

LCS("adcbfgsbd","axcydbacb") # adcb


# 2) Knapsack

def Knapsack_recursion(weight:list[int],profit:list[int],capacity:int,idx:int) -> int:

    if(idx>=len(profit)):
        return 0
    include=0
    if(weight[idx]<=capacity):
        include=Knapsack_recursion(weight,profit,capacity-weight[idx],idx+1)+profit[idx]

    not_include=Knapsack_recursion(weight,profit,capacity,idx+1)

    return max(include,not_include)

def Knapsack_memoisation(weight:list[int], profit:list[int] , capacity:int ,idx:int, memo: list[list[int]]) -> int:

    if(idx>=len(profit)):
        return 0
    if(memo[idx][capacity]!=-1):
        return memo[idx][capacity]

    include=0
    if(weight[idx]<=capacity):
        include=Knapsack_recursion(weight,profit,capacity-weight[idx],idx+1)+profit[idx]

    not_include=Knapsack_recursion(weight,profit,capacity,idx+1)
        
    memo[idx][capacity]=max(include,not_include)

    return memo[idx][capacity]


def Knapsack_dp(weight:list[int],profit:list[int],capacity:int) -> int:

    n=len(weight)
    dp = [[0 for j in range(capacity+1)] for i in range(n+1)]
    
    for idx in range(1,n+1):
        for cap in range(1,capacity+1):
            dp[idx][cap]=dp[idx-1][cap]
            if(weight[idx-1]<=cap):
                dp[idx][cap]=max(dp[idx][cap],profit[idx-1]+dp[idx-1][cap-weight[idx-1]])

    return dp[n][capacity]

def Knapsack(weight:list[int],profit:list[int],capacity:int) -> None :

    assert len(profit)==len(weight) , "Length of profit and weight are different"
    
    memo = [ [-1 for j in range(capacity+1)] for i in range(len(weight))]

    R = Knapsack_recursion(weight,profit,capacity,0)
    M = Knapsack_memoisation(weight,profit,capacity,0,memo)
    D = Knapsack_dp(weight,profit,capacity)

    print(f"Knapsack : ({R},{M},{D})")





weight=[4,5,1,3,2,5]
profit=[2,3,1,5,4,7]
capacity=15

Knapsack(weight,profit,capacity) # 19 


weight=[23,31,29,44,53,38,63,85,89,82]
profit=[92,57,49,68,60,43,67,84,87,72]
capacity=165

Knapsack(weight,profit,capacity) # 109


    

