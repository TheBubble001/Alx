==> 1: RSA-FACTORING-CHALLENGE/README.MD <==

RSA-Factoring-Challenge




==> 2: BINARY_TREES/README.MD <==

# C - Binary trees

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files for all tasks. Provided by ALX.

## Helper File :raised_hands:

* [binary_tree_print.c](./binary_tree_print.c): C function that prints binary
trees in a pretty way.

## Header File :file_folder:

* [binary_trees.h](./binary_trees.h): Header file containing definitions and
prototypes for all types and functions written for the project.

Data Structures
```
struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

typedef struct binary_tree_s binary_tree_t;
typedef struct binary_tree_s bst_t;
typedef struct binary_tree_s avl_t;
typedef struct binary_tree_s heap_t;
```

Function Prototypes

| File                             | Prototype                                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
| `binary_tree_print.c`            | `void binary_tree_print(const binary_tree_t *tree)`                                              |
| `0-binary_tree_node.c`           | `binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);`                             |
| `1-binary_tree_insert_left.c`    | `binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value);`                      |
| `2-binary_tree_insert_right.c`   | `binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value);`                     |
| `3-binary_tree_delete.c`         | `void binary_tree_delete(binary_tree_t *tree);`                                                  |
| `4-binary_tree_is_leaf.c`        | `int binary_tree_is_leaf(const binary_tree_t *node);`                                            |
| `5-binary_tree_is_root.c`        | `int binary_tree_is_root(const binary_tree_t *node);`                                            |
| `6-binary_tree_preorder.c`       | `void binary_tree_preorder(const binary_tree_t *tree, void (*func)(int));`                       |
| `7-binary_tree_inorder.c`        | `void binary_tree_inorder(const binary_tree_t *tree, void (*func)(int));`                        |
| `8-binary_tree_postorder.c`      | `void binary_tree_postorder(const binary_tree_t *tree, void (*func)(int));`                      |
| `9-binary_tree_height.c`         | `size_t binary_tree_height(const binary_tree_t *tree);`                                          |
| `10-binary_tree_depth.c`         | `size_t binary_tree_depth(const binary_tree_t *tree);`                                           |
| `11-binary_tree_size.c`          | `size_t binary_tree_size(const binary_tree_t *tree);`                                            |
| `12-binary_tree_leaves.c`        | `size_t binary_tree_leaves(const binary_tree_t *tree);`                                          |
| `13-binary_tree_nodes.c`         | `size_t binary_tree_nodes(const binary_tree_t *tree);`                                           |
| `14-binary_tree_balance.c`       | `int binary_tree_balance(const binary_tree_t *tree);`                                            |
| `15-binary_tree_is_full.c`       | `int binary_tree_is_full(const binary_tree_t *tree);`                                            |
| `16-binary_tree_is_perfect.c`    | `int binary_tree_is_perfect(const binary_tree_t *tree);`                                         |
| `17-binary_tree_sibling.c`       | `binary_tree_t *binary_tree_sibling(binary_tree_t *node);`                                       |
| `18-binary_tree_uncle.c`         | `binary_tree_t *binary_tree_uncle(binary_tree_t *node);`                                         |
| `100-binary_trees_ancestor.c`    | `binary_tree_t *binary_trees_ancestor(const binary_tree_t *first, const binary_tree_t *second);` |
| `101-binary_tree_levelorder.c`   | `void binary_tree_levelorder(const binary_tree_t *tree, void (*func)(int));`                     |
| `102-binary_tree_is_complete.c`  | `int binary_tree_is_complete(const binary_tree_t *tree);`                                        |
| `103-binary_tree_rotate_left.c`  | `binary_tree_t *binary_tree_rotate_left(binary_tree_t *tree);`                                   |
| `104-binary_tree_rotate_right.c` | `binary_tree_t *binary_tree_rotate_right(binary_tree_t *tree);`                                  |
| `110-binary_tree_is_bst.c`       | `int binary_tree_is_bst(const binary_tree_t *tree);`                                             |
| `111-bst_insert.c`               | `bst_t *bst_insert(bst_t **tree, int value);`                                                    |
| `112-array_to_bst.c`             | `bst_t *array_to_bst(int *array, size_t size);`                                                  |
| `113-bst_search.c`               | `bst_t *bst_search(const bst_t *tree, int value);`                                               |
| `114-bst_remove.c`               | `bst_t *bst_remove(bst_t *root, int value);`                                                     |
| `120-binary_tree_is_avl.c`       | `int binary_tree_is_avl(const binary_tree_t *tree);`                                             |
| `121-avl_insert.c`               | `avl_t *avl_insert(avl_t **tree, int value);`                                                    |
| `122-array_to_avl.c`             | `avl_t *array_to_avl(int *array, size_t size);`                                                  |

## Tasks :page_with_curl:

* **0. New node**
  * [0-binary_tree_node.c](./0-binary_tree_node.c): C function that creates a
  binary tree node with a given parent and value.
  * Returns a pointer to the new node, or `NULL` on failure.

* **1. Insert left**
  * [1-binary_tree_insert](./1-binary_tree_insert): C function that inserts a
  node as the left-child of another.
  * Returns a pointer to the new node, or `NULL` on failure.
  * If the given `parent` already contains a left node, the new node takes its
  place and the old left-child becomes the left-child of the new node.

* **2. Insert right**
  * [2-binary_tree_insert_right.c](./2-binary_tree_insert_right.c): C function that
  inserts a node as the right-child of another.
  * Returns a pointer to the new node, or `NULL` on failure.
  * If the given `parent` already contains a right node, the new node takes its
  place and the old right-child becomes the right-child of the new node.

* **3. Delete**
  * [3-binary_tree_delete.c](./3-binary_tree_delete.c): C function that deletes
  an entire binary tree.

* **4. Is leaf**
  * [4-binary_tree_is_leaf.c](./4-binary_tree_is_leaf.c): C function that checks
  if a given node is a leaf.
  * Returns `1` if the node is a leaf, `0` otherwise.

* **5. Is root**
  * [5-binary_tree_is_root.c](./5-binary_tree_is_root.c): C function that checks
  if a given node is a root.
  * Returns `1` if the node is a root, `0` otherwise.

* **6. Pre-order traversal**
  * [6-binary_tree_preorder.c](./6-binary_tree_preorder.c): C function that
  traverses a tree using pre-order traversal.

* **7. In-order traversal**
  * [7-binary_tree_inorder.c](./7-binary_tree_inorder.c): C function that
  traverses a tree using in-order traversal.

* **8. Post-order traversal**
  * [8-binary_tree_postorder.c](./8-binary_tree_postorder.c): C function that
  traverses a tree using post-order traversal.

* **9. Height**
  * [9-binary_tree_height.c](./9-binary_tree_height.c): C function that returns
  the height of a binary tree.

* **10. Depth**
  * [10-binary_tree_depth.c](./10-binary_tree_depth.c): C function that returns
  the depth of a given node in a binary tree.

* **11. Size**
  * [11-binary_tree_size.c](./11-binary_tree_size.c): C function that returns
  the size of a binary tree.

* **12. Leaves**
  * [12-binary_tree_leaves.c](./12-binary_tree_leaves.c): C function that returns
  the number of leaves in a binary tree.

* **13. Nodes**
  * [13-binary_tree_nodes.c](./13-binary_tree_nodes.c): C function that returns
  the number of nodes in a binary tree with at least one child.

* **14. Balance factor**
  * [14-binary_tree_balance.c](./14-binary_tree_balance.c): C function that
  returns the balance factor of a binary tree.

* **15. Is full**
  * [15-binary_tree_is_full.c](./15-binary_tree_is_full.c): C function that
  checks if a binary tree is full.
  * Returns `1` if a tree is full, `0` otherwise.

