from __future__ import print_function

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_sub_list(head, p, q):
    current = head
    pre_start = None
    end_after = None
    while current.value != p:
        pre_start = current
        current = current.next
        continue
    start = current
    current = current.next
    while current.value != q:
        end = current
        current = current.next
    end = current
    if current.next:
        end_after = current.next
    if pre_start:
        pre_start.next = None
    end.next = None

    current = start


    previous = None
    next = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    if end_after:
        start.next = end_after
    else:
        start.next = None
    if pre_start:
        pre_start.next = end
    else:
        head = end
    return head


def main():
    head = Node(1)
    head.next = Node(7)
    head.next.next = Node(8)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 7, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()

#############################################################################################################################################
################ Following solution is provided by Educative.io #############################################################################
##############################################################################################################################################



from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  if p == q:
    return head

  # after skipping 'p-1' nodes, current will point to 'p'th node
  current, previous = head, None
  i = 0
  while current is not None and i < p - 1:
    previous = current
    current = current.next
    i += 1

  # we are interested in three parts of the LinkedList, the part before index 'p',
  # the part between 'p' and 'q', and the part after index 'q'
  last_node_of_first_part = previous
  # after reversing the LinkedList 'current' will become the last node of the sub-list
  last_node_of_sub_list = current
  next = None  # will be used to temporarily store the next node

  i = 0
  # reverse nodes between 'p' and 'q'
  while current is not None and i < q - p + 1:
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1

  # connect with the first part
  if last_node_of_first_part is not None:
    # 'previous' is now the first node of the sub-list
    last_node_of_first_part.next = previous
  # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
  else:
    head = previous

  # connect with the last part
  last_node_of_sub_list.next = current
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
