# Configuration Guide

## Environment Variables

Dahlia uses environment variables for configuration. Copy `.env.example` to `.env` and customize as needed.

### Server Configuration

```bash
# Server settings
PORT=8080                    # HTTP port to listen on
HOST=0.0.0.0                 # Host to bind to (0.0.0.0 for all interfaces)
ENV=development              # Environment: development, staging, production
LOG_LEVEL=info               # Log level: debug, info, error
```

### Database Configuration (Future)

```bash
# PostgreSQL database
DATABASE_URL=postgres://user:password@localhost:5432/dahlia?sslmode=disable

# Redis cache  
REDIS_URL=redis://localhost:6379/0
```

### Security Settings

```bash
# JWT secret for token signing
JWT_SECRET=your-secret-key-change-in-production

# Rate limiting
RATE_LIMIT=100               # Requests per minute per IP
```

## Configuration Loading

The Go application loads configuration in this order:
1. Environment variables
2. `.env` file (if exists)
3. Default values

```go
// Example: PORT configuration
port := 8080
if p := os.Getenv("PORT"); p != "" {
    if parsed, err := strconv.Atoi(p); err == nil {
        port = parsed
    }
}
```

## Multi-Language Configuration

### Go Configuration
- Located in `internal/config/config.go`
- Struct-based configuration with defaults
- Environment variable parsing
- Validation and type conversion

### Rust Configuration
- CLI argument parsing with Clap
- Server URL configuration via `--url` flag
- JSON output formatting
- Error handling with anyhow

### Python Configuration
- Argument parsing with argparse
- Configuration files support (JSON)
- Environment-specific settings
- Deployment configuration management

## Development vs Production

### Development Settings
```bash
ENV=development
LOG_LEVEL=debug
PORT=8080
HOST=127.0.0.1
```

### Production Settings
```bash
ENV=production
LOG_LEVEL=info
PORT=8080
HOST=0.0.0.0
JWT_SECRET=strong-random-secret-key
```

## Docker Configuration

### Environment Variables in Docker
```yaml
# docker-compose.yml
environment:
  - ENV=development
  - LOG_LEVEL=debug
  - DATABASE_URL=postgres://dahlia:password@postgres:5432/dahlia
  - REDIS_URL=redis://redis:6379/0
```

### Docker Environment File
```bash
# Create .env.docker
cp .env.example .env.docker
# Edit .env.docker for Docker-specific settings
```

## Configuration Validation

The application validates configuration at startup:
- Required fields are checked
- Format validation (URLs, ports, etc.)
- Connection testing for external services
- Graceful fallback to defaults

## Advanced Configuration

### Custom Configuration Files

For complex deployments, create environment-specific files:

```bash
# configs/development.json
{
  "server": {
    "port": 8080,
    "host": "localhost"
  },
  "logging": {
    "level": "debug",
    "format": "text"
  }
}
```

### CLI Tool Configuration

The Rust CLI tool accepts configuration via:
- Command line flags: `--url`, `--timeout`
- Environment variables: `DAHLIA_URL`, `DAHLIA_TIMEOUT`
- Configuration file: `~/.dahlia/config.toml`

### Python Script Configuration

Python scripts support:
- Command line arguments
- Configuration files (JSON/YAML)
- Environment variables
- Default settings

## Configuration Best Practices

1. **Never commit secrets**: Use `.env` files and `.gitignore`
2. **Use strong defaults**: Application should work out of the box
3. **Validate early**: Check configuration at startup
4. **Document everything**: Clear comments and examples
5. **Environment parity**: Same configuration structure across environments

## Troubleshooting Configuration

### Common Issues

1. **Port already in use**:
   ```bash
   Error: listen tcp :8080: bind: address already in use
   Solution: Change PORT in .env or kill existing process
   ```

2. **Invalid database URL**:
   ```bash
   Error: failed to connect to database
   Solution: Check DATABASE_URL format and connectivity
   ```

3. **Missing environment file**:
   ```bash
   Warning: .env file not found, using defaults
   Solution: Copy .env.example to .env
   ```

### Configuration Debugging

Enable debug logging to see configuration loading:
```bash
LOG_LEVEL=debug make run
```

Check current configuration:
```bash
./bin/dahlia-cli info
curl http://localhost:8080/api/v1/status
```