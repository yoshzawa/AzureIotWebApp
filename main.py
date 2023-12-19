from fastapi import FastAPI
from fastapi import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sayHello/{name}")
async def dynamic_content(name: str):

    if not template_path.exists():
        return PlainTextResponse("Error: File not found", status_code=500)
    return {"Hello": "World"}


@app.get("/sayHello2/{name}")
async def dynamic_content(name: str):

    if not template_path.exists():
        return PlainTextResponse("Error: File not found", status_code=500)

    try:
        template_path = Path(__file__).parent / "sayHello.html"
    except Exception as e:
        print(f"Error: {e}")
        return PlainTextResponse(f"Error1: {e}", status_code=500)
    try:
        html_content = template_path.read_text()
    except Exception as e:
        print(f"Error: {e}")
        return PlainTextResponse(f"Error2: {e}", status_code=500)
    try:
        dynamic_html = html_content.replace("{{ name }}", name)  
    except Exception as e:
        print(f"Error: {e}")
        return PlainTextResponse(f"Error3: {e}", status_code=500)
    try:
        return FileResponse(content=dynamic_html, media_type="text/html")
    except Exception as e:
        print(f"Error: {e}")
        return PlainTextResponse(f"Error4: {e}", status_code=500)
