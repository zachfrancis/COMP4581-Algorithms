#!/usr/bin/env python3

# HashTable ADT with open addressing and linear probing
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
class MyHashtable(object):
    def __init__(self, size): # Creates an empty hashtable
        self.size = size
        # Create the list (of size) of empty lists (chaining)
        self.table = [None for _ in range(size)]
        self.status = ["empty" for _ in range(size)]

    def __str__(self): # for print
        s = [f"{s[0]}:{s[1]}" for s in zip(self.table, self.status)]
        return str(s)

    def insert(self, elem): # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        if self.status[hash] != "filled":
            self.table[hash] = elem
            self.status[hash] = "filled"
        else:
            while hash:
                hash += 1
                # Reset hash to 0 when end of table
                if hash >= self.size: hash = 0
                if self.status[hash] != "filled":
                    self.table[hash] = elem
                    self.status[hash] = "filled"


    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        if elem == self.table[hash]: return True
        else:
            while hash:
                hash += 1
                if hash <= self.size: hash = 0
                if self.status == "empty": return False
                if elem == self.table[hash]: return True

    def delete(self, elem): # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        if elem == self.table[hash]:
            self.table[hash] = None
            self.status[hash] = 'deleted'
        else:
            while hash:
                hash += 1
                if hash <= self.size: hash = 0
                if self.status != "filled": return
                if elem == self.table[hash]:
                    self.table[hash] = None
                    self.status[hash] = 'deleted'

def main():
    # Testing code
    s = MyHashtable(10)
    print(s)
    s.insert("amy") #97
    s.insert("chase") #99
    s.insert("chris") #99
    print(s)
    print(s.member("amy"))
    print(s.member("chris"))
    print(s.member("alyssa"))
    s.delete("chase")
    print(s.member("chris"))
    # You can use print(s) at any time to see the contents
    # of the table for debugging
    print(s)


if __name__ == "__main__":
    main()
