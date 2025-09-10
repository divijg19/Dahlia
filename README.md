# 🌸 Dahlia

**A modern, scalable Golang web server template for rapid application development**

[![Go Version](https://img.shields.io/badge/Go-%3E1.25-blue.svg)](https://golang.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Pending-yellow.svg)](https://github.com/divijg19/Dahlia/actions)

## 🎯 Overview

Dahlia is a production-ready Golang web server template designed to accelerate the development of robust, scalable web applications. Built with modern Go practices and industry standards, it provides a solid foundation for building APIs, microservices, and web applications.

## ✨ Goals

- **🚀 Rapid Development**: Get your web server up and running in minutes, not hours
- **🏗️ Scalable Architecture**: Built-in patterns for horizontal and vertical scaling
- **🔒 Security First**: Implement security best practices from day one
- **📊 Observable**: Comprehensive logging, metrics, and health checks
- **🧪 Testable**: High test coverage with examples and testing utilities
- **📚 Well-Documented**: Clear documentation and code examples
- **🔧 Configurable**: Environment-based configuration with sensible defaults
- **🐳 Container Ready**: Docker support for easy deployment and development

## 🚀 Quick Start

```bash
# Clone the template
git clone https://github.com/divijg19/Dahlia.git your-project-name
cd your-project-name

# Initialize your Go module
go mod init your-module-name

# Install dependencies
go mod tidy

# Run the server
go run cmd/server/main.go

# Your server is now running at http://localhost:8080
```

## 📁 Project Structure

```
dahlia/
├── cmd/                    # Application entrypoints
│   └── server/            # Web server main application
├── internal/              # Private application code
│   ├── api/              # API handlers and routes
│   ├── config/           # Configuration management
│   ├── middleware/       # HTTP middleware
│   ├── models/           # Data models and structures
│   ├── services/         # Business logic layer
│   └── storage/          # Data access layer
├── pkg/                  # Public libraries (reusable)
│   ├── logger/           # Logging utilities
│   ├── validator/        # Input validation
│   └── utils/            # Common utilities
├── web/                  # Web assets (if needed)
│   ├── static/           # Static files (CSS, JS, images)
│   └── templates/        # HTML templates
├── deployments/          # Deployment configurations
│   ├── docker/           # Docker configurations
│   └── k8s/              # Kubernetes manifests
├── scripts/              # Build and deployment scripts
├── docs/                 # Project documentation
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── Dockerfile           # Container definition
├── docker-compose.yml   # Local development setup
├── Makefile            # Build automation
└── README.md           # This file
```

## 🗓️ Development Roadmap

### Phase 1: Foundation (Weeks 1-2)
- [x] **Project Setup**
  - [x] Repository structure and README
  - [ ] Go module initialization
  - [ ] Basic project structure creation
  - [ ] Git hooks and CI/CD pipeline setup

- [ ] **Core Server**
  - [ ] HTTP server setup with Gin/Echo framework
  - [ ] Basic routing and middleware structure
  - [ ] Environment-based configuration
  - [ ] Graceful shutdown implementation

### Phase 2: Essential Features (Weeks 3-4)
- [ ] **Middleware & Security**
  - [ ] CORS middleware
  - [ ] Rate limiting
  - [ ] Authentication middleware (JWT)
  - [ ] Request logging and tracing
  - [ ] Input validation and sanitization

- [ ] **Database Integration**
  - [ ] Database connection management
  - [ ] Migration system
  - [ ] Repository pattern implementation
  - [ ] Database health checks

### Phase 3: Observability (Weeks 5-6)
- [ ] **Logging & Monitoring**
  - [ ] Structured logging (JSON format)
  - [ ] Metrics collection (Prometheus)
  - [ ] Health check endpoints
  - [ ] Request tracing and correlation IDs

- [ ] **Error Handling**
  - [ ] Centralized error handling
  - [ ] Custom error types
  - [ ] Error response formatting
  - [ ] Recovery middleware

### Phase 4: Testing & Quality (Weeks 7-8)
- [ ] **Testing Infrastructure**
  - [ ] Unit test examples and utilities
  - [ ] Integration test setup
  - [ ] API testing with test client
  - [ ] Mock implementations

- [ ] **Code Quality**
  - [ ] Linting configuration (golangci-lint)
  - [ ] Code formatting (gofmt, goimports)
  - [ ] Documentation generation
  - [ ] Performance benchmarking

### Phase 5: Deployment & Operations (Weeks 9-10)
- [ ] **Containerization**
  - [ ] Multi-stage Dockerfile
  - [ ] Docker Compose for development
  - [ ] Container security scanning
  - [ ] Size optimization

- [ ] **Production Readiness**
  - [ ] Kubernetes manifests
  - [ ] Helm charts
  - [ ] Production configuration examples
  - [ ] Deployment automation

## 🛠️ Technology Stack

### Core Technologies
- **Language**: Go 1.19+
- **Web Framework**: Gin Gonic (lightweight and fast)
- **Database**: PostgreSQL with GORM
- **Caching**: Redis
- **Configuration**: Viper

### Development Tools
- **Testing**: Testify, GoMock
- **Linting**: golangci-lint
- **Documentation**: godoc, Swagger
- **Build**: Make, Docker

### Observability
- **Logging**: Logrus/Zap
- **Metrics**: Prometheus
- **Tracing**: OpenTelemetry
- **Health Checks**: Custom implementation

## 📋 Prerequisites

- Go 1.19 or higher
- Docker and Docker Compose
- Make (optional, for build automation)
- Git

## 🚀 Getting Started

### 1. Use This Template
```bash
# Using GitHub CLI
gh repo create your-project --template divijg19/Dahlia --public

# Or clone directly
git clone https://github.com/divijg19/Dahlia.git your-project
cd your-project
```

### 2. Setup Your Project
```bash
# Initialize Go module
go mod init github.com/yourusername/your-project

# Copy environment configuration
cp .env.example .env

# Install development dependencies
make setup  # or go mod tidy
```

### 3. Run Development Server
```bash
# Using Make
make run

# Or directly with Go
go run cmd/server/main.go

# With live reloading (requires air)
air
```

### 4. Verify Installation
```bash
# Health check
curl http://localhost:8080/health

# API documentation
open http://localhost:8080/docs
```

## 🧪 Testing

```bash
# Run all tests
make test

# Run tests with coverage
make test-coverage

# Run integration tests
make test-integration

# Run benchmarks
make benchmark
```

## 📊 Monitoring

The template includes built-in observability features:

- **Health Checks**: `/health`, `/ready`
- **Metrics**: `/metrics` (Prometheus format)
- **Profiling**: `/debug/pprof/` (in development mode)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow Go conventions and best practices
- Write tests for new features
- Update documentation as needed
- Ensure all CI checks pass

## 📚 Documentation

- [API Documentation](docs/api.md) - REST API reference
- [Configuration Guide](docs/configuration.md) - Environment and config options
- [Deployment Guide](docs/deployment.md) - Production deployment instructions
- [Development Setup](docs/development.md) - Local development environment
- [Architecture Overview](docs/architecture.md) - System design and patterns

## 🔧 Configuration

Key configuration options (see `.env.example`):

```env
# Server
PORT=8080
HOST=0.0.0.0
ENV=development

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dahlia
DB_USER=user
DB_PASSWORD=password

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
JWT_SECRET=your-secret-key
RATE_LIMIT=100
```

## 🚢 Deployment

### Docker
```bash
# Build image
docker build -t dahlia:latest .

# Run container
docker run -p 8080:8080 --env-file .env dahlia:latest
```

### Docker Compose
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f app
```

### Kubernetes
```bash
# Apply manifests
kubectl apply -f deployments/k8s/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Go community for excellent tools and libraries
- Contributors who help improve this template
- Open source projects that inspire best practices

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/divijg19/Dahlia/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/divijg19/Dahlia/discussions)
- 📖 **Documentation**: [Project Wiki](https://github.com/divijg19/Dahlia/wiki)

---

**Made with ❤️ for the Go community**
