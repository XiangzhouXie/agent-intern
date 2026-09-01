def calculator(a: int, b: int, operation: str) -> int:
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    else:
        return 0


tool_request: dict = {
    "tool": "calculator",
    "a": 10,
    "b": 5,
    "operation": "add"
}
tool_name = tool_request["tool"]
if tool_name == "calculator":
    result = calculator(tool_request["a"], tool_request["b"], tool_request["operation"])
    print(result)
