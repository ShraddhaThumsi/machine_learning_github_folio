import fundamentals.data_structures.linked_list as linked_list
#given a node in a linked list, delete that node and return the list
list_items=[1,2,3,4,5]#[1,2,3,4,5,3,4,5,6,7,6,7,8,9,10]
head=linked_list.build_ll_from_arr(list_items)
print(linked_list.check_list(head))
def del_all_nodes_of_value(head,node):
    n=head
    while n.next is not None:
        if n.next.data==node.data:
            n.next=n.next.next
            n=n.next
        else:
            n=n.next
    return head

node_to_delete = linked_list.ListNode(3)
head_sans_allgiven=del_all_nodes_of_value(head,node_to_delete)
print(linked_list.check_list(head_sans_allgiven))