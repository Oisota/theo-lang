# Let Binding

The `let` keyword will be used to bind a name to a value.
The bindings will be not be able to be changed once assigned and primitive values will be immutable.
Although the name binding may be immutable, changes to a mutable data structure will still be possible.

Variable declaration will look like:
```text
let x: string = 'Hello, World' //with type annotation
let a = 5 // with type inference
```

Should we add a `const` or `define` keyword for compile time constants that are simply inlined wherever used?
```
const FOO = 25
```