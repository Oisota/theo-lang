package org.theolang.compiler;

import java.util.Set;

public class Keywords {
    public static final Set<String> KEYWORDS = Set.of(
		// imports
		"import",

		// vars
		"let",

		// functions
		"fun",
		"fn",
		"done",
		"recur",

		// types
		"class",
		"interface",
		"type",
		"enum",
		"union",
		"distinct",

		// OOP stuff
		"construct",
		"abstract",
		"static",
		"prop",

		// logical
		"case",

		// loops
		"loop",
		"break",
		"continue",

		// misc
		"scope"
	);

    public static final Set<String> RESERVED = Set.of(
		"pub",
		"as",
		"private",
		"public",
		"export",
		"module",
		"mod",
		"const",
		"with",
		"while",
		"do",
		"for",
		"in",
		"struct"
	);

    public static final Set<String> OPERATORS = Set.of(
		// logical
		"and",
		"or",
		"not",
		"==",
		"!=",
		"<=",
		">=",
		"<",
		">",

		// pattern match
		"=>",

		// math
		"+",
		"-",
		"*",
		"/",
		"%",

		// bitwise
		"&",
		"|",
		"^",
		"<<",
		">>",
		"~",

		// assignment
		"=",

		// field access
		".",

		// type annotation
		":"
	);
}
