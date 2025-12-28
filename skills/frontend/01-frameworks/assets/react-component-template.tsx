/**
 * React Component Template
 * Modern React 18+ with TypeScript
 */

import React, { useState, useEffect, useCallback, memo } from 'react';

interface ComponentProps {
  title: string;
  description?: string;
  onAction?: (data: unknown) => void;
  children?: React.ReactNode;
}

/**
 * Modern React functional component with hooks
 */
export const Component: React.FC<ComponentProps> = memo(({
  title,
  description,
  onAction,
  children
}) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  // Effect with cleanup
  useEffect(() => {
    let isMounted = true;

    const fetchData = async () => {
      try {
        setIsLoading(true);
        // Fetch logic here
      } catch (err) {
        if (isMounted) {
          setError(err instanceof Error ? err : new Error('Unknown error'));
        }
      } finally {
        if (isMounted) {
          setIsLoading(false);
        }
      }
    };

    fetchData();

    return () => {
      isMounted = false;
    };
  }, []);

  // Memoized callback
  const handleClick = useCallback(() => {
    onAction?.({ timestamp: Date.now() });
  }, [onAction]);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div className="component-container">
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      <button onClick={handleClick}>Action</button>
      {children}
    </div>
  );
});

Component.displayName = 'Component';
export default Component;
