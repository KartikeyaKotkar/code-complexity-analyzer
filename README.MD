# Code Complexity Analyzer

A Python-based tool to analyze the time and space complexity of code snippets. This project parses Python code using the `ast` module and calculates the complexity based on predefined rules.

---

## Features

- **Time Complexity Analysis**: Estimates the Big O notation for time complexity.
- **Space Complexity Analysis**: Estimates the Big O notation for space complexity.
- **Supports Common Constructs**: Analyzes loops, nested loops, function calls, and more.
- **Extensible**: Easily add new rules for analyzing additional constructs.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/code-complexity-analyzer.git
   cd code-complexity-analyzer
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Analyze a Code Snippet

1. Save your Python code in a file or pass it directly as a string.
2. Use the `analyze_code` function from `src/main.py` to analyze the code.

Example:
```python
from src.main import analyze_code

code = """
for i in range(n):
    for j in range(n):
        print(i, j)
"""
analyze_code(code)
```

Output:
```
Time Complexity: O(n^2)
Space Complexity: O(1)
```

### Run Tests

To ensure the analyzer works correctly, run the unit tests:
```bash
python -m unittest tests/test_code_samples.py
```

---

## How It Works

1. **Parsing**: The code is parsed into an Abstract Syntax Tree (AST) using Python's `ast` module.
2. **Analysis**: The `ComplexityAnalyzer` class traverses the AST and applies rules to calculate time and space complexity.
3. **Rules**: Common constructs like loops, function calls, and recursion are analyzed using predefined rules in `src/rules.py`.

---

## Supported Constructs

| Construct          | Time Complexity | Space Complexity |
|--------------------|-----------------|------------------|
| Single Loop        | O(n)           | O(1)             |
| Nested Loops       | O(n^2)         | O(1)             |
| Function Calls     | Depends on function | Depends on function |
| Recursion          | O(2^n)         | O(n)             |
| Sorting            | O(n log n)     | O(n)             |

---

## Contributing

Contributions are welcome! Here’s how you can help:

1. **Add New Rules**: Extend the `src/rules.py` file to support more constructs.
2. **Improve Accuracy**: Enhance the analyzer to handle edge cases and dynamic inputs.
3. **Add Language Support**: Extend the tool to analyze code in other programming languages.

To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Python's `ast` module for code parsing.
---

