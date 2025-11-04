# Loops

Am thinking that the only looping construct we need is a simple `loop` keyword

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
Probably should just return some kind of `unit` type.

Do we even need loops?
Should be able to take care of all iteration needs with map/filter/reduce.

Also need to consider how loops will play with True/False being just another `enum` and not being intrinsic to the language.

Maybe `for` and `while` de-sugar into a more primitive loop construct?
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

Might only need the `loop` construct for infinite loops.
If not, then an infinite iterator of some sort would be needed and also a way to break out map/filter/reduce.
Not sure how that would work.
Might be easiest to just have the single `loop` construct to create an infinite loop when necessary. (IE system daemon, game engine, anything that needs to run indefinitely)
This way we don't have to think about how `for` and `while` interact with booleans just being enums and not built in.
Just loop and break out if you need to in the loop body.

Can the loop keyword be replaced by a function?

```
// loop sentinel
enum Loop {
	Break,
	Continue
}

fun loop(loop_fn Function) void {
	case loop_fn() {
		Break => done,
		Continue => recur(loop_fn)
	}
}

loop(fn () {
	plugins.each(fn (p) {
		p.tick()
	})

	case plugins.empty() {
		True => Break,
		False => Continue
	}
})
```

I really like the idea of having a `loop()` function.
This allows us to remove another construct from the language and deal with just functions.
The above will require tail call optimization for it to work properly or maybe we just implement it in C as a built-in function.
Either way I like this bettern than a `loop` keyword.
We could potentially remove `loop`, `break`, and `continue` keywords which would futher simplify things.