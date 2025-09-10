# Deployment Guide

## Overview

Dahlia supports multiple deployment methods, from development to production. This guide covers Docker, Docker Compose, and cloud deployment strategies.

## Local Development Deployment

### Quick Start
```bash
# Clone and setup
git clone https://github.com/divijg19/Dahlia.git
cd Dahlia
make setup

# Run locally
make run
```

### Docker Development
```bash
# Build and run with Docker Compose
make docker-compose

# Services available:
# - Dahlia app: http://localhost:8080
# - PostgreSQL: localhost:5432
# - Redis: localhost:6379
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3000
```

## Production Deployment

### Docker Deployment

#### 1. Build Production Image
```bash
# Build multi-stage Docker image
make docker

# Or manually
docker build -t dahlia:latest .
```

#### 2. Run Production Container
```bash
# Run with environment file
docker run -d \
  --name dahlia-app \
  -p 8080:8080 \
  --env-file .env.production \
  dahlia:latest

# Health check
docker exec dahlia-app ./dahlia-cli health
```

#### 3. Docker Compose Production
```bash
# Use production compose file
docker-compose -f docker-compose.prod.yml up -d
```

### Cloud Deployment

#### AWS ECS Deployment
```bash
# Build and tag for ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
docker build -t dahlia .
docker tag dahlia:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/dahlia:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/dahlia:latest

# Deploy with ECS task definition
# See deployments/aws/ecs-task-definition.json
```

#### Google Cloud Run
```bash
# Build and push to GCR
docker build -t gcr.io/PROJECT-ID/dahlia .
docker push gcr.io/PROJECT-ID/dahlia

# Deploy to Cloud Run
gcloud run deploy dahlia \
  --image gcr.io/PROJECT-ID/dahlia \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

#### Digital Ocean App Platform
```yaml
# app.yaml
name: dahlia
services:
- name: dahlia-app
  source_dir: /
  github:
    repo: divijg19/Dahlia
    branch: main
  run_command: ./dahlia
  environment_slug: docker
  instance_count: 1
  instance_size_slug: basic-xxs
  routes:
  - path: /
  envs:
  - key: ENV
    value: production
  - key: PORT
    value: "8080"
```

### Kubernetes Deployment

#### 1. Basic Deployment
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dahlia
spec:
  replicas: 3
  selector:
    matchLabels:
      app: dahlia
  template:
    metadata:
      labels:
        app: dahlia
    spec:
      containers:
      - name: dahlia
        image: dahlia:latest
        ports:
        - containerPort: 8080
        env:
        - name: ENV
          value: production
        - name: PORT
          value: "8080"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

#### 2. Service and Ingress
```yaml
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: dahlia-service
spec:
  selector:
    app: dahlia
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP

---
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dahlia-ingress
spec:
  rules:
  - host: dahlia.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: dahlia-service
            port:
              number: 80
```

#### 3. Deploy to Kubernetes
```bash
# Apply configurations
kubectl apply -f k8s/

# Check deployment
kubectl get pods
kubectl get services
kubectl describe ingress dahlia-ingress

# Port forward for testing
kubectl port-forward svc/dahlia-service 8080:80
```

## Automated Deployment

### Using Python Deployment Script
```bash
# Build and deploy to development
python3 scripts/python/deploy.py --action full --environment development

# Deploy to staging
python3 scripts/python/deploy.py --action full --environment staging

# Health check after deployment
python3 scripts/python/deploy.py --action health --environment production
```

### CI/CD Pipeline (GitHub Actions)
```yaml
# .github/workflows/deploy.yml
name: Deploy Dahlia
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Go
      uses: actions/setup-go@v2
      with:
        go-version: 1.19
    
    - name: Setup Rust
      uses: actions-rs/toolchain@v1
      with:
        toolchain: stable
    
    - name: Build and test
      run: |
        make build
        make test
    
    - name: Build Docker image
      run: make docker
    
    - name: Deploy to staging
      run: python3 scripts/python/deploy.py --environment staging
```

## Environment-Specific Configuration

### Development
```bash
# .env.development
ENV=development
LOG_LEVEL=debug
DATABASE_URL=postgres://localhost/dahlia_dev
REDIS_URL=redis://localhost:6379/0
```

### Staging
```bash
# .env.staging
ENV=staging
LOG_LEVEL=info
DATABASE_URL=postgres://staging-db/dahlia
REDIS_URL=redis://staging-redis:6379/0
JWT_SECRET=${STAGING_JWT_SECRET}
```

### Production
```bash
# .env.production
ENV=production
LOG_LEVEL=error
DATABASE_URL=${DATABASE_URL}
REDIS_URL=${REDIS_URL}
JWT_SECRET=${JWT_SECRET}
```

## Monitoring and Health Checks

### Health Check Endpoints
```bash
# Application health
curl http://your-domain/health

# Readiness check (dependencies)
curl http://your-domain/ready

# Metrics (Prometheus format)
curl http://your-domain/metrics
```

### Using CLI for Monitoring
```bash
# Health check with CLI
./bin/dahlia-cli health --url https://your-domain

# Get detailed status
./bin/dahlia-cli status --url https://your-domain

# Monitor metrics
./bin/dahlia-cli metrics --url https://your-domain
```

## Security Considerations

### Production Checklist
- [ ] Use strong JWT secrets
- [ ] Enable HTTPS with valid certificates
- [ ] Configure rate limiting
- [ ] Use non-root container user
- [ ] Set up firewall rules
- [ ] Enable security headers
- [ ] Regular security updates

### Container Security
```dockerfile
# Use non-root user
USER dahlia

# Health checks
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD ./dahlia-cli health --url http://localhost:8080 || exit 1
```

## Troubleshooting Deployment

### Common Issues

1. **Container won't start**:
   ```bash
   # Check logs
   docker logs dahlia-app
   
   # Check environment
   docker exec dahlia-app env
   ```

2. **Health check failures**:
   ```bash
   # Manual health check
   docker exec dahlia-app ./dahlia-cli health
   
   # Check application logs
   docker logs dahlia-app --tail 100
   ```

3. **Port conflicts**:
   ```bash
   # Check what's using the port
   netstat -tlnp | grep :8080
   
   # Use different port
   docker run -p 8081:8080 dahlia:latest
   ```

### Performance Tuning

1. **Container resources**:
   ```yaml
   resources:
     requests:
       memory: "64Mi"
       cpu: "50m"
     limits:
       memory: "128Mi"
       cpu: "100m"
   ```

2. **Application tuning**:
   - Set appropriate `GOMAXPROCS` for Go
   - Configure Rust release builds
   - Optimize Python script execution

## Rollback Strategy

### Docker Rollback
```bash
# Tag current version
docker tag dahlia:latest dahlia:backup

# Deploy new version
docker tag dahlia:v2.0.0 dahlia:latest

# Rollback if needed
docker tag dahlia:backup dahlia:latest
docker-compose up -d
```

### Kubernetes Rollback
```bash
# Check rollout history
kubectl rollout history deployment/dahlia

# Rollback to previous version
kubectl rollout undo deployment/dahlia

# Rollback to specific revision
kubectl rollout undo deployment/dahlia --to-revision=2
```