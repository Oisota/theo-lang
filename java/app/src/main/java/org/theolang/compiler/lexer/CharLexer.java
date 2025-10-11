package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenizeResult;

class CharLexer extends LexerCallable {

	private TokenType type;
	private String keyword;

	public KeywordLexer(LexContext ctx, TokenType type, char value) {
		super(ctx);
		this.type = type;
		this.value = value;
	}

	public TokenizeResult call() {
		if (value == lexer.getCurrent()) {
			return new TokenizeResult(1, new Token(type, String.valueOf(value)));
		}
		return TokenizeResult.empty();
	}
}
