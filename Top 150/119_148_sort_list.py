class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left if left else right
        return dummy.next