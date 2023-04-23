# Scopes
Functions create their own scope.
Inner functions can see the outer functions data, thus allowing closures.

The **scope** expression creates a subscope *without* access to the enclosing scope.
This is inspired by a video by Brian Will ([Brian Will: OOP is Bad](https://www.youtube.com/watch?v=QM1iUe6IofM#t=41m50s)).
Variables from the enclosing scope must be passed to the **scope** expression in order to be used.
This will be useful in breaking up long functions into subsections.
It will clearly indicate which values are used by the expression.
It will also make it easy to break the block out into a separate function of necessary.
The **scope** expression is basically an immediately invoked anonymous function without access to the outer scope.

```text
fun foo(a int, b string, c Foo) Option[Foo] {
    let x = 5, y = 'hello'

    let j = scope a c {
        //do some stuff
    }

    let k = scope b {
        //do other stuff
    }

    let h = scope x y k {
        //do more stuff
    }

	let t = scope {
		// can also have empty scope that returns a value
	}

	// should also support something like (probably not needed)
	let q = scope var1 as var2 {
		// reassign var1 as var2 inside the scope
	}

    //final stuff
}
```