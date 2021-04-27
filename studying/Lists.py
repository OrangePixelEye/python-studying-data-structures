import numpy as np


class Lists:
    """A list is a sequential set of elements to which you
    can add new elements and remove or change existing ones:
    It has two very distinctive implementations — array list and linked list."""
    class ArrayList:
        """A dynamic array"""
        base_array = np.array([43])

        def add(self, element):
            """adds a new element in the list"""
            # adds a new position in the array
            self.base_array = np.resize(self.base_array, self.base_array.size + 1)
            # size gets the total position not including the 0 so we need to take 1 off
            self.base_array[self.base_array.size - 1] = element

        def remove_at(self, index):
            """remove element in selected position"""
            # create a list to easily manipulate the array
            temp_list = self.base_array.tolist()
            try:
                del temp_list[index]
            except IndexError:
                print("There is no index " + str(index))
            except Exception as e:
                print("This error happened " + e)
            else:
                # rearrange the array list
                self.base_array = np.array(temp_list)

        def remove(self, element):
            """remove element by value"""
            # for in python is kinda like a foreach so we need an index
            index = 0
            for number in self.base_array:
                if number == element:
                    self.remove_at(index)
                index = index + 1

        def insert(self, element, index):
            """insert element in the selected position"""
            if index > self.base_array.size + 1:
                return print("There is no space " + str(index))
            # add space
            self.add(0)
            temp_list = self.base_array.tolist()
            # we don't want to include the last one
            position = self.base_array.size - 2
            # rearranging the values
            for _ in reversed(temp_list):
                if position >= index:
                    temp_list[position + 1] = temp_list[position]
                position = position - 1
            temp_list[index] = element
            self.base_array = np.array(temp_list)

        def get(self, index):
            """get value by index"""
            try:
                return self.base_array[index]
            except IndexError:
                return "there is no value in " + str(index) + " position"

        def print(self):
            """Just prints the array"""
            print(self.base_array)

    class LinkedList:
        """An linked list is kinda like an array but the data is not located sequentially"""

        def __init__(self):
            self.head_value = None

        def add(self, element):
            if self.head_value is None:
                self.head_value = self.Node(element)
                return
            value = self.head_value
            while value.next_value:
                value = value.next_value
            value.next_value = self.Node(element)

        def remove_at(self, index):
            pass

        def remove(self, element):
            pass

        def insert(self, element, index):
            pass

        def get(self, index):
            pass

        def print(self):
            print_value = self.head_value
            while print_value is not None:
                print(print_value.data_value)
                print_value = print_value.next_value

        class Node:
            """Each element in the linked list is called node"""
            def __init__(self, data_value=None):
                self.data_value = data_value
                self.next_value = None
