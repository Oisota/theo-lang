# Unions
Algebraic data types will be able to be defined as so:
```text
union List[A] {
    Cons (A, List[A]),
    Nil,
}

union Option[T] {
	Some(T),
	None
}

//used like so
let mylist = List.Cons (5, List.Cons (6, List.Cons (7, List.Nil)))

let result = Option[string].Some("foo")
```