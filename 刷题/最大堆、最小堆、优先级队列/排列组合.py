##permutations全排列，与内容无关，只与索引有关。所以与数学上的全排列有差别！！！使用时可能需要筛选！
##combinations是组合，同样是依据索引的
from itertools import permutations
test_data = [1,1,1]
res=[]
for i in permutations(test_data,len(test_data)):
     print(''.join(str(s)for s in i))
print(res)

##牛客网：把数组排成最小的数
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        l = len(numbers)
        if l == 0:
            return ""
        for i in range(0,l):
            numbers[i] = str(numbers[i])
        numbers.sort(self.cmp1)
        return "".join(numbers)
    def cmp1(self,e1,e2):
        s1 =e1+e2
        s2 = e2 + e1
        return cmp(s1,s2)##cmp是python2中的,python3不支持


##解决办法：functools底下有个cmp_to_key可以代替cmp 写作key=cmp_to_key(f)
import sys
from functools import cmp_to_key
def cmp_new(x,y):
    if (x+y)>(y+x):
        return 1
    elif (x+y)<(y+x):
        return -1
    else :
        return 0
s=[1,2,3,4,5,6]
for i in range(0, len(s)):
    s[i] = str(s[i])
s.sort(key=cmp_to_key(cmp_new),reverse=True)
print(''.join(str(i) for i in s).lstrip("0"))