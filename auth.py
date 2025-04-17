from fastapi import Request, HTTPException
from fastapi.responses import RedirectResponse

def get_current_admin(request: Request):
    admin = request.session.get("admin")
    if not admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return admin
