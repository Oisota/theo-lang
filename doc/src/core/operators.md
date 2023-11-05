# Operators

## Overloading
Operator overloading will be supported through implementing special interfaces provided by the language/stdlib.
Each operator will have a corresponding interface that any type can implement to be able to be used with the operator.
Probably best to mimic python's dunder method naming scheme to prevent naming collisions.


Example for plus operator:
```text
struct Point {
	x: int
	y: int
}

interface Add[T] {
	fun __add__(self: T, other: T) T
}

impl Add for Point {
	fun __add__(self: Point, other: Point) {
		return Point(self.x + other.x, self.y + other.y)
	}
}

let p1 = Point(0, 0)
let p2 = Point(5, 4)
let p3 = p1 + p2
```