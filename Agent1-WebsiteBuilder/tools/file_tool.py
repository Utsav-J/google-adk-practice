import datetime
from pathlib import Path

def write_to_file(content:str) -> dict:
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = f"output/{timestamp}_generated_page.html"
    Path("output").mkdir(exist_ok=True)
    Path(filename).write_text(content, encoding="utf-8")
    return {"status":200, "message":f"wrote to {filename}"}