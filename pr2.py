class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    dummy = ListNode(0)  # Dummy node
    current = dummy
    for val in values:
        current.next = ListNode(val)  
        current = current.next
    return dummy.next  


def print_linked_list(node):
    values = []
    while node:
        values.append(node.val)  
        node = node.next         
    print(values)  

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next

l1 = create_linked_list([2, 4, 5])  # Represents the number 542
l2 = create_linked_list([5, 6, 7])  # Represents the number 765

# Solution
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Output the result
print_linked_list(result)  # Should print the result as a linked list
