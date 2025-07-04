class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_list(head):
    current=head
    while(current):
        print(current.data,end=' --> ')
        current=current.next
    print("None")
        
def traverse(head):
    current=head
    while(current):
        print(current.data)
        current=current.next
        
def insertion_at_beginning(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    
def insertion_at_end(head,data):
    new_node=Node(data)
    current=head
    while(current.next):
        current=current.next
    current.next=new_node
    
def insertion_after_a_given_node(prev_node,data):
    
    if(prev_node is None):
        return
    new_node=Node(data)
    new_node.next=prev_node.next
    prev_node.next=new_node
    
def delete_by_value(target,head):
    
    current=head
    if current and current.data==target:
        head=current.next
        return
    prev_node=None
    while current and current.data!=target:
        prev_node=current
        current=current.next
    if current is None:
        return
    if current.data is target:
        prev_node.next=current.next
        
def delete_by_position(pos,head):
    current=head
    if current is None:
        return
    if pos==0:
        head=current.next
        return
    for i in range(pos-1):
        current=current.next
        if current is None or current.next is None:
            return
    current.next=current.next.next
    
def search(target,head):
    current=head
    while(current):
        if current.data==target:
            return True
        current=current.next
    return False
    
def reverse(head):
    current=head
    prev=None
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    head=prev
    
https://leetcode.com/problems/linked-list-cycle/description/

https://leetcode.com/problems/middle-of-the-linked-list/description/

https://leetcode.com/problems/reverse-linked-list/description/

https://leetcode.com/problems/remove-linked-list-elements/
        
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

https://leetcode.com/problems/merge-two-sorted-lists/description/
   
https://leetcode.com/problems/palindrome-linked-list/description/

https://leetcode.com/problems/intersection-of-two-linked-lists/description/    

https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
        
https://leetcode.com/problems/delete-node-in-a-linked-list/description/        