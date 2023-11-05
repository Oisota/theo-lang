# Tuples
Tuples will be created by placing parentheses '()' around a list of values.
These values need not be the same type.
A tuples type signature will be represented by each of its elements signatures.
```text
let a = ('blah', 2, 2.3) // type sig = Tuple[string,int,float]
```

Since the language won't have literal notation for collection I'm unsure how best to create tuples.
The paren syntax isn't consistent with the other collection types.
It would be nice to do `let t = Tuple[int, string, int](42, "foo", 534)` , but then we would need variadic generic args and parameter args.

Furthermore, are tuples even needed?
Tuples might make it too easy to create adhoc collections/types.
For example returning `(data, error)` tuple from a function instead of using a proper result type.
Seems like its almost always better from an API standpoint for functions to either return an Option/Result or define their own return types if multiple values need to be returned.

Code Example to illustrate:
```text
fun this_might_fail(data MyData) Result[string, Error] {

	result = fetch("https://some-url.com", data)
	case result {
		Some(response) => Result.Ok("success"),
		None => Result.Error("Error fetching resource")
	}
}

fun this_might_fail(data MyData) Tuple[string, string] {

	result = fetch("https://some-url.com", data)
	case result {
		Some(response) => ("success", "")
		None => ("", "Error fetching resource")
	}
}
```

The return type `Tuple[string, string]` doesn't really tell us what the data in the tuple means.
Is it `(data, error_message)` or `(error_message, data)`.
It's too ambiguous.

Its pretty much always better just define a custom type to hold some data.
I don't think there's a compelling enough use case for needing tuples.
```text
struct MyTuple {
	f1 int,
	f2 string,
	f3 float,
}
```

Leaning towards omitting tuples for now, maybe forever.

Could just have hard coded Tuple types for each variation up to a max.
```text
struct Tuple1[A] {
	_1 A
}
struct Tuple2[A, B] {
	_1 A,
	_2 B
}
struct Tuple3[A, B, C] {
	_1 A,
	_2 B,
	_3 C
}
// up to like Tuple12 or Tuple16 or something

let t1 = Tuple1[int](5)
let t2 = Tuple2[int, string](34, "foo")
let t3 = Tuple3[int, string, Option[int]](34, "foo", Some(4))
```
But these still suffer from the ambiguity mentioned above.
Probably best to leave out, can always be added later.