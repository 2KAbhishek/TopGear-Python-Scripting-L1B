#!/usr/bin/env python

bookstore = {"New Arrivals": {"COOKING": ["Everyday Italian", "Giada De Laurentiis", "2005", "30.00"], "CHILDREN": [
    "Harry Potter", "J K.Rowling", "2005", "29.99"], "WEB": ["Learning XML", "Erik T. Ray", "2003", "39.95"]}}

print("Book Store")
for dic1 in bookstore.values():
    for lst in dic1.values():
        strn = str(lst)
        strn = strn[1:len(strn)-1]
        print(strn)
