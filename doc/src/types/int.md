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