package org.theolang.compiler.lexer;

import java.util.concurrent.Callable;
import org.theolang.compiler.token.TokenizeResult;

abstract class LexerCallable implements Callable<TokenizeResult> {

	protected LexContext ctx;

	public LexerCallable(LexContext ctx) {
		this.ctx = ctx;
	}
}
