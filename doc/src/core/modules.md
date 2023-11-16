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
// this seems best for seeing the public api of a module at a glance
export {
	foo
}

pub {
	foo
}
```
Although the block export suffers from having to type function/type names twice and update them in 2 places when refactoring.
Having `pub` before each function/type will probably work fine.

`pub` seems like the best keyword for this.
Its not too verbose and unlikely to cause naming collisions.

Should only top level functions/types be able to be exposed as public?
What about fields of structs?
Nim allows specifying individual field access for structs.
I can see this being useful but it also complicates things.
Maybe just top level module symbols having access modifiers is enough.
You could always keep a struct definition private while exposing functions that operate on it.


Also need to consider the case of hiding a struct definition while still wanting to use the struct constructor to get the named fields.

```
// User is private
struct User {
	name string,
	age int
}

// this function is public
pub fun createUser(name string, age int) User {

}
```

Since the User struct is private we need a way to create a user but we lose out on being able to say:
```
let u = User(name="Derek", age=30)
```
and instead have to say:
```
let u = createUser("Derek", 30)
```

Could get around this by having a public struct serve as the constructor and a private one for holding the data?
Something like this:
```
struct User {
	name string,
	age int,
}

pub struct UserBuilder {
	name string,
	age int
}

// takes a builder returns a user
pub fun newUser(u UserBuilder) User {
	User(name=u.name, age=u.age)
}
```

or:
```
pub struct UserBuilder {
	name Mut[Option[string]] = Mut(None),
	age Mut[Option[int]] = Mut(None)
}

impl UserBuilder {
	pub fun name(self UserBilder, n string) UserBuilder {
		self.name.set(Some(n))
		self
	}
	pub fun age(self UserBilder, a int) UserBuilder {
		self.age.set(Some(a))
		self
	}
	pub fun build(self) User {
		User(
			name=self.name.get().get(""),
			age=self.age.get().get(0)
		)
	}
}

u = UserBuilder()
	.name("Derek Morey")
	.age(30)
	.build()
```

These access modifiers screw things up IMO.

I'm not convinced the access modifiers provide enough value to be included.
They're nice in theory for working on large code bases where you want to keep certain things hidden but they result in needing to write more code for simple cases like the private User struct example above.
Needing to resort to a builder pattern for such cases seems like bad design.
Seems like with everything being immutable by default, the need to hide things is less common.

Futher consideration regarding interfaces: Struct fields should all be public and not have access modifiers.
This will make implementing interfaces easier since you'll have access to all struct fields.
Otherwise it could be very tricky to implementing an interface for a struct with some private fields.
So if we do add access modifiers they should be only allowed at the top level of the module.
So either the whole struct is public or its completely private, no fine grained access control.