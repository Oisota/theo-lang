# Functions

All execution/computation will be done using functions.
There will be **No Classes** or classical oop.
Functions will be first class and can be treated as any other value.
Tail calls will be optimized.
Functions will return whatever value their last expression evaluates to.

```text
fun add(a int, b int) {
	a + b
}

fun fib(n int) {
	case n {
		0 => 0,
		1 => 1,
		n => fib(n-1) + fib(n-2) 
	}
}
```

Types must be specified for function definitions to aid readability.

## Anonymous Functions (Lambdas)

Anonymous functions can be defined using the `fn` keyword like so:

```text
let add = fn (a, b) => a + b

let l1 = List()
l1.map(fn (a) => a * 2)
```