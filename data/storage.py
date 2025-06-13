from schemas.user_schema import User
from schemas.event_schema import Event
from schemas.speaker_schema import Speaker

# Initialize with sample data
users = [
    User(id=1, name="Admin User", email="admin@example.com"),
    User(id=2, name="Regular User", email="user@example.com")
]

events = [
    Event(id=1, title="Karatu 2024 Graduation ceremony", location="Lagos", date="2024-10-15T09:30:00"),
    Event(id=2, title="Workshop", location="Online", date="2024-11-20T14:00:00")
]

speakers = [
    Speaker(id=1, name="Dr. Smith", topic="Quantum Computing"),
    Speaker(id=2, name="Jane Doe", topic="Web Security"),
    Speaker(id=3, name="Alex Johnson", topic="DevOps Best Practices")
]

event_speakers = [
    {"event_id": 1, "speaker_id": 1},
    {"event_id": 1, "speaker_id": 2},
    {"event_id": 2, "speaker_id": 3}
]

registrations = []