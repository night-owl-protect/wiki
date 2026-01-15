# API Endpoints

Complete reference of Night Owl Protect API endpoints.

## Devices

### List Devices

```http
GET /v1/devices
```

**Response:**
```json
{
  "data": [
    {
      "id": "dev_abc123",
      "name": "Front Door Camera",
      "type": "camera",
      "status": "online",
      "model": "NOP-4K-CAM"
    }
  ]
}
```

### Get Device

```http
GET /v1/devices/{device_id}
```

### Control Device

```http
POST /v1/devices/{device_id}/control
```

**Body:**
```json
{
  "action": "reboot"
}
```

## Recordings

### List Recordings

```http
GET /v1/devices/{device_id}/recordings
```

**Query Parameters:**
- `start_date` - ISO 8601 date
- `end_date` - ISO 8601 date
- `event_type` - motion, human, vehicle

### Get Recording

```http
GET /v1/recordings/{recording_id}
```

### Download Recording

```http
GET /v1/recordings/{recording_id}/download
```

## Alerts

### List Alerts

```http
GET /v1/alerts
```

### Get Alert

```http
GET /v1/alerts/{alert_id}
```

### Mark as Read

```http
POST /v1/alerts/{alert_id}/read
```

## Live Stream

### Get Stream URL

```http
GET /v1/devices/{device_id}/stream
```

**Response:**
```json
{
  "stream_url": "rtsp://...",
  "expires_at": "2024-01-15T12:00:00Z"
}
```

---

For complete documentation, visit [developers.nightowlsp.com](https://developers.nightowlsp.com).
