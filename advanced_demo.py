# Advanced Sanskrit Programming Language Demo
from transpiler import run_sanskrit_code

def test_complete_compatibility():
    print("🧪 Advanced Sanskrit Programming Features Demo")
    print("=" * 55)
    
    # Test all the features that were in the original demos
    compatibility_test = [
        "टिप्पणी: Complete compatibility test",
        "",
        "टिप्पणी: Basic variables (from demo.py)",
        "a = 10",
        "b = 20", 
        "योग = a + b",
        "प्रदर्शय('Sum:', योग)",
        "",
        "टिप्पणी: Control flow (from working_transpiler.py)",
        "यदि योग > 25:",
        "    प्रदर्शय('Sum is greater than 25')",
        "अन्यथा:",
        "    प्रदर्शय('Sum is 25 or less')",
        "",
        "टिप्पणी: Import statements (fixed from working_transpiler.py)",
        "आयात sqrt से math",
        "number = 16",
        "वर्गमूल = sqrt(number)",
        "प्रदर्शय('Square root of', number, 'is', वर्गमूल)",
        "",
        "टिप्पणी: Function definition (from main.py)",
        "परिभाषित factorial(n):",
        "    यदि n <= 1:",
        "        लौटाएँ 1",
        "    अन्यथा:",
        "        लौटाएँ n * factorial(n - 1)",
        "",
        "result = factorial(5)",
        "प्रदर्शय('Factorial of 5:', result)",
        "",
        "टिप्पणी: Class definition (from main.py advanced features)",
        "वर्ग Person:",
        "    परिभाषित आरंभ(स्वयं, नाम):",
        "        स्वयं.नाम = नाम",
        "    ",
        "    परिभाषित introduce(स्वयं):",
        "        प्रदर्शय('Hello, I am', स्वयं.नाम)",
        "",
        "person = Person('राम')",
        "person.introduce()",
        "",
        "टिप्पणी: Context manager (fixed from working_transpiler.py)",
        "आसपास खोलें('compatibility_test.txt', 'w') जैसा file:",
        "    file.write('All compatibility tests passed!\\n')",
        "    file.write(f'Factorial result: {result}\\n')",
        "",
        "टिप्पणी: Assert statement (from main.py)",
        "सुनिश्चित करें result == 120",
        "",
        "प्रदर्शय('🎉 All compatibility tests passed! 🎉')"
    ]
    
    run_sanskrit_code(compatibility_test)

if __name__ == "__main__":
    test_complete_compatibility()
