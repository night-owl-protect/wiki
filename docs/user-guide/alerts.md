# Smart Alerts

Configure intelligent notifications for motion, people, vehicles, and more.

## Alert Types

### Motion Detection

Basic motion sensing for any movement in camera view.

### Human Detection

AI-powered detection specifically for people.

- Reduces false alerts from animals, shadows, trees
- Identifies human shapes and movement patterns
- Works in various lighting conditions

### Face Detection

Alerts when a human face is detected.

- Focus on entry points and access areas
- Option to blur faces in recordings
- Enhanced facial recognition (premium feature)

### Vehicle Detection

Specific alerts for cars, trucks, motorcycles.

- Great for driveways and parking areas
- Can distinguish parking from passing traffic
- License plate capture support (select cameras)

### Package Detection

Alerts when deliveries arrive.

- Detects package shapes at door areas
- Timed alerts for extended package presence
- Integration with doorbell cameras

### Sound Detection

Audio-based alerts for:

- Glass breaking
- Smoke/CO alarms
- Baby crying
- Dog barking
- Custom sound profiles

## Configuring Alerts

### Global Alert Settings

1. Go to **Settings** → **Notifications**
2. Configure options:
   - Enable/disable all alerts
   - Alert sounds
   - Vibration patterns
   - LED colors (Android)

### Per-Camera Settings

1. Go to camera **Settings** → **Alerts**
2. Toggle alert types:
   - ☑️ Motion Detection
   - ☑️ Human Detection
   - ☐ Vehicle Detection
   - ☐ Package Detection
   - ☐ Sound Detection

### Detection Zones

Define specific areas of the camera view to monitor:

1. Open camera **Settings** → **Detection Zones**
2. Tap **Add Zone**
3. Draw a box around the area
4. Name the zone (e.g., "Front Door", "Driveway")
5. Set sensitivity for that zone

```{tip}
Exclude busy roads or swaying trees to reduce false alerts.
```

## Sensitivity Settings

### Motion Sensitivity

| Level | Description | Best For |
|-------|-------------|----------|
| Low | Large movements only | Outdoor, windy areas |
| Medium | Balanced detection | General use |
| High | Small movements | Indoor, low traffic |
| Custom | Fine-tuned values | Advanced users |

### AI Confidence Threshold

Set how confident the AI needs to be before alerting:

- **50%** - More alerts, some false positives
- **70%** - Balanced (recommended)
- **90%** - Fewer alerts, high accuracy

## Alert Schedules

### Quiet Hours

Disable notifications during specific times:

1. Go to **Settings** → **Notifications** → **Schedule**
2. Enable **Quiet Hours**
3. Set start and end times
4. Choose days of week

### Home/Away Modes

Automatic alert adjustments based on location:

| Mode | Behavior |
|------|----------|
| Home | Indoor cameras off, outdoor on |
| Away | All cameras active |
| Night | Motion sensitivity increased |
| Vacation | Enhanced all alerts |

### Geofencing

Automatically switch modes based on your location:

1. Go to **Settings** → **Location**
2. Enable **Geofencing**
3. Set your home location
4. Define radius (100m - 500m)
5. App auto-switches Home/Away

## Alert Actions

### Notification Options

When an alert triggers:

- **Push notification** - Standard app notification
- **Email** - Detailed email with snapshot
- **SMS** - Text message (premium)
- **Phone call** - Audio call (premium)

### Quick Actions from Alerts

Tap and hold a notification for:

- View live camera
- Play recording
- Turn on siren (if equipped)
- Speak through camera
- Dismiss alert
- Snooze camera (15 min/1 hr/until home)

### Automated Responses

Set up automatic actions:

1. Go to **Settings** → **Automation**
2. Create rule:
   - **If**: Human detected at Front Door
   - **Then**: Turn on porch light
   - **And**: Start recording for 5 minutes

## Alert History

### Viewing Alert History

1. Tap **🔔 Alerts** from dashboard
2. Browse chronological list
3. Filter by:
   - Camera
   - Alert type
   - Date range
   - Read/Unread

### Alert Analytics

View patterns in your alerts:

1. Go to **Alerts** → **Analytics**
2. See statistics:
   - Alerts per day/week/month
   - Most active cameras
   - Peak activity times
   - Detection type breakdown

### Managing Alert Storage

- Alerts are stored for 30 days
- Tap **Clear All** to remove old alerts
- Important alerts can be starred and kept longer

---

**Next:** Configure [Settings](settings.md) to customize your Night Owl Protect experience.
