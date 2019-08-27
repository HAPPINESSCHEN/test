##二叉树算法的设计总路线：明确一个节点要做的事情，然后剩下的事抛给框架
def traverse (root):
    ##root需要做什么？在这做
    ##其他的不用root操心，抛给框架
    traverse(root.left)
    traverse(root.right)

##For example
##如何把二叉树所有节点中的值加1:？
def plusOne(root):
    if not root:
        return
    root.val+=1
    plusOne(root.left)
    plusOne(root.right)

##如何判断两颗二叉树是否相同？
def isSameTree(root1,root2):
    if root1==None and root2==None:
        return True
    if not root1 or not root2:
        return False
    if root1.val !=root2.val:
        return False
    return isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)
##在BTS中查找一个数是否存在
#版本1
def isInBTS(root,target):
    if not root:
        return False
    if root.val==target:
        return True
    return isInBTS(root.left,target) or isInBTS(root.right,target)
##版本2
##充分利用二叉搜索树的“左小右大"的特性
##我们不需要递归的搜索两边，类似二分查找思想，可以根据target和root.val的大小比较，就能排除一边。

def isInBTS2(root,target):
    if not root:
        return False
    if root.val < target:
        return True
    if root.val>target:
        return isInBTS2(root.left, target)
    if root.val<target:
        return isInBTS2(root.right,target)

##在BTS中插入一个数
#一旦涉及「改」，函数就要返回 TreeNode 类型，并且对递归调用的返回值进行接收。
def insertIntoBST(root,val):
    if  not root:
        return treenode(val)
    if root.val<val:
        root.right=insertIntoBST(root.right,val)
    if root.val>val:
        root.left=insertIntoBST(root.left,val)
    return root

##在bst中删除一个数
def getMin(node):
    while node.left:
        node=node.left
    return node
def deletenode(root,key):
    if  not root:
        return None
    if root.val==key:
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left
        minnode=getMin(root.right)
        root.val=minnode.val
        root.right=deletenode(root.right,minnode.val)
    if root.val<key:
        root.right=deletenode(root.right,key)
    if root.val>key:
        root.left=deletenode(root.left,key)
    return root

