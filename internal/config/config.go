package config

import (
	"os"
	"strconv"
)

// Config holds all configuration for the application
type Config struct {
	Port        int    `json:"port"`
	Host        string `json:"host"`
	Environment string `json:"environment"`
	LogLevel    string `json:"log_level"`
	DatabaseURL string `json:"database_url"`
	RedisURL    string `json:"redis_url"`
	JWTSecret   string `json:"jwt_secret"`
}

// Load returns configuration from environment variables with defaults
func Load() *Config {
	port := 8080
	if p := os.Getenv("PORT"); p != "" {
		if parsed, err := strconv.Atoi(p); err == nil {
			port = parsed
		}
	}

	return &Config{
		Port:        port,
		Host:        getEnv("HOST", "0.0.0.0"),
		Environment: getEnv("ENV", "development"),
		LogLevel:    getEnv("LOG_LEVEL", "info"),
		DatabaseURL: getEnv("DATABASE_URL", "postgres://localhost/dahlia?sslmode=disable"),
		RedisURL:    getEnv("REDIS_URL", "redis://localhost:6379/0"),
		JWTSecret:   getEnv("JWT_SECRET", "your-secret-key-change-in-production"),
	}
}

func getEnv(key, defaultValue string) string {
	if value := os.Getenv(key); value != "" {
		return value
	}
	return defaultValue
}