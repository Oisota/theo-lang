package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class LineCommentLexer extends LexerCallable {

	public LineCommentLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
        return TokenizeResult.empty();
	}
}
