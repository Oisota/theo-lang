# Modules

The module system will be file and directory based similar to how Python and Node.js do things.
A single file will be considered a "module" and a directory with a special index file (`package.theo`) will be considered a package.
The index file will mark a directory as a package and allow importing any submodules into its namespace.
Under the hood, modules and packages will be transformed into structs with the top-level file contents being the members of the struct.

Libraries/Code can be imported like so:
```text
import (
	"std/io"
	"lib/httpserver"
	"app/routes"
)

fun main() int {
	io.print('Hello!')
}
```
All standard library code will be under the `std` name space.
Maybe also have `lib` namespace for all third party code and `app` namespace for app code.
This might be hard to enforce.

May need an easy way to import C libraries so as to piggyback off its std-lib during initial implementation.
Something like:
```text
import (
	"c_include/stdio"
)
```

### Ideas
- don't allow top level mutable variables
- modules should require "exporting" whatever should be made public
- maybe leave out access modifiers until language is implemented
- python has everything public by default, seems to work ok

Ideas:
```text
// export
export fun foo() {

}

// pub
pub fun foo() {

}

// separate export or pub
fun foo() {

}

export foo
pub foo

// with a block?
export {
	foo
}

pub {
	foo
}

```