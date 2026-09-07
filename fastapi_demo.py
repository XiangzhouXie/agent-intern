from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
import json
load_dotenv()
client = OpenAI(
    api_key = os.getenv("DEEPSEEK_API_KEY"),
    base_url = "https://api.deepseek.com"
)


app = FastAPI()

class ChatRequest(BaseModel):
    message:str

def calculator(a:float,b:float,operation:str):
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        return a / b
tools = [
    {
        "type":"function",
        "name":"calculator",
        "description":"执行两个数字加减乘除运算",
        "parameters":{
           "type":"object",
           "properties":{
            "a":{"type":"number"},
            "b":{"type":"number"},
            "operation":{
                "type":"string",
                "enum":["add","subtract","multiply","divide"]
            }
           },
           "required":["a","b","operation"] 
        }
    }
]  
@app.get("/health")
def health():
    return{
        "status":"ok"
    }

@app.post("/chat")
def chat(request:ChatRequest):
    response = client.responses.create(
        model = "deepseek-v4-flash",
        input = request.message,
        tools = tools
    )
    print(response.output)
    tool_call = None
    for item in response.output:
        if item.type =="function_call":
            tool_call = item
    if tool_call is None:
        return {
            "answer": response.output_text
        }
    arguments = json.loads(tool_call.arguments)
    result = calculator(
        arguments["a"],
        arguments["b"],
        arguments["operation"]
    )
    final_response = client.responses.create(
        model = "deepseek-v4-flash",
        input =[
            {
                "role":"user",
                "content":request.message
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
        tools = tools
    )
    return{
        "answer":final_response.output_text
    }