# '''
# Linked List hash table key/value pair
# '''
import math

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
            return
        x = self.storage[index]
        #check to see if key already exists. If it does update the value.
        while x.next:
            if x.key == key:
                x.value = value
                return
            x = x.next
        if x.key == key:
            x.value = value
            return
        #If key does not exist, create a new pair and add it to the end of the list.
        x.next = LinkedPair(key, value)
        return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
            
        if self.storage[index] == None:
            print("Key not found")
        x = self.storage[index]
        prev = x
        if x.key == key:
            self.storage[index] = x.next
            return
        x = x.next
        while x:
            if x.key == key:
                prev.next = x.next
                return
            prev = x
            x = x.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        
        index = self._hash_mod(key)
        x = self.storage[index]

        if x == None:
            return None
        
        while x.next:
            if x.key == key:
                return x.value
            x = x.next
        
        if x.key == key:
            return x.value
        return None

        

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        double_capacity = self.capacity * 2
        new_storage = [None] * double_capacity

        #loop through each element in current storage
        for i in self.storage:
            if i != None:
                current = i
                while current:
                    index = self._hash(current.key) % double_capacity
                    if new_storage[index] == None:
                        new_storage[index] = LinkedPair(current.key, current.value)
                    else:
                        new_pair = LinkedPair(current.key, current.value)
                        new_pair.next = new_storage[index]
                        new_storage[index] = new_pair
                    current = current.next
        self.storage = new_storage
        self.capacity = double_capacity

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
