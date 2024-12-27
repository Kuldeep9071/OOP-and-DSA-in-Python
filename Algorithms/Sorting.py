# Bubble Sort

def bubble_sort(lst):
    """Time Complexity : O(n^2)
       Space Complexity : O(1)
    """

    i=len(lst)-1
    while(i>=0):
        for j in range(i):
            if(lst[j]>lst[j+1]):
                lst[j+1],lst[j]=lst[j],lst[j+1]
        i-=1

    return lst

# Insertion Sort

def insertion_sort(lst):
    """Time Complexity : O(n^2)
       Space Complexity : O(1)
    """

    for i in range(len(lst)):
        j=i-1;
        while(j>=0 and lst[j]>=lst[i]): 
            j-=1

        if(j>=0): 
            lst[i],lst[j],lst[j],lst[i]

    return lst

# Merge Sort

def Helper(lst,left,right):
    if(left>right):
        return []
    elif(left==right):
        return [lst[left]]

    mid=left+(right-left)//2

    L=Helper(lst,left,mid)
    R=Helper(lst,mid+1,right)
    
    i=0
    j=0
    
    arr=[]

    while(i<=mid-left and j<right-mid):
        if(L[i]<R[j]):
            arr.append(L[i])
            i+=1
        else:
            arr.append(R[j])
            j+=1
    while(i<=mid-left):
        arr.append(L[i])
        i+=1
    while(j<right-mid):
        arr.append(R[j])
        j+=1

    return arr

    

def merge_sort(lst):
    """Time Complexity : O(nlogn)
       Space Complexity : O(n)
    """
    return Helper(lst,0,len(lst)-1)

# Quick Sort

def Helper1(lst,left,right):
    if(left>right): return

    piv=left
    i=left+1

    while(i<=right):
        if(lst[i]<lst[piv]):
            piv+=1
        i+=1
    lst[left],lst[piv],lst[piv],lst[left]

    Helper(lst,left,piv-1)
    Helper(lst,piv+1,right)


def quick_sort(lst):
    """Time Complexity : O(n^2) in Worst case but nlogn on Average
       Space Complexity : O(1)
    """
    Helper1(lst,0,len(lst)-1)
    return lst


lst = [5,6,2,3,4,2,1,10,7,5,-9,2,1,17,-5]
print("Bubble: ",bubble_sort(lst))
print("Insertion: ",insertion_sort(lst))
print("Merge: ",merge_sort(lst))
print("Quick: ",quick_sort(lst))



# Custom Sorting Compare Functions

# return on which side of "b" you want "a" to be

def comp(a,b):
    """Comarision function for Decreasing order"""
    if(a>b):
        return 'lesser'
    elif(a==b):
        return 'equal'
    else:
        return 'greater'



