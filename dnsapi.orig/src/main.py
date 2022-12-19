from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import dns.resolver
import dns.reversename


app = FastAPI()

@app.get("/api/", response_class=HTMLResponse)
async def read_items(domain: str):
    a = dns.resolver.resolve(domain, 'A')

    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    
    for val in a:
        return HTMLResponse(content=html_content, status_code=200)
        return {"The IP for " + domain + " is": val.to_text()}

