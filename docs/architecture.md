# Architecture Overview

## System Design

Dahlia is a modern, polyglot web server template designed to showcase best practices across multiple programming languages. The architecture demonstrates how Go, Rust, and Python can be used together effectively in a single project.

## Multi-Language Architecture

### Go (Core Web Server)
- **Purpose**: Main web server, API handlers, business logic
- **Why Go**: Excellent for web services, strong concurrency, fast compilation
- **Components**:
  - HTTP server with Gin framework
  - API route handlers
  - Configuration management
  - Middleware (CORS, logging, rate limiting)
  - Graceful shutdown handling

### Rust (Performance-Critical Components)
- **Purpose**: CLI tools, system utilities, high-performance processing
- **Why Rust**: Memory safety, zero-cost abstractions, excellent performance
- **Components**:
  - CLI tool for server management (`dahlia-cli`)
  - High-performance utility libraries
  - JSON processing utilities
  - String manipulation and hashing functions

### Python (Automation & Analytics)
- **Purpose**: Analytics, deployment automation, scripting
- **Why Python**: Rapid development, rich ecosystem, excellent for data processing
- **Components**:
  - Log analysis and reporting (`analytics.py`)
  - Deployment automation (`deploy.py`)
  - Configuration management scripts

## Directory Structure

```
dahlia/
├── cmd/                    # Go application entrypoints
│   └── server/            # Main web server
├── internal/              # Private Go code
│   ├── api/              # API handlers and routes
│   ├── config/           # Configuration management
│   ├── middleware/       # HTTP middleware
│   ├── models/           # Data models
│   ├── services/         # Business logic
│   └── storage/          # Data access layer
├── pkg/                  # Public Go libraries
│   ├── logger/           # Logging utilities
│   ├── validator/        # Input validation
│   └── utils/            # Common utilities
│       └── rust-utils/   # Rust performance utilities
├── scripts/              # Build and automation scripts
│   ├── dahlia-cli/       # Rust CLI tool
│   └── python/           # Python automation scripts
├── web/                  # Web assets
│   ├── static/           # Static files
│   └── templates/        # HTML templates
├── deployments/          # Deployment configurations
│   ├── docker/           # Docker configurations
│   └── k8s/              # Kubernetes manifests
└── docs/                 # Documentation
```

## Component Interaction

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CLI Client    │    │  Web Browser    │    │  External API   │
│   (dahlia-cli)  │    │                 │    │                 │
│     [Rust]      │    │                 │    │                 │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         │ HTTP Requests         │ HTTP Requests        │ HTTP Requests
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                    ┌───────────▼────────────┐
                    │    Dahlia Web Server   │
                    │         [Go]           │
                    │                        │
                    │  ┌─────────────────┐   │
                    │  │   Gin Router    │   │
                    │  │                 │   │
                    │  │ ┌─────────────┐ │   │
                    │  │ │ Middleware  │ │   │
                    │  │ │  - CORS     │ │   │
                    │  │ │  - Logging  │ │   │
                    │  │ │  - Rate     │ │   │
                    │  │ │    Limiting │ │   │
                    │  │ └─────────────┘ │   │
                    │  │                 │   │
                    │  │ ┌─────────────┐ │   │
                    │  │ │ API Routes  │ │   │
                    │  │ │  /health    │ │   │
                    │  │ │  /ready     │ │   │
                    │  │ │  /api/v1/*  │ │   │
                    │  │ │  /metrics   │ │   │
                    │  │ └─────────────┘ │   │
                    │  └─────────────────┘   │
                    └────────────────────────┘
                                │
                    ┌───────────▼────────────┐
                    │   Rust Utilities       │
                    │                        │
                    │  ┌─────────────────┐   │
                    │  │ JSON Processing │   │
                    │  │ String Utils    │   │
                    │  │ Hash Functions  │   │
                    │  │ Performance     │   │
                    │  │ Monitoring      │   │
                    │  └─────────────────┘   │
                    └────────────────────────┘
                                │
                    ┌───────────▼────────────┐
                    │   Python Scripts       │
                    │                        │
                    │  ┌─────────────────┐   │
                    │  │ Log Analytics   │   │
                    │  │ Deployment      │   │
                    │  │ Automation      │   │
                    │  │ Health Checks   │   │
                    │  └─────────────────┘   │
                    └────────────────────────┘
```

## Build System

The project uses a multi-language build system:

- **Makefile**: Coordinates builds across all languages
- **Go Modules**: Manages Go dependencies
- **Cargo Workspace**: Manages Rust dependencies
- **Docker Multi-stage**: Builds all components in containers
- **Docker Compose**: Orchestrates development environment

## Deployment Strategy

### Development
- Local builds with `make`
- Docker Compose for full stack
- Live reloading with Air (Go) and cargo watch (Rust)

### Production
- Multi-stage Docker builds
- Kubernetes manifests for orchestration
- Automated deployment with Python scripts
- Health checks and monitoring

## Observability

- **Health Checks**: `/health` and `/ready` endpoints
- **Metrics**: Prometheus-compatible `/metrics` endpoint
- **Logging**: Structured logging with configurable levels
- **Tracing**: Request correlation IDs (planned)

## Security Considerations

- **Input Validation**: Rust utilities for fast sanitization
- **Rate Limiting**: Configurable middleware
- **CORS**: Configurable cross-origin policies
- **JWT Authentication**: Ready for implementation
- **Container Security**: Non-root user, minimal base image

## Performance Characteristics

- **Go**: Fast startup, excellent concurrency, low memory usage
- **Rust**: Zero-cost abstractions, memory safety, optimal performance
- **Python**: Rapid development, rich ecosystem for complex tasks

## Scalability

- Stateless design enables horizontal scaling
- Container-ready for cloud deployment
- Database and Redis for state management
- Load balancer friendly with health checks

## Testing Strategy

- **Go**: Unit tests with standard library, integration tests
- **Rust**: Unit and integration tests with cargo
- **Python**: Unit tests with pytest (planned)
- **End-to-end**: Docker-based testing (planned)

## Future Enhancements

- WebSocket support for real-time features
- GraphQL API alongside REST
- Distributed tracing with OpenTelemetry
- Advanced metrics and alerting
- Database migrations and ORM
- Message queue integration