* **16. Is perfect**
  * [16-binary_tree_is_perfect.c](./16-binary_tree_is_perfect.c): C function
  that checks if a binary tree is perfect.
  * Returns `1` if a tree is perfect, `0` otherwise.

* **17. Sibling**
  * [17-binary_tree_sibling.c](./17-binary_tree_sibling.c): C function that
  returns a pointer to the sibling of a given node in a binary tree.
  * Returns `NULL` if no sibling is found.

* **18. Uncle**
  * [18-binary_tree_uncle.c](./18-binary_tree_uncle.c): C function that
  returns a pointer to the uncle of a given node in a binary tree.
  * Returns `NULL` if no uncle is found.

* **19. Lowest common ancestor**
  * [100-binary_trees_ancestor.c](./100-binary_trees_ancestor.c): C function
  that returns a pointer to the lowest common ancestor node of two given nodes
  in a binary tree.
  * Returns `NULL` if no common ancestor is found.

* **20. Level-order traversal**
  * [101-binary_tree_levelorder.c](./101-binary_tree_levelorder.c): C function
  that traverses a binary tree using level-order traversal.

* **21. Is complete**
  * [102-binary_tree_is_complete.c](./102-binary_tree_is_complete.c): C function
  that checks if a binary tree is complete.
  * Returns `1` if the tree is complete, `0` otherwise.

* **22. Rotate left**
  * [103-binary_tree_rotate_left.c](./103-binary_tree_rotate_left.c): C function
  that performs a left-rotation on a binary tree.
  * Returns a pointer to the new root node of the tree after rotation.

* **23. Rotate right**
  * [104-binary_tree_rotate_right.c](./104-binary_tree_rotate_right.c): C function
  that performs a right-rotation on a binary tree.
  * Returns a pointer to the new root node of the tree after rotation.

* **24. Is BST**
  * [110-binary_tree_is_bst.c](./110-binary_tree_is_bst.c): C function that
  checks if a binary tree is a valid binary search tree.
  * Returns `1` if the tree is a valid BST, `0` otherwise.

* **25. BST - Insert**
  * [111-bst_insert.c](./111-bst_insert.c): C function that inserts a value into
  a binary search tree.
  * Returns a pointer to the new node, or `NULL` on failure.
  * If the tree is `NULL`, the value becomes the root node.
  * The value is ignored if it is already present in the tree.

* **26. BST - Array to BST**
  * [112-array_to_bst.c](./112-array_to_bst.c): C function that builds a binary
  search tree from an array.
  * Returns a pointer to the root node of the created tree, or `NULL` on failure.

* **27. BST - Search**
  * [113-bst_search.c](./113-bst_search.c): C function that searches for a value
  in a binary search tree.
  * If the value is matched in the BST, returns a pointer to the matched node.
  * Otherwise, returns `NULL`.

* **28. BST - Remove**
  * [114-bst_remove.c](./114-bst_remove.c): C function that removes a node from
  a binary search tree.
  * Returns a pointer to the new root node of the tree after deletion.
  * If the node to be deleted has two children, it is replaced with its first
  in-order successor.

* **29. Big O #BST**
  * [115-O](./115-O): Text file containing the average time complexities of
  binary search tree operations (one answer per line):
    * Inserting the value `n`.
    * Removing the node with the value `n`.
    * Searching for a node in a BST of size `n`.

* **30. Is AVL**
  * [120-binary_tree_is_avl.c](./120-binary_tree_is_avl.c): C function that checks if
  a binary tree is a valid AVL tree.
  * If the tree is a valid AVL tree, returns `1`.
  * Otherwise, returns `0`.

* **31. AVL - Insert**
  * [121-avl_insert.c](./121-avl_insert.c): C function that inserts a value in an AVL tree.
  * Returns a value to the inserted node, or `NULL` on failure.

* **32. AVL - Array to AVL**
  * [122-array_to_avl.c](./122-array_to_avl.c): C function that builds an AVL tree
  from an array.
  * Returns a pointer to the root node of the created AVL tree, or `NULL` on failure.
  * Ignores duplicate values.

* **35. Big O #AVL Tree**
  * [125-O](./125-O): Text file containing the average time complexities of AVL tree
  opeartions (one answer per line):
    * Inserting the value `n`.
    * Removing the node with the value `n`.
    * Searching for a node in an AVL tree of size `n`.

* **41. Big O #Binary Heap**
  * [135-O](./135-O): Text file containing the average time complexities of
  binary heap opeartions (one answer per line):
    * Inserting the value `n`.
    * Extracting the root node.
    * Searching for a node in a binary heap of size `n`.

</details>




==> 3: HIGHER_LEVEL_PROGRAMMING/README.MD <==

alx-higher_level_programming




==> 4: HIGHER_LEVEL_PROGRAMMING/0X00-PYTHON-HELLO_WORLD/README.MD <==

Scripting with bash, p
ython and 
C (it seems there's no getting rid of it)




==> 5: HIGHER_LEVEL_PROGRAMMING/0X00-PYTHON-HELLO_WORLD/WHITEBOARD.MD <==

# Function to chec[ if a singli linked list is looping

## Approach
Use a two-pointer approach (thanks leetcode!)

Basically, two pointers are defined - fast_ptr and slow_ptr. Fast_ptr is moved\
 down the loop to the next 2 pointer, slow_ptr goes on at its own pace.

A condition (while statement fits) is written to define what happens when\
fast_ptr, slow_ptr and the node of the next fast_ptr (fast_ptr is moved twice)\
 are true;
 - move fast_ptr 2 nodes up
 - slow_ptr moves at normal pace

A condition is written to handle what happend if both pointers meet/match\
 (returns 1 to signify loop matches). Close the brace of the conditon, return 0\
 to end loop and call it a day.
 



==> 6: HIGHER_LEVEL_PROGRAMMING/0X01-PYTHON-IF_ELSE_LOOPS_FUNCTIONS/README.MD <==

0x01-python-if_else_loops_functions




==> 7: HIGHER_LEVEL_PROGRAMMING/0X02-PYTHON-IMPORT_MODULES/README.MD <==

0x02-python-import_modules




==> 8: HIGHER_LEVEL_PROGRAMMING/0X03-PYTHON-DATA_STRUCTURES/README.MD <==

0x03-python-data_structures




==> 9: HIGHER_LEVEL_PROGRAMMING/0X04-PYTHON-MORE_DATA_STRUCTURES/README.MD <==

This direc directory contains more projects about python data structures.

###<u>Learning Objectives:</u>
At the end of this project, I am expected to be able to explain to anyone, without the help of Google:

* Why Python programming is awesome
* What are sets and how to use them
* What are the most common methods of set and how to use them
* When to use sets versus lists
* How to iterate into a set
* What are dictionaries and how to use them
* When to use dictionaries versus lists or sets
* What is a key in a dictionary
* How to iterate over a dictionary
* What is a lambda function
* What are the map, reduce and filter functions




==> 10: HIGHER_LEVEL_PROGRAMMING/0X05-PYTHON-EXCEPTIONS/README.MD <==

# Python - Exceptions

In this project, I learned handling errors and exceptions in Python with `try`
and `except`.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | <ul><li>`void print_python_list(PyObject *p);`</li><li>`void print_python_bytes(PyObject *p);`</li><li>`void print_python_float(PyObject *p);`</li></ul> |

## Tasks :page_with_curl:

* **0. Safe list printing**
  * [0-safe_print_list.py](./0-safe_print_list.py): Python function that prints `x` elements
  of a list on the same line, followed by a new line.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Returns the real number of elements printed.
  * Without importing modules or using `len()`.

* **1. Safe printing of an integers list**
  * [1-safe_print_integer.py](./1-safe_print_integer.py): Python function that prints an integer in `"{:d}".format()` format.
  * The parameter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer),
  `False` otherwise.
  * Without importing modules or using `type()`.

