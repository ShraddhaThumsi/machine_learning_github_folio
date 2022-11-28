import fundamentals.data_structures.linked_list as linked_list
list_items=[1,2,3,4,5,3,4,5,6,7,6,7,8,9,10]
head=linked_list.build_ll_from_arr(list_items)
print(linked_list.check_list(head))
def find_kth_to_last(head,k):
    runner=0
    n=head
    while n is not None and runner<k-1:
        runner+=1
        n=n.next
    return n
kth_head=find_kth_to_last(head,5)
print(linked_list.check_list(kth_head))
