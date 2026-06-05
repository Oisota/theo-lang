package org.theolang.compiler.ast;

class BinaryExpr extends Expr {
	private Expr left;
	private Expr right;
	private Oper operator;
}
