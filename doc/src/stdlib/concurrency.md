# Concurrency

Implement concurrency using "nurseries" as implemented in the [Trio](https://trio.readthedocs.io/en/stable/) library and detailed in [this]https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) blog post.

```text
import (
	"concurrency" concur
)

fun bar {...}
fun bat {...}

fun foo {
	with n = concur.nursery() {
		n.start_soon(bar)
		n.start_soon(bat)
	}

	with(concur.nursery(), fn (n) {
		n.start_soon(bar)
		n.start_soon(bat)
	})
}
```