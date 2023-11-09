# Option

The option type will be a wrapper type for dealing with the possibility of null.
It will have 2 cases: Some value or None.
If a value may or may not be null, it will get wrapped in an option that can be pattern matched to deal with either case.
This will force an explicit check for the null case.
```
union Option[T] {
	Some(T),
	None
}

let opt = Option.Some(5)

let result = case opt {
	Some value => value,
	None => 0
}

let result = opt.get(0) // get the option value with a defulat of zero
```
