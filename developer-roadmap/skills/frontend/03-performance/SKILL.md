---
name: frontend-performance
description: Optimize frontend performance with techniques for code splitting, lazy loading, caching, image optimization, and Core Web Vitals. Learn profiling and performance budgeting.
---

# Frontend Performance Optimization

## Code Splitting & Lazy Loading
```javascript
// Dynamic imports
const module = await import('./heavy-module.js');

// React lazy
const Component = React.lazy(() => import('./Component'));

// Webpack code splitting
// webpack.config.js - splitChunks configuration
```

## Image Optimization
```html
<!-- Responsive images -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="description">
</picture>

<!-- Lazy loading -->
<img src="image.jpg" loading="lazy" alt="description">
```

## Caching Strategies
```javascript
// Service Worker caching
const cacheName = 'v1';
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

## Monitoring & Profiling
- Lighthouse audits
- Chrome DevTools performance tab
- Web Vitals (LCP, FID, CLS)
- Bundlesize tracking
- Real User Monitoring

## Key Metrics

✅ First Contentful Paint (FCP)
✅ Largest Contentful Paint (LCP)
✅ First Input Delay (FID)
✅ Cumulative Layout Shift (CLS)
✅ Time to Interactive (TTI)

## Best Practices

- Minimize main thread work
- Optimize critical rendering path
- Use efficient data structures
- Debounce/throttle events
- Optimize algorithms
- Use virtual scrolling for large lists
