# Development Setup

## Prerequisites

Ensure you have the following tools installed:

- **Go 1.19+**: [Download Go](https://golang.org/dl/)
- **Rust 1.70+**: [Install Rust](https://rustup.rs/)
- **Python 3.8+**: [Download Python](https://python.org/downloads/)
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Usually included with Docker Desktop
- **Make**: Usually pre-installed on macOS/Linux, [Windows installation](https://gnuwin32.sourceforge.net/packages/make.htm)

## Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/divijg19/Dahlia.git
   cd Dahlia
   ```

2. **Setup development environment**:
   ```bash
   make setup
   ```

3. **Build all components**:
   ```bash
   make build
   ```

4. **Run the application**:
   ```bash
   make run
   ```

5. **Verify installation**:
   ```bash
   curl http://localhost:8080/health
   ```

## Detailed Setup Steps

### Go Setup

1. **Verify Go installation**:
   ```bash
   go version
   # Should show: go version go1.19+ ...
   ```

2. **Initialize Go modules** (already done):
   ```bash
   go mod tidy
   ```

3. **Build Go application**:
   ```bash
   make build-go
   # Or directly: go build -o bin/dahlia ./cmd/server
   ```

### Rust Setup

1. **Verify Rust installation**:
   ```bash
   rustc --version
   cargo --version
   ```

2. **Build Rust components**:
   ```bash
   make build-rust
   # Or directly: cargo build --release
   ```

3. **Test CLI tool**:
   ```bash
   ./bin/dahlia-cli --help
   ```

### Python Setup

1. **Verify Python installation**:
   ```bash
   python3 --version
   # Should show: Python 3.8+ ...
   ```

2. **Install Python dependencies**:
   ```bash
   pip3 install requests
   # Or create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install requests
   ```

3. **Test Python scripts**:
   ```bash
   python3 scripts/python/analytics.py --help
   python3 scripts/python/deploy.py --help
   ```

## Development Workflow

### Running the Server

1. **Development mode** (with live reloading):
   ```bash
   make run-dev
   # Requires 'air' tool: go install github.com/cosmtrek/air@latest
   ```

2. **Production mode**:
   ```bash
   make run
   ```

3. **Docker mode**:
   ```bash
   make docker-compose
   ```

### Making Changes

1. **Go changes**: Server will restart automatically with `make run-dev`
2. **Rust changes**: Rebuild with `make build-rust`
3. **Python changes**: Run scripts directly

### Testing

1. **Run all tests**:
   ```bash
   make test
   ```

2. **Run specific language tests**:
   ```bash
   make test-go
   make test-rust
   ```

3. **Test with coverage**:
   ```bash
   make test-coverage
   ```

### Code Quality

1. **Format code**:
   ```bash
   make fmt
   ```

2. **Run linters**:
   ```bash
   make lint
   ```

3. **Check build**:
   ```bash
   make build
   ```

## Configuration

### Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```bash
# Server configuration
PORT=8080
HOST=0.0.0.0
ENV=development
LOG_LEVEL=debug

# Database (when implemented)
DATABASE_URL=postgres://dahlia:password@localhost:5432/dahlia

# Redis (when implemented)
REDIS_URL=redis://localhost:6379/0

# Security
JWT_SECRET=your-secret-key-change-in-production
```

### Development Services

Start supporting services with Docker:
```bash
docker-compose up -d postgres redis
```

## IDE Setup

### VS Code

Install recommended extensions:
- Go extension
- Rust Analyzer
- Python extension
- Docker extension

Workspace settings (`.vscode/settings.json`):
```json
{
  "go.toolsManagement.checkForUpdates": "local",
  "rust-analyzer.linkedProjects": [
    "./Cargo.toml"
  ],
  "python.defaultInterpreterPath": "./venv/bin/python"
}
```

### IntelliJ/GoLand

1. Import as Go project
2. Enable Rust plugin
3. Configure Python interpreter

## Troubleshooting

### Common Issues

1. **Port 8080 already in use**:
   ```bash
   # Change port in .env file or kill existing process
   lsof -ti:8080 | xargs kill -9
   ```

2. **Rust build fails**:
   ```bash
   # Update Rust toolchain
   rustup update
   cargo clean
   make build-rust
   ```

3. **Go dependencies issues**:
   ```bash
   go clean -modcache
   go mod tidy
   ```

4. **Docker issues**:
   ```bash
   # Clean Docker
   docker system prune
   # Rebuild images
   docker-compose build --no-cache
   ```

### Debug Mode

1. **Enable debug logging**:
   ```bash
   export LOG_LEVEL=debug
   make run
   ```

2. **Use Rust CLI for debugging**:
   ```bash
   ./bin/dahlia-cli health -v
   ./bin/dahlia-cli status -v
   ```

3. **Python debugging**:
   ```bash
   python3 -u scripts/python/analytics.py --log-file /dev/stdin
   ```

## Performance Tips

1. **Use release builds for Rust**:
   ```bash
   cargo build --release
   ```

2. **Optimize Go builds**:
   ```bash
   go build -ldflags="-s -w" -o bin/dahlia ./cmd/server
   ```

3. **Use Docker multi-stage builds** for production:
   ```bash
   make docker
   ```

## Development Tools

### Recommended Tools

1. **Air** (Go live reloading):
   ```bash
   go install github.com/cosmtrek/air@latest
   ```

2. **golangci-lint** (Go linting):
   ```bash
   go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
   ```

3. **cargo-watch** (Rust live reloading):
   ```bash
   cargo install cargo-watch
   ```

4. **Black** (Python formatting):
   ```bash
   pip install black
   ```

## Next Steps

1. Read the [Architecture Overview](architecture.md)
2. Explore the [API Documentation](api.md)
3. Check the [Deployment Guide](deployment.md)
4. Review the [Configuration Guide](configuration.md)