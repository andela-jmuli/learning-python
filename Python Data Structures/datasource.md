

Python data structures offer a very large choice of operations. One can choose different kinds of data structures depending on what the data involves, either if it needs to be modified, or if it's fixed data, and even what access type one would like.

### Lists

Lists are best used in the following situations:
* When you need a mixed collection of data all in one place
* When the data needs to be ordered.
* When your data requires the ability to be changed or extended(lists are mutable).
* When you don't require data to be indexed by a custom value. Lists are numerically indexed and to retrieve an element, you must know its numeric position in the list.
* When you need a stack or a queue. Lists can be easily manipulated by appending/removing elements from the beginning/end of the list.
* When your data doesn't have to be unique.


### Sets

A set is an unordered collection with no duplicate values. A set can be created by using the keyword ``` set ``` or by using curly braces. However to create an empty set you can only use the set construct,  curly braces alone will create an empty dictionary.

sets supports mathematical ops like:
* Unions
```
set1 = set([1,2,3])
set2 = set([4,5,6])
set1 | set2
# set ([1,2,3,4,5,6])
```
* Intersection
```
sset1 & set2
# set([3])
```
* Difference
```
set1 - set2
# set([1,2])
```
* Symmetric Difference
```
set1 ^ set2
# set([1,2,4,5])
```

#### Frozensets

A frozenset is basically like a regular set, except it's immutable It is created using the keyword ``` frozenset```, like so:
``` frozen = frozenset([1,2,3])```

Sets are used in the following situations:
* When you need a unique set of data
* When your data constantly changes(sets are mutable)
* when you need a collection that can be manipulated mathematically
* When you don't need nested lists, sets or dictionaries in a data structure.


### Tuples
A tuple is represented by a number of values seperated by commas.  Unlike lists, tuples are immutable and the output is seperated by parenthesis so that nested tuples are processed correctly.

Tuples are used in the following situations:
* When you need to store data that doesn't have to change.
* When the performance of the application is very important, in this case, use tuples when you have fixed data collections.
* When you want to store your data in logical immutable pairs, triples.....


### Dictionaries

Dictionaries are represented by a ``` key: value ``` pair. They are basically maps or associative collections.

When to use a Dictionary:
* When you need a logical association between a ```key:value``` pair.
* When you need fast lookup for your data, based on a custom key.
* When your data is being constantly modified(Dictionaries are mutable).

### NOTE:
1. Every data structure has a multitude of built in methods and capabilities.
2. Most of the time, one's data needs to adapt to the operations that one wants to perform. So if you know your object will be hashed, create an immutable structure.
3. Always find out on the performance of the data structure you choose e.g. through documentation as most structures have multiple ways of constructing or accessing data.
4.  While debugging, many devs find it useful to learn how to identify and connect the error they are receiving to a specific data structure as some structures may give different errors from the rest.
