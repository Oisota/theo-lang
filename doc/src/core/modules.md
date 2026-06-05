# Modules

The module system will be file and directory based similar to how Python and Node.js do things.
A single file will be considered a "module" and a directory with a special index file (`package.theo`/`index.theo`/etc) will be considered a package.
The index file will mark a directory as a package and allow importing any submodules into its namespace.

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

## Import Alias
Imports can be aliased under a new name or only specific types can be imported if desired.
```text
import (
    "app/foo/bar" bam // import library under a new name
    "app/views" (
        FooView
        BarView
    ) // import specific items
)
bam.do_something()
```

### Ideas
- don't allow top level mutable variables
- modules should require "exporting" whatever should be made public
- maybe leave out access modifiers until language is implemented
- python has everything public by default, seems to work ok
- Can we allow multiple different versions of a library? (One module needs Foo==1.0.0 and another modules needs Foo=1.5.0)
	- maybe wait to implement this behavior

## Module member access
The `pub` keyword will be used to indicate which members of a module are available when the module is imported.
Anything not marked as public will only be accessible by code inside the module.
For Example:
```text
// module foo.theo
pub fun foo() {
    io.println("Foo!")
}

fun bar() {
    io.println("I'm private to the module")
}

// other file
import (
    "./foo"
)

foo.foo() // prints Foo!
foo.bar() // compilation error
```

## Re-Export of Types
It can be useful for a package to re-export types from submodules into the package scope.
This can be done in `package.theo`. 

Say we have this directory structure:
```
bat/
|- package.theo
|- foo.theo
|- bar.theo
|- bam.theo
```

And each file `foo.theo`, `bar.theo`, and `bam.theo` have public types `Foo`, `Bar`, and `Bam` respectively.
Then re-exporting those types to the `bat` package would look like:

`package.theo`:
```
import (
	"./foo"
	"./bar"
	"./bam"
)

// explicit republish types
pub foo.Foo
pub bar.Bar
pub bam.Bam
```

We could also just do explicit imports like so:
```
import (
	"./foo" ( Foo )
	"./bar" ( Bar )
	"./bam" ( Bam )
)
```
Then we wouldn't need the `pub` keyword at all.

```
import (
	"bat"
)

let f = bat.Foo(a=5)
let b = bat.Bar(x=5)
let j = bat.Bam(y=5)
```

This seems to make sense.
