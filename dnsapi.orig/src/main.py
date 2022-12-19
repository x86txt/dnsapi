from fastapi import FastAPI
import dns.resolver
import dns.reversename
import json

app = FastAPI()

@app.get("/api/")
async def read_item(domain: str | None = None):
    a = dns.resolver.resolve(domain, 'A')
    for val in a:
        print(vars(a))
        #return {"IP": val}

