# Romain Tranchant
# CIS103 : Fundamentals of Programming
# Instructor: MD Ali
# Homework Assignment: Inheritance and Abstract Classes
# Objective: Demonstrate an understanding of inheritance, subclassing, and
# abstract classes by answering questions and implementing example code.



# Import the time module to measure the performance of operations
import time

# Abstract base class that provides common functionality for bags
class AbstractBag:

# Initializes the bag with a source collection, or an empty list if no source is provided
    def __init__(self, sourceCollection=None):
# Set the initial size of the bag to 0
        self.size = 0
# Initialize the items list as an empty list
        self.items = []
# If a source collection is provided
        if sourceCollection:
# Iterate over each item in the source collection
            for item in sourceCollection:
# Add each item to the bag using the abstract 'add' method
                self.add(item)

# Abstract method 'add' that must be implemented by subclasses
    def add(self, item):
        raise NotImplementedError("Subclasses must implement this method")

# Returns the number of items in the bag when len() is called
    def __len__(self):
# Return the length of the items list
        return len(self.items)

# Checks if the bag is empty by verifying if its size is 0
    def isEmpty(self):
# Return True if size is 0, indicating the bag is empty
        return self.size == 0

# Checks if an item is present in the bag using the 'in' operator
    def __contains__(self, item):
# Check if the item is in the items list
        return item in self.items

# Converts the list of items into a string representation of the bag
    def __str__(self):
# Return the string representation of the items list
        return str(self.items)




class ArrayBag(AbstractBag):

# Initializes the bag from a source collection or an empty list if no source collection is provided.
# If a collection is passed, it converts it into a list and assigns it to self.items.
# The size of the bag is also initialized.
    def __init__(self, sourceCollection=None):
# If no collection is passed, initialize an empty list
        if sourceCollection is None:
# Set self.items as an empty list
            self.items = []
# If a collection is passed, initialize with the provided collection
        else:
# Convert source collection to a list
            self.items = list(sourceCollection)
# Set the size of the bag to the length of the items list
        self.size = len(self.items)


# Adds an item to the bag by appending it to the list and incrementing the size.
    def add(self, item):
# Add the item to the list of items
        self.items.append(item)
# Increase the size of the bag by 1
        self.size += 1

# Returns the number of items in the bag when the len() function is called.
# This method returns the length of the items list.
    def __len__(self):
# Return the length of the items list
        return len(self.items)

# Returns a list of items in the bag. This is a simple getter for the items list.
    def display(self):
# Return the list of items in the bag
        return self.items




class ArraySortedBag(ArrayBag):

# Initializes the sorted bag using the ArrayBag's constructor.
# The parent class constructor is called using super().
    def __init__(self, sourceCollection=None):
# Call the parent class constructor to initialize the items list and size
        super().__init__(sourceCollection)
# Checks if an item exists in the sorted bag using binary search for faster lookup.
# Binary search divides the search interval in half, reducing the time complexity to O(log n).
    def __contains__(self, item):
# Start of the search interval
        left = 0
# End of the search interval
        right = len(self) - 1
# Continue searching while there is still a range to search
        while left <= right:
# Calculate the middle index
            midPoint = (left + right) // 2
# If the item is at the midpoint, return True
            if self.items[midPoint] == item:
                return True
            elif self.items[midPoint] > item:
# If the item is smaller, search in the left half
                right = midPoint - 1
# If the item is larger, search in the right half
            else:
                left = midPoint + 1
# Return False if the item is not found after the search
        return False


# Adds an item to the sorted bag in sorted order.
# The item is inserted at the correct position while maintaining the sorted order.
    def add(self, item):
# If the bag is empty or the item is greater than or equal to the last item
        if self.isEmpty() or item >= self.items[len(self) - 1]:
# Use the ArrayBag's add method to append the item at the end
            super().add(item)
        else:
# Start searching from the beginning of the list
            targetIndex = 0
