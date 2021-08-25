#• Use spaces instead of tabs for indentation.

#• Use four spaces for each level of syntactically significant indenting.

#• Lines should be 79 characters in length or less.

#• Continuations of long expressions onto additional lines should be indented by four
# extra spaces from their normal indentation level.

#• In a file, functions and classes should be separated by two blank lines.

#• In a class, methods should be separated by one blank line.

#• Don’t put spaces around list indexes, function calls, or keyword argument
# assignments.

#• Put one—and only one—space before and after variable assignments.

#• Functions, variables, and attributes should be in lowercase_underscore
#  format.

#• Protected instance attributes should be in _leading_underscore format.

#• Private instance attributes should be in __double_leading_underscore
#  format.
#
#• Classes and exceptions should be in CapitalizedWord format.

#• Module-level constants should be in ALL_CAPS format.

#• Instance methods in classes should use self as the name of the first parameter
#  (which refers to the object).

#• Class methods should use cls as the name of the first parameter (which refers to
#  the class).

# In Python 3, bytes contains sequences of 8-bit values, str contains sequences of
# Unicode characters. bytes and str instances can’t be used together with operators
# (like > or +).

# In Python 2, str contains sequences of 8-bit values, unicode contains sequences
# of Unicode characters. str and unicode can be used together with operators if
# the str only contains 7-bit ASCII characters.

# Use helper functions to ensure that the inputs you operate on are the type of
# character sequence you expect (8-bit values, UTF-8 encoded characters, Unicode
# characters, etc.).

# If you want to read or write binary data to/from a file, always open the file using a
# binary mode (like 'rb' or 'wb').

# Python’s syntax makes it all too easy to write single-line expressions that are overly
# complicated and difficult to read.

# Move complex expressions into helper functions, especially if you need to use the
# same logic repeatedly.

# The if/else expression provides a more readable alternative to using Boolean
# operators like or and and in expressions.

# Avoid being verbose: Don’t supply 0 for the start index or the length of the
# sequence for the end index.

# Slicing is forgiving of start or end indexes that are out of bounds, making it easy
# to express slices on the front or back boundaries of a sequence (like a[:20] or
# a[-20:]).

# Assigning to a list slice will replace that range in the original sequence with
# what’s referenced even if their lengths are different.

# Specifying start, end, and stride in a slice can be extremely confusing.

# Prefer using positive stride values in slices without start or end indexes.
# Avoid negative stride values if possible.

# Avoid using start, end, and stride together in a single slice. If you need all
# three parameters, consider doing two assignments (one to slice, another to stride) or
# using islice from the itertools built-in module.

# List comprehensions are clearer than the map and filter built-in functions
# because they don’t require extra lambda expressions.

# List comprehensions allow you to easily skip items from the input list, a behavior
# map doesn’t support without help from filter.

# Dictionaries and sets also support comprehension expressions.

# List comprehensions support multiple levels of loops and multiple conditions per
# loop level.

# List comprehensions with more than two expressions are very difficult to read and
# should be avoided.

# List comprehensions can cause problems for large inputs by using too much
# memory.

# Generator expressions avoid memory issues by producing outputs one at a time as
# an iterator.

# Generator expressions can be composed by passing the iterator from one generator
# expression into the for subexpression of another.

# Generator expressions execute very quickly when chained together.

#enumerate provides concise syntax for looping over an iterator and getting the
#index of each item from the iterator as you go.

#Prefer enumerate instead of looping over a range and indexing into a sequence.

#You can supply a second parameter to enumerate to specify the number from
#which to begin counting (zero is the default).

#The zip built-in function can be used to iterate over multiple iterators in parallel.

#In Python 3, zip is a lazy generator that produces tuples. In Python 2, zip returns
#the full result as a list of tuples.

#zip truncates its output silently if you supply it with iterators of different lengths.

#The zip_longest function from the itertools built-in module lets you iterate
#over multiple iterators in parallel regardless of their lengths

# Python has special syntax that allows else blocks to immediately follow for and
# while loop interior blocks.

# The else block after a loop only runs if the loop body did not encounter a break
# statement.

# Avoid using else blocks after loops because their behavior isn’t intuitive and can
# be confusing.

# Functions that return None to indicate special meaning are error prone because
# None and other values (e.g., zero, the empty string) all evaluate to False in
# conditional expressions.

# Raise exceptions to indicate special situations instead of returning None. Expect the
# calling code to handle exceptions properly when they’re documented.

# Closure functions can refer to variables from any of the scopes in which they were
# defined.

# By default, closures can’t affect enclosing scopes by assigning variables.

# In Python 3, use the nonlocal statement to indicate when a closure can modify a
# variable in its enclosing scopes.

# In Python 2, use a mutable value (like a single-item list) to work around the lack of
# the nonlocal statement.

# Avoid using nonlocal statements for anything beyond simple functions.

# Using generators can be clearer than the alternative of returning lists of accumulated
# results.

# The iterator returned by a generator produces the set of values passed to yield
# expressions within the generator function’s body.

# Generators can produce a sequence of outputs for arbitrarily large inputs because
# their working memory doesn’t include all inputs and outputs.

# Beware of functions that iterate over input arguments multiple times. If these
# arguments are iterators, you may see strange behavior and missing values.

# Python’s iterator protocol defines how containers and iterators interact with the
# iter and next built-in functions, for loops, and related expressions.

# You can easily define your own iterable container type by implementing the
# __iter__ method as a generator.

# You can detect that a value is an iterator (instead of a container) if calling iter on
# it twice produces the same result, which can then be progressed with the next built-
# in function.




























