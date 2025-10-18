# Dynamic Profile Endpoint

This project is part of the **Backend Engineering Task** — 
a simple Flask API that returns your dynamic profile information along with a random fact from an external API.

---

## Live Endpoint

**Base URL:**  
[https://web-production-28480.up.railway.app](https://web-production-28480.up.railway.app)

**Endpoint:**  
`GET /me`

**Full URL:**  
[https://web-production-28480.up.railway.app/me](https://web-production-28480.up.railway.app/me)

---

## Example Response

```json
{
  "status": "success",
  "user": {
    "email": "your_email@example.com",
    "name": "Oba Republic",
    "stack": "Backend (Python/Flask)"
  },
  "timestamp": "2025-10-18T14:33:21.512Z",
  "fact": "Cats can rotate their ears 180 degrees."
}
