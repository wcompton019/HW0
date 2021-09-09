# a "Sortable" class contains
# Private (prefixed with two underscores, not visible to users of the object)
# - a __data field, that contains the sortable data
# - a __isAppropriate method, that determines if an argument is appropriate
# Public
# - a getData method that returns the data
# - a setData method that updates the data if the input argument is appropriate, and returns true if successful
# - a constructor __init__ that initializes with a default value
# - a greaterThan method given another sortable s, returns true if data is greater than s.data

# a Set is a collection of values.  https://docs.python.org/2/library/stdtypes.html#set
# The values are not ordered within sets, and
# there is no built-in sorting method for sets.
# Sort them by size, and break ties by comparing them alphabetically when converted to strings using str()
# So {1,2,3,4} > {1,2,3} (4 comes AFTER 3, so 4 is greater)
# And {"b"} > {"a"} (b comes AFTER a, so b is greater)
class SortableSet:

    def __init__(self):
        self.__data = 0
        self.__arglength = 0
        self.__datalength = 0

    def __isAppropriate(self, arg):
        if type(arg) == set:
            return True

    def setData(self, arg):
        if self.__isAppropriate(arg):
            self.__data = arg
            return True
    def getData(self):
        return self.__data

    def greaterThan(self, arg):
        if type(arg.getData()) == int:
            self.__arglength = 1
        if type(arg.getData()) != int:
            for i in arg.getData():
                self.__arglength +=1
        if type(self.__data) == int:
            self.__datalength = 1
        if type(self.__data) != int:
            for i in self.__data:
                self.__datalength +=1
        if self.__datalength > self.__arglength:
            return True
        if self.__datalength <= self.__arglength:
            return False
            #greaterThan = False
        #for i in self.__data:
        #    if i > arg.getData():
        #        greaterThan = True


    def SortSet(self, arg):
        return sorted(arg)
        

