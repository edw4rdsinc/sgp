#!/usr/bin/env node

// Email summary script for Vero Autoglass using Resend API
// Usage: node send-vero-email.js

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
  to: ['Devin@veroautoglass.com', 'jesse@veroautoglass.com'],
  subject: 'Vero Autoglass Website - SEO Optimization & Analytics Update Complete',
  html: `<p>Hi Devin and Jesse,</p>

<p>I've completed a comprehensive SEO optimization of the Vero Autoglass website along with updating your analytics tracking. All changes have been committed and pushed to your GitHub repository (commit e4e9a1e).</p>

<h2>Summary of Changes</h2>

<h3>1. Critical SEO Files Created</h3>

<p><strong>robots.txt</strong></p>
<ul>
<li>Guides search engine crawlers on how to index your site</li>
<li>Points to your sitemap for efficient crawling</li>
<li>Location: <a href="https://veroautoglass.com/robots.txt">https://veroautoglass.com/robots.txt</a></li>
</ul>

<p><strong>sitemap.xml</strong></p>
<ul>
<li>Complete site map with all 8 pages</li>
<li>Includes priorities and update frequencies for each page</li>
<li>Location: <a href="https://veroautoglass.com/sitemap.xml">https://veroautoglass.com/sitemap.xml</a></li>
<li><strong>Action Required:</strong> Submit this sitemap to Google Search Console</li>
</ul>

<h3>2. Meta Tags Added to All Pages</h3>

<p>Updated all 8 HTML pages (index, services, about, contact, insurance, warranty, privacy, terms) with:</p>

<p><strong>Canonical URLs</strong></p>
<ul>
<li>Prevents duplicate content issues with search engines</li>
<li>Ensures proper page indexing</li>
</ul>

<p><strong>Open Graph Tags</strong></p>
<ul>
<li>Enables rich previews when pages are shared on Facebook, LinkedIn, and other social media</li>
<li>Includes title, description, image, and URL for each page</li>
<li>Your shares will now display professional previews with your logo</li>
</ul>

<p><strong>Meta Descriptions</strong></p>
<ul>
<li>Added missing descriptions to privacy.html and terms.html</li>
<li>All pages now have unique, SEO-optimized descriptions</li>
</ul>

<h3>3. Structured Data (Schema.org) Markup</h3>

<p>This is the most impactful change - it enables "rich snippets" in Google search results:</p>

<p><strong>FAQ Schema (Homepage)</strong></p>
<ul>
<li>Marks up your 3 FAQ questions</li>
<li>Can display FAQ dropdowns directly in Google search results</li>
<li>Increases visibility and click-through rates</li>
</ul>

<p><strong>Service Schema (Services Page)</strong></p>
<p>Details all 8 services you offer:</p>
<ul>
<li>Windshield Replacement</li>
<li>Windshield Repair</li>
<li>Side & Back Glass</li>
<li>ADAS Calibration</li>
<li>Regulator Replacement</li>
<li>Hydrophobic Treatment</li>
<li>Anti-Damage Treatment</li>
<li>Wiper Replacement</li>
</ul>
<p>Helps Google understand and display your service offerings</p>

<p><strong>Breadcrumb Schema (5 Pages)</strong></p>
<ul>
<li>Added to services, about, contact, insurance, and warranty pages</li>
<li>Displays navigation breadcrumbs in search results</li>
<li>Improves user experience and SEO</li>
</ul>

<h3>4. Analytics Update</h3>

<p><strong>Updated Plausible Analytics Script</strong></p>
<ul>
<li>Replaced old self-hosted script with new Plausible.io script</li>
<li>Applied consistently across all 8 pages</li>
<li>Privacy-friendly analytics now active</li>
</ul>

<hr>

<h2>Expected SEO Impact</h2>

<p><strong>Immediate Benefits:</strong></p>
<ul>
<li>Search engines can now efficiently discover and index all pages</li>
<li>Social media shares will show professional previews</li>
<li>No duplicate content issues</li>
<li>Better organized site structure</li>
</ul>

<p><strong>Within 2-4 Weeks:</strong></p>
<ul>
<li>Potential for FAQ rich snippets in Google search results (star ratings, expandable FAQs)</li>
<li>Breadcrumb trails appearing in search results</li>
<li>Improved local search visibility</li>
<li>Better click-through rates from search results</li>
</ul>

<p><strong>Long-term:</strong></p>
<ul>
<li>Enhanced search engine rankings for local auto glass searches</li>
<li>Increased organic traffic</li>
<li>Better conversion rates from improved search appearance</li>
</ul>

<hr>

<h2>Recommended Next Steps</h2>

<ol>
<li><strong>Google Search Console (High Priority)</strong>
  <ul>
  <li>Verify domain ownership if not already done</li>
  <li>Submit the sitemap: https://veroautoglass.com/sitemap.xml</li>
  <li>Monitor indexing status and search performance</li>
  </ul>
</li>

<li><strong>Test Social Sharing (Quick Win)</strong>
  <ul>
  <li>Share a page on Facebook or LinkedIn to see the new previews</li>
  <li>Should display your logo, title, and description</li>
  </ul>
</li>

<li><strong>Monitor Rich Snippets (2-4 weeks)</strong>
  <ul>
  <li>Search for "vero autoglass" in Google</li>
  <li>Watch for FAQ expansions and enhanced listings</li>
  <li>Rich snippets typically appear within 2-4 weeks of indexing</li>
  </ul>
</li>

<li><strong>Analytics Verification</strong>
  <ul>
  <li>Confirm Plausible.io is receiving data</li>
  <li>Check that all pages are tracking properly</li>
  </ul>
</li>
</ol>

<hr>

<h2>Technical Details</h2>

<ul>
<li><strong>Files Changed:</strong> 10 files (8 HTML pages + 2 new files)</li>
<li><strong>Lines Added:</strong> 447 lines of SEO code</li>
<li><strong>Commit Hash:</strong> e4e9a1e</li>
<li><strong>Branch:</strong> main (live)</li>
<li><strong>Repository:</strong> https://github.com/edw4rdsinc/vero.git</li>
</ul>

<hr>

<h2>Questions?</h2>

<p>All changes follow current SEO best practices and are fully compliant with Google's guidelines. The site maintains its existing design and functionality - all changes are "under the hood" to improve search visibility.</p>

<p>Let me know if you have any questions or would like me to walk through any of these changes in more detail.</p>

<p>Best regards,<br>
Sam</p>
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

console.log('Sending email to Devin@veroautoglass.com and jesse@veroautoglass.com...');

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
