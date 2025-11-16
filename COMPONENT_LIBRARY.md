# Sound Guy Productions - Component Library

XLB-inspired professional design components that work alongside Tailwind CSS.

## Color Palette

### Primary Navy (from logo: #003F87)
- `--brand-navy-500`: #003F87 (Main brand color)
- `--brand-navy-600`: #003366 (Dark navy)
- Shades available: 50-900

### Secondary Cyan (from logo: #00A8E8)
- `--brand-cyan-500`: #00A8E8 (Accent color)
- `--brand-cyan-600`: #0086ba (Dark cyan)
- Shades available: 50-900

### Cool Grays
- Professional neutrals for dark theme
- Shades available: 50-900

### Dark Mode Palette
- `--dark-bg-primary`: #1F2937 (Existing SGP background)
- `--dark-bg-secondary`: #111827
- `--dark-text-primary`: #F9FAFB

## Typography

Use fluid, responsive typography:
```html
<h1 class="text-fluid-4xl">Large Heading</h1>
<h2 class="text-fluid-3xl">Section Title</h2>
<p class="text-fluid-lg">Body text</p>
```

## Enhanced Buttons

Professional buttons with hover lift effects.

```html
<!-- Cyan enhanced button -->
<button class="btn-cyan-enhanced px-6 py-3 rounded-lg font-semibold">
    Book Now
</button>

<!-- Navy enhanced button -->
<button class="btn-navy-enhanced px-6 py-3 rounded-lg font-semibold">
    Learn More
</button>

<!-- Generic enhanced (works with Tailwind bg classes) -->
<button class="btn-enhanced bg-purple-600 text-white px-6 py-3 rounded-lg">
    Get Started
</button>
```

**Features:**
- Automatic lift on hover (`translateY(-2px)`)
- Glow shadow effects (cyan/navy)
- Smooth transitions
- Active state feedback

## Enhanced Cards

Cards with hover effects and professional shadows.

```html
<!-- Standard enhanced card -->
<div class="card-enhanced">
    <h3 class="text-xl font-semibold mb-2">Card Title</h3>
    <p>Card content with hover lift effect.</p>
</div>

<!-- Cyan accent card -->
<div class="card-enhanced card-cyan-accent">
    <h3>Cyan Accent</h3>
    <p>Left border in brand cyan color.</p>
</div>

<!-- Navy accent card -->
<div class="card-enhanced card-navy-accent">
    <h3>Navy Accent</h3>
    <p>Left border in brand navy color.</p>
</div>

<!-- Crisp shadow card -->
<div class="card-enhanced card-crisp">
    <h3>Bold Design</h3>
    <p>Offset shadow for distinctive look.</p>
</div>
```

## Gradient Text

```html
<h1 class="text-gradient-cyan font-bold">Cyan Gradient Heading</h1>
<h2 class="text-gradient-navy font-bold">Navy Gradient Heading</h2>
<h1 class="text-gradient-brand font-bold">Navy to Cyan Gradient</h1>
```

## Image Overlays

Hover effect with gradient overlay and sliding content.

```html
<div class="image-overlay">
    <img src="concert.jpg" alt="Live concert" class="w-full h-full object-cover">
    <div class="image-overlay-content text-white">
        <h3 class="font-bold text-xl">Project Name</h3>
        <p>Details revealed on hover</p>
    </div>
</div>
```

## Backdrop Blur

Modern glass effect for modals and captions.

```html
<div class="backdrop-blur bg-gray-900/80 p-6 rounded-lg">
    <p class="text-white">Content with blur effect behind</p>
</div>
```

**Variants:**
- `backdrop-blur-sm` - Subtle blur
- `backdrop-blur` - Standard blur
- `backdrop-blur-lg` - Heavy blur

## Section Backgrounds

Themed section styles for dark theme site.

```html
<!-- Navy background -->
<section class="section-navy py-20">
    <div class="container mx-auto px-6">
        <h2 class="text-white">Navy Section</h2>
    </div>
</section>

<!-- Navy gradient -->
<section class="section-navy-gradient py-20">
    <div class="container mx-auto px-6">
        <h2 class="text-white">Navy Gradient Section</h2>
    </div>
</section>

<!-- Cyan gradient -->
<section class="section-cyan-gradient py-20">
    <div class="container mx-auto px-6">
        <h2 class="text-white">Cyan Gradient Section</h2>
    </div>
</section>

<!-- Brand gradient (navy to cyan) -->
<section class="section-gradient-brand py-20">
    <div class="container mx-auto px-6">
        <h2 class="text-white">Multi-color Brand Gradient</h2>
    </div>
</section>

<!-- Darker background -->
<section class="section-darker py-20">
    <div class="container mx-auto px-6">
        <h2 class="text-white">Extra Dark Section</h2>
    </div>
</section>
```

