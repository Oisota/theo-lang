package org.theolang.compiler.lexer;

import org.theolang.compiler.token.TokenType;
import org.theolang.compiler.token.TokenizeResult;
import org.theolang.compiler.token.Token;

class CharLexer extends LexerCallable {

	private TokenType type;
	private String keyword;
    private char value;

	public CharLexer(LexContext ctx, TokenType type, char value) {
		super(ctx);
		this.type = type;
		this.value = value;
	}

	public TokenizeResult call() {
		if (value == ctx.current()) {
			return new TokenizeResult(1, new Token(type, String.valueOf(value)));
		}
		return TokenizeResult.empty();
	}
}
