

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
