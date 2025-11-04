# Mut

Mutability can be achieved using the `Mut` type.
It is a wrapper type that wraps any other type and allows updating its value.
This type will be the only source of mutability.
No other type will be mutable unless it uses this type somewhere in its implementation.
Mutable data would then be declared and used like so:

```text
let x_var = Mut[int](56) // initial assignment
x_var.set(67) // update with .set() method
let x = x_var.get() //dereference to get value

let mut_str = Mut[str]("Test String")
mut_str.set("New String")
io.print(mut_str.get())
```

The usage may seem verbose but this is intential as we want mutability to be intentially noisy so that its obvious when its being used and to encourage users to prefer writing pure code instead.

We may also want to consider promoting `SCREAMING_SNAKE_CASE` for mutable variables as another way to indicate mutability.
This is contrary to most other languages where this naming convention is for constants.
Since immutable data should be the norm and mutability the exception, I think this could be a good style to follow.
