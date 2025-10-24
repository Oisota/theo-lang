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

class TestCharLexer {
	@ParameterizedTest
	@MethodSource("testCharProvider")
	void testLexChar(
		String input,
		String output,
		char value,
		int consumed,
		TokenType type
	) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new CharLexer(ctx, type, value);
		var result = lexer.call();
		assertEquals(consumed, result.consumedChars);
		if (output == null) {
			assertEquals(null, result.token);
		} else {
			assertEquals(type, result.token.type);
			assertEquals(output, result.token.value);
		}
	}

	static Stream<Arguments> testCharProvider() {
		return Stream.of(
			Arguments.of("(", "(", '(', 1, TokenType.PAREN_OPEN),
			Arguments.of("x", null, '(', 0, TokenType.PAREN_OPEN)
		);
	}
}
