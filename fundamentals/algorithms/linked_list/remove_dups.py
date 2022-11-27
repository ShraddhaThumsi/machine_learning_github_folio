#removing duplicate values from a linked list
import fundamentals.data_structures.linked_list as linked_list
list_items=[1,3,4,6,4,5,6,7,8]
#the final linked list should be 1->3->4->6->
head=linked_list.build_ll_from_arr(list_items)

def remove_dups(h):
    visited={}

    n=h
    while n is not None:
        visited[n.data]=False
        n=n.next
    n=h
    visited[n.data] = True
    while n.next is not None:
        if visited[n.next.data]:
            n.next=n.next.next
        else:
            visited[n.next.data]=True
            n=n.next
    return h
print('list before removing dups')
print(linked_list.check_list(head))
new_head=remove_dups(head)
print('linked list after removing dups')
print(linked_list.check_list(new_head))
