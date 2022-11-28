#Given two lists represeting digits of a number in
# 1. reverse order
# 2. proper order
# write a function to sum up the numbers and
# split them into digits in the same order as they came in (CTCI, Problem 2.5)
import fundamentals.data_structures.linked_list as linked_list
list1 = [7,1,6] #7->1->6=617
list2 = [5,9,2] #5->9->2=295 .... Therefore the list returned should be the value 912, i.e. 2->1->9
head1=linked_list.build_ll_from_arr(list1)
head2=linked_list.build_ll_from_arr(list2)
print(linked_list.check_list(head1))
print(linked_list.check_list(head2))
def find_sum_of_list_items_in_reverse(h1, h2):

    n1=h1
    n2=h2
    def makenum_from_list(temphead,num,pow_to_use):
        while temphead is not None:
            num+=temphead.data*(10**pow_to_use)
            pow_to_use+=1
            temphead=temphead.next
        return num
    num1=makenum_from_list(n1,0,0)
    num2=makenum_from_list(n2,0,0)
    return num1+num2
def find_sum_of_list_items_forward(h1,h2):

    size1=linked_list.sizeof_list(h1)
    size2=linked_list.sizeof_list(h2)
    def makenum_from_list(temphead,num,pow_to_use):
        while temphead is not None:
            num+=temphead.data*(10**pow_to_use)
            pow_to_use-=1
            temphead=temphead.next
        return num
    num1=makenum_from_list(h1,0,size1-1)
    num2=makenum_from_list(h2,0,size2-1)
    return num1+num2
def listify(sum,reversed_flag=True):
    digits_of_sum=[]
    while sum > 0:
        digit = sum % 10
        digits_of_sum.append(digit)
        sum = sum // 10
    if reversed_flag:

        return linked_list.build_ll_from_arr(digits_of_sum)
    else:
        return linked_list.build_ll_from_arr(list(reversed(digits_of_sum)))

print(find_sum_of_list_items_in_reverse(head1, head2))
print(linked_list.check_list(listify(find_sum_of_list_items_in_reverse(head1, head2),reversed_flag=True)))


list1 = [6,1,7] #7->1->6=617
list2 = [2,9,5] #5->9->2=295 .... Therefore the list returned should be the value 912, i.e. 2->1->9
head1=linked_list.build_ll_from_arr(list1)
head2=linked_list.build_ll_from_arr(list2)
print(linked_list.check_list(head1))
print(linked_list.check_list(head2))
print(find_sum_of_list_items_forward(head1,head2))
print(linked_list.check_list(listify(find_sum_of_list_items_forward(head1,head2),reversed_flag=False)))
