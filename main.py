from fastapi import FastAPI
from fastapi import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sayHello/{name}")
async def dynamic_content(name: str):
    html_content = open("sayHello.html").read()  
    dynamic_html = html_content.replace("{{ name }}", name)  
    return FileResponse(content=dynamic_html, media_type="text/html")
