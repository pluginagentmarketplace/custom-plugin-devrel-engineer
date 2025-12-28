#!/bin/bash
# Docker Build Script with best practices

set -e

IMAGE_NAME=${1:-"app"}
TAG=${2:-"latest"}
REGISTRY=${DOCKER_REGISTRY:-""}

echo "Building Docker image: $IMAGE_NAME:$TAG"

# Build with caching
docker build \
  --cache-from "$REGISTRY$IMAGE_NAME:latest" \
  --build-arg BUILDKIT_INLINE_CACHE=1 \
  -t "$IMAGE_NAME:$TAG" \
  -t "$IMAGE_NAME:latest" \
  .

# Run security scan if trivy available
if command -v trivy &> /dev/null; then
    echo "Running security scan..."
    trivy image --severity HIGH,CRITICAL "$IMAGE_NAME:$TAG"
fi

# Size check
echo "Image size:"
docker images "$IMAGE_NAME:$TAG" --format "{{.Size}}"

echo "Build complete!"
