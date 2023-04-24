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