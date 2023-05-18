def partition(a,pivot_index,end):
    swapindex=pivot_index
    
    for i in range (pivot_index+1, end):
        if a[i] < a[pivot_index]:
            swapindex+=1
            (a[i],a[swapindex])=(a[swapindex],a[i])
        
        (a[pivot_index],a[swapindex])=(a[swapindex],a[pivot_index])
    return swapindex
    
def quicksort(a,l,h):
    if (l<h):
        pivot_index=partition(a,l,h)
        quicksort(a,l,pivot_index-1)
        quicksort(a,pivot_index+1,h)
    return a
    

a=[3,5,7,89,13,64,3]
end=len(a)
print(quicksort(a,0,end))
