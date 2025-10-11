package org.theolang.compiler.util;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.lang.Character;
import java.lang.Iterable;
import java.util.Iterator;
import java.util.Optional;
import java.util.Collections;
import java.nio.charset.Charset;

public class CharFileIterable implements Iterable<Character> {
	private File file;
	private Charset encoding;

	public CharFileIterable(String fileName) {
		this.file = new File(fileName);
		this.encoding = Charset.forName("UTF-8");
	}

	private Optional<Reader> getReader() {
		InputStream in;
		try {
			in = new FileInputStream(file);
		} catch (FileNotFoundException e) {
			System.out.println(e);
			System.out.println("Could not open file: " + file.toString());
			return Optional.empty();
		}
		Reader reader = new InputStreamReader(in, encoding);
		// buffer for efficiency
		Reader bufReader = new BufferedReader(reader);
		return Optional.of(bufReader);
	}

	@Override
	public Iterator<Character> iterator() {
		Optional<Reader> option = getReader();
		if (option.isPresent()) {
			return new CharFileIterator(option.get());
		} else {
			return Collections.emptyIterator();
		}
	}
}
