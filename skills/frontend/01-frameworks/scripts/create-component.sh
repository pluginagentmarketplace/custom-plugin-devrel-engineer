#!/bin/bash
# React Component Generator
# Creates a new component with TypeScript and tests

set -e

COMPONENT_NAME=$1
COMPONENT_DIR="src/components"

if [ -z "$COMPONENT_NAME" ]; then
    echo "Usage: create-component.sh <ComponentName>"
    exit 1
fi

# Create directory
mkdir -p "$COMPONENT_DIR/$COMPONENT_NAME"

# Create component file
cat > "$COMPONENT_DIR/$COMPONENT_NAME/$COMPONENT_NAME.tsx" << 'EOF'
import React from 'react';
import styles from './${COMPONENT_NAME}.module.css';

interface ${COMPONENT_NAME}Props {
  // Add props here
}

export const ${COMPONENT_NAME}: React.FC<${COMPONENT_NAME}Props> = () => {
  return (
    <div className={styles.container}>
      ${COMPONENT_NAME}
    </div>
  );
};

export default ${COMPONENT_NAME};
EOF

# Create test file
cat > "$COMPONENT_DIR/$COMPONENT_NAME/$COMPONENT_NAME.test.tsx" << 'EOF'
import { render, screen } from '@testing-library/react';
import { ${COMPONENT_NAME} } from './${COMPONENT_NAME}';

describe('${COMPONENT_NAME}', () => {
  it('renders without crashing', () => {
    render(<${COMPONENT_NAME} />);
    expect(screen.getByText('${COMPONENT_NAME}')).toBeInTheDocument();
  });
});
EOF

# Create styles
cat > "$COMPONENT_DIR/$COMPONENT_NAME/$COMPONENT_NAME.module.css" << 'EOF'
.container {
  /* Styles here */
}
EOF

# Create index
cat > "$COMPONENT_DIR/$COMPONENT_NAME/index.ts" << 'EOF'
export { default, ${COMPONENT_NAME} } from './${COMPONENT_NAME}';
EOF

echo "Created component: $COMPONENT_NAME"
