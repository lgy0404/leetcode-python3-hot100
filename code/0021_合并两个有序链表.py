class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        
        return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Helper function to create a list from a Python list
def create_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

# Test cases
list1 = create_list([2, 4, 8])
list2 = create_list([1, 3, 5])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

print("Merged list:")
print_list(merged_list)
