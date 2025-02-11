import ast

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.time_complexity = "O(1)"
        self.space_complexity = "O(1)"
        self.loop_depth = 0  # Track nested loops

    def visit_For(self, node):
        """
        Analyze 'for' loops.
        """
        self.loop_depth += 1
        if self.loop_depth == 1:
            self.time_complexity = "O(n)"
        elif self.loop_depth == 2:
            self.time_complexity = "O(n^2)"
        self.generic_visit(node)
        self.loop_depth -= 1

    def visit_While(self, node):
        """
        Analyze 'while' loops.
        """
        self.loop_depth += 1
        if self.loop_depth == 1:
            self.time_complexity = "O(n)"
        elif self.loop_depth == 2:
            self.time_complexity = "O(n^2)"
        self.generic_visit(node)
        self.loop_depth -= 1

    def visit_Call(self, node):
        """
        Analyze function calls.
        """
        if isinstance(node.func, ast.Name):
            if node.func.id == "sort":
                self.time_complexity = "O(n log n)"
        self.generic_visit(node)

    def analyze(self, tree):
        """
        Analyze the given AST.
        """
        self.visit(tree)
        return self.time_complexity, self.space_complexity