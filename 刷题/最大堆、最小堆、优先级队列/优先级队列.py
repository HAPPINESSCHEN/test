###leecode23;合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
#输出: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from Queue import PriorityQueue  ##Python2

##python2
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         head = point = ListNode(0)
#         q = PriorityQueue()
#         for l in lists:
#             if l:##每个列表元素是一个链表头指针
#                 q.put((l.val, l))
#         while not q.empty():
#             val, node = q.get()
#             point.next = node
#             point = point.next
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#         return head.next


##python不允许插入优先级相同的值或者是无法判断优先级的值到优先队列。所以插入的时候加入一个index,就不会出现优先级相同的情况了。
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for index,l in enumerate(lists):
            if l:
                q.put((l.val,index,l))
        while not q.empty():
            val,index,node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,index, node))
        return head.next

    # coding:gbk
    import heapq
    from queue import Queue, PriorityQueue

    # 使用heapq实现优先队列
    # 定义一个可比较对象
    #############重点
    class CompareAble:
        def __init__(self, priority, jobname):
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

    pq = PriorityQueue()
    pq.put(CompareAble(80, 'eat'))
    pq.put(CompareAble(70, 'a write plan2'))
    pq.put(CompareAble(70, 'write plan'))
    pq.put(CompareAble(90, 'sleep'))
    pq.put(CompareAble(100, 'write code'))

    while pq.qsize() != 0:
        task = pq.get_nowait()
        print(task.jobname, task.priority)