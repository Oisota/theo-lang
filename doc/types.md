Types
=====

Primitives
----------
The primitive types will be built into the language and not implemented as syntax sugar or as code.

### Integer
32-bit integer number.
```text
let x = 5
```

### Float
64-bit floating point number
```text
let y = 5.6
```

**Should we also provide other types like i8, i16, u8, u16, u32, etc. for ints and floats?** (probably yes)

### Char
Single character value.
Denoted using single quotes: `'a'`

Not sure if there should be literal syntax for this.
Want the language to be high level and not sure a char literal will be used very often.

### Key
The key type will be like a constant string that is replaced at compile time.
It will take the place of using strings as keys.
Still deciding on a notation. (#foo :foo $foo @foo)
Leaning towards `#foo` as the symbol is already called `hash` and the symbols will likely turn into hashes at compile time anyway.

```text
x[#foo] = 5
```

### Function
All execution/computation will be done using functions.
There will be **No Classes** or classical oop.
Functions will be first class and can be treated as any other value.
Tail calls will be optimized.
Functions will also be automatically curried.
Functions will return whatever value their last expression evaluates to.

Functions defined like so will be curried.
```text
fun add x y = x + y 
```
This will be equivalent to:
```text
let add = fn x { 
    fn y { 
        x + y
    }
}
```
Functions should work like ML functions in that they only take one value.
See [Example](../samples/blah.func) for more detail.
**May change this**

#### Scopes
Functions create their own scope.
Inner functions can see the outer functions data, thus allowing closures.

The **scope** expression creates a subscope *without* access to the enclosing scope.
This is inspired by a video by Brian Will ([Brian Will: OOP is Bad](https://www.youtube.com/watch?v=QM1iUe6IofM#t=41m50s)).
Variables from the enclosing scope must be passed to the **scope** expression in order to be used.
This will be useful in breaking up long functions into subsections.
It will clearly indicate which values are used by the expression.
It will also make it easy to break the block out into a separate function of necessary.
The **scope** expression is basically an immediately invoked anonymous function without access to the outer scope.

```text
fun foo(a int, b string, c Foo) Option[Foo] {
    let x = 5, y = 'hello'

    let j = scope a c {
        //do some stuff
    }

    let k = scope b {
        //do other stuff
    }

    let h = scope x y k {
        //do more stuff
    }

	let t = scope {
		// can also have empty scope that returns a value
	}

	// should also support something like (probably not needed)
	let q = scope var1 as var2 {
		// reassign var1 as var2 inside the scope
	}

    //final stuff
}
```

#### Tuples
Tuples will be created by placing parentheses '()' around a list of values.
These values need not be the same type.
A tuples type signature will be represented by each of its elements signatures.
```text
let a = ('blah', 2, 2.3) // type sig = (string,int,float)
```

Non-Primitive Types
-------------------
Nonprimitive types will be types that will be implemented in the standard library and will not be available by default.
They will be implemented in terms of the other primitives.

### Boolean
Booleans will be implemented as simple enum with `True` and `False` constructors as so:
```text
enum Bool { True, False }

let my_bool = True

io.print(if my_bool { 
    'b is true'
} else { 
    'b is false'
})

io.print(if 5 > 9 {
    'foo'
} else {
    'bar'
});
```

Collections
-----------
Theo will have **lists**, **vectors**, **sets**, and **dictionaries** as collection types.
Lists, vectors, and sets will all behave similarly due to them being all types of sequential data.
Strings will be implemented as char vectors.
Dictionaries will be separate due to their nature.

### Dictionary
Dicts will be a set of key/value pairs.
Dicts will map any key to any value.
Dicts are created with syntax derived from JavaScript object literals.
Arbitrary key/values mappings will be supported, i.e. mapping a number to a function, or a function to a string, etc.
Dictionaries will map one type to another type and will be type checked based upon this.
The dictionary, `x`, below would have the type `Dict<String, Int>` for example.

```text
let x = {
    'key1': 56,
    'key2': 5,
    'key3': 23
}

x['key1'] = 567
x['key2'] = 6
```

#### Comparison
Dicts will be compared by reference.
Deep comparison won't be supported out of the box.

### Sequences
#### Vector
Vectors will be created by placing brackets '<>' around a list of values.
These values must be the same type.
Vectors will be zero indexed.
Vectors will be implemented as contiguous blocks of memory, making random access efficient.
Elements will be accessed using brackets with the index inside the brackets.

```text
let a = <'blah', 'skah', 'Hello'>
let x = a[2] // -> 'Hello'
```

#### List
Lists will be created by placing '[]' around a list of values.
These values must be the same type.
Lists will be implemented as singly linked lists, making insertion at the head of the list efficient.
```text
let l1 = [1, 2, 3]
let l2 = ['FOO', 'Bar', 'Bat']
```

#### Set
Sets will be created by placing '#{}' around a list of values.
These values need be the same type.
Sets will maintain the mathematical properties of sets
```text
let s = #{'Foo', 'Bar', 'Bat'}
```

#### String
Strings will be considered as a sequence of characters and will behave the same as the other sequence data types.
String comparison should work as one would expect it to.
For ex:
```text
"hello" == "hello" -> true
"a" == "b" -> false
```
Only the '=' and '!=' operators will be defined for string comparison.

### References
References are a wrapper type that wraps any other type in a mutable reference cell.
Creating a reference will done using the `ref` keyword.
A `ref` will function like `ref`'s in ML.
A `ref` is basically a cell whose data can be changed.
Mutable data would then be declared as so:
```text
let mymut = ref 56
mymut := 67 //assignment with special operator ':='
let myimmut = !mymut //dereference to get value
```
### Option
The option type will be a wrappper type for dealing with the possibility of null.
It will have 2 cases: Some value or None.
If a value may or may not be null, it will get wrapped in an option that can be pattern matched to deal with either case.
This will force an explicit check for the null case.
```
enum Option<a> {
	Some a,
	None
}

let opt = Option::Some 5

let result = case opt {
	Option::Some value => value,
	Option::None => 0
}
```

### Alias
Might want to be able to alias types
```text
type foo = string

struct Foo {
	bar: foo
}
```