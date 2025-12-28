# React Best Practices & Patterns

## Component Patterns

### 1. Container/Presentational Pattern

```typescript
// Container (logic)
const UserListContainer = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => { fetchUsers(); }, []);
  return <UserList users={users} />;
};

// Presentational (UI)
const UserList = ({ users }) => (
  <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
);
```

### 2. Compound Components

```typescript
const Menu = ({ children }) => <nav>{children}</nav>;
Menu.Item = ({ children }) => <a>{children}</a>;

// Usage
<Menu>
  <Menu.Item>Home</Menu.Item>
  <Menu.Item>About</Menu.Item>
</Menu>
```

### 3. Render Props

```typescript
const MouseTracker = ({ render }) => {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return render(pos);
};
```

## Hooks Best Practices

| Hook | When to Use |
|------|-------------|
| useState | Simple local state |
| useReducer | Complex state logic |
| useContext | Global state |
| useMemo | Expensive calculations |
| useCallback | Stable function references |

## Performance Optimization

1. **React.memo** - Prevent unnecessary re-renders
2. **useMemo/useCallback** - Memoize values/functions
3. **Code Splitting** - React.lazy + Suspense
4. **Virtual Lists** - For large lists

## Testing Strategy

```typescript
// Component test with RTL
import { render, screen, fireEvent } from '@testing-library/react';

test('button click works', () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click</Button>);
  fireEvent.click(screen.getByText('Click'));
  expect(handleClick).toHaveBeenCalled();
});
```
