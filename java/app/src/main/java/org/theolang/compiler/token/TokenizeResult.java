package org.theolang.compiler.token;

public class TokenizeResult {
	public final int consumedChars;
	public final Token token;

	public TokenizeResult(int consumedChars, Token token) {
		this.consumedChars = consumedChars;
		this.token = token;
	}

	public TokenizeResult(int consumedChars) {
		this.consumedChars = consumedChars;
		this.token = null;
	}

	public String toString() {
		return "TokenizeResult(%d, %s)"
			.formatted(consumedChars, token);
	}

    /*
     * Util method for creating an empty result
     */
    public static TokenizeResult empty() {
        return new TokenizeResult(0, null);
    }
}