* **2. Print and count integers**
  * [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): Python function that prints the first `x` elements of a list that are integers on the same line, followed by a new line.
  * The parameter `my_list` can contain any type.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Reutnrs the real number of integers printed.
  * Without importing modules or using `len()`.

* **3. Integers division with debug**
  * [3-safe_print_division.py](./3-safe_print_division.py): Python function that divides two integers and prints the result using `finally:`.
  * The function assumes that the arguments are integers.
  * Upon success, returns the value of the division; otherwise - returns `None`.
  * Without importing modules.

* **4. Divide a list**
  * [4-list_division.py](./4-list_division.py): Python function that divides two lists element by element.
  * Returns a new list of length `list_length` with all divisions.
  * The lists `my_list_1` and `my_list_2` can contain any type.
  * The parameter `list_length` can be larger than the lengths of either list.
  * If an element is not an integer or float, the function prints `wrong type`.
  * If the division cannot be done, the result of the division is `0` and the
  function prints: `division by 0`.
  * If either of `my_list_1` or `my_list_2` are too short, the function prints:
  `out of range`.
  * Without importing modules.

* **5. Raise exception**
  * [5-raise_exception.py](./5-raise_exception.py): Python function that raises
  a type exception.
  * Without importing modules.

* **6. Raise a message**
  * [6-raise_exception_msg.py](./6-raise_exception_msg.py): Python function that raises a
  name exception with a message.
  * Without importing modules.

* **7. Safe integer print with error message**
  * [100-safe_print_integer_err.py](./100-safe_print_integer_err.py): Python function that
  prints an integer with type-checking in `"{:d}".format())` format.
  * The paramter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer).
  * Otherwise, prints an exception error to `stderr` and returns `False`.
  * Without importing modules.

* **8. Safe function**
  * [101-safe_function.py](./101-safe_function.py): Python function that executes
  a function safely.
  * The function assumes that the paramter `fct` is always a pointer to a function.
  * Upon success, returns the result of the function.
  * Otherwise, prints an en exception error to `stderr` and returns `None`.

* **9. ByteCode -> Python #4**
  * [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a
  bytecode provided by ALX.

* **10. CPython #2: PyFloatObject**
  * [103-python.c](./103-python.c): C functions that print basic information
  about Python lists, bytes, and float objects.




==> 11: HIGHER_LEVEL_PROGRAMMING/0X06-PYTHON-CLASSES/README.MD <==

# List Of Files In The Project


### 0-square.py
This is a file which contains the definition of the `Square` class which is an empty class which does nothing.

### 1-square.py
This is a file which contains the definition of the `Square` class which has the private instance variable `size`.

### 2-square.py
This is a file which contains an extended definition of the `Square` class which contains the private instance variable `size` and a property `size` aimed at validating the value of the `size` private instance variable.

### 3-square.py
Incorporates the function `area` into the definition of the `Square` class which calculates the area of the square using the `size` variable and then returns the result.

### 4-square.py
Incorporates the `size` property getter and setter to enable us update the `size` of the `Square`.

### 5-square.py
Incorporates the function `my_print` into the definition of the `Square` class which prints out the Square to the screen using the `#` character as units/symbols for the printed square.

### 6-square.py
Adds the `position` private instance variable to the definition of the `Square` class and provides the getters and setters for it.

### 100-singly_linked_list.py
Implements a singly linked list in python using the Object Oriented features of the language.

###     




==> 12: HIGHER_LEVEL_PROGRAMMING/0X07-PYTHON-TEST_DRIVEN_DEVELOPMENT/README.MD <==

Test Driven Development (TDD)




==> 13: HIGHER_LEVEL_PROGRAMMING/0X08-PYTHON-MORE_CLASSES/README.MD <==

# List of Programs In The Project

### 0-rectangle.py
Contains the definition of an empty class `Rectangle`.

### 1-rectangle.py
Contains the definition of a version of the class `Rectangle` with the `width` and `height` properties defined.

### 2-rectangle.py
Contains the definition of a version of the class `Rectangle` with the `area` and `perimeter` instance methods provided for determining the `area` and `perimeter` respectively of the rectangle.

### 3-rectangle.py
Contains the definition of a version of the class `Rectangle` which defines functionality that enables it's shape to be printed out to the screen by the `str` and `print` functions.

### 4-rectangle.py
Contains the definition of a version of the class `Rectangle` which defines the `__str__` and `__repr__` special methods for unofficial and official representation of the rectangle.

### 5-rectangle.py
Contains the definition of a version of the `Rectangle` class which prints the message; `Bye rectangle...` whenever an instance of a `Rectangle` is deleted.

### 6-rectangle.py
Contains the definition of a version of the `Rectangle` class which keeps a count of all instances of the class that have been created, incrementing or decrementing that count as the need arises.

### 7-rectangle.py
Contains the definition of a version of the `Rectangle` class which enables us to change the symbols which are used to represent the rectangle when it is being printed to the screen.

### 8-rectangle.py
Contains the definition of a version of the `Rectangle` class which contains the static method `bigger_or_equal` which is used to determine which among two Rectangles passed into it as arguments is bigger.

### 9-rectangle.py
Contains the definition of a version of the `Rectangle` class which contains the class method `square` which creates a Rectangle of equal `width` and `height`. Hence it uses the `Rectangle` class in order to create a `Square`.

###    




==> 14: HIGHER_LEVEL_PROGRAMMING/0X09-PYTHON-EVERYTHING_IS_OBJECT/README.MD <==

# List Of Files In The Project

### 




==> 15: HIGHER_LEVEL_PROGRAMMING/0X0A-PYTHON-INHERITANCE/README.MD <==

# Python - Inheritance

In this project, I learned about Python class inheritance. I learned about the
differences between super- and sub-classes while practicing inheritance,
definining classes with multiple base classes, and overiding inherited methods
and attributes.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files provided by ALX, as well as the following two independently-developed:
    * [1-my_list.txt](./1-my_list.txt)
    * [7-base_geometry.txt](./7-base_geometry.txt)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

## Tasks :page_with_curl:

* **0. Lookup**
  * [0-lookup.py](./0-lookup.py): Python function that returns a list of available attributes
  and methods of an objects.

* **1. My list**
  * [1-my_list.py](./1-my_list.py): Python class `MyList` that inherits from `list`. Includes:
    * Public instance method `def print_sorted(self):` that prints the list in
    ascending sorted order (assumes all list elements are `int`s).

* **2. Exact same object**
  * [2-is_same_class.py](./2-is_same_class.py): Python function that returns `True` if an object is
  exactly an instance of a specified class; otherwise `False`.

* **3. Same class or inherit from**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py): Python function that returns `True` if an object is
  an instance or inherited instance of a specified class; otherwise `False`.

* **4. Only sub class of**
  * [4-inherits_from.py](./4-inherits_from.py): Python function that returns `True` if an object is
  an inherited instance (either directly or indirectly) from a specified class;
  otherwise `False`.

* **5. Geometry module**
  * [5-base_geometry.py](./5-base_geometry.py): An empty Python class `BaseGeometry`.

* **6. Improve Geometry**
  * [6-base_geometry.py](./6-base_geometry.py): Python class `BaseGeometry`. Builds on
  [5-base_geometry.py](./5-base_geometry.py) with:
    * Public instance method `def area(self):` that raises an `Exception` with
    the message `area() is not implemented`.

