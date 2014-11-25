__author__ = 'christianvelez'

class Node:
	def __init__(self, name='Node'):
		self.name = name
		pass
	def __eq__(self, other):
		if type(other) == str:
			return self.name == other
		elif type(other) == type(self):
			return self.name == other.name

class NegExpr(Node):
	def __init__(self, expr=None):
		Node.__init__(self, 'NegExpr')
		self.expr = expr

	def __repr__(self):
		return "<%s expr=%s >" % (self.name, repr(self.expr))

class ThenExpr(Node):
	def __init__(self, lexpr=None, rexpr=None):
		Node.__init__(self, 'ThenExpr')
		self.lexpr = lexpr
		self.rexpr = rexpr

	def __repr__(self):
		return "<%s l=%s r=%s>" % (self.name, repr(self.lexpr), repr(self.rexpr))

class OrExpr(Node):
	def __init__(self, lexpr=None, rexpr=None, exclusive=False):
		Node.__init__(self, 'OrExpr')
		self.lexpr = lexpr
		self.rexpr = rexpr
		self.exclusive = exclusive
		
	def __repr__(self):
		return "<%s l=%s r=%s>" % (self.name, repr(self.lexpr), repr(self.rexpr))

class AndExpr(Node):
	def __init__(self, lexpr=None, rexpr=None):
		Node.__init__(self, 'AndExpr')
		self.lexpr = lexpr
		self.rexpr = rexpr

	def __repr__(self):
		return "<%s l=%s r=%s >" % (self.name, repr(self.lexpr), repr(self.rexpr))

class Variable(Node):
	def __init__(self, string=None):
		Node.__init__(self, 'Variable')
		self.string = string

	def __repr__(self):
		return "<%s var=%s >" % (self.name, repr(self.string))