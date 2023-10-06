# With Blocks

Should `with` blocks have their own dedicated syntax or can it be done using a simple built-in function?

Dedicated Syntax:
```
with f = open('./foo.txt') {
	let r = f.read()
	print(r)
}
```
A little cleaner looking.

Function Syntax:
```
with(open('./foo.txt'), fn(f) {
	let r = f.read()
	print(r)
})
```
Don't need dedicated syntax, easier to parse, easier to remember, more consistent with rest of language.
Kinda like this way of doing it.

Either way, going to need an interface to define an auto-closeable/resource type.
Something like so:

```
interface Resource[T] {
	fun enter() Result[T]
	fun exit()
}

fun with(resource: Resource, lam: Function) {
	let r = resource.enter()
	let lam(r)
	r.close()
}
```