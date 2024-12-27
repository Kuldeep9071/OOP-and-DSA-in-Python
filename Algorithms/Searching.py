def Linear_Search(lst,target):
    """Linear Search on list of numbers"""
    
    n=len(lst)
    for i in range(n):
        if(lst[i]==target):
            return i
    return -1 # Not Found
    
def Binary_Search(lst,target):
    """Binary Search on non decreasing list of numbers"""
    
    l=0
    r=len(lst)-1
    while(l<=r):
        m=l+(r-l)//2
        if(lst[m]==target):
            return m
        elif(lst[m]<target):
            l=m+1
        else:
            r=m-1
    return -1 # Not Found




lst = [1,4,6,6,7]
print(Linear_Search(lst,6))
print(Binary_Search(lst,6))
