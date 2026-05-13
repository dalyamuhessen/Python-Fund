class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         if not list1:
#             return list2
#         if not list2:
#             return list1

#         if list1.val<=list2.val:
#             list1.next=self.mergeTwoLists(list1.next,list2)
#             return list1
#         else:
#             list2.next=self.mergeTwoLists(list1,list2.next) 
#             return list2         



class Solution:
    def mergeTwoLists(self,list1,list2):
        d=ListNode()
        cur=d
        while list1 and list2:
          if list1.val<list2.val:
              cur.next=list1
              cur=list1
              list1=list1.next
          else:
             cur.next=list2
             cur=list2
             list2=list2.next
        
        cur.next=list1 if list1 else list2
        return d.next