* **7. Integer validator**
  * [7-base_geometry.py](./7-base_geometry.py): Python class `BaseGeometry`. Builds on
  [6-base_geometry.py](./6-base_geometry.py) with:
    * Public instance method `def integer_validator(self, name, value):` that
    validates the parameter `value`.
    * Assumes the parameter `name` is always a string.
    * The parameter `value` must be an `int`, otherwise, a `TypeError` exception
    is raised with the message `<name> must be an integer`.
    * The parameter `value` must be greater than `0`, otherwise, a
    `ValueError` exception is raised with the message `<value> must be greater
    than 0`.

* **8. Rectangle**
  * [8-rectangle.py](./8-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry`
  ([7-base_geometry.py](./7-base_geometry.py)). Includes:
    * Private attributes `width` and `height` - validated with `integer_validator`.
    * Instantiation with `width` and `height`: `def __init__(self, width, height):`

* **9. Full rectangle**
  * [9-rectangle.py](./9-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry`
  ([7-base_geometry.py](./7-base_geometry.py)). Builds on [8-rectangle.py](./8-rectangle.py) with:
    * Implementation of the method `area()`.
    * Special method `__str__` to print `Rectangle`s in the format `[Rectangle]
    <width>/<height>`.

* **10. Square #1**
  * [10-square.py](./10-square.py): Python class `Square` that inherits from `Rectangle`
  ([9-rectangle.py](./9-rectangle.py)). Includes:
    * Private attribute `size` - validated with `integer_validator`.
    * Instantiation with `size`: `def __init__(self, size):`.
    * Implementation of the `area()` method.

* **11. Square #2**
  * [11-square.py](./11-square.py): Python class `Square` that inherits from `Rectangle`
  ([9-rectangle.py](./9-rectangle.py)). Builds on [10-square.py](./10-square.py) with:
    * Special method `__str__` to print squares in the format `[Square]
    <width>/<height>`.

* **12. My integer**
  * [100-my_int.py](./100-my_int.py): Python class `MyInt` that inherits from `int`. Includes:
    * Inversion of the `==` and `!=` operators.

* **13. Can I?**
  * [101-add_attribute.py](./101-add_attribute.py): Python function that adds a new attribute to an
  object if possible.
    * If an attribute cannot be added, a `TypeError` exception is raised with the
    message `can't add new attribute`.




==> 16: HIGHER_LEVEL_PROGRAMMING/0X0B-PYTHON-INPUT_OUTPUT/README.MD <==

# List Of Files In The Project

## Code Files

### 0-read_file.py
contains the definition of the function `read_file` which takes the name of a file as it's argument, reads it's contents and prints out those contents to the standard output.

### 1-write_file.py
contains the definition of the function `write_file` which takes the name of a file `filename` and a string `text` as it's arguments and writes the contents of `text` to `filename`. Returns the number of characters written each time the program is run.

### 2-append_write.py
contains the definition of the function `append_write` which takes the name of a file `filename` and a string `text` as it's arguments and appends `text` to `filename`. Returns the number of characters appended each time the program is run.

### 3-to_json_string.py
contains the definition of the function `to_json_string` which takes a single object as it's argument and returns the JSON string representation of that object.

### 4-from_json_string.py
contains the definition of the function `from_json_string` which takes a single JSON string as it's argument and then returns the object that it represents.

### 5-save_to_json_file.py
contains the definition of the function `save_to_json_file` which takes an object `my_obj` and a file name `filename` as it's arguments and saves the JSON string representation of `my_obj` to the file named `filename`.

### 6-load_from_json_file.py
contains the definition of the  function `load_from_json_file` which takes a file name `filename` as it's single argument and returns an object based on the JSON string found in the file.

### 7-add_item.py
A script that updates a file containing the JSON string representation of a list with a new item (supplied from the command line).

### 8-class_to_json.py
outputs a dictionary containing all the attributes in the class.

### 9-student.py

### 10-student.py

### 11-student.py

### 12-pascal_triangle.py
returns a 2D list which contains a pascal triangle.

###       




==> 17: HIGHER_LEVEL_PROGRAMMING/0X0C-PYTHON-ALMOST_A_CIRCLE/README.MD <==

# List Of Files In This Project

## Code Files

### models/base.py
contains the definition of the `Base` class which is to serve as the base or super class from which all the other classes in this project will inherit from.

### models/rectangle.py
contains the definition of the `Rectangle` class which is a subclass of the `Base` class. 

### models/square.py
contains the definition of the `Square` class which is a subclass of the `Rectangle` class.

###

## Test Files

### tests/test_models/test_base.py
this is the test file created for the sole purpose of unit testing the `Base` class defined in the `base.py` file.

### tests/test_models/test_rectangle.py
this is the test file created for the sole purpose of unit testing the `Rectangle` class defined in the `rectangle.py` file.

### tests/test_models/test_square.py
this is the test file created for the sole purpose of unit testing the `Square` class defined in the `square.py` file.

### 




==> 18: HIGHER_LEVEL_PROGRAMMING/0X0D-SQL_INTRODUCTION/README.MD <==

# SQL - Introduction

This is my first project in which I began to work with SQL and relational databases. I began practicing introductory data definition and data
manipulation language, making subqueries, and using functions.

## Usage :dolphin:

* Scripts [3-list_tables.sql](./3-list_tables.sql) forward take the database to query
from MySQL command line argument.

```
$ cat 3-list_tables.sql | mysql -h localhost -u root -p mysql
```

* Tasks 101-103 query from the database [temperatures.sql](./temperatures.sql).

## Tasks :page_with_curl:

* **0. List databases**
  * [0-list_databases.sql](./0-list_databases.sql): MySQL script that lists all databases.

* **1. Create a database**
  * [1-create_database.sql](./1-create_database.sql): MySQL script that creates the database
  `hbtn_0c_0`.

* **2. Delete a database**
  * [2-remove_databases.sql](./2-remove_databases.sql): MySQL script that deletes the database
  `hbtn_0c_0`.

* **3. List tables**
  * [3-list_tables.sql](./3-list_tables.sql): MySQL script that lists all tables.

* **4. First table**
  * [4-first_table.sql](./4-first_table.sql): MySQL script that creates a table `first_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)

* **5. Full description**
  * [5-full_table.sql](./5-full_table.sql): MySQL script that prints the full description of the
  table `first_table`.

* **6. List all in table**
  * [6-list_values.sql](./6-list_values.sql): MySQL script that lists all rows of the table
  `first_table`.

* **7. First add**
  * [7-insert_value.sql](./7-insert_value.sql): MySQL script that inserts a new row in the table
  `first_table`.
  * Description:
    * `id` = `89`
    * `name` = `Best School`

* **8. Count 89**
  * [8-count_89.sql](./8-count_89.sql): MySQL script that displays the number records with `id =
  89` in the table `first_table`.

* **9. Full creation**
  * [9-full_creation.sql](./9-full_creation.sql): MySQL script that creates and fills a table
  `second_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

* **10. List by best**
  * [10-top_score.sql](./10-top_score.sql): MySQL script that lists the `score` and `name` of all
  records of the table `second_table` in order of descending `score`.

* **11. Select the best**
  * [11-best_score.sql](./11-best_score.sql): MySQL script that lists the `score` and `name` of all
  records with a `score >= 10` in the table `second_table` in order of descending score.

* **12. Cheating is bad**
  * [12-no_cheating.sql](./12-no_cheating.sql): MySQL script that updates the score of Bob to 10
  the table `second_table`.

* **13. Score too low**
  * [13-change_class.sql](./13-change_class.sql): MySQL script that removes all records with a
  `score <= 5` in the table `second_table`.

* **14. Average**
  * [14-average.sql](./14-average.sql): MySQL script that computes the average `score` of all
  records in the table `second_table`.

* **15. Number by score**
  * [15-groups.sql](./15-groups.sql): MySQL script that lists the `score` and number of records
  with the same score in the table `second_table` in order of descending count.

* **16. Say my name**
  * [16-no_link.sql](./16-no_link.sql): MySQL script that lists the `score` and `name` of all
  records in the table `second_table` in order of descending `score`.
  * Does not display rows without a `name` value.

* **17. Go to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): MySQL script that converts the `hbtn_0c_0`
  database to UTF8.

