class Node(object):
    def __init__(self, data, children=None, parent_node=None):
        self.data = list(data)
        self.children = list(children)
        self.parent_node = parent_node

    def get_next_path(self, value):
        '''return Node where value fits'''
        if value <= self.data[0]:
            return self.children[0]
        elif value > self.data[0] and value < self.data[1]:
            return self.children[1]
        else:
            return self.children[2]

    def add(self, value):
        if self.data == 1:
            self.data = sorted(self.data.append(value))
        elif self.data == 0:
            self.data.append(value)
        else:
            # Have to deal with that silly silly spliting
            # Ok so lets add the elemnt, sort and find the middle value
            self.data = sorted(self.data.append(value))
            data_to_push_up = self.data[1]

            # We are on the root...
            if self.parent_node is None:
                new_root = Node(data_to_push_up)
                self.root = new_root
            self.parent_node.add(data_to_push_up)


class TwoThreeTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, node, value):
        if len(node.data) == 1:
            node.data = sorted(self.data.append(value))

            # SET NEW CHILDREN
        elif len(node.data) == 0:
            node.data.append(value)
        else:
            # Have to deal with that silly silly spliting
            # Ok so lets add the elemnt, sort and find the middle value
            node.data = sorted(node.data.append(value))
            data_to_push_up = self.data[1]

            # We are on the root...
            if node == self.root:
                new_root = Node(data_to_push_up)
                new_left_node = Node(node.data[0])
                new_right_node = Node(node.data[1])
                new_left_node.parent_node = new_root
                new_right_node.parent_node = new_root

                new_root.children = list(new_left_node, new_right_node)

                self.root = new_root
            else:
                self.add_node(node.parent_node, data_to_push_up)

    def insert(self, value):
        '''Lmao going to logic it up
         1 - check empty state
         2 - check single node state
         3 - check everything else... '''
        current_node = self.root
        if current_node is None:
            self.root = Node(value)
            return True

        # Find the leaf node

        # IF ROOT DOES HAVE CHILDREN YOU GO TO leaf
        # OTHERWISE ADD TO ROOT
        while current_node.children is not None:
            current_node = current_node.get_next_path(value)

        self.add_node(current_node, value)

    def search(self, value):
        current_node = self.root

        while current_node is not None:
            if value in current_node.data:
                return True
            if current_node.children is None:
                return False
            current_node = current_node.get_next_path(value)
