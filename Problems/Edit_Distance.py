""" Problem Statement:
    Given two strings A,B find the minimum number of steps to convert A into B using following 3 steps

    1) Insert a charactor
    2) Delete a charactor
    3) Replace a charctor

"""

def Edit_distance_recursion(A:str, B:str, m:int, n:int) -> int:

    if(m<=0):
        return n
    elif(n<=0):
        return m

    if(A[m-1]==B[n-1]):
        return Edit_distance_recursion(A,B,m-1,n-1)
    else:
        p=Edit_distance_recursion(A,B,m-1,n) # delete
        q=Edit_distance_recursion(A,B,m,n-1) # insert
        r=Edit_distance_recursion(A,B,m-1,n-1) # replace
        
        return 1+min(p,q,r)


def Edit_distance_memoisation(A:str, B:str, m:int, n:int, memo:list[list[int]]) -> int:

    if(m<=0):
        return n
    elif(n<=0):
        return m

    if(memo[m][n]!=-1):
        return memo[m][n]

    if(A[m-1]==B[n-1]):
        memo[m][n]=Edit_distance_recursion(A,B,m-1,n-1)
    else:
        p=Edit_distance_memoisation(A,B,m-1,n,memo) # delete
        q=Edit_distance_memoisation(A,B,m,n-1,memo) # insert
        r=Edit_distance_memoisation(A,B,m-1,n-1,memo) # replace
    
        memo[m[n]]=1+min(p,q,r)

    return memo[m][n]


def Edit_distance_dp(A:str, B:str) -> int:

    m=len(A)
    n=len(B)

    dp= [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j
    
    for i in range(m):
        for j in range(n):
            if(A[i]==B[j]):
                dp[i+1][j+1]=dp[i][j]
            else:
                p=dp[i+1][j] # delete
                q=dp[i][j+1] # insert
                r=dp[i][j] # replace

                dp[i+1][j+1]=1+min(p,q,r)

    return dp[m][n]

def Edit_distance(A:str, B:str) -> int:
    
    m=len(A)
    n=len(B)
    # No Need to call all functions just for practive i did this
    memo= [[-1]*(n+1) for _ in range(m+1)]
    x=Edit_distance_recursion(A,B,m,n)
    y=Edit_distance_memoisation(A,B,m,n,memo)
    z=Edit_distance_dp(A,B)
    
    assert x==y and y==z , f"1 of Edit distance implementation is wrong {(x,y,z)}"

    return x
    
    

A="intention"
B="execution"

print(Edit_distance(A,B))
