# Unions
Sum types (tagged unions) will be able to be defined as so:

```text
union List[A] {
    Node(A, List[A]),
    Nil,
}

union Option[T] {
	Some(T),
	None
}

//used like so
let mylist: List[int] = List.Node(5, List.Node(6, List.Node(7, List.Nil)))

//or without type name qualifying
let mylist = Node(5, Node(6, Node(7, Nil)))

let result = Option[string].Some("foo")
```

Unions can also have methods defined on them:
```
union Option[T] {
	Some(T),
	None

    fun map(func Function) {
        case self {
            Some(v) => Some(func(v))
            None => None
        }
    }
}

let o = Some(5)
let o1 = o.map(fn (v int) { v * v }) // -> o1 == Some(25)
```

TODO: need to figure out if the following are equivalent or not and if so, how are they different:
```
union Foo {
	Boo,
	Zoo,
}

enum Foo {
	Boo,
	Zoo
}
```

The latter would be the preferred way since the `Foo` type truly is just an `enum` but the union type must allow for empty constructors as seen in the linked list example above.
This means that the `union Foo {...}` is valid syntactically and can be used but it would not be the ideal way to do it.
Choices are either both syntaxes are equivalent and the `enum` approached is preferred, or they are different and should behave differently.

I Am thinking that a `union` type must have at least one constructor that contains some data.
`enum` types would then be strictly for an enumerated set of labeled values with the default being `int`s.
Or we can allow a `union` with no data but then it must be constructed with parens after it like so `Foo.Zoo()` in order to indicate its a `union` and not an `enum`.
I like the first option, forcing `union`s to have at least one field with data.