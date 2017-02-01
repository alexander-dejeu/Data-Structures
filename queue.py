#!python
from linkedlist import LinkedList


# class Queue(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this queue and enqueue the given items, if any"""
#         self.data = list()
#         if iterable:
#             for item in iterable:
#                 self.enqueue(item)
#
#     def __repr__(self):
#         """Return a string representation of this queue"""
#         return 'Queue({})'.format(self.length())
#
#     def is_empty(self):
#         """Return True if this queue is empty, or False otherwise"""
#         return not self.data
#
#     def length(self):
#         """Return the number of items in this queue"""
#         return len(self.data)
#
#     def peek(self):
#         """Return the next item in this queue without removing it,
#         or None if this queue is empty"""
#         if self.is_empty():
#             return None
#         return self.data[0]
#
#     def enqueue(self, item):
#         """Enqueue the given item into this queue"""
#         self.data.append(item)
#
#     def dequeue(self):
#         """Return the next item and remove it from this queue,
#         or raise ValueError if this queue is empty"""
#         if self.is_empty():
#             raise ValueError, 'the queue is empty'
#         next = self.peek()
#         del self.data[0]
#         return next

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        self.data = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        return self.data.head is None

    def length(self):
        """Return the number of items in this queue"""
        return self.data.length

    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None
        return self.data.head.data

    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        self.data.append(item)

    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError, 'the queue is empty'
        next = self.peek()
        self.data.delete(next)
        return next
