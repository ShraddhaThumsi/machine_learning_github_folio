import fundamentals.data_structures.stack_using_ll as stack
import fundamentals.data_structures.linked_list as linked_list
class SetOfStacks:
    def __init__(self,stacks=[], max_size=10):
        self.stack_set = stacks
        self.maxsize_per_stack = max_size
    def push(self,item):
        stacknode = linked_list.ListNode(item)
        least_occupied_stack = self.stack_set.pop(

        )