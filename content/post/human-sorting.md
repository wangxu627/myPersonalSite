---
title: "Human Sorting"
date: 2020-10-29T16:07:43+08:00
Description: ""
Tags: []
Categories: []
DisableComments: false
---

Kate Rhodes wrote a post about simplistic vs. useful sorting: [Alphabetical != ASCIIbetical](http://weblog.masukomi.org/2007/12/10/alphabetical-asciibetical) (cute name). In it, she points to Dave Koelle’s [Alphanum algorithm](http://www.davekoelle.com/alphanum.html), which says to split the string to be sorted into numeric and non-numeric chunks, then sort so that the numeric chunks are treated as numbers. This makes “z2” sort after “z100”, for example.

I looked at the code Dave provided (in Java, C++, or Perl), and all of it is much longer than I expected: the C++ is 40 or so lines. A comment in there says it’s easier in a pattern language like Perl, but the Perl is still 20 iterative lines.

In Python:

```
import re

def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s
    
def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)
```

A few helpful Python features make this more compact: re.split provides just the function we want for chunking the string, sort takes a key function for computing sort keys from data, the key to sort on can itself be a list, and comparing two lists compares lexicographically among the elements of the list.

Each of these features in and of itself may have only occasional use, but here they conspire to help me write code nearly as expressive as the English description in my first paragraph. And there are enough of those features that they often help make expressive code like that.

# stack overflow demo
```
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

alist=[
    "something1",
    "something12",
    "something17",
    "something2",
    "something25",
    "something29"]

alist.sort(key=natural_keys)
print(alist)
```

Another article:
* [Sorting for Humans : Natural Sort Order](https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/)