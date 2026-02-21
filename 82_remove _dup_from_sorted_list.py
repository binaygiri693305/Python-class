class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        start = end = None
        temp = tm = None
        while head.next:
            if head.val == head.next.val or head.val == (temp and temp.val):
                temp = head
                head = head.next
            else:
                tm = temp = head
                head = head.next
                tm.next = None
                if start == None:
                    start = end = tm
                else:
                    end.next = tm
                    end = tm
        if head.val != (temp and temp.val):
            if start == None:
                return head
            else:
                end.next = head
        return start
        
        