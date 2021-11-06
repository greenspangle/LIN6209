# Practice Worksheet 4

## Section – Iteration using the keyword 'for'

Collections are iterable. That means they can be processed one element at time until the collection is
exhausted. There are two ways in which a collection can be iterated.

1. Using a while loop
2. Using a for loop

Both have features that make them preferrable or necessary in particular circumstances:

+ **while**
    + the collection must be indexable
    + order of item processing is under direct control
    + items in the collection can be replaced with a new object
    + items adjacent to the current item can be accessed and modified

+ **for**
    + simpler syntax
    + applicable to any collection
    + oder of processing is unknown and, possibly, non-repeatable
    + collection cannot be modified while iterating over it
    + there is no notion of 'adjacency' between objects

The 'for' loop is generally preferred as it has a simpler syntax and is easier to read.

### General form of _while_ loop iteration

```python
a_collection = list('abracadabra')
# while loop - generic outline
num_items = len(a_collection)  # get number of items in collection
count = 0  # create a pointer to the current item being processed
while count < num_items:
    # do whatever needs to be done to that item
    print(a_collection[count])
    # etc, etc, 
# end of while loop
```

### General form of _for_ loop iteration

```python
a_collection = list('abracadabra')
# for loop - generic outline
for each_item in a_collection:
    # do whatever needs to be done to that item
    print(each_item)
    # etc, etc, 
# end of for loop
```

### A few problems to try:

1) Create a list of every odd number less than 100.
