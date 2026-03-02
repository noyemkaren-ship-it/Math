
from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

formul = ["S = п*r²","C = п*d", "S=a*b", "P=a2+b2", "P = 2πr"]

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "so": formul[0],
            "co": formul[1],
            "po": formul[4]
        })

@app.get("/fSO")
async def fso(a: float):
    result = a * a * 3.14
    return {"answer": round(result, 2)}  # Округляем до 2 знаков

@app.get("/fCO")
async def fco(a: float):
    result = a * 3.14
    return {"answer": round(result, 2)}

@app.get("/fPO")
async def fpo(a: float):
    result = 2* 3.14 * a
    return {
        "answer": round(result, 2)
    } #p=2пr

@app.get("/test")
async def root(request: Request):
    return templates.TemplateResponse(
        "test.html", {
            "request": request,
        })

@app.get("/teorema_pifagora")
async def teoremap(request: Request):
    return templates.TemplateResponse(
        "teorema_pifagora.html", {
            "request": request,
        }
    )

@app.get("/seven")
async def sseven(request: Request):
    return templates.TemplateResponse(
        "seven.html", {
            "request": request
        }
    )