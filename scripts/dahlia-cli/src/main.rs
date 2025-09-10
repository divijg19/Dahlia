use anyhow::Result;
use clap::{Parser, Subcommand};
use reqwest::Client;
use serde_json::Value;

#[derive(Parser)]
#[command(name = "dahlia")]
#[command(about = "CLI tool for Dahlia web server management")]
#[command(version = "1.0.0")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Check server health
    Health {
        #[arg(short, long, default_value = "http://localhost:8080")]
        url: String,
    },
    /// Get server status
    Status {
        #[arg(short, long, default_value = "http://localhost:8080")]
        url: String,
    },
    /// Get server information
    Info {
        #[arg(short, long, default_value = "http://localhost:8080")]
        url: String,
    },
    /// Get server metrics
    Metrics {
        #[arg(short, long, default_value = "http://localhost:8080")]
        url: String,
    },
}

#[tokio::main]
async fn main() -> Result<()> {
    let cli = Cli::parse();
    let client = Client::new();

    match cli.command {
        Commands::Health { url } => {
            let response = client.get(&format!("{}/health", url)).send().await?;
            let json: Value = response.json().await?;
            println!("🌸 Health Check:");
            println!("{}", serde_json::to_string_pretty(&json)?);
        }
        Commands::Status { url } => {
            let response = client.get(&format!("{}/api/v1/status", url)).send().await?;
            let json: Value = response.json().await?;
            println!("📊 Server Status:");
            println!("{}", serde_json::to_string_pretty(&json)?);
        }
        Commands::Info { url } => {
            let response = client.get(&format!("{}/api/v1/info", url)).send().await?;
            let json: Value = response.json().await?;
            println!("ℹ️  Server Info:");
            println!("{}", serde_json::to_string_pretty(&json)?);
        }
        Commands::Metrics { url } => {
            let response = client.get(&format!("{}/metrics", url)).send().await?;
            let text = response.text().await?;
            println!("📈 Server Metrics:");
            println!("{}", text);
        }
    }

    Ok(())
}