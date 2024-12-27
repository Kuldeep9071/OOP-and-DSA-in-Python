""" Problem Statement : 
 You are given an array of non negative numbers find a sub array with sum equals to given array
 """

# BruteForce Method

def Subarray_with_given_sum1(arr : list[int], target : int) -> list[int]:
    """Time Complexity : O(n^2)
       Space Complexity : O(1)
    """

    n=len(arr)

    for i in range(n):
        for j in range(i+1,n+1):
            if(sum(arr[i:j])==target):
                return arr[i:j]

    return []


# BruteForce Method with a bit better

def Subarray_with_given_sum2(arr : list[int], target : int) -> list[int]:
    """Time Complexity : O(n^2)
       Space Complexity : O(1)
    """

    n=len(arr)
    if(n==0 or target<=0):
        return []

    for i in range(n):
        sum=arr[i];
        for j in range(i+1,n+1):
            if(sum==target):
                return arr[i:j]
            elif(sum<target):
                sum+=arr[j]
            else:
                break

    return []



# Optimised Method

def Subarray_with_given_sum3(arr : list[int], target : int) -> list[int]:
    """Time Complexity : O(n)
       Space Complexity : O(1)
    """
    if(len(arr)==0 or target<=0):
        return []

    i=0
    j=1
    n=len(arr)
    sum=arr[0]
    while(j<=n):
        if(sum<target):
            if(j>=n):
                return []
            sum+=arr[j]
            j+=1            
        elif(sum>target):
            sum-=arr[i]
            i+=1
        else:
            return arr[i:j]

    return []

arr = [1,7,4,2,1,3,11,5]

print(Subarray_with_given_sum1(arr,19))
print(Subarray_with_given_sum2(arr,19))
print(Subarray_with_given_sum3(arr,19))
