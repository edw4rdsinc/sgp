# Pre-Launch Checklist for Soundguy Productions Website

## ✅ COMPLETED

### SEO Optimization
- [x] Meta descriptions with Portland/Seattle geo-targeting
- [x] Enhanced title tags with location keywords
- [x] LocalBusiness structured data (JSON-LD)
- [x] Open Graph and Twitter Card tags
- [x] Canonical URLs on all pages
- [x] Geo-location meta tags
- [x] robots.txt created
- [x] sitemap.xml created

### Analytics Setup
- [x] Plausible Cloud script installed (all 4 pages)
- [x] Phone click tracking implemented
- [x] Form submission tracking added
- [x] Request Quote button tracking
- [x] Service package interest tracking
- [x] Email click tracking

### Bug Fixes
- [x] Fixed all 7 broken links in services.html

---

## ⚠️ CRITICAL - MUST DO BEFORE LAUNCH

### 1. Update Production API Endpoint
**File:** `contact.html` (line 437)

**Current (Dev):**
```javascript
const response = await fetch('http://5.78.156.118:5003/api/lead', {
```

**Change to:**
```javascript
const response = await fetch('https://api.prosoundguy.com/lead', {
// OR your actual production API URL
```

### 2. Replace Placeholder Images
**3 placeholders need real images:**

1. **about.html (line 86)** - Hero background
   - Current: `https://placehold.co/1920x1080/1F2937/4B5563?text=Concert+Collage`
   - Need: Concert/festival collage image (1920x1080)

2. **about.html (line 151)** - Founder photo
   - Current: `https://placehold.co/600x400/7B3FF2/FFFFFF?text=Rich+at+Console`
   - Need: Photo of Rich at mixing console (600x400)

3. **index.html (line 319)** - Solution section image
   - Current: `https://placehold.co/600x400/7B3FF2/FFFFFF?text=Engineer+at+Work`
   - Need: Sound engineer at work photo (600x400)

### 3. SSL Certificate Setup
**MUST have HTTPS before launch!**

See SSL configuration instructions below.

---

## 📱 MOBILE TESTING CHECKLIST

### Test on Real Devices
Test the following on actual mobile devices (iOS & Android):

#### Homepage (index.html)
- [ ] Video background plays on mobile (or shows fallback)
- [ ] Particle effects don't lag on slower devices
- [ ] Navigation menu hamburger works
- [ ] All text is readable (not too small)
- [ ] "Request Quote" buttons are easily tappable
- [ ] Phone number links trigger phone dialer
- [ ] Stats counter animates smoothly
- [ ] Logo strip scrolls without jank

#### Services Page (services.html)
- [ ] Service cards stack properly on mobile
- [ ] Images load and display correctly
- [ ] FAQ accordions expand/collapse smoothly
- [ ] All buttons are tappable (min 44px touch target)

#### About Page (about.html)
- [ ] Text is readable in 2-column layout
- [ ] Images don't overflow on small screens
- [ ] Testimonial cards display properly

#### Contact Page (contact.html)
- [ ] Form fields are easy to fill on mobile
- [ ] Phone number auto-formatting works
- [ ] Date picker opens correctly
- [ ] Dropdown selects work properly
- [ ] Submit button is easily tappable
- [ ] Success/error messages display correctly

#### Cross-Device Tests
- [ ] Test on iPhone (Safari)
- [ ] Test on Android (Chrome)
- [ ] Test in landscape orientation
- [ ] Test on tablet (iPad)
- [ ] Check in Chrome DevTools mobile emulator

### Performance Checks
- [ ] Page load time < 3 seconds on 4G
- [ ] Images are optimized (WebP format)
- [ ] No console errors in mobile browser
- [ ] Animations don't cause lag

### Mobile-Specific Issues to Check
- [ ] Text isn't cut off at edges
- [ ] Buttons don't overlap
- [ ] Footer displays correctly
- [ ] Email links work (`mailto:`)
- [ ] Phone links work (`tel:`)
- [ ] No horizontal scrolling

---

## 🔒 SSL/HTTPS CONFIGURATION

### Why SSL is Critical
- **SEO**: Google penalizes non-HTTPS sites
- **Security**: Form data needs encryption
- **Trust**: Browsers show "Not Secure" without SSL
- **Requirements**: Your meta tags reference HTTPS URLs

### How to Get SSL Certificate

#### Option 1: Free SSL with Let's Encrypt (Recommended)
If hosting on:
- **VPS/Dedicated Server**: Use Certbot
- **Shared Hosting**: Check cPanel for "SSL/TLS" or "Let's Encrypt"

