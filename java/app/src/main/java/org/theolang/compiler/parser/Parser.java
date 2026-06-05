package org.theolang.compiler.parser;

import java.util.ArrayList;

import org.theolang.compiler.token.Token;
import org.theolang.compiler.ast.Program;

class Parser {
	private ArrayList<Token> tokens;

	public Parser(ArrayList<Token> tokens) {
		this.tokens = tokens;
	}

	public Program parse() {
	}
}
