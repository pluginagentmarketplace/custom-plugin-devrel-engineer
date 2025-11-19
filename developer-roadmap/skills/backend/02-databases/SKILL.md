---
name: backend-databases
description: Master database technologies including SQL, PostgreSQL, MongoDB, Redis. Learn schema design, optimization, indexing, and data modeling strategies.
---

# Databases & Data Persistence

## SQL Fundamentals
```sql
-- Create & index
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  INDEX idx_email (email)
);

-- CRUD operations
SELECT * FROM users WHERE id = 1;
INSERT INTO users (email) VALUES ('user@example.com');
UPDATE users SET email = 'new@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;

-- Joins & aggregations
SELECT u.name, COUNT(o.id) as orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

## PostgreSQL
```sql
-- JSON support
CREATE TABLE data (content JSONB);
SELECT content->>'key' FROM data;

-- Window functions
SELECT name, salary,
  ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- CTEs
WITH ranked_users AS (
  SELECT id, ROW_NUMBER() OVER (ORDER BY created_at) as rank
  FROM users
)
SELECT * FROM ranked_users WHERE rank <= 10;
```

## MongoDB
```javascript
// Document operations
db.users.insertOne({ email: 'user@example.com', name: 'John' });
db.users.findOne({ email: 'user@example.com' });
db.users.updateOne({ id: 1 }, { $set: { name: 'Jane' } });
db.users.deleteOne({ id: 1 });

// Aggregation
db.users.aggregate([
  { $match: { active: true } },
  { $group: { _id: '$country', count: { $sum: 1 } } }
]);
```

## Redis
```bash
# String operations
SET key value
GET key
INCR counter

# List operations
LPUSH mylist value
RPOP mylist

# Cache patterns
SET user:1:profile {...} EX 3600
GET user:1:profile
```

## Key Concepts

✅ Schema design
✅ Indexing strategies
✅ Query optimization
✅ Normalization vs denormalization
✅ Transactions & ACID
✅ Replication & sharding
✅ Backup & recovery

## Choosing Databases

- **PostgreSQL**: General-purpose, reliability
- **MongoDB**: Flexible schema, documents
- **Redis**: Caching, real-time data
- **Elasticsearch**: Full-text search
