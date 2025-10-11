package org.theolang.compiler.lexer;

import java.lang.Character;
import java.util.ArrayList;

/*
 * Context for storing char list and current position.
 * This gets passed to each lexer callable.
 */
class LexContext {
	private ArrayList<Character> data;
	private int index = 0;

	public LexContext(ArrayList<Character> data) {
		this.data = data;
	}

	public char current() {
		return data.get(index);
	}

	public char atOffset(int offset) {
		return data.get(index + offset);
	}

	public int length() {
		return data.size();
	}

	public void consume(int n) {
		index += n;
	}

    /*
     * Check if we can consume the next n chars without
     * going past the data length
     */
    public boolean checkConsume(int n) {
        return (index + n) < data.size();
    }

    public boolean hasNext() {
        return index < data.size();
    }
}