**Steps for most hosting:**
1. Log into hosting control panel
2. Find "SSL/TLS" or "Let's Encrypt" section
3. Select domain: `prosoundguy.com`
4. Click "Install Certificate"
5. Wait 5-10 minutes for activation

#### Option 2: Hosting Provider SSL
Many hosts include free SSL:
- **Netlify**: Auto SSL (just enable in settings)
- **Vercel**: Auto SSL (enabled by default)
- **Cloudflare**: Free SSL + CDN
- **GitHub Pages**: Free SSL (custom domains)

#### Option 3: Purchase SSL Certificate
- Namecheap: $8/year
- SSLs.com: $5/year
- Your domain registrar

### After Installing SSL

**1. Force HTTPS redirect** (add to `.htaccess` if Apache):
```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

**2. Update these files if domain differs:**
- sitemap.xml (line 13, 20, 27, 34)
- All HTML files with canonical URLs
- Structured data in index.html

**3. Test SSL:**
- Visit: https://www.ssllabs.com/ssltest/
- Enter: prosoundguy.com
- Aim for: A or A+ rating

---

## 🚀 DEPLOYMENT CHECKLIST

### Before Upload
- [ ] All placeholder images replaced
- [ ] Production API endpoint updated
- [ ] SSL certificate obtained
- [ ] Backup created of current site (if replacing)

### During Upload
- [ ] Upload all HTML files to server
- [ ] Upload images folder
- [ ] Upload robots.txt to root
- [ ] Upload sitemap.xml to root
- [ ] Set correct file permissions (644 for files, 755 for folders)

### After Upload
- [ ] Visit site in incognito/private window
- [ ] Check all 4 pages load correctly
- [ ] Test contact form submission
- [ ] Click phone number (should dial)
- [ ] Click email link (should open mail app)
- [ ] Verify SSL certificate (green padlock in browser)
- [ ] Check Plausible dashboard (see pageviews)

### DNS Configuration
- [ ] Domain points to hosting server IP
- [ ] WWW and non-WWW both work
- [ ] DNS propagation complete (check: whatsmydns.net)

### Final Validation
- [ ] Google PageSpeed Insights (aim for 80+)
- [ ] Mobile-Friendly Test: search.google.com/test/mobile-friendly
- [ ] Structured Data Test: search.google.com/test/rich-results
- [ ] SSL Test: ssllabs.com/ssltest

---

## 📊 POST-LAUNCH MONITORING

### Week 1
- [ ] Check Plausible analytics daily
- [ ] Monitor phone call events
- [ ] Check form submissions
- [ ] Review any error reports

### Submit to Search Engines
- [ ] Google Search Console (submit sitemap.xml)
- [ ] Bing Webmaster Tools
- [ ] Update Google Business Profile with new website

### Track These Metrics
- Phone call clicks
- Form submissions
- Quote requests
- Service package interest
- Page bounce rates
- Traffic sources

---

## 📝 OPTIONAL (CAN DO AFTER LAUNCH)

### Additional Pages
- [ ] Create Privacy Policy page
- [ ] Create Terms of Service page
- [ ] Create custom 404 error page
- [ ] Create Thank You page (post-form submission)

### Performance Optimization
- [ ] Compress images further
- [ ] Add lazy loading to images
- [ ] Host video on CDN or YouTube
- [ ] Minify HTML/CSS/JS

### Marketing
- [ ] Set up Google Business Profile
- [ ] Create Facebook Business Page
- [ ] List in local directories
- [ ] Set up email signatures with website link

---

## 🆘 TROUBLESHOOTING

### Contact Form Not Working
- Check API endpoint URL
- Verify API server is running
- Check browser console for errors
- Test with browser dev tools network tab

### Analytics Not Tracking
- Check browser console for errors
- Disable ad blockers for testing
- Verify Plausible domain matches exactly
- Check Plausible dashboard settings

### Mobile Layout Broken
- Check viewport meta tag present
- Test with actual devices, not just emulator
- Clear browser cache
- Check for missing CSS files

### SSL Certificate Issues
- Wait 24 hours for DNS propagation
- Clear browser cache
- Check certificate installation
- Contact hosting support

---

## 📞 WHO TO CONTACT FOR HELP

### Technical Issues
- **Hosting Support**: Your hosting provider
- **Domain Issues**: Your domain registrar
- **API/Form Issues**: Your API developer

### Content Updates
- **Photos**: Need original images from client
- **Copy Changes**: Get approval before changing text

---

**Last Updated:** Ready for launch pending 3 critical items above
