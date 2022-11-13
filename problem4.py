# 4. Sorted insert in a Link list.
# My solution's time complexity is O(N) at most, when insert number is the largest in the linked list.
# And the N is the number of list nodes.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortedInsert(self, head, num):

        dummy = ListNode(-float('inf'), head)

        prev, curr = dummy, head
        while curr:
            if prev.val < num <= curr.val:
                break
            prev, curr = prev.next, curr.next

        prev.next = ListNode(num, curr)
        return dummy.next

# helper function
def listToLinkedlist(input):
    if not input:
        return None

    head = tail = ListNode(input[0])
    for x in input[1:]:
        tail.next = ListNode(x)
        tail = tail.next

    return head

# helper function
def printLinkedlist(head):
    result = []
    if not head:
        return result

    while head:
        result.append(head.val)
        head = head.next

    print(result)

# TEST
printLinkedlist( Solution().sortedInsert(listToLinkedlist([1,3,5,7,8,11]), 9) )
printLinkedlist( Solution().sortedInsert(listToLinkedlist([0]), 9) )
printLinkedlist( Solution().sortedInsert(listToLinkedlist([]), 9) )
printLinkedlist( Solution().sortedInsert(listToLinkedlist([1,3,5,7,8,11]), 20) )
printLinkedlist( Solution().sortedInsert(listToLinkedlist([1,3,5,7,8,11]), -2) )