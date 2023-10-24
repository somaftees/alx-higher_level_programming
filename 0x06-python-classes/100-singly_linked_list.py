#!/usr/bin/python3
"""class"""


class Node:
    """node class"""
    def __init__(self, data, next_node=None):
        """init"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """singlyLinkedList class"""
    def __init__(self):
        """init"""
        self.__head = None

    def sorted_insert(self, value):
        """sorted insert"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """str"""
        arry = []
        tmp = self.__head
        while tmp is not None:
            arry.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(arry))
