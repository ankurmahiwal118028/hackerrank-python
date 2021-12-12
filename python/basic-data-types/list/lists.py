# https://www.hackerrank.com/challenges/python-lists/problem
"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data,
  the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

"""


if __name__ == "__main__":

    N = int(input())
    arr = list()

    for i in range(0,N):
        cmd = input().split(' ')

        # Insert(a,b) - insert at position a, value b, rest of the list will move one index ahead
        if cmd[0] == 'insert':
            arr.insert(int(cmd[1]), int(cmd[2]))

        # Delete the first occurance of value
        elif cmd[0] == 'remove':
            arr.remove(int(cmd[1]))

        # append at the end
        elif cmd[0] == 'append':
            arr.append(int(cmd[1]))

        # sort the list
        elif cmd[0] == 'sort':
            arr.sort()

        # Pop the last element from the list.
        elif cmd[0] == 'pop':
            arr.pop()

        # Reverse teh list
        elif cmd[0] == 'reverse':
            arr.reverse()
        # print list
        elif cmd[0] == 'print':
            print(arr)
