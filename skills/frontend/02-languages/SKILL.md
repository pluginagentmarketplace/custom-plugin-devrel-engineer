---
name: frontend-languages
description: Master JavaScript and TypeScript for frontend development. Learn ES6+ features, async programming, DOM APIs, and type-safe JavaScript development.
---

# JavaScript & TypeScript Essentials

## JavaScript ES6+

```javascript
// Arrow functions & destructuring
const greet = ({ name, age = 18 }) => `${name} is ${age}`;

// Template literals
const message = `Hello, ${name}!`;

// Spread operator
const merged = { ...obj1, ...obj2 };
const arr = [...array1, ...array2];

// Async/await
async function fetchData() {
  try {
    const data = await fetch(url).then(r => r.json());
    return data;
  } catch (error) {
    console.error(error);
  }
}

// Promise chains
Promise.all([fetch1, fetch2])
  .then(([data1, data2]) => process(data1, data2))
  .catch(err => handleError(err));

// Map, filter, reduce
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((a, b) => a + b, 0);
```

## TypeScript

```typescript
// Types & interfaces
interface User {
  id: number;
  name: string;
  email?: string;
}

// Generics
function identity<T>(value: T): T { return value; }

// Union & intersection
type Status = 'success' | 'error' | 'pending';
type AdminUser = User & { role: 'admin' };

// Enums
enum Color { Red, Green, Blue }

// Decorators
@Component
class MyComponent {}
```

## DOM APIs

```javascript
// DOM selection & manipulation
const element = document.querySelector('.class');
element.textContent = 'Hello';
element.classList.add('active');
element.addEventListener('click', handler);

// Event delegation
document.addEventListener('click', (e) => {
  if (e.target.matches('.button')) {
    handleClick(e);
  }
});

// Local Storage
localStorage.setItem('key', JSON.stringify(data));
const saved = JSON.parse(localStorage.getItem('key'));
```

## Key Concepts

✅ Closures & scope
✅ Prototypes & inheritance
✅ Event loop & microtasks
✅ Promises & async/await
✅ Module systems (ESM, CommonJS)
✅ Type systems (TypeScript)
✅ Functional vs object-oriented

## Best Practices

- Use `const` by default
- Leverage async/await over callbacks
- Use TypeScript for type safety
- Understand event delegation
- Optimize bundle size
- Use modern ES6+ features

## Resources

- MDN Web Docs
- JavaScript.info
- TypeScript Handbook
- ECMAScript standard docs
