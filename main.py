from fastapi import FastAPI, Response
from pathlib import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sayHello/{name}")
async def dynamic_content3(name: str):
    template_path = Path(__file__).parent / "sayHello.html"
    if not template_path.exists():
        return PlainTextResponse("Error: File not found", status_code=500)
    html_content = template_path.read_text()
    dynamic_html = html_content.replace("{{ name }}", name)  
    return Response(content=dynamic_html, media_type="text/html")