[This link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) was used for the following tasks:

* **18. Temperatures #0**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): MySQL script that displays the average
  temperature (Fahrenheit) by city in descending order.

* **19. Temperatures #1**
  * [102-top_city.sql](./102-top_city.sql): MySQL script that displays the three cities with the
  highest average temperature from July to August in descending order.

* **20. Temperature #2**
  * [103-max_state.sql](./103-max_state.sql): MySQL script that displays the max temperature of each
  )state in order of state nam




==> 19: HIGHER_LEVEL_PROGRAMMING/0X0E-SQL_MORE_QUERIES/README.MD <==

# SQL - More queries

In this project, I continued to practicing SQL queries, working with
permissoins, joins, and constraints.

## Usage :dolphin:

* Scripts [3-force_name.sql](./3-force_name.sql) forward take the database to query from
as a MySQL command line argument.

```
$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

* Tasks 10-101 query from the database [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql).
* Tasks 102-103 query from the database [hbtn_0d_tvshows_rate.sql](./hbtn_0d_tvshows_rate.sql).

## Tasks :page_with_curl:

* **0. My privileges!**
  * [0-privileges.sql](./0-privileges.sql): MySQL script that lists all privileges of the users
  `user_0d_1` and `user_0d_2`.

* **1. Root user**
  * [1-create_user.sql](./1-create_user.sql): MySQL script that creates the user `user_0d_1` with
  all privileges and password `user_0d_1_pwd`.

* **2. Read user**
  * [2-create_read_user.sql](./2-create_read_user.sql): MySQL script that creates the database
  `hbtn_0d_2` and user `user_0d_2` with password `user_0d_2_pwd`.
  * `user_0d_2` only has SELECT privilege on the database `hbtn_0d_2`.

* **3. Always a name**
  * [3-force_name.sql](./3-force_name.sql): MySQL script that creates the table `force_name`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256) (cannot be null)

* **4. ID can't be null**
  * [4-never_empty.sql](./4-never_empty.sql): MySQL script that creates the table `id_not_null`.
  * Description:
    * `id`: INT (default value = 1)
    * `name`: VARCHAR(256)

* **5. Unique ID**
  * [5-unique_id.sql](./5-unique_id.sql): MySQL script that creates the table `unique_id`.
  * Description:
    * `id`: INT (default value = 1, must be unique)
    * `name`: VARCHAR(256)

* **6. States table**
  * [6-states.sql](./6-states.sql): MySQL script that creates the database `hbtn_0d_usa`
  with a table `states`.
  * `states` description:
    * `id`: INT (unique, auto-generated, cannot be null and is a primary key)
    * `name`: VARCHAR(256) (cannot be null)

* **7. Cities table**
  * [7-cities.sql](./7-cities.sql): MySQL script that creates the database `hbtn_0d_usa`
  with a table `cities`.
  * `cities` description:
    * `id`: INT (unique, auto-generated, cannot be null and is a primary key)
    * `state_id`: INT (cannot be null, foreign key that references to id of the
    `states` table)
    * `name`: VARCHAR(256) (cannot be null)

* **8. Cities of California**
  * [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql):
  MySQL script that lists all the cities of California that can be found in the
  database `hbtn_0d_usa`, ordered by ascending city id.

* **9. Cities by States**
  * [9-cities_by_state_join.sql](./9-cities_by_state_join.sql): MySQL script that lists
  all cities contained in the database `hbtn_0d_usa`, ordered by ascending city id.

* **10. Genre ID by show**
  * [10-genre_id_by_show.sql](./10-genre_id_by_show.sql): MySQL script that lists all
  shows contained in `hbtn_0d_tvshows` that have at least one genre linked, in order of ascending
`tv_shows.title` and `tv_show_genres.genre_id`.

* **11. Genre ID for all shows**
  * [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql): MySQL script that lists all shows contained
  in the database `hbtn_0d_tvshows`, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`.
  * If a show does not have a genre, displays `NULL`.

* **12. No genre**
  * [12-no_genre.sql](./12-no_genre.sql): MySQL script that lists all shows contained in
  `hbtn_0d_tvshows` without a genre linked, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`.

* **13. Number of shows by genre**
  * [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql): MySQL script that lists all genres from
  `hbtn_0d_tvshows` and displays the number of shows linked to each, in order of descending number of shows linked.
  * Does not display a genre if it has no linked shows.

* **14. My genres**
  * [14-my_genres.sql](./14-my_genres.sql): MySQL script that uses the `hbtn_0d_tvshows` database
  to list all genres of the show Dexter, in order of ascending genre name.

* **15. Only Comedy**
  * [15-comedy_only.sql](./15-comedy_only.sql): MySQL script that lists all comedy shows in the
  database `hbtn_0d_tvshows`, in order of ascending show title.

* **16. List shows and genres**
  * [16-shows_by_genre.sql](./16-shows_by_genre.sql): MySQL script that lists all shows, and all genres
  linked to that show, from the database `hbtn_0d_tvshows`, in order of ascending show title and genre name.

* **17. Not my genre**
  * [100-not_my_genres.sql](./100-not_my_genres.sql`) MySQL script that uses the `hbtn_0d_tvshows`
  database to list all genres not linked to the show Dexter, in order of ascending genre name.

* **18. No Comedy tonight!**
  * [101-not_a_comedy.sql](./101-not_a_comedy.sql): MySQL script that lists all shows without the
  genre comedy in the database `hbtn_0d_tvshows`, in order of ascending show title.

* **19. Rotten tomatoes**
  * [102-rating_shows.sql](./102-rating_shows.sql): MySQL script that lists all shows from
  `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.

* **20. Best genre**
  * [103-rating_genres.sql](./103-rating_genres.sql): MySQL script that lists all genres in the
  database `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.




==> 20: LOW_LEVEL_PROGRAMMING/README.MD <==

low level programming in C




==> 21: LOW_LEVEL_PROGRAMMING/0X00-HELLO_WORLD/README.MD <==

c Hello world




==> 22: LOW_LEVEL_PROGRAMMING/0X01-VARIABLES_IF_ELSE_WHILE/README.MD <==

variables, if... else ....while




==> 23: LOW_LEVEL_PROGRAMMING/0X02-FUNCTIONS_NESTED_LOOPS/README.MD <==

functions_nested_loops




==> 24: LOW_LEVEL_PROGRAMMING/0X03-DEBUGGING/README.MD <==

This task exposes us to the debugging processes and techniques.




==> 25: LOW_LEVEL_PROGRAMMING/0X04-MORE_FUNCTIONS_NESTED_LOOPS/README.MD <==

0x04-more_functions_nested_loops




==> 26: LOW_LEVEL_PROGRAMMING/0X05-POINTERS_ARRAYS_STRINGS/README.MD <==

These are tasks about pointers and arrays of the popular LLPL (C)




==> 27: LOW_LEVEL_PROGRAMMING/0X06-POINTERS_ARRAYS_STRINGS/README.MD <==

0x06-pointers_arrays_strings,we move!




==> 28: LOW_LEVEL_PROGRAMMING/0X07-POINTERS_ARRAYS_STRINGS/README.MD <==

