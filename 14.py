import sys

# Reused my Linked List implementation of Day 9, hoping it might get useful for part 2. Guessed wrong :)

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        # support for constructing both with and without next/prev pointers
        self.prev = self
        self.next = self
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next

    def __repr__(self):
        prev = self.prev.value if self.prev is not self else 'self'
        next = self.next.value if self.next is not self else 'self'
        return " ".join(map(str, [self.value, prev, next]))

def list_as_string(start_node, amount=sys.maxsize):
    it = start_node
    result = str(it.value)
    i = 0
    while it.next != start_node and i < amount-1:
        it = it.next
        i += 1
        result += str(it.value)
    return result




start_node = Node(3)
last_node = Node(7, start_node, start_node)
start_node.next = last_node
start_node.prev = last_node

elf1 = start_node
elf2 = last_node

my_input = 793061

for x in range(my_input):
    new_recipe = str(elf1.value + elf2.value)
    for v in new_recipe:
        recipe = Node(int(v), last_node, start_node)
        start_node.prev = recipe
        last_node.next = recipe
        last_node = recipe

    for i in range(1+elf1.value):
        elf1 = elf1.next
    for i in range(1+elf2.value):
        elf2 = elf2.next
    # part 2
    # ls = list_as_string(start_node)
    # if "793061" in ls:
    #     print(ls.index("793061"))
    #     break

n = start_node
for i in range(my_input):
    n = n.next
print(list_as_string(n, 10))
