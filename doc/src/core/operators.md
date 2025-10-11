# Operators

## Overloading
Operator overloading will be supported through implementing special interfaces provided by the language/stdlib.
Each operator will have a corresponding interface that any type can implement to be able to be used with the operator.
Probably best to mimic python's dunder method naming scheme to prevent naming collisions.


Example for plus operator:
```text
interface Add[T] {
	fun __add__(other: T) T
}

class Point : Add {
	x int
	y int

	fun __add__(self Point, other Point) Point {
		Point(this.x + other.x, this.y + other.y)
	}
}

let p1 = Point(0, 0)
let p2 = Point(5, 4)
let p3 = p1 + p2
```

I'm thinking that all usage of operators should translate to their corresponding method calls.
```
let r = p1 + p2
// this would become
let r = p1.__add__(p2)
```