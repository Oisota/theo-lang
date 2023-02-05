# Modules
### Ideas
- don't allow top level mutable variables
- modules should require "exporting" whatever should be made public
- maybe leave out access modifiers until language is implemented

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