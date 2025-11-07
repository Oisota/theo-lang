package org.theolang.compiler.lexer;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.Arguments;
import static org.junit.jupiter.api.Assertions.*;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Character;

import org.theolang.compiler.token.TokenType;

class TestWhitespaceLexer {
	@ParameterizedTest
	@MethodSource("testTextProvider")
	void testLexWhitespace(
		String input,
		int consumed
	) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new WhitespaceLexer(ctx);
		var result = lexer.call();
		assertEquals(consumed, result.consumedChars);
		assertEquals(null, result.token);
	}

	static Stream<Arguments> testTextProvider() {
		return Stream.of(
			Arguments.of("    ", 4),
			Arguments.of("        ", 8),
			Arguments.of("\t", 1),
			Arguments.of("\n", 1),
			Arguments.of("\t    \n", 6),
			Arguments.of("abcd", 0),
			Arguments.of("    abcd", 4)
		);
	}
}
