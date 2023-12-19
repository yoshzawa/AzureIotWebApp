from fastapi import FastAPI
from fastapi import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sayHello/{name}")
async def dynamic_content(name: str):
    try:
        template_path = Path(__file__).parent / "sayHello.html"
        html_content = template_path.read_text()
        dynamic_html = html_content.replace("{{ name }}", name)  
        return FileResponse(content=dynamic_html, media_type="text/html")
    except Exception as e:
        return PlainTextResponse(f"Error: {e}", status_code=500)
