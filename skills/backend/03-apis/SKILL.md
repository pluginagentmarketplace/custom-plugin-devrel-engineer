---
name: backend-apis
description: Master API design and development. Learn REST, GraphQL, authentication, rate limiting, versioning, and building scalable APIs.
---

# API Design & Development

## REST API Design
```javascript
// Proper HTTP methods & paths
GET    /api/users           // List
POST   /api/users           // Create
GET    /api/users/:id       // Get
PUT    /api/users/:id       // Replace
PATCH  /api/users/:id       // Update
DELETE /api/users/:id       // Delete

// Status codes
200 OK
201 Created
400 Bad Request
401 Unauthorized
404 Not Found
500 Internal Server Error
```

## GraphQL
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Query {
  user(id: ID!): User
  users: [User!]!
}

type Mutation {
  createUser(name: String!, email: String!): User!
}
```

## Authentication & Security
```javascript
// JWT
const token = jwt.sign(
  { userId: user.id },
  SECRET,
  { expiresIn: '24h' }
);

// OAuth 2.0
// Passport.js integration
app.post('/login', passport.authenticate('local'));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});
```

## Error Handling
```javascript
// Consistent error responses
{
  error: {
    code: 'VALIDATION_ERROR',
    message: 'Invalid request',
    details: { field: 'email', reason: 'required' }
  }
}
```

## Pagination & Filtering
```
GET /api/users?page=1&limit=20&sort=-created_at&status=active

Response:
{
  data: [...],
  pagination: {
    page: 1,
    limit: 20,
    total: 150,
    pages: 8
  }
}
```

## Best Practices

✅ Consistent URL structure
✅ Proper HTTP methods
✅ Meaningful status codes
✅ Clear error messages
✅ API versioning
✅ Authentication & authorization
✅ Rate limiting
✅ Caching strategies
✅ Documentation (OpenAPI/Swagger)

## API Documentation

- **Swagger/OpenAPI**: Standard API docs
- **GraphQL Schema**: Self-documenting
- **Postman**: Collection sharing
- **API Blueprint**: Markdown-based
