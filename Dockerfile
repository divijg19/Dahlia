# Multi-stage Docker build for Dahlia
FROM rust:1.75 as rust-builder

WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY scripts/dahlia-cli/ ./scripts/dahlia-cli/
COPY pkg/utils/rust-utils/ ./pkg/utils/rust-utils/

# Build Rust components
RUN cargo build --release

FROM golang:1.21-alpine as go-builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
# Build Go application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o bin/dahlia ./cmd/server

FROM python:3.11-slim as python-base

# Install Python dependencies for scripts
WORKDIR /app
RUN pip install requests

FROM alpine:3.18

# Install runtime dependencies
RUN apk --no-cache add ca-certificates tzdata

WORKDIR /root/

# Copy binaries from builders
COPY --from=go-builder /app/bin/dahlia .
COPY --from=rust-builder /app/target/release/dahlia ./dahlia-cli
COPY --from=python-base /usr/local/bin/python3 /usr/local/bin/
COPY --from=python-base /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY scripts/python/ ./scripts/

# Create non-root user
RUN adduser -D -s /bin/sh dahlia
USER dahlia

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD ./dahlia-cli health --url http://localhost:8080 || exit 1

# Run the application
CMD ["./dahlia"]