#!/usr/bin/env node

// Email summary script using Resend API
// Usage: node send-summary-email.js

const https = require('https');

// You'll need to set your RESEND_API_KEY environment variable
const RESEND_API_KEY = process.env.RESEND_API_KEY;

if (!RESEND_API_KEY) {
  console.error('Error: RESEND_API_KEY environment variable not set');
  console.error('Set it with: export RESEND_API_KEY=your_api_key_here');
  process.exit(1);
}

const emailData = JSON.stringify({
  from: 'sam@updates.edw4rds.com',
  to: ['rich@prosoundguy.com'],
  subject: 'SGP Website Updates - Comprehensive Summary for October 19, 2025',
  html: `<p>Hi Rich,</p>

<p>Here's a comprehensive summary of all the updates made to the Soundguy Productions website today:</p>

<h2>Major SEO Enhancements</h2>

<h3>Meta Tags & Search Optimization (All Pages)</h3>
<ul>
<li>Added comprehensive meta tags with location-specific keywords (Portland, Seattle, Pacific Northwest)</li>
<li>Implemented SEO-optimized title tags and descriptions for better search rankings</li>
<li>Added canonical URLs to prevent duplicate content issues</li>
<li>Included keyword meta tags for regional targeting</li>
</ul>

<h3>Social Media Optimization</h3>
<ul>
<li>Added Open Graph tags for Facebook/LinkedIn sharing previews</li>
<li>Implemented Twitter Card metadata</li>
<li>Configured social sharing images (sgp-logo.png)</li>
</ul>

<h3>Geographic Targeting</h3>
<ul>
<li>Added geo tags for Oregon (US-OR) and Washington (US-WA)</li>
<li>Included geo placenames for Portland and Seattle</li>
<li>Added GPS coordinates for Portland location (45.5152, -122.6784)</li>
</ul>

<h3>Structured Data (Schema.org)</h3>
<ul>
<li>Implemented LocalBusiness schema on homepage</li>
<li>Added complete business information:
  <ul>
  <li>Address: PO Box 642, Gresham, OR 97030</li>
  <li>Phone: (503) 998-5420</li>
  <li>Email: rich@prosoundguy.com</li>
  <li>Service areas: Portland, Seattle, Gresham, Salem, Beaverton, Lake Oswego, Oregon, Washington</li>
  <li>Business hours: 9 AM - 9 PM, 7 days/week</li>
  <li>Founded: 2004</li>
  <li>Price range: $$</li>
  </ul>
</li>
</ul>

<h3>Analytics Migration & Event Tracking</h3>
<ul>
<li>Migrated from self-hosted Plausible to official Plausible.io service</li>
<li>Implemented comprehensive event tracking:
  <ul>
  <li>Phone number clicks (tracks which page and number)</li>
  <li>Email clicks</li>
  <li>"Request Quote" button clicks (tracks location on page)</li>
  <li>Form submissions (tracks event type, guest count, priority score)</li>
  <li>"View Services" link clicks</li>
  </ul>
</li>
</ul>

<h3>New SEO Files</h3>
<ul>
<li>Added robots.txt for search engine crawling guidance</li>
<li>Created sitemap.xml for better indexing</li>
<li>Added photo-gallery.html page</li>
</ul>

<hr>

<h2>Regional Branding Updates</h2>

<h3>Unified Pacific Northwest Messaging</h3>
<ul>
<li>Homepage (index.html):
  <ul>
  <li>Hero: "Professional Sound Production for Pacific Northwest Events"</li>
  <li>Solution section: "...your Pacific Northwest event"</li>
  </ul>
</li>
<li>About page (about.html):
  <ul>
  <li>Hero: "MAKING PACIFIC NORTHWEST EVENTS SOUND AMAZING SINCE 2004"</li>
  </ul>
</li>
<li>Footer (index.html):
  <ul>
  <li>Service Area section now lists "The Pacific Northwest" followed by specific cities</li>
  </ul>
</li>
</ul>

<p>All references to "Portland Metro" have been updated to "Pacific Northwest" for broader regional appeal while maintaining Portland/Seattle city-specific SEO in meta tags.</p>

<hr>

<h2>Image Updates</h2>

<h3>Replaced Placeholder Images</h3>
<ul>
<li>Homepage "Engineer at Work" → sound-engineer.jpg</li>
<li>About page "Rich at Console" → on-stage-musician.jpg</li>
</ul>

<h3>Updated Service Page Images</h3>
<ul>
<li>Fixed image paths (cozy-venue-final.jpg, full-production.jpg, festival-stage.jpg)</li>
<li>Replaced cozy-venue-final.jpg with updated version</li>
<li>Replaced full-production.jpg with updated version</li>
<li>Updated festival-stage.jpg with new version</li>
</ul>

<h3>New Images Added</h3>
<ul>
<li>sound-engineer.jpg (homepage Solution Overview section)</li>
<li>cozy-venue-final8.jpg (available for future use)</li>
</ul>

<hr>

<h2>Content & Structure Improvements</h2>

<h3>Homepage (index.html)</h3>
<ul>
<li>Moved "Scaled to Your Needs" as a purple subheadline under "PROFESSIONAL SOUND, WITHOUT THE DRAMA"</li>
<li>Changed Services section heading from "SCALED TO YOUR NEEDS" to "OUR SERVICES"</li>
<li>Added introductory paragraph to Our Services section: "From intimate coffee houses to major outdoor festivals, we provide the right sound solution for your event. Choose the package that fits your needs, or contact us for a custom quote."</li>
</ul>

<h3>Footer Improvements</h3>
<ul>
<li>Service Area section now has clearer hierarchy with "The Pacific Northwest" as primary descriptor</li>
</ul>

<hr>

<h2>Bug Fixes</h2>

<h3>Services Page (services.html)</h3>
<ul>
<li>Fixed Quick Links footer section alignment by adding missing div wrapper</li>
</ul>

<hr>

<h2>Technical Summary</h2>

<ul>
<li><strong>Total Files Changed:</strong> 1,206+ files (including all preview images and supporting files)</li>
<li><strong>Total Commits:</strong> 16 commits</li>
<li><strong>Pages Updated:</strong> index.html, about.html, services.html, contact.html</li>
<li><strong>New Files Added:</strong> robots.txt, sitemap.xml, photo-gallery.html, multiple images</li>
</ul>

<hr>

<h2>Impact & Benefits</h2>

<h3>SEO Improvements:</h3>
<ul>
<li>Better search engine visibility for Portland, Seattle, and Pacific Northwest searches</li>
<li>Enhanced local search rankings with structured data</li>
<li>Improved social media sharing appearance</li>
<li>Better tracking of user engagement and conversion actions</li>
</ul>

<h3>Brand Consistency:</h3>
<ul>
<li>Unified Pacific Northwest messaging across all pages</li>
<li>Professional imagery replacing all placeholders</li>
<li>Clearer service offerings and calls-to-action</li>
</ul>

<h3>User Experience:</h3>
<ul>
<li>More informative service descriptions</li>
<li>Better visual presentation with real photos</li>
<li>Improved footer navigation and organization</li>
<li>Enhanced analytics to understand visitor behavior</li>
</ul>

<p>All changes have been committed and pushed to the GitHub repository and should be live on the website.</p>

<p>Let me know if you have any questions or need any adjustments!</p>

<p>Best,<br>Sam</p>
  `
});

const options = {
  hostname: 'api.resend.com',
  port: 443,
  path: '/emails',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${RESEND_API_KEY}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(emailData)
  }
};

console.log('Sending email to rich@prosoundguy.com...');

const req = https.request(options, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    if (res.statusCode === 200) {
      console.log('✓ Email sent successfully!');
      console.log('Response:', JSON.parse(data));
    } else {
      console.error('✗ Failed to send email');
      console.error('Status:', res.statusCode);
      console.error('Response:', data);
    }
  });
});

req.on('error', (error) => {
  console.error('✗ Error sending email:', error.message);
});

req.write(emailData);
req.end();