This directory contains some practice tasks about
Pointers to pointers (to pointers),
*p,**p,***p,
It is a continuation of the C pointers and arrays.
It also contains tasks about arrays (2 dimensional and multidimensional arrays).




==> 29: LOW_LEVEL_PROGRAMMING/0X08-RECURSION/README.MD <==

This repo contains task about C recursion (excercises)




==> 30: LOW_LEVEL_PROGRAMMING/0X09-STATIC_LIBRARIES/README.MD <==

The file libmy.a is a static library as requested by the project.

The file  create_static_lib.sh is a script that creates a static library called liball.a from the  \*.c files that are in the current directory.

While main.h is a header file that contains all the prototypes of the functions stored in the libmy.a library.




==> 31: LOW_LEVEL_PROGRAMMING/0X0A-ARGC_ARGV/README.MD <==

In this repo I will be submitting project task on the followings:
How to use arguments passed to your program
What are two prototypes of main that you know of, and in which case do you use one or the other
How to use __attribute__((unused)) or (void) to compile functions with unused variables or parameters




==> 32: LOW_LEVEL_PROGRAMMING/0X0B-MALLOC_FREE/README.MD <==

user defined memory allocation




==> 33: LOW_LEVEL_PROGRAMMING/0X0C-MORE_MALLOC_FREE/README.MD <==

More about dynamic memory allocation.




==> 34: LOW_LEVEL_PROGRAMMING/0X0D-PREPROCESSOR/README.MD <==

This directory contain projects about C Pre-processors, CPP




==> 35: LOW_LEVEL_PROGRAMMING/0X0E-STRUCTURES_TYPEDEF/README.MD <==

header file (dog.h):
Define a new type struct dog with the following elements:

name, type = char *
age, type = float
owner, type = char *

Task 1:
Write a function that initialize a variable of type struct dog

Prototype: void init_dog(struct dog \*d, char \*name, float age, char \*owner);




==> 36: LOW_LEVEL_PROGRAMMING/0X0F-FUNCTION_POINTERS/README.MD <==

Function pointers




==> 37: LOW_LEVEL_PROGRAMMING/0X10-VARIADIC_FUNCTIONS/README.MD <==

Vaiadic (varargs) functions are functions that take variable number of arguments

File 0-sum_them_all.c is a function that returns the sum of all its parameters.

File 1-print_numbers.c is a function that prints numbers, followed by a new line.

File 2-print_strings.c is a function that prints strings, followed by a new line.

File 3-print_all.c is a function that prints anything.

File variadic_functions.h is the header file that contains all the function prototypes.




==> 38: LOW_LEVEL_PROGRAMMING/0X12-SINGLY_LINKED_LISTS/README.MD <==

# 0x12 C - Singly linked lists
This directory contains some tasks to see how linked lists work;




==> 39: LOW_LEVEL_PROGRAMMING/0X13-MORE_SINGLY_LINKED_LISTS/README.MD <==

This is additional projects about the previous **Singly Linked Lists**
It is meant to teach us more of it;
therefore named **More Singly Linked Lists**




==> 40: LOW_LEVEL_PROGRAMMING/0X14-BIT_MANIPULATION/README.MD <==

# 0x14. C - Bit manipulation
* This sectino train  us on how to work and manipulate bits using several techniques;
* Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter
than a word.




==> 41: LOW_LEVEL_PROGRAMMING/0X15-FILE_IO/README.MD <==

0x15-file_io




==> 42: LOW_LEVEL_PROGRAMMING/0X17-DOUBLY_LINKED_LISTS/README.MD <==

0x17-Doubly_linked_list




==> 43: LOW_LEVEL_PROGRAMMING/0X18-DYNAMIC_LIBRARIES/README.MD <==

Dynamic library




==> 44: LOW_LEVEL_PROGRAMMING/0X1A-HASH_TABLES/README.MD <==

# C - Hash tables

In this project, I learned about hashing by implementing hash functions
and hash tables in C.

## Header File :file_folder:

* [hash_tables.h](./hash_tables.h): Header file containing definitions and prototypes for
all types and functions written for the project.

Data Structures:
```
typedef struct hash_node_s
{
	char *key;
	char *value;
	struct hash_node_s *next;
} hash_node_t;

typedef struct hash_table_s
{
	unsigned long int size;
	hash_node_t **array;
} hash_table_t;

typedef struct shash_node_s
{
	char *key;
	char *value;
	struct shash_node_s *next;
	struct shash_node_s *sprev;
	struct shash_node_s *snext;
} shash_node_t;

typedef struct shash_table_s
{
	unsigned long int size;
	shash_node_t **array;
	shash_node_t *shead;
	shash_node_t *stail;
} shash_table_t;
```

Function Prototypes:

| File | Prototype |
| --- | --- |
| `0-hash_table_create.c` | `hash_table_t *hash_table_create(unsigned long int size);` |
| `1-djb2.c` | `unsigned long int hash_djb2(const unsigned char *str);` |
| `2-key_index.c` | `unsigned long int key_index(const unsigned char *key, unsigned long int size);` |
| `3-hash_table_set.c` | `int hash_table_set(hash_table_t *ht, const char *key, const char *value);` |
| `4-hash_table_get.c` | `char *hash_table_get(const hash_table_t *ht, const char *key);` |
| `5-hash_table_print.c` | `void hash_table_print(const hash_table_t *ht);` |
| `6-hash_table_delete.c` | `void hash_table_delete(hash_table_t *ht);` |
| `100-sorted_hash_table.c` | `shash_table_t *shash_table_create(unsigned long int size);` |
| | `int shash_table_set(shash_table_t *ht, const char *key, const char *value);` |
| | `char *shash_table_get(const shash_table_t *ht, const char *key);` |
| | `void shash_table_print(const shash_table_t *ht);` |
| | `void shash_table_print_rev(const shash_table_t *ht);` |
| | `void shash_table_delete(shash_table_t *ht);` |

## Tasks :page_with_curl:

* **0. >>> ht = {}**
  * [0-hash_table_create.c](./0-hash_table_create.c): C function that creates a `hash_table_t`
  hash table.
    * If the function fails - returns `NULL`.
    * Otherwise - returns a pointer to the new hash table.

* **1. djb2**
  * [1-djb2.c](./1-djb2.c): C function that implements the djb2 hashing algorithm.

* **2. key -> index**
  * [2-key_index.c](./2-key_index.c): C function that returns the index at which a key/value
  pair should be stored in the array of a `hash_table_t` hash table.

* **3. >>> ht['betty'] = 'cool'**
  * [3-hash_table_set.c](./3-hash_table_set.c): C function that adds an element to a
  `hash_table_t` table.
    * The parameter `key` cannot be an empty string.
    * Returns `1` on success, `0` otherwise.

* **4. >>> ht['betty']**
  * [4-hash_table_get.c](./4-hash_table_get.c): C function that retrieves a value associated
  with a key in a `hash_table_t` hash table.
    * If `key` cannot be matched - returns `NULL`.
    * Otherwise - returns the value associated with `key`.

* **5. >>> print(ht)**
  * [5-hash_table_print.c](./5-hash_table_print.c): C function that prints a `hash_table_t`
  hash table.
    * Prints each `key`/`value` pair in the order they appear in the array of the hash table.
    * Does not print anything if the hash table is `NULL`.

* **6. >>> del ht**
  * [6-hash_table_delete.c](./6-hasb_table_delete.c): C function that deletes a
  `hash_table_t` hash table.

* **7. $ht['Betty'] = 'Cool'**
  * [100-sorted_hash_table.c](./100-sorted_hash_table.c): C functions that define a sorted
  hash table `shash_table_t`.
    * Identical in function to a `hash_table_t` hash table except key/value
    pairs are inserted in alphabetical order according to the ASCII value of the key.
    * Key/value pairs are printed in the order they are sorted.
    * Includes a function `shash_table_print_rev()` that prints the hash table
    in reverse order.




