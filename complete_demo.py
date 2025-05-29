# Complete Sanskrit Programming Language Demo
from transpiler import run_sanskrit_code

def demo_basic_features():
    print("\n🔸 Basic Programming Constructs")
    print("-" * 40)
    
    basic_code = [
        "टिप्पणी: Basic variables and arithmetic",
        "a = 10",
        "b = 20",
        "योग = a + b",
        "प्रदर्शय('Sum:', योग)",
        "",
        "टिप्पणी: Conditional statements",
        "यदि योग > 25:",
        "    प्रदर्शय('Sum is greater than 25')",
        "अन्यथा:",
        "    प्रदर्शय('Sum is 25 or less')"
    ]
    
    run_sanskrit_code(basic_code)

def demo_loops_and_functions():
    print("\n🔸 Loops and Functions")
    print("-" * 40)
    
    loop_code = [
        "टिप्पणी: Loop example",
        "के लिये i में श्रेणी(5):",
        "    यदि i % 2 == 0:",
        "        प्रदर्शय('Even:', i)",
        "",
        "टिप्पणी: Function definition",
        "परिभाषित factorial(n):",
        "    यदि n <= 1:",
        "        लौटाएँ 1",
        "    अन्यथा:",
        "        लौटाएँ n * factorial(n - 1)",
        "",
        "result = factorial(5)",
        "प्रदर्शय('Factorial of 5:', result)"
    ]
    
    run_sanskrit_code(loop_code)

def demo_advanced_features():
    print("\n🔸 Advanced Features")
    print("-" * 40)
    
    advanced_code = [
        "टिप्पणी: Import statements",
        "आयात sqrt से math",
        "आयात datetime से datetime",
        "",
        "टिप्पणी: List operations",
        "numbers = [1, 4, 9, 16, 25]",
        "के लिये num में numbers:",
        "    root = sqrt(num)",
        "    प्रदर्शय(f'Square root of {num} is {root}')",
        "",
        "टिप्पणी: File operations with context manager",
        "आसपास खोलें('sanskrit_output.txt', 'w') जैसा file:",
        "    file.write('यह संस्कृत भाषा में लिखा गया है!\\n')",
        "    file.write('This was written in Sanskrit language!\\n')",
        "",
        "प्रदर्शय('File created successfully!')"
    ]
    
    run_sanskrit_code(advanced_code)

if __name__ == "__main__":
    print("🕉️  संस्कृत प्रोग्रामिंग भाषा - पूर्ण प्रदर्शन  🕉️")
    print("🕉️  Sanskrit Programming Language - Complete Demo  🕉️")
    print("=" * 70)
    
    demo_basic_features()
    demo_loops_and_functions()
    demo_advanced_features()
    
    print("\n✨ All Sanskrit programming features working successfully! ✨")
    print("🎯 Context managers, imports, functions, loops - everything works!")
