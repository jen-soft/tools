# -*- coding: utf-8 -*-

"""# - - -
   data-edit: 2018-04-28(05:30)

   name:   Jen-Soft-Print (JSP)
   author: jen-soft
   email:  jen.soft.master@gmail.com

   license: Licensed under the Apache License, Version 2.0
            http://www.apache.org/licenses/LICENSE-2.0

   description: short tools for using in interactive-python

   features:
       import p
# - - -
       p.dir(obj)  # return all publick atters from object
       #  p.dir( str, True, 7 )
# - - -
"""
import math


print(__doc__.split('import p')[1])


class origin:
    dir = dir


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def dir(obj, show_private=False, count_columns=5):
    # get object attributes
    if show_private:  # allow:  "_name..."
        obj_attr = [n for n in origin.dir(obj) if not n.startswith('__')]
    else:
        obj_attr = [n for n in origin.dir(obj) if not n.startswith('_')]

    # split list attributes for columns
    obj_attr.sort()
    column_len = int(math.ceil(len(obj_attr) / count_columns))
    columns = list(chunks(obj_attr, column_len))
    for column_items in columns:
        dummy_items = range(0, column_len - len(column_items))
        column_items.extend(['' for d in dummy_items])
    # text format columns (normalize width)
    for i, column_items in enumerate(columns):
        column_width = len(max(column_items, key=len))
        formatted_items = []
        for item in column_items:
            indent = ' ' * (column_width - len(item))
            formatted_items.append(item + indent)
        columns[i] = formatted_items
    # print result data
    for line_data in list(zip(*columns)):
        line = '    '.join(line_data)
        print(line)
    print('\n')


if __name__ == '__main__':
    dir(str, True)

