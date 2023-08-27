# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []

        for x in lists:
            if(x == None):
                pass
            else:
                head = x
                while(head!=None):
                    arr.append(head.val)
                    head = head.next
        
        arr.sort()

        if(len(arr) == 0):
            return None
        
        head = ListNode(arr[0])
        temp = head

        for x in arr:
            temp.next = ListNode(x)
            temp = temp.next
        return head.next

            


        