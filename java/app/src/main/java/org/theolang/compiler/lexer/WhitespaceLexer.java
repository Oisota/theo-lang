package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class WhitespaceLexer extends LexerCallable {

	public WhitespaceLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
        return TokenizeResult.empty();
	}
}
