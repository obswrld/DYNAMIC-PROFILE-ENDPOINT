# Profile API

A simple RESTful API built with **Python + Flask** that returns my profile information and a random cat fact fetched from an external API.

---

## Features
- Returns JSON profile data
- Fetches a random cat fact dynamically from [catfact.ninja](https://catfact.ninja/fact)
- Includes current UTC timestamp in ISO 8601 format
- Handles external API errors gracefully

---

## Endpoint
**GET** `/me`

## Live Link
[https://web-production-28480.up.railway.app/me](https://web-production-28480.up.railway.app/me)

### Example Response
```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Name",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-17T12:00:00.000Z",
  "fact": "Cats can rotate their ears 180 degrees."
}
