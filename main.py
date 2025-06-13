from fastapi import FastAPI
from routes.user import router as user_router
from routes.event import router as event_router
from routes.speaker import router as speaker_router
from routes.registration import router as registration_router


app = FastAPI()

app.include_router(user_router, prefix="/api/users")
app.include_router(event_router, prefix="/api/events")
app.include_router(speaker_router, prefix="/api/speakers")
app.include_router(registration_router, prefix="/api/registrations")