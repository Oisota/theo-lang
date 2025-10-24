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

class TestStringLexer {
	@ParameterizedTest
	@MethodSource("testStringProvider")
	void testLexString(String input, String output, int consumed) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new StringLexer(ctx);
		var result = lexer.call();
		assertEquals(consumed, result.consumedChars);
		if (output == null) {
			assertEquals(null, result.token);
		} else {
			assertEquals(TokenType.STRING, result.token.type);
			assertEquals(output, result.token.value);
		}
	}

	static Stream<Arguments> testStringProvider() {
		return Stream.of(
			Arguments.of("\"abc\"", "abc", 5),
			Arguments.of("'def'", "def", 5),
			Arguments.of("abc'hij'", null, 0)
		);
	}
}
