import ast

def parse_code(code):
    """
    Parse the input code into an AST.
    """
    try:
        tree = ast.parse(code)
        return tree
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return None