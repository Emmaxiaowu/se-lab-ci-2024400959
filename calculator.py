class Calculator:
    """一个简单的计算器类"""

    def add(self, a, b):
        """加法"""
        return a + b

    def subtract(self, a, b):
        """减法"""
        return a - b

    def multiply(self, a, b):
        """乘法"""
        return a * b

    def divide(self, a, b):
        """除法，除数为0时抛出异常"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
