# Classes

Classes allow creating a custom type that bundles data and functionality.

Kitchen sink example of what a class might look like:
```
class Person : SuperClass {
    // instance fields
    name string
    age int

    // static vars shared between all instances
    static {
         foo int
    }
    // or maybe keyword in front of var
    static foo int

    // constructor (function name tbd, construct/init/new/etc)
    construct(self, name string, age int) {
        self.name = name
        self.age = age
    }

    fun say_hi() { // should self be implicit? or use this?
        print(this.name)
    }

    static fun do_stuff() {...}

    // property syntax?
    prop greeting(self) {
        "My name is {}, I am {} years old".format(self.name, self.age)
    }
}
```

## Constructors
Constructors are defined using the special `construct` keyword.
A classes may have multiple constructors that take different arguments.

Should have a default constructor that automatically takes all fields as parameters and assigns them to the instance? (Maybe some kinda of dataclass concept is needed for that)
```
class Foo {
    construct(...) {...} // special keyword (construct/init/build/etc)
}
```

## Field Access
Class members will be *protected* by default.
They can only be accessed by methods of the class and in methods of inheriting classes.
This enforces encapsulation by default which I think is a good thing.
Public access can be granted through properties.
Using properties to make things public also gives us flexibility if the underlying field changes since the public api of class won't change.
Properties are also more verbose than just having access modifiers so this will discourage exposing fields from the get go.
```
class User {
    name string
    age int


    prop name() { name }
}

let u = User("joe", 30)
print(u.name) // prints joe
print(u.age) // compilation error since age is not public
```

## Methods
Methods are just functions defined within the class definition.
An implicity `this` keyword pointing to the current instance is available inside methods.
Currently planning on all methods being public by default but thinking that it might be nice to have a way of marking methods private.
Maybe using a leading underscore or required use of the `pub` keyword.

## Inheritance
Can inherit using the `:` syntax.
Can inherit from other classes, interfaces, or both.
```
class Point2D {
    x int
    y int
}
class Point3D : Point2D {
    z int
}

interface Foo {
}

class Bar : Foo {
}
```

## Updates
Since class fields are immutable by default, it might be nice to have a simple way of updating the fields by creating a new object with the new data.
```
let p = Point(x = 5, y = 6)
let j = p.update(x=10) // simple method present on all classes? (Don't have keyword args so this wouldn't work)
let j = Point(base=p, x=10) // use a special base arg to specify data to inherit (This seems like the best option)
let j = Point(**p, x=10) // some kind of splat operator that expands collections?

// Could do
let p2 = Point.from(p) // from method creates a builder from the existing object
    .x(4)
    .build()
```
