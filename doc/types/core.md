# Types

*To Do: update doc to remove literal notations where applicable*

## Primitives
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
x.at(#foo) = 5
```


## Non-Primitive Types
Non-primitive types will be types that will be implemented in the standard library and will not be available by default.
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

Might also make sense to add some simple helper enums in a `std/bool` package:
```text
enum Toggle { On, Off }
enum Answer { Yes, No}
```
I am thinking it might be nice to facilitate using booleans other than true/false depending on the context.
Might make for more readable code.
For example feature flags might make more sense as either `On` or `Off` instead of `True` and `False`.
Will need to decide how this interacts with `if`/`else` expressions.
Maybe if expressions can work with any enum that has only 2 choices and assumes the first choice is the "truthy" value.
Need to think on this, could be abused.
Maybe limit if expressions to only work with values defined in `std/bool`.

### Mutable
Mutability can be achieved using the `Mut` type.
It is a wrapper type that wraps any other type and allows updating its value.
Mutable data would then be declared as so:
```text
let mymut = Mut[int](56)
mymut := 67 //assignment with special operator ':='
let myimmut = mymut.get() //dereference to get value
```

### Option
The option type will be a wrapper type for dealing with the possibility of null.
It will have 2 cases: Some value or None.
If a value may or may not be null, it will get wrapped in an option that can be pattern matched to deal with either case.
This will force an explicit check for the null case.
```
enum Option[T] {
	Some(T),
	None
}

let opt = Option::Some(5)

let result = case opt {
	Some value => value,
	None => 0
}

let result = opt.get(0) // get the option value with a defulat of zero
```

### Result
Result type similar to Rust's result type.
```text
enum Result[T, E] {
	Ok(T),
	Err(E)
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