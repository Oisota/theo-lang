package org.theolang.compiler.lexer;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

import org.theolang.compiler.token.TokenizeResult;
import org.theolang.compiler.token.TokenType;
import org.theolang.compiler.token.Token;

class IdentifierLexer extends LexerCallable {

	private Pattern pattern = Pattern.compile("([A-Z]|[a-z]|_|[0-9])+");
	private Pattern initialPattern = Pattern.compile("([A-Z]|[a-z]|_)+");

	public IdentifierLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
		int consumed = 0;
		String value = "";
		char current = ctx.current();
		Matcher matcher = initialPattern.matcher(String.valueOf(current));
		if (matcher.matches()) {
			matcher = pattern.matcher(String.valueOf(current));
			while (matcher.matches()) {
				consumed += 1;
				value += current;
				try {
					current = ctx.atOffset(consumed);
				} catch (IndexOutOfBoundsException e) {
					break;
				}
			}
			return new TokenizeResult(consumed, new Token(TokenType.IDENTIFIER, value));
		}
		return TokenizeResult.empty();
	}
}
