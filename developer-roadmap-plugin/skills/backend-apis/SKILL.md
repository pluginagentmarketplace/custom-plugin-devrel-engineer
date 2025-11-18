---
name: backend-apis
description: Build robust backend systems and APIs with Node.js, Python, Java, and Go. Master database design, REST APIs, authentication, and scalable architecture patterns. Use when designing APIs, building server-side logic, or optimizing database queries.
---

# Backend APIs & Server Development

Build scalable, maintainable backend systems and APIs that power modern applications.

## Quick Start

### Node.js with Express
```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());

// Routes
app.get('/api/users/:id', async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) return res.status(404).json({ error: 'Not found' });
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/users', async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.status(201).json(user);
});

app.listen(3000, () => console.log('Server running'));
```

### FastAPI (Python)
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    user = await db.users.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users")
async def create_user(user: UserSchema):
    result = await db.users.insert_one(user.dict())
    return {"id": result.inserted_id, **user.dict()}
```

### Database Design
```sql
-- User table with proper indexing
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_email (email),
  INDEX idx_created (created_at)
);

-- Query optimization with aggregation
SELECT
  category,
  COUNT(*) as total,
  AVG(price) as avg_price
FROM products
WHERE status = 'active'
GROUP BY category
ORDER BY total DESC;
```

## API Design Patterns

### REST API Best Practices
```
GET    /api/users           # List all users with pagination
GET    /api/users/{id}      # Get single user
POST   /api/users           # Create user
PUT    /api/users/{id}      # Replace user
PATCH  /api/users/{id}      # Partial update
DELETE /api/users/{id}      # Delete user

# Proper status codes
201 - Created
204 - No Content
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
409 - Conflict
500 - Internal Server Error
```

### Pagination & Filtering
```javascript
// Query parameters
GET /api/users?page=1&limit=20&sort=-created_at&status=active

// Implementation
app.get('/api/users', (req, res) => {
  const { page = 1, limit = 20, sort = '-id' } = req.query;
  const skip = (page - 1) * limit;

  User.find()
    .sort(sort)
    .skip(skip)
    .limit(parseInt(limit))
    .exec((err, users) => res.json(users));
});
```

## Authentication & Security

### JWT Implementation
```javascript
const jwt = require('jsonwebtoken');

// Generate token
const generateToken = (userId) => {
  return jwt.sign(
    { userId },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
};

// Verify middleware
const verifyToken = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (error) {
    res.status(403).json({ error: 'Invalid token' });
  }
};

app.get('/api/protected', verifyToken, (req, res) => {
  res.json({ message: 'Protected data' });
});
```

### Security Headers
```javascript
// Helmet.js for security headers
const helmet = require('helmet');
app.use(helmet());

// CORS configuration
const cors = require('cors');
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS.split(','),
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
}));

// Rate limiting
const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});
app.use('/api/', limiter);
```

## Database Optimization

### Indexing Strategy
- Indexes on frequently queried columns
- Composite indexes for multi-column queries
- Regular ANALYZE and VACUUM for PostgreSQL
- Monitor slow query logs

### Connection Pooling
```javascript
// Connection pool for multiple connections
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'mydb',
  password: 'password',
  max: 20, // Maximum connections
  idleTimeoutMillis: 30000
});

pool.query('SELECT * FROM users WHERE id = $1', [userId]);
```

## Caching Strategies

### Redis Caching
```javascript
const redis = require('redis');
const client = redis.createClient();

app.get('/api/users/:id', async (req, res) => {
  // Try cache first
  const cached = await client.get(`user:${req.params.id}`);
  if (cached) return res.json(JSON.parse(cached));

  // Fetch from DB
  const user = await User.findById(req.params.id);

  // Store in cache
  await client.setEx(`user:${req.params.id}`, 3600, JSON.stringify(user));
  res.json(user);
});
```

## Testing APIs

```javascript
const request = require('supertest');
const app = require('./app');

describe('Users API', () => {
  test('GET /api/users returns 200', async () => {
    const response = await request(app).get('/api/users');
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });

  test('POST /api/users creates user', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'test@example.com' });
    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
  });
});
```

## Interview Questions

1. How do you handle database migrations?
2. What's the N+1 query problem and how to fix it?
3. How do you implement request validation?
4. Explain pagination vs cursor-based pagination
5. How do you handle distributed transactions?

## Resources

- Express.js: https://expressjs.com
- FastAPI: https://fastapi.tiangolo.com
- REST API Best Practices: https://restfulapi.net
- API Security: https://owasp.org/www-community/attacks/
