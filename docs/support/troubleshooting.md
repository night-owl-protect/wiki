# Troubleshooting Guide

Solutions for common issues with Night Owl Protect.

## Connection Issues

### Camera Shows "Offline"

**Symptoms:**
- Camera tile shows offline status
- Cannot view live feed
- No recordings available

**Solutions:**

1. **Check power**
   - Verify camera is receiving power
   - Check power adapter and cables
   - Try a different outlet

2. **Check network**
   - Ensure router is working
   - Test other devices on same network
   - Restart router

3. **Restart camera**
   - Unplug power for 30 seconds
   - Plug back in
   - Wait 2 minutes for boot

4. **Check WiFi signal**
   - Move camera closer to router
   - Remove interference sources
   - Consider WiFi extender

### App Cannot Connect to Devices

**Solutions:**

1. **Check internet connection**
   - Switch between WiFi and mobile data
   - Test other apps requiring internet

2. **Force close and reopen app**
   - iOS: Swipe up and close app
   - Android: Clear from recent apps

3. **Check firewall settings**
   ```
   Required ports:
   - TCP: 80, 443, 8080
   - UDP: 1024-65535
   ```

4. **Update app**
   - Check App Store/Play Store for updates

### Slow or Buffering Video

**Causes:**
- Insufficient bandwidth
- Network congestion  
- Distance from router

**Solutions:**

1. Lower video quality in settings
2. Connect to 5GHz WiFi if available
3. Close other streaming apps
4. Restart router
5. Check ISP for outages

## Video Quality Issues

### Blurry Video

**Solutions:**
- Clean camera lens
- Check focus setting (if adjustable)
- Ensure adequate lighting
- Verify resolution settings

### Dark Night Vision

**Solutions:**
- Check IR LED status
- Clean lens cover
- Ensure night vision is enabled
- Check for IR reflection (avoid pointing at walls)

### Washed Out or Overexposed

**Solutions:**
- Adjust WDR settings
- Check exposure settings
- Reposition camera away from direct light
- Enable backlight compensation

## Alert Issues

### Not Receiving Notifications

**Checklist:**

1. **App settings**
   - Settings → Notifications → Enabled ✓
   
2. **Phone settings**
   - iOS: Settings → Night Owl Protect → Notifications
   - Android: Settings → Apps → Night Owl Protect → Notifications

3. **Camera settings**
   - Detection enabled for camera ✓
   - Sensitivity not too low ✓

4. **Schedule**
   - Quiet hours not active ✓
   - Home mode not suppressing alerts ✓

5. **Battery optimization**
   - Disable battery saver for app
   - Allow background activity

### Too Many False Alerts

**Solutions:**

1. **Adjust sensitivity**
   - Lower motion sensitivity
   - Increase AI confidence threshold

2. **Set detection zones**
   - Exclude roads, trees, flags
   - Focus on entry points only

3. **Enable smart detection**
   - Human-only detection
   - Vehicle-only detection
   - Package detection

4. **Check camera placement**
   - Avoid pointing at busy areas
   - Mount at appropriate height (8-10 ft)

## Recording Issues

### Recordings Missing

**Check:**
- Storage plan status
- HDD health (for NVR)
- Recording schedule
- Detection settings

**Solutions:**
1. Verify cloud subscription active
2. Check NVR storage isn't full
3. Review recording mode settings
4. Ensure motion detection is on

### Cannot Download Clips

**Solutions:**
- Check available storage on phone
- Verify internet connection
- Try smaller clip duration
- Use web portal instead

### Playback Not Working

**Solutions:**
1. Wait for video to buffer
2. Try different playback speed
3. Check internet connection
4. Clear app cache
5. Reinstall app if persistent

## Hardware Issues

### Camera Not Powering On

1. Test power adapter with multimeter
2. Try different power outlet
3. Check cable connections
4. If PoE: verify NVR port working
5. Contact support for warranty claim

### Audio Not Working

**2-Way Audio:**
1. Check microphone permissions
2. Verify speaker not muted
3. Test with different device
4. Reset camera to defaults

### NVR HDD Issues

**Symptoms:**
- Recording stops
- "No HDD" error
- Clicking sounds

**Solutions:**
1. Check HDD connections
2. Initialize/format HDD in settings
3. Replace HDD if failing
4. Verify HDD compatibility

## App Issues

### App Crashing

1. Update to latest version
2. Restart phone
3. Clear app cache
4. Reinstall app
5. Check for iOS/Android updates

### Login Problems

1. Verify email and password
2. Reset password if forgotten
3. Check 2FA method working
4. Try web portal login
5. Contact support if locked out

### Sync Issues Between Devices

1. Sign out and back in
2. Force sync in settings
3. Check account on web portal
4. Reinstall app on affected device

---

## Still Need Help?

If these solutions don't resolve your issue:

1. **Check status page**: [status.nightowlsp.com](https://status.nightowlsp.com)
2. **Community forum**: [community.nightowlsp.com](https://community.nightowlsp.com)
3. **Email support**: support@nightowlsp.com
4. **Phone support**: 1-866-390-1303

See [Contact Support](contact.md) for more options.
