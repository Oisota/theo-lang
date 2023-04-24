# Collections

Theo will have **lists**, **vectors**, **sets**, and **dictionaries** as collection types.
Lists, vectors, and sets will all behave similarly due to them being all types of sequential data.
Strings will be implemented as char vectors.
Dictionaries will be separate due to their nature.

## Dictionary
Dicts will be a set of key/value pairs.
Dicts will map any key to any value.
Dicts are created with syntax derived from JavaScript object literals.
Arbitrary key/values mappings will be supported, i.e. mapping a number to a function, or a function to a string, etc.
Dictionaries will map one type to another type and will be type checked based upon this.
The dictionary, `x`, below would have the type `Dict[String, Int]` for example.

```text
let x = Dict[string, int]()
x.set('key1', 56)
x.set('key2', 5)
x.set('key3', 23)

x.set('key1', 567)
x.set('key2', 6)
```

## Sequences
### Vector
Sequence of data of the same type.
Vectors will be zero indexed.
Will have fixed length saved at creation time.

```text
let a = Vector[string](8) // string vector with length 8
a.append('blah')
a.append('skah')
a.append('Hello')
let x = a.at(2) // -> 'Hello'
```

### List
Sequence data type with variable length.
These values must be the same type.
```text
let l1 = List[int]()
l1.append(1)
l1.append(2)
l1.append(3)
```

### Set
Sets will be created by placing '#{}' around a list of values.
These values need be the same type.
Sets will maintain the mathematical properties of sets
```text
let s = Set[string]()
s.add('Foo')
s.add('Bar')
s.add('Bat')
```

### String
Strings will be considered as a sequence of characters and will behave the same as the other sequence data types.
String comparison should work as one would expect it to.
For ex:
```text
"hello" == "hello" -> true
"a" == "b" -> false
```
Only the '=' and '!=' operators will be defined for string comparison.