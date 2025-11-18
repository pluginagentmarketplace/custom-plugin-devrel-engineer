---
name: architecture-patterns
description: Master design patterns and SOLID principles. Learn creational, structural, behavioral patterns, and their real-world applications.
---

# Design Patterns & SOLID Principles

## SOLID Principles

### Single Responsibility
```python
# Bad
class User:
    def save(self):
        # Save to database
        pass
    def send_email(self):
        # Send email
        pass

# Good
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, user):
        pass
```

## Creational Patterns

### Singleton
```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory
```python
class PaymentFactory:
    @staticmethod
    def create(payment_type):
        if payment_type == 'card':
            return CardPayment()
        elif payment_type == 'paypal':
            return PayPalPayment()
```

### Builder
```python
class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, *fields):
        self.query += f"SELECT {','.join(fields)} "
        return self

    def where(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def build(self):
        return self.query

query = QueryBuilder().select('*').where('age > 18').build()
```

## Structural Patterns

### Adapter
```python
class OldPaymentGateway:
    def charge(self, amount):
        pass

class PaymentAdapter:
    def __init__(self, gateway):
        self.gateway = gateway

    def process(self, amount):
        return self.gateway.charge(amount)
```

### Decorator
```python
def with_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@with_logging
def process():
    pass
```

## Behavioral Patterns

### Observer
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
```

### Strategy
```python
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        # Process credit card payment
        pass

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        return self.strategy.pay(amount)
```

## Key Patterns

✅ Singleton - One instance
✅ Factory - Object creation
✅ Observer - Event notification
✅ Strategy - Algorithm variation
✅ Adapter - Interface compatibility
✅ Decorator - Add functionality
✅ Repository - Data access
✅ MVC - Architecture pattern

