🎟️ Event Manager API

Streamline event registrations, track attendance, and manage speakers—all via a clean, fast API.

🚀 Quick Start

Install: Clone repo → pip install -r requirements.txt

Run: uvicorn main:app --reload

Explore: http://localhost:8000/docs (Swagger UI)

🔍 Core Features
📌 Entities

User: Register, toggle active status

Event: Open/close registration, CRUD

Speaker: Pre-loaded (3 speakers on init)

Registration: One-click signups + attendance tracking

✅ Smart Rules

✔ Active users only

✔ No duplicate event registrations

✔ Event must be open to register

🌐 Endpoints at a Glance
Entity	HTTP Method	Endpoint	Action
Users	POST	/users/	Create a user
GET	/users/{user_id}	Get user details
PATCH	/users/{user_id}/deactivate	Deactivate user (is_active=False)
Events	POST	/events/	Create an event
PATCH	/events/{event_id}/close	Close registration (is_open=False)
Registrations	POST	/registrations/	Register a user for an event
PATCH	/registrations/{reg_id}	Mark attendance (attended=True)
GET	/registrations/user/{user_id}	List all registrations for a user

💡 Example Use Cases

🎤 Conference Mgmt: Track speaker topics + attendee ratios

🏫 Workshop Signups: Close registration when seats fill

📊 Attendance Reports: Filter users who attended ≥1 event (optional bonus)

🛠️ Tech Stack

FastAPI (Python) + Pydantic validation

In-memory storage (lists/dicts)

Modular design: routes/, schemas/, services/

✨ No auth needed—focus on the event logic, not permissions.

Inspired? Fork it, break it, build atop it. 🚀