# API Authentication

Secure your API requests with proper authentication.

## Authentication Methods

### OAuth 2.0 (Recommended)

Night Owl Protect API uses OAuth 2.0 for authentication. We support:

- **Authorization Code** - For web applications
- **PKCE** - For mobile and SPA applications
- **Client Credentials** - For server-to-server

### API Keys (Legacy)

API keys are being phased out. Please migrate to OAuth 2.0.

## OAuth 2.0 Flow

### Step 1: Register Application

1. Go to [developers.nightowlsp.com](https://developers.nightowlsp.com)
2. Create new application
3. Note your `client_id` and `client_secret`
4. Add redirect URIs

### Step 2: Authorization Request

Direct users to:

```
https://auth.nightowlsp.com/oauth/authorize?
  client_id=YOUR_CLIENT_ID&
  redirect_uri=YOUR_REDIRECT_URI&
  response_type=code&
  scope=devices:read alerts:read recordings:read&
  state=random_state_string
```

### Step 3: Handle Callback

User is redirected back with authorization code:

```
https://your-app.com/callback?code=AUTHORIZATION_CODE&state=random_state_string
```

### Step 4: Exchange for Tokens

```bash
curl -X POST https://auth.nightowlsp.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "code": "AUTHORIZATION_CODE",
    "redirect_uri": "YOUR_REDIRECT_URI"
  }'
```

Response:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...",
  "scope": "devices:read alerts:read recordings:read"
}
```

## Using Access Tokens

Include the access token in all API requests:

```bash
curl -X GET https://api.nightowlsp.com/v1/devices \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Refreshing Tokens

Access tokens expire after 1 hour. Use refresh token to get new ones:

```bash
curl -X POST https://auth.nightowlsp.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "refresh_token",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "refresh_token": "YOUR_REFRESH_TOKEN"
  }'
```

## Available Scopes

| Scope | Description |
|-------|-------------|
| `devices:read` | List and view device info |
| `devices:write` | Control devices |
| `alerts:read` | View alerts |
| `alerts:write` | Manage alerts |
| `recordings:read` | Access recordings |
| `recordings:write` | Download/export recordings |
| `users:read` | View user profile |
| `users:write` | Update user settings |

## Security Best Practices

1. **Never expose secrets** - Keep `client_secret` server-side only
2. **Use HTTPS** - All requests must use HTTPS
3. **Validate state** - Prevent CSRF attacks
4. **Store tokens securely** - Encrypt at rest
5. **Implement token rotation** - Refresh tokens regularly
6. **Use minimum scopes** - Request only what you need

## Error Codes

| Code | Description |
|------|-------------|
| `invalid_request` | Malformed request |
| `invalid_client` | Unknown client |
| `invalid_grant` | Invalid authorization code |
| `unauthorized_client` | Client not authorized for grant |
| `access_denied` | User denied access |
| `invalid_scope` | Unknown scope requested |

---

**Next:** Explore available [API Endpoints](endpoints.md).
