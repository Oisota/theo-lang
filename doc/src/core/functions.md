# Functions

All execution/computation will be done using functions.
There will be **No Classes** or classical oop.
Functions will be first class and can be treated as any other value.
Tail calls will be optimized.
Functions will return whatever value their last expression evaluates to.

```text
fun add(a int, b int) int {
	a + b
}

fun fib(n int) int {
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

```
let add = fn (a, b) { a + b }

let l1 = List()
l1.map(fn (a) { a * 2 }) // single expression
	.filter(fn (a) { // multiple expressions
		let x = a * 25
		let z = a - 34
		x > z
	})
```

## Early returns
Can we support early returns from functions?
Early returns greatly simplify error handling and read-ability of code.

Ideas:
```text
// without early return
fun foo(some_var string) Option[string] {
	if some_var == 'boo' {
		Option.None
	} else {
		// all remaining code inside else
	}
}

// with early return
fun foo(some_var string) Option[string] {
	if some_var == 'boo' {
		Option.None
		done
	}
	
	case some_var == "boo" {
		True => { 
			Option.None
			done
		}
	}

	if some_var == '' {
		Option.None
		done
	}

	// all remaining code outside if block
}
```

Am thinking `done` would be a good keyword for this.
Could use `return` but don't want to encourage useless `return` expressions at the end of functions unnecessarily.

This would cause problems with `if`/`else` and case expressions.
Since everything is an expression and `if`/`else` will be sugar for case expressions, an `if` with no `else` will compile to a `case` expression that is non-exhaustive in its pattern matching.
This will be a compiler error.
Maybe we can get around this with the `done` keyword since we'll know  that we're exiting the function and don't need to handle the other possible cases.
Will need to see how this plays out but I'm thinking the `done` keyword should be enough to make this work.
Early returns are very useful it would be annoying to have to implement a function using chained `Option.map()`/`Option.flatMap()`

## Named Parameters?
It would be nice to support named parameters in functions.
Not sure what it would take to support this.

For example, a function for sending an http request with lots of args:
```
fun send_request(url string, method Method, body string, timeout int, follow_redirects Bool) HttpResponse {

}
```

Would be inconvenient to remember all the args so it could be nice to be able to pass them in like so:
```
let result = send_request(
	url="www.google.com",
	method=Method.GET,
	timeout=10,
	follow_redirects=False,
	body="",
)
```

Might be easiest to just do something like:
```
struct HttpRequest {
	url string,
	method Method,
	timeout int,
	follow_redirects Bool
	body string
}

fun send_request(req HttpRequest) HttpResponse {

}

let result = send_request(HttpRequest(
	url="www.google.com",
	method=Method.GET,
	timeout=10,
	follow_redirects=False,
	body="",
))
```

Probably don't need named parameters when you can just make a struct to go with the function.
This requires slightly more syntax but keeps the language cleaner without needing more constructs.
The only issue would be if you want to have both positional and named arguments which could be useful in a refactoring scenario to keep backwards compatibility but doesn't seem like a compelling enough case to warrant the extra work.

I could see the possibility of auto generating the param struct definition in the future.
Something like an auto named type like `<func-name>Args` or something.

```
fun foo_bar(a int, b string, c Bool) Result[string] {

}

// this would be auto created by the compiler:
struct Args_foo_bar {
	a int,
	b string,
	c Bool,
}

//then you can call foo_bar like so
foo_bar(Args_foo_bar(a=2, b="hello", c=False))
```

This could work although we probably want some way to indicate which functions it would generate for and not just generate for all functions.
This probably isn't necessary to worry about now.
Writing a simple struct should be more than fine if named params are needed.

This would be a good case for a macro that would take a function and write the corresponding param struct

Another option could be something like:
```
fun send_request({
	url string,
	method Method,
	timeout int,
	follow_redirects Bool
	body string
}) {
}
```

## Recursion keyword
Should a `recur` keyword be added?
This would be a nice to have so you don't have to repeat the function name and would make renaming a recursive function simpler.
Might make it easier to identify recursive functions vs non-recursive.

```
fun fib(n int) int {
	case n {
		0 => 0,
		1 => 1,
		n => recur(n-1) + recur(n-2) 
	}
}
```