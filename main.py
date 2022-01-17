from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def main():
    content = head_html + """
    <marquee width="525" behavior="alternate"><h1 style="color:red;font-family:Arial">Please Upload Your Scenes!</h1></marquee>
    """
    return content



head_html = """
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
"""