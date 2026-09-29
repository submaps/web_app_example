from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utils import get_values

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return f"""
    <html>
        <head>
            <title>Web app example</title>
        </head>
        <body>
            <h1> y = x ^ 2 </h1>
            {get_values()}
        </body>
    </html>
    """