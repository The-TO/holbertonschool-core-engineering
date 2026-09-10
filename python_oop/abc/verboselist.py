#!/usr/bin/env python3
"""Module definisssanrt une extension de liste"""

class VerboseList(list):
    def append(self, object):
        super().append(object)
        print ("Added [{}] to the list.".format(object))
    
    def extend(self, iterable):
        super().extend(iterable)
        print (f"Extended the list with [{len(iterable)}] items.")
    
    def remove(self, value):
        print (f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index = -1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        super().pop(index)
        return item

verbolist = VerboseList([1, 2, 3])

verbolist.append(4)
verbolist.extend([5, 6])
verbolist.remove(2)
verbolist.pop()
verbolist.pop(0)

