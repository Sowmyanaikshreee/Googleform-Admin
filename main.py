from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import JSONResponse, RedirectResponse, FileResponse
from starlette.middleware.sessions import SessionMiddleware
from models import verify_admin, get_user_tasks
from auth import get_current_admin
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

@app.get("/")
def root():
    return FileResponse("static/index.html")



@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    admin = verify_admin(username, password)
    if admin:
        request.session["admin"] = admin["email"]
        return RedirectResponse("/dashboard", status_code=302)
    return JSONResponse(content={"error": "Invalid credentials"}, status_code=401)

@app.get("/dashboard", response_class=FileResponse)
def dashboard_page(admin: str = Depends(get_current_admin)):
    return FileResponse("static/dashboard.html")

@app.get("/dashboard/data")
def dashboard_data(admin: str = Depends(get_current_admin)):
    tasks = get_user_tasks()
    return {"tasks": tasks}


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=302)
