"""
Clean Architecture Template
Domain-Driven Design with dependency inversion
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

# ============== ENTITIES ==============
@dataclass
class User:
    """Domain entity."""
    id: str
    email: str
    name: str

# ============== USE CASES ==============
class UserRepository(ABC):
    """Port - Repository interface."""

    @abstractmethod
    def find_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

class GetUserUseCase:
    """Use case - Application business logic."""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> Optional[User]:
        return self.user_repository.find_by_id(user_id)

# ============== ADAPTERS ==============
class InMemoryUserRepository(UserRepository):
    """Adapter - In-memory implementation."""

    def __init__(self):
        self._users: dict[str, User] = {}

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)

    def save(self, user: User) -> User:
        self._users[user.id] = user
        return user

# ============== COMPOSITION ROOT ==============
def create_get_user_use_case() -> GetUserUseCase:
    """Dependency injection."""
    repository = InMemoryUserRepository()
    return GetUserUseCase(repository)
