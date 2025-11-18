---
name: architecture-design
description: Master software architecture with design patterns, system design, scalability principles, and architectural decision-making. Learn about microservices, domain-driven design, and enterprise patterns. Use when designing systems, making architectural decisions, or solving design problems.
---

# Software Architecture & System Design

Design scalable, maintainable systems with proven architectural patterns and design principles.

## SOLID Principles

### Single Responsibility Principle (SRP)
```python
# Bad: User class does too much
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        # Saving logic
        pass

    def send_email(self):
        # Email sending logic
        pass

# Good: Separate concerns
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        # Saving logic
        pass

class EmailService:
    def send(self, recipient, message):
        # Email sending logic
        pass
```

### Open/Closed Principle (OCP)
```python
# Bad: Need to modify class for new types
class PaymentProcessor:
    def process(self, payment):
        if payment.type == 'credit_card':
            # Credit card logic
        elif payment.type == 'paypal':
            # PayPal logic

# Good: Open for extension, closed for modification
class PaymentProcessor:
    def process(self, payment_method):
        return payment_method.process()

class CreditCardPayment:
    def process(self):
        # Credit card specific logic
        pass

class PayPalPayment:
    def process(self):
        # PayPal specific logic
        pass
```

### Liskov Substitution Principle (LSP)
```python
# Bad: Subclass violates parent contract
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

# Good: Use composition or proper hierarchy
class FlyingBird:
    def fly(self):
        pass

class Bird:
    pass

class Eagle(FlyingBird):
    pass

class Penguin(Bird):
    pass
```

## Design Patterns

### Creational Patterns
```python
# Singleton
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):
        if payment_type == 'card':
            return CardPayment()
        elif payment_type == 'bank':
            return BankPayment()

# Builder
class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, *fields):
        self.query += f"SELECT {', '.join(fields)} "
        return self

    def where(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def build(self):
        return self.query

query = QueryBuilder().select('*').where('age > 18').build()
```

### Structural Patterns
```python
# Adapter
class LegacyPaymentGateway:
    def charge(self, amount):
        pass

class PaymentGatewayAdapter:
    def __init__(self, legacy_gateway):
        self.gateway = legacy_gateway

    def process_payment(self, amount):
        return self.gateway.charge(amount)

# Decorator
def with_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@with_logging
def process_order(order_id):
    print(f"Processing {order_id}")
```

## Architectural Styles

### Layered Architecture
```
┌─────────────────────────────┐
│    Presentation Layer       │ (API, Controllers)
├─────────────────────────────┤
│     Business Logic Layer    │ (Services, Use Cases)
├─────────────────────────────┤
│   Persistence Layer         │ (Repositories, DAOs)
├─────────────────────────────┤
│     Database Layer          │ (Database)
└─────────────────────────────┘
```

### Microservices Architecture
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ User Service │  │ Order Service│  │Payment Service│
└──────────────┘  └──────────────┘  └──────────────┘
        │                 │                  │
        └─────────────────┼──────────────────┘
                          │
                    ┌──────────────┐
                    │ API Gateway  │
                    └──────────────┘
```

### Event-Driven Architecture
```
┌──────────────┐         ┌──────────────┐
│   Producer   │────────▶│ Message Bus  │◀─────────┐
└──────────────┘         └──────────────┘          │
                                │                  │
                    ┌───────────┴────────┐         │
                    ▼                    ▼         │
              ┌──────────────┐     ┌──────────────┐
              │  Consumer 1  │     │  Consumer 2  │
              └──────────────┘     └──────────────┘
```

## System Design Example: URL Shortener

### Requirements
- Shorten long URLs
- Redirect short URLs to original
- Handle millions of requests
- Expiration support

### Design
```
┌─────────────┐         ┌──────────────┐
│   Client    │────────▶│  API Gateway │
└─────────────┘         └──────────────┘
                              │
                ┌─────────────┴──────────────┐
                ▼                            ▼
        ┌────────────────┐          ┌────────────────┐
        │ Shorten Service│          │Redirect Service│
        └────────────────┘          └────────────────┘
                │                            │
        ┌───────┴────────┬──────────────┐    │
        ▼                ▼              ▼    ▼
    ┌────────────────────────────────────────────┐
    │           Cache (Redis)                    │
    └────────────────────────────────────────────┘
        │
    ┌───┴───────────────┐
    ▼                   ▼
┌─────────┐     ┌─────────────┐
│Database │     │ File Storage│
└─────────┘     └─────────────┘
```

### Database Schema
```sql
CREATE TABLE short_urls (
    id BIGINT PRIMARY KEY,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    original_url TEXT NOT NULL,
    created_at TIMESTAMP,
    expires_at TIMESTAMP,
    click_count INT DEFAULT 0,
    INDEX idx_short_code (short_code),
    INDEX idx_created (created_at)
);

CREATE TABLE analytics (
    id BIGINT PRIMARY KEY,
    short_code VARCHAR(10),
    ip_address VARCHAR(45),
    user_agent TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (short_code) REFERENCES short_urls(short_code)
);
```

## Scalability Principles

### Horizontal Scaling
- Stateless services
- Load balancing
- Database replication
- Cache layers

### Vertical Scaling
- Optimize algorithms
- Profile and optimize
- Database indexes
- Connection pooling

## Interview Questions

1. Design a Twitter-like system
2. Design an Instagram feed system
3. How would you design a real-time notification system?
4. Design a rate limiting system
5. How would you handle distributed transactions?

## Resources

- Design Patterns: https://refactoring.guru/design-patterns
- System Design Primer: https://github.com/donnemartin/system-design-primer
- SOLID Principles: https://en.wikipedia.org/wiki/SOLID
- Architecture Decision Records: https://adr.github.io/
