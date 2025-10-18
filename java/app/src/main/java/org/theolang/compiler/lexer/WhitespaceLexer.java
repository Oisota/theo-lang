package org.theolang.compiler.lexer;

import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.IndexOutOfBoundsException;

import org.theolang.compiler.token.TokenizeResult;

class WhitespaceLexer extends LexerCallable {
	private Pattern pattern = Pattern.compile("\s");

	public WhitespaceLexer(LexContext ctx) {
		super(ctx);
	}

	public TokenizeResult call() {
        int consumed = 0;
        char current = ' ';

        try {
            current = ctx.atOffset(consumed);
        } catch (IndexOutOfBoundsException e) {
            return new TokenizeResult(consumed, null);
        }
        Matcher matcher = pattern.matcher(String.valueOf(current));
        while (matcher.matches()) {
            consumed += 1;
            matcher = pattern.matcher(String.valueOf(current));
            try {
                ctx.atOffset(consumed);
            } catch (IndexOutOfBoundsException e) {
                break;
            }
        }
        return TokenizeResult.empty();
	}
}
