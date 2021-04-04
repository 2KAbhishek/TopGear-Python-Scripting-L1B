#!/usr/bin/env python

str1 = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to concepts in fewer lines of code than possible languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small scale and a large scale. Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython , the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
str2 = "Python is Python are Python was Python not Python yes Python no Python awesome Python abcd"


def getDic(strn):
    dic = {}
    wordList = strn.split()
    length = len(wordList)
    for index, word in enumerate(wordList):
        if word in dic.keys():
            continue
        tmpList = []
        for i in range(index, length):
            if index == length-1:
                break
            if word == wordList[i]:
                nextWord = wordList[i+1]
                tmpList.append(nextWord)
        dic[word] = tmpList
    return dic


def predict(strn, word):
    wordDictionary = getDic(strn)
    print(word, "is likely to be followed by -> ", wordDictionary[word])


predict(str1, "Python")
usr = input('Enter a word: ')
predict(str1, usr)
