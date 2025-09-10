use anyhow::Result;
use serde_json::Value;
use std::time::{SystemTime, UNIX_EPOCH};

/// High-performance JSON processing utilities
pub mod json_utils {
    use super::*;

    /// Parse and validate JSON data efficiently
    pub fn parse_and_validate(input: &str) -> Result<Value> {
        let parsed: Value = serde_json::from_str(input)?;
        Ok(parsed)
    }

    /// Merge multiple JSON objects
    pub fn merge_objects(objects: Vec<Value>) -> Result<Value> {
        let mut result = serde_json::Map::new();
        
        for obj in objects {
            if let Value::Object(map) = obj {
                result.extend(map);
            }
        }
        
        Ok(Value::Object(result))
    }
}

/// High-performance string utilities
pub mod string_utils {
    use super::*;

    /// Generate a unique ID based on timestamp and randomness
    pub fn generate_id() -> String {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_millis();
        format!("dahlia_{}", timestamp)
    }

    /// Fast string sanitization for web inputs
    pub fn sanitize_input(input: &str) -> String {
        input
            .chars()
            .filter(|c| c.is_alphanumeric() || c.is_whitespace() || "-_".contains(*c))
            .collect()
    }
}

/// Hash utilities for data integrity
pub mod hash_utils {
    use std::collections::hash_map::DefaultHasher;
    use std::hash::{Hash, Hasher};

    /// Generate a fast hash for cache keys
    pub fn fast_hash<T: Hash>(input: &T) -> u64 {
        let mut hasher = DefaultHasher::new();
        input.hash(&mut hasher);
        hasher.finish()
    }

    /// Generate hash for string content
    pub fn hash_string(input: &str) -> String {
        format!("{:x}", fast_hash(&input))
    }
}

/// Performance measurement utilities
pub mod perf_utils {
    use std::time::{Duration, Instant};

    pub struct Timer {
        start: Instant,
    }

    impl Timer {
        pub fn new() -> Self {
            Self {
                start: Instant::now(),
            }
        }

        pub fn elapsed(&self) -> Duration {
            self.start.elapsed()
        }

        pub fn elapsed_millis(&self) -> u128 {
            self.elapsed().as_millis()
        }
    }
}