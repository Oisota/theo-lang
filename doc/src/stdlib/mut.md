# Mut

Mutability can be achieved using the `Mut` type.
It is a wrapper type that wraps any other type and allows updating its value.
Mutable data would then be declared as so:
```text
let mymut = Mut[int](56)
mymut := 67 //assignment with special operator ':='
let myimmut = mymut.get() //dereference to get value
```
