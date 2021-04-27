import numpy


class Array:
    """Array is a structure that contains a group of elements with the same
    data type"""

    _int_array = 0

    def create_array(self):
        # creating an int array
        self._int_array = numpy.array([1, 2, 3])
        print("this array contains:" + str(self._int_array))
