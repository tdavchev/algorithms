# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2

        carry = 0

        temp = ((l1.val + l2.val + carry) % 10) 
        carry = (l1.val + l2.val + carry) / 10
        ans = ListNode(temp)
        answer = ans
        l1 = l1.next
        l2 = l2.next

        while l1 != None and l2 != None:
            temp = ((l1.val + l2.val + carry) % 10) 
            carry = (l1.val + l2.val + carry) / 10
            ans.next = ListNode(temp)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next

        if l1 != None:
            while l1 != None:
                temp = (l1.val + carry) % 10
                carry = (l1.val+carry) / 10
                ans.next = ListNode(temp)
                ans = ans.next
                l1 = l1.next
            

        if l2 != None:
            while l2 != None:
                temp = (l2.val + carry) % 10
                carry = (l2.val+carry) / 10
                ans.next = ListNode(temp)
                ans = ans.next
                l2 = l2.next
            
        if carry != 0:
            ans.next = ListNode(carry)

        return answer


a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
g = ListNode(8)

d.val = e
e.val = f
f.val = g

a.val = b
b.val = c

ans = Solution()
a = ans.addTwoNumbers(a, d)
while a != None:
    print(a.val)
    a = a.next