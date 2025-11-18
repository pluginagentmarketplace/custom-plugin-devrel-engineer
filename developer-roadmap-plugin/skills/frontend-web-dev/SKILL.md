---
name: frontend-web-dev
description: Master modern frontend development with React, Vue, Angular, and vanilla JavaScript. Learn responsive design, performance optimization, and building accessible user interfaces. Use when working on UI components, styling, or web application development.
---

# Frontend Web Development

Master modern web development tools and techniques for building responsive, performant user interfaces.

## Quick Start

### JavaScript ES6+
```javascript
// Arrow functions and destructuring
const greet = ({ name, greeting = 'Hello' }) => `${greeting}, ${name}!`;

// Async/await for API calls
const fetchUser = async (id) => {
  const response = await fetch(`/api/users/${id}`);
  const data = await response.json();
  return data;
};

// Promises and error handling
Promise.all([fetch1, fetch2])
  .then(([data1, data2]) => ({ data1, data2 }))
  .catch(err => console.error('Error:', err));
```

### React Hooks
```javascript
import { useState, useEffect, useCallback } from 'react';

function UserComponent() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetchUser(1)
      .then(setUser)
      .finally(() => setLoading(false));
  }, []);

  const handleUpdate = useCallback((newData) => {
    setUser(prev => ({ ...prev, ...newData }));
  }, []);

  return (
    <div>
      {loading ? <p>Loading...</p> : <UserCard user={user} onUpdate={handleUpdate} />}
    </div>
  );
}
```

### CSS Grid & Flexbox
```css
/* Responsive grid layout */
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  padding: 1rem;
}

/* Flexbox for navigation */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

/* Mobile-first responsive */
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}
```

## Core Concepts

### State Management
- **Local State** - useState, useReducer for component state
- **Context API** - Global state without external libraries
- **Redux/Zustand** - Predictable state containers
- **React Query** - Server state management, caching

### Performance Optimization
- **Code Splitting** - Lazy loading with React.lazy() and Suspense
- **Memoization** - React.memo, useMemo, useCallback
- **Virtual Scrolling** - Rendering large lists efficiently
- **Image Optimization** - Lazy loading, responsive images, WebP

### Accessibility
- **Semantic HTML** - Proper use of heading, nav, main, section tags
- **ARIA Attributes** - aria-label, aria-describedby for screen readers
- **Keyboard Navigation** - Tab order, focus management
- **Color Contrast** - WCAG standards for readability

### Testing
```javascript
import { render, screen, fireEvent } from '@testing-library/react';

test('button click triggers callback', () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click me</Button>);
  fireEvent.click(screen.getByText('Click me'));
  expect(handleClick).toHaveBeenCalled();
});
```

## Framework Comparisons

### React
- **Pros**: Large ecosystem, job market, JSX learning curve
- **Best for**: Complex UIs, large teams, scalable apps
- **Learning**: JSX, hooks, virtual DOM concept

### Vue.js
- **Pros**: Gentle learning curve, great documentation, template syntax
- **Best for**: Rapid prototyping, startups, single-page apps
- **Learning**: Composition API, template syntax

### Angular
- **Pros**: Full framework, TypeScript, enterprise support
- **Best for**: Enterprise applications, large teams
- **Learning**: Decorators, RxJS, dependency injection

## Best Practices

1. **Component Design**
   - Single responsibility principle
   - Props validation with TypeScript
   - Reusable, composable components

2. **Performance**
   - Lazy load routes and components
   - Optimize bundle size
   - Use production builds

3. **Accessibility**
   - Use semantic HTML
   - Test with screen readers
   - Keyboard navigation support

4. **Security**
   - Sanitize user input
   - Use HTTPS
   - Content Security Policy (CSP)

## Common Interview Questions

1. What's the difference between `useEffect` and `useLayoutEffect`?
2. How do you optimize React performance?
3. What are controlled vs uncontrolled components?
4. Explain the virtual DOM and why it matters
5. How would you implement infinite scroll?

## Resources

- React Documentation: https://react.dev
- Vue.js Guide: https://vuejs.org/guide/
- MDN Web Docs: https://developer.mozilla.org/
- Web.dev Performance Guide: https://web.dev/performance/
