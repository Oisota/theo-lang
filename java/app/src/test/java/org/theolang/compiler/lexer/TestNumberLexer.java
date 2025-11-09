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

class TestNumberLexer {
	@ParameterizedTest
	@MethodSource("testNumberProvider")
	void testLexNumber(String input, String output, int consumed, TokenType type) {
		var arr = new ArrayList<Character>();
		for (char c : input.toCharArray()) {
			arr.add(c);
		}
		var ctx = new LexContext(arr);
		var lexer = new NumberLexer(ctx);
		var result = lexer.call();
		assertEquals(consumed, result.consumedChars);
		if (output == null) {
			assertEquals(null, result.token);
		} else {
			assertEquals(type, result.token.type);
			assertEquals(output, result.token.value);
		}
	}

	static Stream<Arguments> testNumberProvider() {
		return Stream.of(
			Arguments.of("123", "123", 3, TokenType.INTEGER),
			Arguments.of("10_000", "10000", 6, TokenType.INTEGER),
			Arguments.of("0b1010", "0b1010", 6, TokenType.INTEGER),
			Arguments.of("0xFF", "0xFF", 4, TokenType.INTEGER),
			Arguments.of("lmnop", null, 0, TokenType.INTEGER),
			Arguments.of("52.4", "52.4", 4, TokenType.FLOAT),
			Arguments.of("52.4  ", "52.4", 4, TokenType.FLOAT)
			// TODO this should fail but its parsing since the individual chars are allowed as a number but it should fail since its not a hex number
			//Arguments.of("_abc", null, 0) 
		);
	}
}
