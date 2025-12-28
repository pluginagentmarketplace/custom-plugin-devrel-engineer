# Node.js Best Practices

## Project Structure

```
src/
├── controllers/    # Route handlers
├── services/       # Business logic
├── models/         # Data models
├── middleware/     # Express middleware
├── routes/         # Route definitions
├── utils/          # Utilities
├── config/         # Configuration
└── index.js        # Entry point
```

## Error Handling

```javascript
// Centralized error handling
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
  }
}

// Async wrapper
const catchAsync = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};
```

## Security Checklist

- [ ] Use helmet for HTTP headers
- [ ] Implement rate limiting
- [ ] Validate all inputs
- [ ] Sanitize user data
- [ ] Use parameterized queries
- [ ] Store secrets in env vars
- [ ] Enable CORS properly

## Performance

| Tip | Impact |
|-----|--------|
| Use caching (Redis) | High |
| Enable gzip | Medium |
| Pool DB connections | High |
| Use streams for large data | High |

## Monitoring

```javascript
// Simple health check
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    uptime: process.uptime(),
    memory: process.memoryUsage()
  });
});
```
