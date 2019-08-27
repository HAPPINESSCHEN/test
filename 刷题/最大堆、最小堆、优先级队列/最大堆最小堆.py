##牛客 数据流中的中位数
##往堆中插入一个数据的时间效率是O（logn），得到堆顶数据的时间复杂度为O（1）。
import heapq
class Solution:
    def __init__(self):
        self.left=[] ##最大堆存储最大值
        self.right=[]##最小堆存储最小值
    def Insert(self, num):
        # write code here
        if len(self.right)>0 and num<self.right[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        while len(self.right)-len(self.left)>1:
            heapq.heappush(self.left,-heapq.heappop(self.right))
        while len(self.left)-len(self.right)>1:
            heapq.heappush(self.right,-heapq.heappop(self.left))
    def GetMedian(self,x=1.2):
        # write code here
        if len(self.left)>len(self.right):
            return -self.left[0]
        elif len(self.left)<len(self.right):
            return self.right[0]
        else:
            return (self.right[0]-self.left[0])/2.0
13940556825
#使用heapq实现小顶堆（TOPK大），大顶堆（btmK小）
import heapq
import random
class TopkHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []
    def Push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)

        def TopK(self):
            return [x for x in reversed([heapq.heappop(self.data) for _ in range(len(self.data))])]
if __name__ == "__main__":
    list_rand = random.sample(range(1000000), 100)
    th = TopkHeap(3)
    for i in list_rand:
        th.Push(i)
    sorted(list_rand, reverse=True)[0:3]

#给出N长的序列，求出BtmK小的元素，即使用大顶堆
##将push(e)改为push(-e)、pop(e)改为-pop(e)。
##也就是说，在存入堆、从堆中取出的时候，都用相反数，而其他逻辑与TopK完全相同，看代码：

class BtmkHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def Push(self, elem):
     # Reverse elem to convert to max-heap
        elem = -elem
        # Using heap algorighem
        if len(self.data) < self.k:
             heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)##删除现有元素并将其替换为一个新值。

    def BtmK(self):
        return sorted([-x for x in self.data])
###经过测试，是完全没有问题的，这思路太Trick了……
####可以用heapq.nlargest(n, iterable) 和 heapq.nsmallest(n, iterable)返回列表中的n个最大值和最小值
data = range(1,6)
l = heapq.nlargest(3, data)
print (l )    # [5, 4, 3]

s = heapq.nsmallest(3, data)
print (s)     # [1, 2, 3]

##其他函数heapq.heapify(list);将list类型转化为heap, 在线性时间内, 重新排列列表。
heapq.heapify(data)

##参考链接：1.https://www.jb51.net/article/87552.htm
# 2.https://www.cnblogs.com/lexus/p/3325000.html


#其实在上面也说到 sorted 方法，这个方法其实就是在调用对象的 __cmp__ 方法，
# 好么我可以单独定义一个带有 __cmp__ 方法的对象则可以实现优先队列中的对象排序。
#coding:gbk
import heapq

# 使用heapq实现优先队列
#定义一个可比较对象
class CompareAble:
    def __init__(self,priority,jobname):
        self.priority = priority
        self.jobname = jobname

    def __cmp__(self, other):
        if self.priority < other.priority:
            return -1
        elif self.priority == other.priority:
            return 0
        else:
            return 1
    ##python3没有cmp方法，需要在上面定义一个 __lt__ 方法
    # def __lt__(self, other):
    #     if self.priority <= other.priority:
    #         return False
    #     else:
    #         return True


joblist = []

heapq.heappush(joblist,CompareAble(80,'eat'))
heapq.heappush(joblist,CompareAble(70,'a write plan2'))
heapq.heappush(joblist,CompareAble(70,'write plan'))
heapq.heappush(joblist,CompareAble(90,'sleep'))
heapq.heappush(joblist,CompareAble(100,'write code'))

while joblist:
    task = heapq.heappop(joblist)
    print(task.priority,task.jobname)