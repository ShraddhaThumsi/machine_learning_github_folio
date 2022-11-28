import fundamentals.data_structures.linked_list as linked_list
#given a node in a linked list, split the list elements such that all smaller values are to the left and equal and greater values to the right.
# Then return the long list with the elements all stitched together

list_items=[10,1,1,2,2,3,19,8,7,18,34,5,6,3,2,6,4,7,9]
head=linked_list.build_ll_from_arr(list_items)
print(linked_list.check_list(head))
def partition_list_by_node(head,node):
    n=head
    lt_items=[]
    gt_eq_items=[]
    while n is not None:
        if int(n.data) < int(node.data):
            lt_items.append(n.data)
        else:
            gt_eq_items.append(n.data)
        n = n.next
    lt_items.extend(gt_eq_items)
    return lt_items

test_node = linked_list.ListNode(18)
partitioned_list=partition_list_by_node(head,test_node)
partitioned_list_head=linked_list.build_ll_from_arr(partitioned_list)
print(linked_list.check_list(partitioned_list_head))

