# Mut

Mutability can be achieved using the `Mut` type.
It is a wrapper type that wraps any other type and allows updating its value.
Mutable data would then be declared as so:

```text
let mymut = Mut[int](56)
mymut := 67 //assignment with special operator ':='
let myimmut = mymut.get() //dereference to get value
```

I'm thinking that the `:=` makes more sense over having a `.set()` method on the type.
This way mutation will be easier to visually scan and grep for in the code.
A simple method could be overlooked if in a hurry.
We should ensure that the mutation operator doesn't allow for being overloaded by other types.
It should strictly be for mutation and nothing else.
