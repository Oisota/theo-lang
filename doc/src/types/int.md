# Integer

32-bit integer number.
```text
let x: int = 5
```

`int` will be an alias for `i32` meaning a signed 32 bit integer.
Other integer types will also be available: `i64`, `i32`, `i16`, `i8` .
As well as unsigned variants: `u64`, `u32`, `u16`, `u8`.
`byte` will be an alias for `u8`.

# Range Types?
It would be nice to support range types.
For example an `int` thats guaranteed to be in `[1..10]`.

```
fun foo(a Range(1,10)) int {
}
```

Can this be created using built-in features or does it need to be a built-in type?

Could easily have a class for creating range objects but it doesn't quite give us an actual type that can be typechecked on.
It may good enough to just use this to check integer params against though.
A true range type would need to be builtin I think and might be out of scope when a simple class like the following can be used.
```
class Range {
    min int
    max int

    fun contains(n int) Bool {
        min <= n and n >= max
    }
}

let r = Range(0, 10)

```

Maybe we can use generics to do this?
```
class Range[MIN, MAX] {
    min int = MIN
    max int = MAX
    value int

    constructor(i int) {
        case this.contains(i) {
            True => value = i
            False => ???
        }
        value = i
    }
}

type MyRange = Range[1,100]
fun foo(MyRange a) {
}
```

Looks kinda weird but it makes sense to instantiate the generic params with ints.