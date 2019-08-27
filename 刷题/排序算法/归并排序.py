##归并排序是将两个（或以上）有序表合并成一个新的有序表，即将待排序序列分为
##若干个子序列，每个子序列是有序的。然后再把有序子序列合并为整体有序序列

#实现
def mergeSort(arr):
    if len(arr)<2:
        return
    helpmergeSort(arr,0,len(arr)-1)

def helpmergeSort(arr,l,r):
    if l==r:
        return
    mid=(l+r)//2
    helpmergeSort(arr,l,mid)
    helpmergeSort(arr,mid+1,r)
    helpmerge(arr,l,mid,r)

def helpmerge(arr,l,m,r):
    #申请一个额外的空间
    help1=[]
    i=0
    p1=l
    p2=m+1
    while p1<=m and p2<=r:
        if arr[p1]>arr[p2]:
            help1.append(arr[p2])
            p2+=1
        else:
            help1.append(arr[p1])
            p1+=1
    if p1<=m:
        help1=help1+arr[p1:m+1]

    if p2<=r:
        help1=help1+arr[p2:r+1]

    for i in range(len(help1)):
        arr[l+i]=help1[i]

arr=[2,4,5,1,2,34,5,7,6,4]
print(mergeSort(arr),arr)



