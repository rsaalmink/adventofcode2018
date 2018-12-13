player_count = 413 
last_marble = 71082
last_marble = 71082*100

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


current_node = Node(0)

player, player_scores = -1, [0] * player_count
for i in range(1, last_marble+1):
    player = (player+1) % player_count
    if i % 23:
        # regular case, insert inline
        one_clockwise = current_node.next
        two_clockwise = one_clockwise.next
        current_node = Node(i,one_clockwise,two_clockwise)
        one_clockwise.next = current_node
        two_clockwise.prev = current_node
    else:
        # handle 23 case
        player_scores[player] = player_scores[player] + i
        for j in range(7):
            current_node = current_node.prev
        player_scores[player] = player_scores[player] + current_node.value
        prevone = current_node.prev
        nextone = current_node.next        
        prevone.next = nextone
        nextone.prev = prevone
        current_node = nextone


start = current_node
while current_node.next != start:
    print(current_node.value, end=' ')
    current_node = current_node.next

print(max(player_scores))