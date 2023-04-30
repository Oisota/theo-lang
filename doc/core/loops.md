# Loops

How should looping work?
Not sure how loops will work since everything is an expression.

What should this return?
```text
let result = while x < 10 {
	io.print(x)
	x += 1
}
```

What should this return?
```text
let result = for x in range(10) {
	io.print(x)
}
```

Should they just return void or something?

Do we even need loops?
Should be able to take care of all iteration needs with map/filter/reduce.

Also need to consider how loops will play with True/False being just another `enum` and not being intrinsic to the language.

```text
loop {
	case x < 10 {
		True => {
			// loop body
		},
		False => {
			break
		}
	}
}

// don't think for loops are really needed at all
range(10).each(fn (x) => {
	io.print(x)
})
```