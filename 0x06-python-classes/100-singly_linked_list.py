#!/usr/bin/python3
"""define class for single link list"""

class Node:
    """make node of single link"""

    def __init__(self, data , next_node=None):
        """ define the args and inie new node.
        args:
            data (int): data of new node
            next_node : to next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """data setter """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next node getter"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if  not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """ class to print the single link list in lines manner"""

    def __init__(self):
        """ init new single link list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert anew node to the singley link list 
        args:
            value (int): new node """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:  
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """print this node in string manner"""
        values = []
        tmp = self.__head
        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
