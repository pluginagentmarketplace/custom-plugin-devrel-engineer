---
name: backend-runtimes
description: Master backend runtimes and programming languages. Learn Node.js, Python, Java, Go fundamentals, async patterns, and runtime-specific best practices.
---

# Backend Runtimes & Languages

## Node.js
```javascript
// Express server
const express = require('express');
const app = express();

app.get('/api/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});

app.listen(3000);

// Async/await pattern
async function processData() {
  const data = await fetchData();
  return transform(data);
}
```

## Python
```python
# FastAPI server
from fastapi import FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

# Django ORM
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

## Java
```java
// Spring Boot
@SpringBootApplication
public class Application {
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }
}

@RestController
@RequestMapping("/api/users")
public class UserController {
  @GetMapping("/{id}")
  public User getUser(@PathVariable Long id) {
    return userService.findById(id);
  }
}
```

## Go
```go
// HTTP server
package main

import (
  "net/http"
  "encoding/json"
)

func handler(w http.ResponseWriter, r *http.Request) {
  user := User{Name: "John"}
  json.NewEncoder(w).Encode(user)
}

func main() {
  http.HandleFunc("/user", handler)
  http.ListenAndServe(":8080", nil)
}
```

## Key Concepts

✅ HTTP methods & status codes
✅ Request/response handling
✅ Routing & middleware
✅ Error handling
✅ Logging
✅ Configuration management
✅ Dependency injection

## When to Choose

- **Node.js**: Full-stack JS, real-time apps
- **Python**: Data-heavy, rapid development
- **Java**: Enterprise, scalability
- **Go**: Performance, microservices