## Animations

### Scroll Animations
```html
<div class="fade-in-up">Fades in from bottom</div>
<div class="fade-in-left">Slides in from left</div>
<div class="fade-in-right">Slides in from right</div>
<div class="scale-in">Scales up</div>
```

**Note:** Add `.visible` class via JavaScript when element enters viewport.

```javascript
// Simple scroll animation trigger
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in-up, .fade-in-left, .fade-in-right, .scale-in').forEach(el => {
    observer.observe(el);
});
```

### Staggered List Animation
```html
<ul class="stagger-animation space-y-4">
    <li class="bg-gray-700 p-4 rounded">Item 1 (animates first)</li>
    <li class="bg-gray-700 p-4 rounded">Item 2 (animates second)</li>
    <li class="bg-gray-700 p-4 rounded">Item 3 (animates third)</li>
</ul>
```

### Hover Scale
```html
<img src="photo.jpg" class="hover-scale rounded-lg">
<button class="hover-scale-sm bg-cyan-500 px-4 py-2">Subtle scale</button>
<div class="hover-scale-lg p-6">Big scale effect</div>
```

## Shadow System

```html
<!-- Professional shadow utilities -->
<div class="shadow-soft">Subtle professional shadow</div>
<div class="shadow-bold">Bold prominent shadow</div>
<div class="shadow-crisp">Offset cyan shadow</div>
<div class="shadow-deep">Deep dimensional shadow</div>
<div class="shadow-glow-cyan">Cyan glow effect</div>
<div class="shadow-glow-navy">Navy glow effect</div>
```

## Tailwind Integration

Custom brand color utilities that integrate with Tailwind:

```html
<!-- Background colors -->
<div class="bg-brand-navy">Navy background</div>
<div class="bg-brand-cyan">Cyan background</div>

<!-- Text colors -->
<p class="text-brand-navy">Navy text</p>
<p class="text-brand-cyan">Cyan text</p>

<!-- Border colors -->
<div class="border-2 border-brand-navy">Navy border</div>
<div class="border-2 border-brand-cyan">Cyan border</div>
```

## Usage Examples

### Enhanced CTA Button
```html
<button class="btn-cyan-enhanced px-8 py-4 rounded-full text-lg font-bold shadow-glow-cyan">
    Get Your Free Quote
</button>
```

### Feature Card with Hover Effect
```html
<div class="card-enhanced card-cyan-accent fade-in-up">
    <div class="flex items-center mb-4">
        <svg class="w-12 h-12 text-brand-cyan mr-4">...</svg>
        <h3 class="text-gradient-cyan text-2xl font-bold">Professional Sound</h3>
    </div>
    <p class="text-gray-300">Crystal-clear audio engineering for every performance.</p>
</div>
```

### Gradient Hero Heading
```html
<h1 class="text-gradient-brand text-fluid-6xl font-bebas tracking-wider">
    SOUNDGUY PRODUCTIONS
</h1>
```

### Image Gallery with Hover
```html
<div class="grid grid-cols-3 gap-4">
    <div class="image-overlay hover-scale-sm">
        <img src="event1.jpg" alt="Event">
        <div class="image-overlay-content">
            <h3>Summer Festival 2024</h3>
            <p>10,000+ attendees</p>
        </div>
    </div>
    <!-- More images... -->
</div>
```

## CSS Variables Reference

All CSS variables are available for custom styling:

```css
/* Use brand colors */
.custom-element {
    background: var(--brand-navy-500);
    color: var(--brand-cyan-500);
    box-shadow: var(--shadow-glow-cyan);
    border-radius: var(--radius-xl);
    transition: var(--transition-base);
}

/* Fluid typography */
.custom-text {
    font-size: var(--text-fluid-3xl);
}
```

## Usage Notes

- **Tailwind Compatible**: All classes work alongside Tailwind utilities
- **Dark Theme Optimized**: Colors and shadows designed for dark backgrounds
- **Performance**: GPU-accelerated transforms, optimized animations
- **Accessibility**: Focus states, reduced motion support, semantic HTML
- **Mobile-First**: Responsive design with fluid typography
- **Individual Editing**: Each site can override variables without affecting others

Copy and adapt these components to your specific pages while maintaining consistency across the Sound Guy Productions site.
