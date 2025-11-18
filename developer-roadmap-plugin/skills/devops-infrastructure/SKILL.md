---
name: devops-infrastructure
description: Master DevOps practices with Docker, Kubernetes, CI/CD, AWS, and infrastructure automation. Learn containerization, orchestration, monitoring, and deployment strategies. Use when setting up infrastructure, optimizing deployments, or managing cloud resources.
---

# DevOps & Infrastructure

Build and manage scalable, reliable cloud infrastructure with containerization, orchestration, and automation.

## Quick Start

### Docker Basics
```dockerfile
# Dockerfile - Multi-stage build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
# Build and run
docker build -t myapp:1.0.0 .
docker run -p 3000:3000 myapp:1.0.0
docker ps
docker logs <container-id>
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:1.0.0
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
```

### Terraform Infrastructure
```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "main-vpc"
  }
}

# Security Group
resource "aws_security_group" "app" {
  name        = "app-sg"
  description = "Security group for app"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.app.id]

  tags = {
    Name = "MyApp"
  }
}

output "instance_ip" {
  value = aws_instance.app.public_ip
}
```

## CI/CD Pipeline

### GitHub Actions
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18

      - run: npm install
      - run: npm test
      - run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: success()
    steps:
      - uses: actions/checkout@v3

      - name: Deploy to production
        run: |
          echo "Deploying to production"
          # Add your deployment commands
```

## Monitoring & Observability

### Prometheus & Grafana
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'nodejs'
    static_configs:
      - targets: ['localhost:3000']
```

### Log Aggregation with ELK Stack
```bash
# Elasticsearch - Logstash - Kibana setup
docker-compose up -d

# Ship logs
curl -X POST "localhost:9200/logs-2024/_doc" \
  -H 'Content-Type: application/json' \
  -d '{
    "timestamp": "2024-01-15T10:30:00Z",
    "level": "error",
    "message": "Database connection failed"
  }'
```

## Best Practices

### Container Security
- Use minimal base images (Alpine, distroless)
- Scan images for vulnerabilities
- Don't run as root
- Use secrets management for sensitive data

### Kubernetes Security
- Network policies for pod communication
- RBAC for access control
- Pod security policies
- Regular backup of etcd

### Infrastructure as Code
- Version control all infrastructure
- Code review for infrastructure changes
- Automated testing for IaC
- State management (Terraform state)

### Deployment Strategies
- **Blue-Green**: Run two identical production environments
- **Canary**: Gradually roll out to small percentage of users
- **Rolling**: Update instances one at a time
- **Feature Flags**: Control feature rollout independently

## Interview Questions

1. How do you handle database migrations in Kubernetes?
2. Explain the difference between stateful and stateless applications
3. How do you implement disaster recovery?
4. What's the difference between Docker and Kubernetes?
5. How do you scale Kubernetes clusters?

## Resources

- Docker Documentation: https://docs.docker.com
- Kubernetes: https://kubernetes.io/docs
- Terraform: https://www.terraform.io/docs
- AWS Documentation: https://docs.aws.amazon.com
- SRE Book: https://sre.google/sre-book
