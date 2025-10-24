package org.theolang.compiler.lexer;

import java.lang.Exception;

import org.theolang.compiler.token.TokenizeResult;
import org.theolang.compiler.token.TokenType;
import org.theolang.compiler.token.Token;

class StringLexer extends LexerCallable {

	public StringLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		String value = "";
		int consumed = 0;
		char current = ctx.current();
		if (current == '"' || current == '\'') {
			consumed = 1;
			char closingQuote = current;
			current = ctx.atOffset(consumed);
			while (!(current == closingQuote)) {
				value += current;
				consumed += 1;
				current = ctx.atOffset(consumed);
			}
			return new TokenizeResult(
				consumed + 1,
				new Token(TokenType.STRING, value)
			);
		}
		return TokenizeResult.empty();
	}
}