==> 45: LOW_LEVEL_PROGRAMMING/0X1C-MAKEFILES/README.MD <==

# C - Makefiles

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files.

## Helper Files :raised_hands:

* [school.c](./school.c): C function that displays a seahorse in text.
Used for Makefile practice purposes throughout project.

* [main.c](./main.c): Main C function that runs the function defined in
[school.c](./school.c).

## Header File :file_folder:

* [m.h](./m.h): Header file defining the function prototype used in `school.c`.

## Tasks :page_with_curl:

* **0. make -f 0-Makefile**
  * [0-Makefile](./0-Makefile): Makefile that creates an executable `school` based on
  [school.c](./school.c) and [main.c](./main.c). Includes:
    * Rule `all` that builds the executable.

* **1. make -f 1-Makefile**
  * [1-Makefile](./1-Makefile): Makefile that creates an executable `school` based on
  [school.c](./school.c) and [main.c](./main.c). Builds on [0-Makefile](./0-Makefile)
  with:
    * Variable `CC` that defines the compiler to be used.
    * Variable `SRC` that defines the `.c` files to compile.
    * The `all` rule only recompiles updated source files.

* **2. make -f 2-Makefile**
  * [2-Makefile](./2-Makefile): Makefile that creates an executable `school` based on
  [school.c](./school.c) and [main.c](./main.c). Builds on [1-Makefile](./1-Makefile)
  with:
    * Variable `OBJ` that defines the `.o` files to compile.
    * Variable `NAME` that defines the name of the executable.

* **3. make -f 3-Makefile**
  * [3-Makefile](./3-Makefile): Makefile that creates an executable `school` based on
  [school.c](./school.c) and [main.c](./main.c). Builds on [2-Makefile](./2-Makefile)
  with:
    * Rule `clean` that deletes all Emacs/Vim temporary files as well as the
    executable.
    * Rule `oclean` that deletes the object files.
    * Rule `fclean` that deltes all of the temporary files, executable, and
    object files.
    * Rule `re` that forces recompilation of all source files.
    * Variable `RM` that defines the command to delete files.

* **4. A complete Makefile**
  * [4-Makefile](./4-Makefile): Makefile that creates an executable `school` based on
  [school.c](./school.c) and [main.c](./main.c). Builds on [3-Makefile](./3-Makefile)
  with:
    * Variable `CFLAGS` that defines the compiler flags `-Wall -Werror -Wextra
    -pedantic`.

* **5. Island Perimeter**
  * [5-island_perimeter.py](./5-island_perimeter.py): Python function that returns the
  perimeter of an island defined in a grid.
  * Prototype: `def island_perimeter(grid):`
  * The parameter `grid` is a list of a list of integers.
    * Water is represented by `0`.
    * Land is represented by `1`.
    * Each element of the lists represents a cell square of side length 1.
    * Grid cells are connected horizontally/verticaly (not diagonally).
    * The grid is rectangular, with a width and height not exceeding 100.
    * The grid is completely surrounded by water, and there is either exactly
    one island or nothing.
    * The island does not contain lakes (water inside disconnected from
    surrounding land).

* **6. make -f 100-Makefile**
  * [100-Makefile](./100-Makefile): Makefile that creates an executable `school` based on
  [school.c](./school.c) and [main.c](./main.c). Builds on [4-Makefile](./4-Makefile)
  with:
    * Does not define the variable `RM`.
    * Never uses the string `$(CFLAGS)`.
    * Does not compile if the header `m.h` is missing.
    * Works even if there are existing files of the same name as any of the
    Makefile rules in the current directory.




==> 46: LOW_LEVEL_PROGRAMMING/TESTING/README.MD <==

test files for printf project




==> 47: MONTY/README.MD <==

Our Monty Team Project




==> 48: MONTY/BF/README.MD <==

Brainf*ck Still Team Project




==> 49: PRINTF/README.MD <==

the printf project
life




==> 50: SIMPLE_SHELL/README.MD <==

readme




==> 51: SORTING_ALGORITHMS/README.MD <==

# C - Sorting algorithms & Big O

This is an algorithm-based project in C Programming Language, by **Mubarak Dederi** during the Full Stack Software Engineering studies at **ALX**. Several sorting algorithms are implemented, as well as their corresponding Big O notations.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. 

## Helper Files :raised_hands:

* [print_array.c](./print_array.c): C function that prints an array of integers. 
* [print_list.c](./print_list.c): C function that prints a `listint_t` doubly-linked list. 

## Header Files :file_folder:

* [sort.h](./sort.h): Header file containing definitions and prototypes for all types and functions written for the project.

Data Structure:
```
typedef struct listint_s
{
	const int n;
	struct listint_s *prev;
	struct listint_s *next;
} listint_t;
```

Function Prototypes:

| File                       | Prototype                                         |
| -------------------------- | ------------------------------------------------- |
| `print_array.c`            | `void print_array(const int *array, size_t size)` |
| `print_list.c`             | `void print_list(const listint_t *list)`          |
| `0-bubble_sort.c`          | `void bubble_sort(int *array, size_t size);`      |
| `1-insertion_sort_list.c`  | `void insertion_sort_list(listint_t **list);`     |
| `2-selection-sort.c`       | `void selection_sort(int *array, size_t size);`   |
| `3-quick_sort.c`           | `void quick_sort(int *array, size_t size);`       |
| `100-shell_sort.c`         | `void shell_sort(int *array, size_t size);`       |
| `101-cocktail_sort_list.c` | `void cocktail_sort_list(listint_t **list);`      |
| `102-counting_sort.c`      | `void counting_sort(int *array, size_t size);`    |
| `103-merge_sort.c`         | `void merge_sort(int *array, size_t size);`       |
| `104-heap_sort.c`          | `void heap_sort(int *array, size_t size);`        |
| `105-radix_sort.c`         | `void radix_sort(int *array, size_t size);`       |
| `106-bitonic_sort.c`       | `void bitonic_sort(int *array, size_t size);`     |
| `107-quick_sort_hoare.c`   | `void quick_sort_hoare(int *array, size_t size);` |

* [deck.h](./deck.h): Header file containing definitions and prototypes for all types and functions written for the task `1000-sort_deck.c`.

Data Structures:
```
typedef enum kind_e
{
	SPADE = 0,
	HEART,
	CLUB,
	DIAMOND
} kind_t;

typedef struct card_s
{
	const char *value;
	const kind_t kind;
} card_t;

typedef struct deck_node_s
{
	const card_t *card;
	struct deck_node_s *prev;
	struct deck_node_s *next;
} deck_node_t;
```

Function Prototype:

| File               | Prototype                             |
| ------------------ | ------------------------------------- |
| `1000-deck_node.c` | `void sort_deck(deck_node_t **deck);` |

## Tasks :page_with_curl:

* **0. Bubble sort**
  * [0-bubble_sort.c](./0-bubble_sort.c): C function that sorts an array of integers in ascending order using the Bubble Sort algorithm.
  * Prints the array after each swap.
  * [0-O](./0-O): Text file containing the best, average, and worst case time complexities of the Bubble Sort algorithm, one per line.

* **1. Insertion sort**
  * [1-insertion_sort_list.c](./1-insertion_sort_list.c): C function that sorts a `listint_t` doubly-linked list of integers in ascending order using the
  Insertion Sort algorithm.
  * Prints the list after each swap.
  * [1-O](./1-O): Text file containing the best, average, and worst case time complexities of the Insertion Sort algorithm, one per line.

