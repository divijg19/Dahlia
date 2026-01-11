# 🌸 Dahlia

**A modern, polyglot web server template showcasing Go, Rust, and Python integration**


[![Go Version](https://img.shields.io/badge/Go-%3E1.25-cyan.svg)](https://golang.org/)
[![Rust Version](https://img.shields.io/badge/Rust-%3E%3D1.94-red.svg)](https://rust-lang.org/)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D3.13-blue.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](#)

## 🎯 Overview

Dahlia is a production-ready, multi-language web server template that demonstrates how to effectively combine **Go**, **Rust**, and **Python** in a single, cohesive project. This template showcases modern development practices, clean architecture, and optimal language selection for different components.

**🔥 Perfect for showcasing technical versatility and modern development skills!**

## 🚀 Multi-Language Architecture

### 🏗️ **Go** - Core Web Server
- **Purpose**: Main HTTP server, API handlers, business logic
- **Why Go**: Excellent concurrency, fast compilation, robust web ecosystem
- **Components**: REST API, middleware, configuration, graceful shutdown

### ⚡ **Rust** - High-Performance Utilities  
- **Purpose**: CLI tools, system utilities, performance-critical components
- **Why Rust**: Memory safety, zero-cost abstractions, blazing fast execution
- **Components**: CLI management tool, data processing utilities

### 🐍 **Python** - Analytics & Automation
- **Purpose**: Analytics, deployment automation, scripting
- **Why Python**: Rapid development, rich ecosystem, excellent for data processing
- **Components**: Log analytics, deployment scripts, monitoring tools

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
# Clone the repository
git clone https://github.com/divijg19/Dahlia.git your-project-name
cd your-project-name

# Setup development environment (installs deps, creates bin/ dir)
make setup

# Build all components (Go, Rust, Python)
make build

# Run the server
make run

# Your server is now running at http://localhost:8080
# Test with: curl http://localhost:8080/health
```

### CLI Usage
```bash
# Use the Rust CLI tool for server management
./bin/dahlia-cli health          # Check server health
./bin/dahlia-cli status          # Get detailed status  
./bin/dahlia-cli info            # Get server information
./bin/dahlia-cli metrics         # Get Prometheus metrics

# Analytics with Python
python3 scripts/python/analytics.py --format text

# Deployment automation
python3 scripts/python/deploy.py --action build
```

## 📁 Project Structure

```
dahlia/
├── cmd/                    # Go application entrypoints
│   └── server/            # Main web server (Go)
├── internal/              # Private Go code
│   ├── api/              # API handlers and routes
│   ├── config/           # Configuration management
│   ├── middleware/       # HTTP middleware
│   ├── models/           # Data models and structures
│   ├── services/         # Business logic layer
│   └── storage/          # Data access layer
├── pkg/                  # Public libraries
│   ├── logger/           # Logging utilities (Go)
│   ├── validator/        # Input validation (Go)
│   └── utils/            # Common utilities
│       └── rust-utils/   # High-performance utilities (Rust)
├── scripts/              # Build and automation scripts
│   ├── dahlia-cli/       # Server management CLI (Rust)
│   └── python/           # Analytics & deployment (Python)
│       ├── analytics.py  # Log analysis and reporting
│       └── deploy.py     # Deployment automation
├── web/                  # Web assets (future)
│   ├── static/           # Static files
│   └── templates/        # HTML templates
├── deployments/          # Deployment configurations
│   ├── docker/           # Docker configurations
│   └── k8s/              # Kubernetes manifests
├── docs/                 # Documentation
│   ├── api.md           # API reference
│   ├── architecture.md  # System design
│   ├── development.md   # Development setup
│   └── deployment.md    # Deployment guide
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules  
├── Dockerfile           # Multi-stage container build
├── docker-compose.yml   # Development environment
├── Makefile            # Multi-language build system
├── go.mod              # Go dependencies
├── Cargo.toml          # Rust workspace
└── README.md           # This file
```

## ✅ Implementation Status

### ✅ Phase 1: Foundation (COMPLETED)
- [x] **Project Setup**
  - [x] Multi-language repository structure
  - [x] Go, Rust, and Python integration
  - [x] Build system with Makefile
  - [x] Documentation and README

- [x] **Core Server (Go)**
  - [x] HTTP server with Gin framework
  - [x] Basic routing and API endpoints
  - [x] Environment-based configuration
  - [x] Graceful shutdown implementation
  - [x] Health and readiness checks

### ✅ Phase 2: Multi-Language Components (COMPLETED)
- [x] **Rust Components**
  - [x] CLI tool for server management (`dahlia-cli`)
  - [x] High-performance utilities library  
  - [x] JSON processing and string utilities
  - [x] Integrated build system

- [x] **Python Components**
  - [x] Log analytics script (`analytics.py`)
  - [x] Deployment automation (`deploy.py`)
  - [x] Configuration management
  - [x] Health check automation

### ✅ Phase 3: Infrastructure (COMPLETED)
- [x] **Containerization**
  - [x] Multi-stage Dockerfile
  - [x] Docker Compose for development
  - [x] Environment configuration
  - [x] Health checks in containers

- [x] **Documentation**
  - [x] API documentation
  - [x] Architecture overview  
  - [x] Development setup guide
  - [x] Multi-language build instructions

### 🔄 Future Enhancements (TODO)
- [ ] **Database Integration**
  - [ ] PostgreSQL with GORM
  - [ ] Database migrations
  - [ ] Repository pattern

- [ ] **Advanced Features**
  - [ ] JWT authentication middleware
  - [ ] Rate limiting with Redis
  - [ ] Distributed tracing
  - [ ] Advanced metrics collection

- [ ] **Production Readiness**
  - [ ] Kubernetes manifests
  - [ ] CI/CD pipeline setup
  - [ ] Security hardening
  - [ ] Performance optimization

## 🛠️ Technology Stack

### Core Technologies
- **Go 1.22+**: Web server, APIs, business logic
  - Framework: Gin Gonic (lightweight and fast)
  - Configuration: Environment-based with defaults
  - Logging: Custom structured logging
- **Rust 2024**: CLI tools, performance utilities
  - CLI: Clap for command-line interface
  - HTTP: Reqwest for API clients
  - JSON: Serde for serialization
- **Python 3.11+**: Analytics, automation, deployment
  - HTTP: Requests for API interactions  
  - Analytics: Custom log processing
  - Deployment: Docker and process automation

### Development Tools
- **Build System**: Make (multi-language coordination)
- **Containerization**: Docker multi-stage builds
- **Orchestration**: Docker Compose for development
- **Documentation**: Markdown with architecture diagrams

### Observability  
- **Health Checks**: `/health`, `/ready` endpoints
- **Metrics**: Prometheus-compatible `/metrics`
- **Logging**: Structured logging with levels
- **CLI Monitoring**: Rust CLI for server management

## 📋 Prerequisites

- **Go 1.22+**: [Download Go](https://golang.org/dl/)
- **Rust 1.89+**: [Install Rust](https://rustup.rs/)  
- **Python 3.11+**: [Download Python](https://python.org/downloads/)
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Make**: Usually pre-installed (Linux/macOS) or [Windows](https://gnuwin32.sourceforge.net/packages/make.htm)

## 🚀 Getting Started

### 1. Use This Template
```bash
# Clone the repository  
git clone https://github.com/divijg19/Dahlia.git your-project
cd your-project

# Or use GitHub CLI
gh repo create your-project --template divijg19/Dahlia --public
```

### 2. Setup Your Project
```bash
# Setup development environment
make setup

# This will:
# - Copy .env.example to .env
# - Install Go dependencies (go mod tidy) 
# - Check Rust components (cargo check)
# - Create bin/ and logs/ directories
```

### 3. Build All Components
```bash
# Build everything (Go + Rust + Python check)
make build

# Or build individually:
make build-go    # Build Go web server
make build-rust  # Build Rust CLI and utilities
```

### 4. Run the Server
```bash
# Run in development mode
make run

# Or with live reloading (requires 'air')
make run-dev

# Or with Docker Compose (full stack)
make docker-compose
```

### 5. Verify Installation
```bash
# Health check
curl http://localhost:8080/health

# Use the CLI tool  
./bin/dahlia-cli health
./bin/dahlia-cli info

# Check logs with Python analytics
python3 scripts/python/analytics.py --format text
```

## 🧪 Testing

```bash
# Run all tests (Go + Rust)
make test

# Run specific language tests
make test-go
make test-rust

# Generate test coverage report
make test-coverage

# Manual testing with CLI
./bin/dahlia-cli health --url http://localhost:8080
./bin/dahlia-cli metrics
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
