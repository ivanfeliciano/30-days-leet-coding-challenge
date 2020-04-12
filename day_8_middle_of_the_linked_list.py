# Definition for singly-linked list.
from math import ceil
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
    	return "Node({}, {})".format(self.val, self.next)

class Solution:
    def middleNode(self, head):
    	counter = 0
    	pointer = head
    	while pointer:
    		print(pointer.val)
    		counter += 1
    		pointer = pointer.next
    	ans = head
    	for i in range(counter // 2 + 1):
	    	if i + 1 == counter // 2 + 1: return ans
	    	ans = ans.next

def main():
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	d = ListNode(4)
	e = ListNode(5)
	# f = ListNode(6)
	a.next = b
	b.next = c
	c.next = d
	d.next = e
	# e.next = f
	print(Solution().middleNode(a))

if __name__ == '__main__':
	main()