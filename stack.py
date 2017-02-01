#!python
from linkedlist import LinkedList, Node


# class Stack(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         self.data = list()
#         pass
#         if iterable:
#             for item in iterable:
#                 self.push(item)
#
#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.length())
#
#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         return not self.data
#
#     def length(self):
#         """Return the number of items in this stack"""
#         return len(self.data)
#
#     def peek(self):
#         """Return the top item on this stack without removing it,
#         or None if this stack is empty"""
#         if self.is_empty():
#             return None
#         return self.data[0]
#
#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.data.insert(0, item)
#
#     def pop(self):
#         """Return the top item and remove it from this stack,
#         or raise ValueError if this stack is empty"""
#         if self.is_empty():
#             raise ValueError, 'stack is empty'
#         head = self.peek()
#         del self.data[0]
#         return head


# class Stack(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         self.data = LinkedList()
#         pass
#         if iterable:
#             for item in iterable:
#                 self.push(item)
#
#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.length())
#
#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         return self.data.head is None
#
#     def length(self):
#         """Return the number of items in this stack"""
#         return self.data.length
#
#     def peek(self):
#         """Return the top item on this stack without removing it,
#         or None if this stack is empty"""
#         if self.is_empty():
#             return None
#         return self.data.head.data
#
#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.data.prepend(item)
#
#     def pop(self):
#         """Return the top item and remove it from this stack,
#         or raise ValueError if this stack is empty"""
#         if self.is_empty():
#             raise ValueError, 'stack is empty'
#         head = self.peek()
#         self.data.delete(head)
#         return head
