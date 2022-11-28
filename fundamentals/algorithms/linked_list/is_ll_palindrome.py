import fundamentals.data_structures.linked_list as linked_list
#list_items=[1,3,1] #the final output should be True since 131 is a palindrome
list_items=[1,2,3] #thefinal output should be False since 123 is not a palindrome

head=linked_list.build_ll_from_arr(list_items)
def is_palindrome(h):
    list_as_str=linked_list.delistify(h)
    rev = list_as_str[::-1]
    return list_as_str==rev
print(is_palindrome(head))
