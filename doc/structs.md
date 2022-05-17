# Structs
Structures provide a data type with named fields that can be of differing types.
```
struct Point {
	x: float,
	y: float
}

struct Person {
	name: string,
	age: int
}

struct Card {
	rank: Rank,
	suit: Suit
}

let p1 = Point { 
	x = 5, 
	y = 6 
}
let {x, y} = p1
let x = p1.x
let y = p1.y

let p2 = Person { 
	name = "Derek Morey", 
	age = 23 
}

let card = Card {
	rank = Rank.Jack,
	suit = Suit.Heart
}
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