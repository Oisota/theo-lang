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

Do we want `type Foo = Bar` to mean that any `Bar` can be used where a `Foo` is expected or must it explicitly be a `Foo`?
Nim uses a `distinct` keyword to indicate if it should be such.
Wondering if that should just be the default behavior.
Need to think on this.

I can see times when you would want both behaviors.
The loose typing behavior would be nice when you're using an alias just to save typing an instantiated generic type.
It's merely a typing convenience but you don't want to actually create a new type.
See the `Point` type above.

Other times you might want a new type that disallows all other types.
This would be useful where you want all instances to be created using your API functions or the actual type constructor.
This would also allow you to change the base type to a different one in the future without majorly breaking things.
For Ex:
```
type Name = distinct string

fun newName(n str) {
	Name(n)
}

// could update this at some point to be a struct
struct Name {
	first: string,
	last: string
}

fun newName(n str) {
	let parts = n.split(" ")
	Name(
		first=parts(0)
		last=parts(1)
	)
}
```