---
name: devops-containers
description: Master containerization with Docker. Learn building images, running containers, registry management, and container security best practices.
---

# Docker & Container

ization

## Dockerfile
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "server.js"]
```

## Docker Commands
```bash
# Build image
docker build -t myapp:1.0.0 .

# Run container
docker run -p 3000:3000 myapp:1.0.0

# Container management
docker ps              # List running
docker logs <id>       # View logs
docker exec -it <id> bash  # Enter container
docker stop <id>       # Stop container

# Image management
docker tag myapp:1.0.0 myrepo/myapp:latest
docker push myrepo/myapp:latest
```

## Docker Compose
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://...
    depends_on:
      - db

  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: password
    volumes:
      - dbdata:/var/lib/postgresql/data

volumes:
  dbdata:
```

## Container Security
✅ Use minimal base images (Alpine)
✅ Run as non-root
✅ Scan images for vulnerabilities
✅ Use secrets management
✅ Keep layers small
✅ Use .dockerignore

## Registry
- **Docker Hub**: Default public registry
- **ECR**: AWS container registry
- **GCR**: Google Container Registry
- **Private**: Nexus, Harbor

