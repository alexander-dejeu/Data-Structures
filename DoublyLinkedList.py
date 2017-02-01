from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    # def __iter__(self):
    #     current = self.head
    #     while current is not None:
    #         yield current
    #         current = current.next

        # my_list = []
        # current_node = self.head
        # while current_node is not None:
        #     my_list.append(current_node.data)
        #     current_node = current_node.next
        # return iter(my_list)

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item
        # If the head is None then this is first item being added
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        # If the head and tail equal eachother then there should only be one
        # element.
        elif self.head == self.tail:
            self.tail = Node(item)
            self.tail.previous = self.head
            self.head.next = self.tail
        # All other cases should just update the old and new tail data
        else:
            new_tail = Node(item)
            self.tail.next = new_tail
            new_tail.previous = self.tail
            self.tail = new_tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        elif self.head == self.tail:
            self.head = Node(item)
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            new_head = Node(item)
            new_head.next = self.head
            self.head.previous = new_head
            self.head = new_head

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        current_node = self.head

        if current_node is None:
            raise ValueError('could not find %c in LinkedList' % (item))

        # There is only one node
        if self.head.data == item and self.head == self.tail:
            self.head = current_node.next
            self.tail = self.head
            return
        # Deleting the head node
        elif self.head.data == item:
            self.head = current_node.next
            self.previous = None
            return
        else:
            while current_node.next is not None:
                if current_node.next.data == item:

                    if current_node.next == self.tail:
                        self.tail = current_node
                        self.tail.next = None
                        return

                    current_node.next = current_node.next.next
                    current_node.next.previous = current_node.next.previous.previous

                    return
                current_node = current_node.next

            raise ValueError('could not find %c in LinkedList' % (item))

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        current_node = self.head

        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next

        return None


def test_linked_list():
    ll = DoublyLinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    # print('iterable testing:')
    # for node in ll:
    #     print(node)
    #     print(node.data)
    #     print(node.next)
    # print('done testing interable')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
