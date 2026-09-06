from pydantic import BaseModel,ValidationError
import os
from dotenv import load_dotenv
from openai import OpenAI
class Student(BaseModel):
    name:str 
    age:int
    major:str | None = None
load_dotenv()
client = OpenAI(
    api_key = os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
response = client.responses.create(
    model="deepseek-v4-flash",
    input="从这句话中提取学生信息:小明今年20岁,是计算机专业。",
    text={
        "format": {
            "type": "json_schema",
            "name": "student",
            "schema": Student.model_json_schema()
        }
    }
)
print(response.output_text)
student = Student.model_validate_json(response.output_text)
print(student)
print(student.model_dump())
bad_data = '''
{
    "name": "小明",
    "age": "20"
}
'''
try:
    student2 = Student.model_validate_json(bad_data)
    print(student2)
    print(type(student2.age))
except ValidationError as e:
    print("数据校验失败：",e)