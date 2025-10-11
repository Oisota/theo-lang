package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class IdentifierLexer extends LexerCallable {

	public IdentifierLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
        return TokenizeResult.empty();
	}
}
