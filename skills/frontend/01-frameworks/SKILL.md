---
name: frontend-frameworks
description: Master modern frontend frameworks including React, Vue.js, Angular, Next.js. Learn component architecture, state management, routing, and framework-specific best practices for building scalable web applications.
---

# Frontend Frameworks

Learn to build modern, scalable web applications with the most popular JavaScript frameworks.

## React.js
```javascript
// Hooks
import { useState, useEffect } from 'react';

function Component() {
  const [state, setState] = useState(0);
  useEffect(() => { /* effect */ }, []);
  return <div>{state}</div>;
}

// Context API
const ThemeContext = React.createContext();
```

## Vue.js
```javascript
// Composition API
import { ref, reactive } from 'vue';

export default {
  setup() {
    const count = ref(0);
    const state = reactive({ name: 'Vue' });
    return { count, state };
  }
};
```

## Angular
```typescript
// Components & Dependency Injection
import { Component, Injectable } from '@angular/core';

@Component({
  selector: 'app-root',
  template: '<div>{{ message }}</div>'
})
export class AppComponent {
  constructor(private service: MyService) {}
}
```

## Next.js
```javascript
// Server Components & API Routes
export default function Page() {
  return <h1>Next.js Page</h1>;
}

// API Route
export async function POST(req) {
  const data = await req.json();
  return Response.json({ success: true });
}
```

## Key Concepts

✅ Component composition
✅ Props & state management
✅ Lifecycle hooks
✅ Event handling
✅ Conditional rendering
✅ Lists & keys
✅ Forms
✅ Routing

## When to Choose Each

**React**: Largest ecosystem, most jobs, flexible
**Vue**: Gentle learning curve, great docs
**Angular**: Enterprise, full framework, TypeScript
**Next.js**: SSR/SSG, full-stack, modern React

## Resources

- react.dev - Official React docs
- vuejs.org - Vue documentation
- angular.io - Angular docs
- nextjs.org - Next.js guides
