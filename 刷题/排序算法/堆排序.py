##堆排序，将待排序的序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的跟节点。将其与末尾元素进行交换，此时末尾就是最大值
##然后将n-1个元素重新构成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列。

##堆排序
def heapSort(arr):
    if len(arr)<2:
        return
    for i in range(len(arr)):
        heapInsert(arr,i)
    size=len(arr)
    swap(arr,0,size-1)
    while size>0:
        heapify(arr,0,size)
        swap(arr,0,size-1)

def heapInsert(arr,index):

