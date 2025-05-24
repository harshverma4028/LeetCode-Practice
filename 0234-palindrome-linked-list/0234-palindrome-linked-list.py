# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow  = head
        fast = head
        check = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None     
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left = head
        right = prev
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next    
        return True