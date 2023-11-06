# Interfaces

Interfaces allow specifying behavior for a type that implements the interface.
This allows passing different types to functions as long as they implement the same interface.

```
interface Shape {
	fun area() float
}

struct Rect {
	length float,
	width float
}

impl Shape for Rect {
	fun area(self Rect) {
		length * width
	}
}

struct Circle {
	radius float
}

impl Shape for Circle {
	fun area(self Circle) {
		r * Math.pow(Math.PI, 2)
	}
}

fun main() {
	let c = Circle(radius=5)
	let r = Rect(length=5, width=6)

	let l = List[Shape]()
	l.add(c)
	l.add(r) // can add both c and r since l is a list of Shapes

	let s = l.sumBy(fn (i) { i.area() })
}
```