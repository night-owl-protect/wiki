# API Overview

Night Owl Protect offers a REST API for developers to integrate with our platform.

```{warning}
The API is currently in beta. Features and endpoints may change.
```

## Getting Started

### API Access

To use the Night Owl Protect API:

1. Create a developer account at [developers.nightowlsp.com](https://developers.nightowlsp.com)
2. Register your application
3. Obtain API credentials (Client ID and Secret)
4. Review API documentation

### Base URL

All API requests use this base URL:

```
https://api.nightowlsp.com/v1
```

### API Features

- 📹 **Device Management** - List and control cameras
- 🔔 **Alerts** - Retrieve and manage alerts
- 📼 **Recordings** - Access recorded footage
- 👤 **Users** - Manage account and sharing
- 📊 **Analytics** - Event statistics and reports

## Quick Example

Here's a simple example to list your devices:

```python
import requests

API_BASE = "https://api.nightowlsp.com/v1"
ACCESS_TOKEN = "your_access_token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(f"{API_BASE}/devices", headers=headers)
devices = response.json()

for device in devices["data"]:
    print(f"Device: {device['name']} - Status: {device['status']}")
```

## Rate Limits

| Plan | Requests/Hour | Requests/Day |
|------|---------------|--------------|
| Free | 100 | 1,000 |
| Developer | 1,000 | 10,000 |
| Business | 10,000 | 100,000 |
| Enterprise | Custom | Custom |

Rate limit headers included in responses:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1609459200
```

## Response Format

All responses use JSON format:

```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 100
  }
}
```

Error responses:

```json
{
  "success": false,
  "error": {
    "code": "INVALID_TOKEN",
    "message": "The access token is invalid or expired"
  }
}
```

## SDKs

Official SDKs available:

- **Python**: `pip install nightowl-protect`
- **JavaScript/Node**: `npm install nightowl-protect`
- **Java**: Maven repository

## Support

- 📚 [Full API Documentation](https://developers.nightowlsp.com/docs)
- 💬 [Developer Forum](https://community.nightowlsp.com/developers)
- 📧 [API Support](mailto:api-support@nightowlsp.com)

---

**Next:** Learn about [Authentication](authentication.md) to secure your API requests.
