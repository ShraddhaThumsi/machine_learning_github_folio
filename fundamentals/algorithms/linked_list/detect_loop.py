import fundamentals.data_structures.linked_list as linked_list

def detect_loop(head):
    t = head
    visited = []
    while t is not None:
        if t in visited:
            return True
        visited.append(t)
        t=t.next
    return False


list_items=[20,4,15,10]
#the final linked list should be 1->3->4->6->5->7>8
head=linked_list.build_ll_from_arr(list_items)


# Create a loop for testing
head.next.next.next.next = head
print(detect_loop(head))