# Find the position where the item should be inserted
            while item > self.items[targetIndex]:
                targetIndex += 1
# Make space for the new item by appending None
            self.items.append(None)
# Shift elements to the right to make space for the new item
            for i in range(len(self.items) - 2, targetIndex - 1, -1):
# Shift each item one position to the right
                self.items[i + 1] = self.items[i]
# Insert the new item at the target position
            self.items[targetIndex] = item
# Increment the size of the bag
            self.size += 1


# Compares two sorted bags to check if they contain the same items in the same order.
# This method returns True if the items and size of both bags are identical.
    def __eq__(self, other):
# If both are the same object, they are equal
        if self is other:
            return True
# Check if types or lengths differ
        if type(self) != type(other) or len(self) != len(other):
# If types or lengths are different, the bags are not equal
            return False
# Compare the items lists to see if they are identical
        return self.items == other.items

# Testing ArrayBag

# Create an empty ArrayBag instance amd add items to the ArrayBag
test_arraybag = ArrayBag()

test_arraybag.add(1)
test_arraybag.add(4)
test_arraybag.add(2)
test_arraybag.add(10)
test_arraybag.add(9)
test_arraybag.add(7)

# Check if the ArrayBag is empty
test_empty = test_arraybag.isEmpty()

# Print the string representation of the ArrayBag, which will call __str__()
print(f"The ArrayBag: {test_arraybag}")

# Print the result of the operation checking if the ArrayBag was empty
print(f"Is the ArrayBag empty?  {test_empty}")

# Check the length of ArrayBag and print the result
test_length = test_arraybag.__len__()
print(f"The length of ArrayBag is {test_length}")

# Record the starting time using perf_counter() for high resolution
start_arraybag_time = time.perf_counter()

# Check if item '9' is in the bag using the __contains__ method
test_contains_arraybag = test_arraybag.__contains__(9)

# Record the ending time after the contains check
end_arraybag_time = time.perf_counter()

# Calculate the elapsed time for the contains operation
elapsed_arraybag = end_arraybag_time - start_arraybag_time

# Print the result of the contains check
print(f"Is 9 in the ArrayBag? {test_contains_arraybag}")

# Print the elapsed time in seconds to 9 decimal places
print(f"Linear search (9) in ArrayBag: {elapsed_arraybag:.9f} seconds\n")

# Testing ArraySortedBag

# Create an instance of ArraySortedBag and add items to the ArraySortedBag
test_arraysortedbag = ArraySortedBag()


test_arraysortedbag.add(4)
test_arraysortedbag.add(8)
test_arraysortedbag.add(3)
test_arraysortedbag.add(1)
test_arraysortedbag.add(11)
test_arraysortedbag.add(7)

# Print the sorted bag
print(f"The ArraySortedBag: {test_arraysortedbag}")

# Record the starting time for binary search
start_arraysortedbag_time = time.perf_counter()

# Check if item '8' exists in the sorted bag using binary search
test_binary_search = test_arraysortedbag.__contains__(8)

# Record the ending time for the binary search
end_arraysortedbag_time = time.perf_counter()

# Calculate the elapsed time for the binary search
elapsed_arraysortedbag = end_arraysortedbag_time - start_arraysortedbag_time

# Print the result of the binary search
print(f"Is 8 in the ArraySortedBag? {test_binary_search}")

# Print the elapsed time for binary search
print(f"Binary search (8) in ArraySortedBag: {elapsed_arraysortedbag:.9f} seconds\n")

# Create a second sorted bag with predefined items
# Testing equality of two ArraySortedBags
test_arraysortedbag_2 = ArraySortedBag([1, 3, 4, 7, 8, 11])
print(f"The second ArraySortedBag: {test_arraysortedbag_2}")
print(f"Are the two ArraySortedBags equal? {test_arraysortedbag == test_arraysortedbag_2}")

