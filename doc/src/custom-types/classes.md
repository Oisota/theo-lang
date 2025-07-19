# Classes

*NOTE: this is my unfinished ramblings on whether we should add classes to the language*

Rough concept of what a class might look like
```
class Person {
    // instance vars
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

    fun say_hi(self) { // should self be implicit?
        print(self.name)
    }

    static fun do_stuff() {...}
}
```

## Should theo have classes?
I'm generally against this, as stated in other places, but I'm wondering if it wouldn't simplify certain problems.
It's not uncommon to have a base class with a fair amount of functionality and simple child classes that just provide configuration values to change their behavior.
Code like this is usually pretty DRY, declarative, and convenient to use.
An example of this would be something like django's ModelForm classes where you inherit from the base form class and specify model, fields, and any other config in the child classes.
If we added classes, we could also think about removing the struct impl functionality since if you need methods you could just use classes.
This would significantly change the language so I'm not sure about it.
Lots to think about still.

Class based approach:

It might look something like the following:
```
class ModelForm {
    // lots of complex logic here
    fun validate() {...}
}

class FooForm(Form) {
    model = FooModel
}

class BarForm(Form) {
    model = BarModel
}
```

Struct based approach:

The only way I can think to implement would be using an interface to define how a form should behave and then needing to provide implementations for every form struct.
This seems like it would be hard to provide default implementations and not end up with lots of repeated code.
```
interface ModelForm {
    fun validate() {...}
    fun model() {...}
}

struct FooForm {
    _model = FooModel
}

struct BarForm {
    _model = BarModel
}

impl ModelForm for FooForm {
    fun model(self) {
        self._model
    }
}

impl ModelForm for BarForm {
    fun model(self) {
        self._model
    }
}
```

Another example might be database models where you want to have a base model with fields like id/created_at/updated_at/etc and have this apply to all child models.

classes:
```
class Model {
   id int
   created_at datetime
   updated_at datetime
}

class FooModel(Model) {
    user User = ForeignKey(...),
}
```

structs:

Not sure how this would work, Golang has struct embedding which might be a possible solution but it seems hacky to me.
```
???
```

I think my general worries are that classes can be used to create over engineerd and over abstracted code that is difficult to use and maintain.
The solution would be to remove classes and only use structs and functions.
This then makes things more complex when a problem is encountered that lends itself to OOP.
I guess this is the age old problem of simple language making problem solving more complex vs a more complex language that makes problem solving easier.
We need to figure out where this balance should be.
I'm currently leaning towards adding classes in since this is suppposed to be a high level language and everyone already understands OOP for the most part.
We don't want to hinder adoption unecessarily.

The other thing that must be considered is if we add classes, then what should structs be used for and if they should still be in the language.
Seems superfluous to have both since they have significant overlap in functionality.
I guess structs could be reworked to be a lightweight alternative to a class.
A struct would only hold data and have no other built in functionality whereas classes/objects would all inherit from a base class and would have some basic functionality built in.
