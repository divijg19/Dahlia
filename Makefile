.PHONY: help build test clean run docker setup
.DEFAULT_GOAL := help

# Variables
BINARY_NAME := dahlia
DOCKER_IMAGE := dahlia:latest
RUST_COMPONENTS := scripts/dahlia-cli pkg/utils/rust-utils

help: ## Show this help message
	@echo "🌸 Dahlia Makefile"
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*##"; printf "\n"} /^[a-zA-Z_-]+:.*##/ { printf "  %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

setup: ## Setup development environment
	@echo "🔧 Setting up development environment..."
	@cp .env.example .env 2>/dev/null || true
	@go mod tidy
	@cargo check
	@pip3 install -r scripts/python/requirements.txt 2>/dev/null || echo "⚠️  Python requirements.txt not found, skipping"
	@mkdir -p bin logs
	@echo "✅ Setup complete"

build: build-go build-rust ## Build all components
	@echo "✅ All components built successfully"

build-go: ## Build Go application
	@echo "🔨 Building Go application..."
	@mkdir -p bin
	@go build -o bin/$(BINARY_NAME) ./cmd/server
	@echo "✅ Go build complete"

build-rust: ## Build Rust components
	@echo "🔨 Building Rust components..."
	@cargo build --release
	@cp target/release/dahlia bin/dahlia-cli 2>/dev/null || echo "⚠️  CLI binary not found"
	@echo "✅ Rust build complete"

test: test-go test-rust ## Run all tests
	@echo "✅ All tests passed"

test-go: ## Run Go tests
	@echo "🧪 Running Go tests..."
	@go test -v ./...

test-rust: ## Run Rust tests  
	@echo "🧪 Running Rust tests..."
	@cargo test --workspace

test-coverage: ## Run tests with coverage
	@echo "📊 Running tests with coverage..."
	@go test -coverprofile=coverage.out ./...
	@go tool cover -html=coverage.out -o coverage.html
	@echo "📋 Coverage report: coverage.html"

run: build-go ## Run the application
	@echo "🚀 Starting Dahlia server..."
	@./bin/$(BINARY_NAME)

run-dev: ## Run with live reloading (requires air)
	@echo "🔄 Starting development server with live reload..."
	@air || go run ./cmd/server

docker: ## Build Docker image
	@echo "🐳 Building Docker image..."
	@docker build -t $(DOCKER_IMAGE) .
	@echo "✅ Docker image built: $(DOCKER_IMAGE)"

docker-run: docker ## Build and run Docker container
	@echo "🐳 Running Docker container..."
	@docker run -p 8080:8080 --env-file .env $(DOCKER_IMAGE)

docker-compose: ## Start all services with docker-compose
	@echo "🐳 Starting all services..."
	@docker-compose up -d
	@echo "✅ Services started. Check: http://localhost:8080/health"

docker-compose-logs: ## Show docker-compose logs
	@docker-compose logs -f

docker-compose-down: ## Stop docker-compose services
	@docker-compose down

clean: ## Clean build artifacts
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf bin/ target/ coverage.out coverage.html
	@go clean
	@cargo clean
	@echo "✅ Clean complete"

lint: ## Run linters
	@echo "🔍 Running linters..."
	@golangci-lint run ./... 2>/dev/null || echo "⚠️  golangci-lint not installed"
	@cargo clippy --workspace
	@echo "✅ Linting complete"

fmt: ## Format code
	@echo "📝 Formatting code..."
	@go fmt ./...
	@cargo fmt --all
	@black scripts/python/ 2>/dev/null || echo "⚠️  black not installed"
	@echo "✅ Formatting complete"

deps: ## Update dependencies
	@echo "📦 Updating dependencies..."
	@go mod tidy
	@cargo update
	@echo "✅ Dependencies updated"

# Analytics and deployment helpers
analytics: ## Run analytics script
	@echo "📊 Running analytics..."
	@python3 scripts/python/analytics.py

deploy: ## Deploy to development
	@echo "🚀 Deploying to development..."
	@python3 scripts/python/deploy.py --environment development

deploy-staging: ## Deploy to staging
	@echo "🚀 Deploying to staging..."
	@python3 scripts/python/deploy.py --environment staging

health-check: ## Check application health
	@echo "🏥 Checking application health..."
	@./bin/dahlia-cli health 2>/dev/null || curl -s http://localhost:8080/health | jq .

install: ## Install binaries to system
	@echo "📦 Installing binaries..."
	@sudo cp bin/$(BINARY_NAME) /usr/local/bin/
	@sudo cp bin/dahlia-cli /usr/local/bin/
	@echo "✅ Installation complete"