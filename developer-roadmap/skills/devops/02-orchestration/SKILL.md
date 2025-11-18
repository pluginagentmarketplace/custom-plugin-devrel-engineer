---
name: devops-orchestration
description: Master Kubernetes container orchestration. Learn pods, services, deployments, scaling, networking, and production Kubernetes patterns.
---

# Kubernetes Orchestration

## Deployment Manifest
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
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

## Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 3000
  type: LoadBalancer
```

## Helm Charts
```bash
# Create chart
helm create myapp

# Install release
helm install myapp ./myapp

# Upgrade
helm upgrade myapp ./myapp

# Uninstall
helm uninstall myapp
```

## Key Concepts

✅ Pods - smallest deployable unit
✅ Services - networking & discovery
✅ Deployments - managing replicas
✅ StatefulSets - stateful apps
✅ ConfigMaps - configuration
✅ Secrets - sensitive data
✅ Namespaces - isolation
✅ RBAC - access control

## Monitoring
- Prometheus for metrics
- Grafana for dashboards
- ELK for logging
- Jaeger for tracing

## Best Practices
- Use readiness/liveness probes
- Resource limits
- Network policies
- Pod security policies
- Regular backups
