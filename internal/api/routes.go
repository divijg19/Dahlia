package api

import (
	"fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

// Logger interface for dependency injection
type Logger interface {
	Info(msg string)
	Error(msg string)
	Debug(msg string)
}

// SetupRoutes configures all API routes
func SetupRoutes(router *gin.Engine, logger Logger) {
	// Health check endpoints
	router.GET("/health", healthCheck)
	router.GET("/ready", readinessCheck)
	
	// API v1 routes
	v1 := router.Group("/api/v1")
	{
		v1.GET("/status", getStatus)
		v1.GET("/info", getInfo)
	}
	
	// Metrics endpoint (Prometheus format)
	router.GET("/metrics", metricsHandler)
}

// healthCheck returns the health status of the application
func healthCheck(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"status": "healthy",
		"timestamp": time.Now().UTC(),
	})
}

// readinessCheck returns the readiness status of the application
func readinessCheck(c *gin.Context) {
	// Add database connectivity check, redis check, etc.
	c.JSON(http.StatusOK, gin.H{
		"status": "ready",
		"timestamp": time.Now().UTC(),
		"services": gin.H{
			"database": "connected", // TODO: actual check
			"redis":    "connected", // TODO: actual check
		},
	})
}

// getStatus returns basic application status
func getStatus(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"service": "dahlia",
		"version": "1.0.0",
		"uptime":  time.Since(startTime).String(),
		"status":  "running",
	})
}

// getInfo returns application information
func getInfo(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"name":        "Dahlia",
		"description": "Modern multi-language web server template",
		"version":     "1.0.0",
		"languages":   []string{"Go", "Rust", "Python"},
		"features": []string{
			"RESTful API",
			"Health checks",
			"Graceful shutdown",
			"Multi-language architecture",
			"Container ready",
		},
	})
}

// metricsHandler returns basic metrics in Prometheus format
func metricsHandler(c *gin.Context) {
	// Basic metrics - in production, use prometheus client
	uptime := time.Since(startTime).Seconds()
	metrics := fmt.Sprintf(`# HELP dahlia_uptime_seconds Uptime in seconds
# TYPE dahlia_uptime_seconds counter
dahlia_uptime_seconds %.2f
# HELP dahlia_requests_total Total requests
# TYPE dahlia_requests_total counter
dahlia_requests_total{method="GET"} 0
`, uptime)
	c.Header("Content-Type", "text/plain")
	c.String(http.StatusOK, metrics)
}

var startTime = time.Now()