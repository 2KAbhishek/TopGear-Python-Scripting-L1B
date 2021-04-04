#!/usr/bin/env python

urlList = ["www.annauniv.edu", "www.google.com", "www.ndtv.com",
           "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

tldList = set()

for url in urlList:
    rev = url[::-1]
    tldList.add(rev[:rev.index('.')][::-1])

tldList = list(tldList)
tldList.sort()
print(tldList)


def sortURL(domainList, urlList):
    sortedUrlList = []

    for dom in domainList:
        for url in urlList:
            if url.endswith(dom):
                sortedUrlList.append(url)

    return sortedUrlList


print(sortURL(tldList, urlList))
