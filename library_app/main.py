from models.book import Book
from services.library_service import search_book,borrow_book
from utils.json_utils import save_json

book = Book("Python",100)
book.introduce()
search_result = search_book("Python")
if search_result is not None:
    print("搜索结果:",search_result)
else:
    print("搜索失败")
borrow_result = borrow_book("YesPython")
if borrow_result is not None:   
    print("借书结果:",borrow_result)
    save_json(borrow_result,"borrow_result.json")
    print("借书结果已保存")
else:
    print("借书失败，本次操作未保存")