* **2. Selection sort**
  * [2-selection_sort.c](./2-selection_sort.c): C function that sorts an array of integers in ascending order using the Selection Sort algorithm.
  * Prints the array after each swap.
  * [2-O](./2-O): Text file containing the best, average, and worst case time complexities of the Selection Sort algorithm, one per line.

* **3. Quick sort**
  * [3-quick_sort.c](./3-quick_sort.c): C function that sorts an array of integers in ascending order using the Quick Sort algorithm.
  * Implements the Lomuto partition scheme.
  * Always uses the last element of the partition being sorted as the pivot.
  * Prints the array after each swap.
  * [3-O](./3-O): Text file containing the best, average, and worst case time complexities of the Quick Sort Lomuto Partition scheme algorithm, one per line.

* **4. Shell sort - Knuth Sequence**
  * [100-shell_sort.c](./100-shell_sort.c): C function that sorts an array of integers in ascending order using the Shell sort algorithm.
  * Implements the Knuth interval sequence.
  * Prints the array each time the interval is decreased.

* **5. Cocktail shaker sort**
  * [101-cocktail_sort_list.c](./101-cocktail_sort_list.c): C function that sorts
  a `listint_t` doubly-linked list of integers in ascending order using the Cocktail Shaker Sort algorithm.
  * Prints the list after each swap.
  * [101-O](./101-O): Text file containing the best, average, and worst case time complexities of the Cocktail Shaker Sort algorithm, one per line.

* **6. Counting sort**
  * [102-counting_sort.c](./102-counting_sort.c): C function that sorts an array of integers in ascending order using the Counting Sort algorithm.
  * Assumes that the array will only contain numbers `>= 0`.
  * Prints the counting array after it has been initialized.
  * [102-O](./102-O): Text file containing the best, average, and worst case time complexities of the Counting Sort algorithm, one per line.

* **7. Merge sort**
  * [103-merge_sort.c](./103-merge_sort.c): C function that sorts an array of integers in ascending order using the Merge Sort algorithm.
  * Implements the `top-down` Merge Sort algorithm.
    * When an array is divided, the size of the left subarray is always less than or equal to the size of the right subarray.
    * Always sorts the left subarray before the right one.
  * Prints subarrays each time they are merged.
  * [103-O](./103-O): Text file containing the best, average, and worst case time complexities of the Merge Sort algorithm, one per line.

* **8. Heap sort**
  * [104-heap_sort.c](./104-heap_sort.c): C function that sorts an array of integers in ascending order using the Heap Sort algorithm.
  * Implements the `sift-down` Heap Sort algorithm.
  * Prints the array after each swap.
  * [104-O](./104-O): Text file containing the best, average, and worst case time complexiites of the Heap Sort algorithm, one per line.

* **9. Radix sort**
  * [105-radix_sort.c](./105-radix_sort.c): C function that sorts an array of integers in ascending order using the Radix Sort algorithm.
  * Implements the Least-Significant-Digit (LSD) Radix Sort algorithm.
  * Assumes that the array will only contain numbers `>= 0`.
  * Prints the array for each significant digit increase.
  * [105-O](./105-O): Text file containing the best, average, and worst case time complexities of the Radix Sort algorithm, one per line.

* **10. Bitonic sort**
  * [106-bitonic_sort.c](./106-bitonic_sort.c): C function that sorts an array of integers in ascending order using the Bitonic Sort algorithm.
  * Assumes that `size` is a power of 2 (ie. `size` can be expressed as `2^k` where `k >= 0`).
  * Prints subarrays each time they are merged.
  * [106-O](./106-O): Text file containing the best, average, and worst case time complexities of the Bitonic Sort algorithm, one per line.

* **11. Quick Sort - Hoare Partition scheme**
  * [107-quick_sort_hoare.c](./107-quick_sort_hoare.c): C function that sorts an array of integers in ascending order using the Quick Sort algorithm.
  * Implements the Hoare partition scheme.
  * Always uses the last elemement of the partition being sorted as the pivot.
  * Prints the array after each swap.
  * [107-O](./107-O): Text file containing the best, average, and worst case time complexities of the Quick Sort Hoare Partition cheme algorithm, one per line.

* **12. Dealer**
  * [1000-sort_deck.c](./1000-sort_deck.c): C function that sorts a `deck_node_t` doubly-linked list deck of cards.
  * Assumes that there are exactly `52` elements in the doubly-linked list.
  * Orders the deck from spades to diamonds and from aces to kings.


## The author
<details>
    <summary>Mubarak Dederi</summary>
    <ul>
    <li><a href="https://www.github.com/TheBubble01">Github</a></li>
    <li><a href="https://www.twitter.com/mji_dederi">Twitter</a></li>
    <li><a href="mailto:mjdederi01@gmail.com">e-mail</a></li>
    </ul>
</details>




==> 52: SYSTEM_ENGINERRING-DEVOPS/README.MD <==

shell BASH




==> 53: SYSTEM_ENGINERRING-DEVOPS/0X00-SHELL_BASICS/README.MD <==

with God...




==> 54: SYSTEM_ENGINERRING-DEVOPS/0X01-SHELL_PERMISSIONS/README.MD <==

shell permisions




==> 55: SYSTEM_ENGINERRING-DEVOPS/0X02-SHELL_REDIRECTIONS/README.MD <==

0-hello_world




==> 56: SYSTEM_ENGINERRING-DEVOPS/0X03-SHELL_VARIABLES_EXPANSIONS/README.MD <==

readme




==> 57: SYSTEM_ENGINERRING-DEVOPS/0X04-LOOPS_CONDITIONS_AND_PARSING/README.MD <==

Sytem and Devops engineering, RSA & SSH




==> 58: SYSTEM_ENGINERRING-DEVOPS/0X05-PROCESSES_AND_SIGNALS/README.MD <==

# Processes and signals

## Mandatory tasks

* [0. What is my PID](./0-what-is-my-pid)
* [1. List your processes](./1-list_your_processes)
* [2. Show your Bash PID](./2-show_your_bash_pid)
* [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
* [4. To infinity and beyond](./4-to_infinity_and_beyond)
* [5. Don't stop me now!](./5-dont_stop_me_now)
* [6. Stop me if you can](./6-stop_me_if_you_can)
* [7. Highlander](./7-highlander)
* [8. Beheaded process](./8-beheaded_process)

## Advanced tasks

* [9. Process and PID file](./100-process_and_pid_file)
* [10. Manage my process](./101-manage_my_process)
* [11. Zombie](./102-zombie.c)




==> 59: SYSTEM_ENGINERRING-DEVOPS/0X06-REGULAR_EXPRESSIONS/README.MD <==

Regular expression | ruby




==> 60: SYSTEM_ENGINERRING-DEVOPS/0X07-NETWORKING_BASICS/README.MD <==

# Networking basics #0

## Mandatory Tasks

* [0. OSI model](./0-OSI_model)
* [1. Types of network](./1-types_of_network)
* [2. MAC and IP address](./2-MAC_and_IP_address)
* [3. UDP and TCP](./3-UDP_and_TCP)
* [4. TCP and UDP ports](./4-TCP_and_UDP_ports)
* [5. Is the host on the network](./5-is_the_host_on_the_network)




==> 61: SYSTEM_ENGINERRING-DEVOPS/0X08-NETWORKING_BASICS_2/README.MD <==

# Networking basics #1

## Mandatory Tasks

* [0. Change your home IP](./-change_your_home_IP)
* [1. Show attached IPs](./1-show_attached_IPs)

## Advanced Task

* [2. Port listening on localhost](./100-port_listening_on_localhost)




==> 62: ZERO_DAY/README.MD <==

**This file is mandatory in projects**




==> 63: ZERO_DAY/0X00-VAGRANT/README.MD <==

**Testing on how to use a markdown**




