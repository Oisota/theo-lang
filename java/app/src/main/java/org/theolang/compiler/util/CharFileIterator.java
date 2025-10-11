package org.theolang.compiler.util;

import java.io.Reader;
import java.io.IOException;
import java.lang.Character;
import java.util.Iterator;
import java.util.NoSuchElementException;


class CharFileIterator implements Iterator<Character> {
	private Reader reader;

	public CharFileIterator(Reader reader) {
		this.reader = reader;
	}

	@Override
	public boolean hasNext() {
		try {
			return reader.ready();
		} catch (IOException e) {
			return false;
		}
	}

	@Override
	public Character next() {
		int result;
		try {
			result = reader.read();
			return (char) result;
		} catch (IOException e) {
			throw new NoSuchElementException("No more characters in file");
		}
	}
}
