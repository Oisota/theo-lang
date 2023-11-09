# Type Alias

Types can be aliased like so:

```text
type Point = Coord[int, int] // instantiate a generic type with concrete types
type Name = string
type DollarAmount = int

let p = Point(5, 6)
let n:name = "Derek"
let amt = DollarAmount(5)
```

