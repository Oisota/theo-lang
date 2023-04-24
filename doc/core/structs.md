# Structs

Structures provide grouping of related data in a single type with named fields.

```
struct Point {
	x float,
	y float
}

struct Person {
	name string,
	age int
}

struct Card {
	rank Rank,
	suit Suit
}

let p1 = Point( 
	x = 5, 
	y = 6
)
let x = p1.x
let y = p1.y

let p2 = Person( 
	name="Derek Morey", 
	age=23 
)

let card = Card(
	rank=Rank.Jack,
	suit=Suit.Heart
)
```

## Fields
Fields may have an optional default value like so:
```
struct Bar {
	my_field string = "BOOM!"
	other_field int
}

let bar = Bar(other_field=34) // only other_field requires assigning at creation
```
### Mutability
Struct fields function like `let` assignments.
Once a struct is created its fields can not be reassigned.
The underlying field may be mutable though.

```text
// normal struct
struct Foo {
	a: int
}

let foo = Foo(5)
foo.a = 6 // compile time error

// mutable field struct
struct Bar {
	a: Mut[int]
}

let bar = Bar(5)
bar.a = 6
```

## Methods
Structs can have methods defined in `impl` blocks.
An `impl` block of the form `impl <struct-name>` will define methods on the struct whereas the form `impl <interface-name> for <struct-name>` will define an implementation of an interface for a given struct.
```
struct Rect {
	x1: int,
	y1: int,
	x2: int,
	y2: int,
}

impl Rect {
	fun area(self) {
		(x2 - x1) * (y2 - y1)
	}
}

// This could just as easily be an interface implementation
interface Shape {
	fun area(self): int
}

impl Shape for Rect {
	fun area(self) {
		(x2 - x1) * (y2 - y1)
	}
}

let rect = Rect { x1 = 4, y1 = 0, x2 = 10, y2 = 20 }
let area = rect.area()
```

## Creation/Initialization
Structs instances can be created by calling the struct name like a function.
Values for all fields without default values must be provided at creation time.
Values can be provided in the same order as defined or with named arguments.

```text
struct Point {
	x int,
	y int,
}

let p1 = Point(5, 6)
let p2 = Point(x=3, y=5)
let p3 = Point(3) // compile time error
let p4 = Point(3, x=3) // compile time error
let p5 = Point(y=3, x=3) // ok
let p6 = Point(y=3, x) // compile time error
let p7 = Point() // compile time error
```