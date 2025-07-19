# Mut

Mutability can be achieved using the `Mut` type.
It is a wrapper type that wraps any other type and allows updating its value.
Mutable data would then be declared and used like so:

```text
let x_var = Mut[int](56)
x_var.set(67) // assignment with .set() method
let x = x_var.get() //dereference to get value

let mut_str = Mut[str]("Test String")
mut_str.set("New String")
io.print(mut_str.get())
```

The usage may seem verbose but this is intential as we want mutability to be intentially noisy so that its obvious when its being used and to encourage users to prefer writing pure code instead.
