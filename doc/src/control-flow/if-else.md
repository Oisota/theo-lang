# If Else Expressions
Conditional branching will be expression based.
Each `if` expression will evaluate to a value.
Every `if` must have a corresponding `else`.

```text
let x = 5
let y = 8

if x == 10 { 'Foo' }
else if y == 9 { 'Bar' }
else { 'Bat' }
```

*Idea:* This may be best implemented as syntax sugar over case expressions.
This would simplify things since every if/else can just be translated to its corresponding case expressions.
The above example would be translated to a nested case expression:

```text
case x == 10 {
	True => 'Foo',
	False => case y == 9 {
		True => 'Bar',
		False => 'Bat
	}
}
```

This would make sense since booleans wouldn't necessarily need to be built into the language.
They could just be a simple enum.

Noting that [Gleam](https://gleam.run/book/tour/case-expressions.html) *only* has case expressions.
Could possible simplify the language and do away with if/else all together.

Fibonacci function example:
```
fun fib(n int) int {
	if n == 0 or n == 1 {
		n
	} else {
		recur(n - 1) + recur(n - 2)
	}
}

fun fib(n int) int {

	case n {
		0 => 0,
		1 => 1,
		n => recur(n - 1) + recur(n - 2)
	}

	// alternate way of writing it, slightly shorter
	case n == 0 or n == 1 {
		True => n,
		False => recur(n - 1) + recur(n - 2)
	}
}
```