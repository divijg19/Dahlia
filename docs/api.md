# API Documentation

## Overview

The Dahlia API provides endpoints for health monitoring, status checking, and basic application information.

## Base URL

```
http://localhost:8080
```

## Authentication

Currently, no authentication is required for the basic endpoints. JWT authentication middleware is available for protected routes.

## Endpoints

### Health Check

Check if the application is healthy and running.

**URL:** `/health`  
**Method:** `GET`  
**Response:**

```json
{
  "status": "healthy",
  "timestamp": "2024-01-10T12:00:00Z"
}
```

**Status Codes:**
- `200 OK` - Application is healthy

---

### Readiness Check

Check if the application is ready to serve traffic.

**URL:** `/ready`  
**Method:** `GET`  
**Response:**

```json
{
  "status": "ready",
  "timestamp": "2024-01-10T12:00:00Z",
  "services": {
    "database": "connected",
    "redis": "connected"
  }
}
```

**Status Codes:**
- `200 OK` - Application is ready
- `503 Service Unavailable` - Application dependencies are not ready

---

### Application Status

Get detailed application status information.

**URL:** `/api/v1/status`  
**Method:** `GET`  
**Response:**

```json
{
  "service": "dahlia",
  "version": "1.0.0",
  "uptime": "2h30m15s",
  "status": "running"
}
```

---

### Application Information

Get general information about the application.

**URL:** `/api/v1/info`  
**Method:** `GET`  
**Response:**

```json
{
  "name": "Dahlia",
  "description": "Modern multi-language web server template",
  "version": "1.0.0",
  "languages": ["Go", "Rust", "Python"],
  "features": [
    "RESTful API",
    "Health checks",
    "Graceful shutdown",
    "Multi-language architecture",
    "Container ready"
  ]
}
```

---

### Metrics

Get application metrics in Prometheus format.

**URL:** `/metrics`  
**Method:** `GET`  
**Response:** Plain text in Prometheus format

```
# HELP dahlia_uptime_seconds Uptime in seconds
# TYPE dahlia_uptime_seconds counter
dahlia_uptime_seconds 9015.50
# HELP dahlia_requests_total Total requests
# TYPE dahlia_requests_total counter
dahlia_requests_total{method="GET"} 0
```

## Error Responses

All endpoints may return error responses in the following format:

```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An internal server error occurred"
  }
}
```

**Common Error Codes:**
- `400 Bad Request` - Invalid request
- `404 Not Found` - Endpoint not found
- `500 Internal Server Error` - Server error

## Rate Limiting

Rate limiting is implemented but currently allows unlimited requests. In production, configure appropriate limits.

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for all endpoints with permissive settings suitable for development.

## CLI Tool

The `dahlia-cli` tool provides command-line access to these APIs:

```bash
# Check health
dahlia health

# Get status
dahlia status

# Get information
dahlia info

# Get metrics
dahlia metrics
```