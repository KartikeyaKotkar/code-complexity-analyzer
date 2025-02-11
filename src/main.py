from parser import parse_code
from analyzer import ComplexityAnalyzer

def analyze_code(code):
    tree = parse_code(code)
    if tree:
        analyzer = ComplexityAnalyzer()
        time, space = analyzer.analyze(tree)
        print(f"Time Complexity: {time}")
        print(f"Space Complexity: {space}")

code = """
for i in range(n):
    for j in range(n):
        print(i, j)
"""
analyze_code(code)