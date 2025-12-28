# Docker Best Practices

## Image Optimization

| Practice | Impact |
|----------|--------|
| Multi-stage builds | -70% size |
| Alpine base images | -80% size |
| .dockerignore | -50% build time |
| Layer caching | -90% rebuild time |

## Security

1. **Non-root user**: Always run as non-root
2. **Minimal base**: Use distroless or alpine
3. **Scan images**: Use trivy/snyk
4. **Pin versions**: Lock base image tags
5. **No secrets**: Use build args/env vars

## Dockerfile Checklist

- [ ] Multi-stage build
- [ ] .dockerignore exists
- [ ] Non-root user
- [ ] HEALTHCHECK defined
- [ ] Minimal layers
- [ ] Pinned versions

## Docker Compose

```yaml
version: '3.8'
services:
  app:
    build: .
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
    deploy:
      resources:
        limits:
          memory: 512M
```
