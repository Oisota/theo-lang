# Generics

Generic types can be specified using square brackets.

```text
union Option[A] {
	Some(A)
	None
}

struct Point2D[A] {
	x A,
	y A
}

type FloatPoint2D = Point2D[float]

let f1 = FloatPoint2D(x=4.65, y=3.23)
```
