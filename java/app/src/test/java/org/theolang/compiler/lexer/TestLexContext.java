package org.theolang.compiler.lexer;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.lang.Character;

class TestLexContext {
	@Test
	void testLexContext() {
		var arr = new ArrayList<Character>();
		arr.add('a');
		arr.add('b');
		arr.add('c');
		var ctx = new LexContext(arr);

		assertEquals(ctx.length(), 3);
		assertEquals(ctx.current(), 'a');
		assertEquals(ctx.atOffset(1), 'b');
		assertTrue(ctx.hasNext());
		assertTrue(ctx.checkConsume(1));
		assertFalse(ctx.checkConsume(5));
		ctx.consume(1);
		assertEquals(ctx.current(), 'b');
		ctx.consume(2);
		assertFalse(ctx.hasNext());
	}

	@Test
	void testPositionTracking() {
		var arr = new ArrayList<Character>();
		arr.add('a');
		arr.add('b');
		arr.add('c');
		arr.add('\n');
		arr.add('a');
		var ctx = new LexContext(arr);
		ctx.consume(5);
		assertEquals(ctx.getCurrentLine(), 2);
		assertEquals(ctx.getCurrentColumn(), 2);
	}
}
