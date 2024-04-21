class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def isPalindrome(head):
    rev = None # 역순으로 된 연결리스트를 저장하기 위한 포인터 None으로 시작
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(isPalindrome(head))
