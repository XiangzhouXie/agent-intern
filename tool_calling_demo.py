from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import os
import json
def calculator(a:float,b:float,operation:str):
    if operation == "add":
        return a+b
    if operation == "subtract":
        return a-b
    if operation == "multiply":
        return a*b
    if operation == "divide":
        return a/b

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tools = [
    {
        "type": "function",
        "name": "calculator",
        "description": "执行两个数字的加减乘除运算",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number"
                },
                "b": {
                    "type": "number"
                },
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"]
                }
            },
            "required": ["a", "b", "operation"]
        }
    },
    {
        "type":"function",
        "name":"get_time",
        "description":"获取当前时间"
    }
]
load_dotenv()
client = OpenAI(
    api_key = os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
response = client.responses.create(
    model = "deepseek-v4-flash",
    input = "现在几点了",
    tools = tools
)
print(response.output)
tool_call = None
for item in response.output:
    if item.type == "function_call":
        tool_call = item
print(tool_call.name)
print(tool_call.arguments)
arguments = json.loads(tool_call.arguments)
print(arguments)
print(type(arguments))
if tool_call.name == "calculator":
    result = calculator(
    arguments["a"],
    arguments["b"],
    arguments["operation"]
    )
elif tool_call.name == "get_time":
    result = get_time()
print(result)
final_response = client.responses.create(
    model = "deepseek-v4-flash",
    input =[
        {
            "role":"user",
            "content":"现在几点了"
        },
        {
            "type":"function_call",
            "call_id":tool_call.call_id,
            "name":tool_call.name,
            "arguments":tool_call.arguments
        },
        {
            "type":"function_call_output",
            "call_id":tool_call.call_id,
            "output":str(result)
        }
    ],
    tools=tools
)
print(final_response.output_text)