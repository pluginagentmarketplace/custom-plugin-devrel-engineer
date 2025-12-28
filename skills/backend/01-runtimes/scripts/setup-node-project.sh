#!/bin/bash
# Node.js Project Setup Script

set -e

PROJECT_NAME=${1:-"my-app"}

echo "Creating Node.js project: $PROJECT_NAME"

mkdir -p "$PROJECT_NAME"/{src,tests,config}
cd "$PROJECT_NAME"

# Initialize package.json
cat > package.json << EOF
{
  "name": "$PROJECT_NAME",
  "version": "1.0.0",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "lint": "eslint src/"
  }
}
EOF

# Create main file
cat > src/index.js << 'EOF'
require('dotenv').config();
const app = require('./app');

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server on port ${PORT}`));
EOF

# Create .env template
cat > .env.example << 'EOF'
PORT=3000
NODE_ENV=development
DATABASE_URL=
EOF

echo "Project created successfully!"
echo "Next: cd $PROJECT_NAME && npm install"
