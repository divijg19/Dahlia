package logger

import (
	"log"
	"os"
	"strings"
)

// Logger provides structured logging capabilities
type Logger struct {
	level LogLevel
}

// LogLevel represents different log levels
type LogLevel int

const (
	DEBUG LogLevel = iota
	INFO
	ERROR
)

// New creates a new logger instance
func New(level string) *Logger {
	var logLevel LogLevel
	switch strings.ToLower(level) {
	case "debug":
		logLevel = DEBUG
	case "info":
		logLevel = INFO
	case "error":
		logLevel = ERROR
	default:
		logLevel = INFO
	}

	return &Logger{
		level: logLevel,
	}
}

// Debug logs debug messages
func (l *Logger) Debug(msg string) {
	if l.level <= DEBUG {
		log.Printf("[DEBUG] %s", msg)
	}
}

// Info logs info messages
func (l *Logger) Info(msg string) {
	if l.level <= INFO {
		log.Printf("[INFO] %s", msg)
	}
}

// Error logs error messages
func (l *Logger) Error(msg string) {
	if l.level <= ERROR {
		log.SetOutput(os.Stderr)
		log.Printf("[ERROR] %s", msg)
		log.SetOutput(os.Stdout)
	}
}