#!/usr/bin/env python3
"""
Dahlia Deployment Automation Script
Automates deployment processes and health checks
"""

import json
import subprocess
import time
import requests
from typing import Dict
import argparse
import sys


class DeploymentManager:
    """Manages deployment automation for Dahlia"""

    def __init__(self, config_file: str = "deployment.json"):
        self.config = self._load_config(config_file)
        self.deployment_log = []

    def _load_config(self, config_file: str) -> Dict:
        """Load deployment configuration"""
        try:
            with open(config_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Default configuration
            return {
                "environments": {
                    "development": {
                        "url": "http://localhost:8080",
                        "health_timeout": 30,
                    },
                    "staging": {
                        "url": "http://staging.example.com",
                        "health_timeout": 60,
                    },
                    "production": {
                        "url": "http://production.example.com",
                        "health_timeout": 120,
                    },
                },
                "docker": {"image_name": "dahlia", "container_name": "dahlia-app"},
            }

    def _log_action(self, action: str, status: str, details: str = "") -> None:
        """Log deployment action"""
        log_entry = {
            "timestamp": time.time(),
            "action": action,
            "status": status,
            "details": details,
        }
        self.deployment_log.append(log_entry)
        print(f"[{status}] {action}: {details}")

    def build_application(self) -> bool:
        """Build the application"""
        self._log_action("BUILD", "STARTING", "Building Go application")

        try:
            # Build Go application
            result = subprocess.run(
                ["go", "build", "-o", "bin/dahlia", "./cmd/server"],
                capture_output=True,
                text=True,
                cwd=".",
            )

            if result.returncode == 0:
                self._log_action(
                    "BUILD", "SUCCESS", "Go application built successfully"
                )
                return True
            else:
                self._log_action("BUILD", "FAILED", f"Go build failed: {result.stderr}")
                return False

        except Exception as e:
            self._log_action("BUILD", "ERROR", f"Build error: {str(e)}")
            return False

    def build_docker_image(self) -> bool:
        """Build Docker image"""
        image_name = self.config["docker"]["image_name"]
        self._log_action(
            "DOCKER_BUILD", "STARTING", f"Building Docker image: {image_name}"
        )

        try:
            result = subprocess.run(
                ["docker", "build", "-t", image_name, "."],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                self._log_action(
                    "DOCKER_BUILD", "SUCCESS", f"Docker image {image_name} built"
                )
                return True
            else:
                self._log_action(
                    "DOCKER_BUILD", "FAILED", f"Docker build failed: {result.stderr}"
                )
                return False

        except Exception as e:
            self._log_action("DOCKER_BUILD", "ERROR", f"Docker error: {str(e)}")
            return False

    def deploy_container(self, environment: str = "development") -> bool:
        """Deploy application container"""
        if environment not in self.config["environments"]:
            self._log_action("DEPLOY", "ERROR", f"Unknown environment: {environment}")
            return False

        container_name = self.config["docker"]["container_name"]
        image_name = self.config["docker"]["image_name"]

        self._log_action("DEPLOY", "STARTING", f"Deploying to {environment}")

        try:
            # Stop existing container
            subprocess.run(
                ["docker", "stop", container_name], capture_output=True, text=True
            )
            subprocess.run(
                ["docker", "rm", container_name], capture_output=True, text=True
            )

            # Run new container
            result = subprocess.run(
                [
                    "docker",
                    "run",
                    "-d",
                    "--name",
                    container_name,
                    "-p",
                    "8080:8080",
                    image_name,
                ],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                self._log_action(
                    "DEPLOY", "SUCCESS", f"Container deployed: {container_name}"
                )
                return True
            else:
                self._log_action("DEPLOY", "FAILED", f"Deploy failed: {result.stderr}")
                return False

        except Exception as e:
            self._log_action("DEPLOY", "ERROR", f"Deploy error: {str(e)}")
            return False

    def health_check(self, environment: str = "development", retries: int = 3) -> bool:
        """Perform health check on deployed application"""
        env_config = self.config["environments"].get(environment)
        if not env_config:
            self._log_action(
                "HEALTH_CHECK", "ERROR", f"Unknown environment: {environment}"
            )
            return False

        url = f"{env_config['url']}/health"
        timeout = env_config["health_timeout"]

        self._log_action("HEALTH_CHECK", "STARTING", f"Checking {url}")

        for attempt in range(retries):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("status") == "healthy":
                        self._log_action(
                            "HEALTH_CHECK", "SUCCESS", f"Application healthy at {url}"
                        )
                        return True

                self._log_action(
                    "HEALTH_CHECK",
                    "RETRY",
                    f"Attempt {attempt + 1} failed, retrying...",
                )
                time.sleep(5)

            except requests.RequestException as e:
                self._log_action("HEALTH_CHECK", "RETRY", f"Request failed: {str(e)}")
                if attempt < retries - 1:
                    time.sleep(5)

        self._log_action("HEALTH_CHECK", "FAILED", "All health checks failed")
        return False

    def full_deployment(self, environment: str = "development") -> bool:
        """Perform full deployment pipeline"""
        print(f"🚀 Starting full deployment to {environment}")

        steps = [
            ("Build Application", lambda: self.build_application()),
            ("Build Docker Image", lambda: self.build_docker_image()),
            ("Deploy Container", lambda: self.deploy_container(environment)),
            ("Health Check", lambda: self.health_check(environment)),
        ]

        for step_name, step_func in steps:
            if not step_func():
                print(f"❌ Deployment failed at step: {step_name}")
                return False

        print("✅ Deployment completed successfully!")
        return True

    def export_deployment_log(self, output_file: str) -> None:
        """Export deployment log to file"""
        with open(output_file, "w") as f:
            json.dump(self.deployment_log, f, indent=2)
        print(f"📋 Deployment log exported to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Dahlia Deployment Manager")
    parser.add_argument(
        "--action",
        choices=["build", "docker", "deploy", "health", "full"],
        default="full",
        help="Deployment action",
    )
    parser.add_argument(
        "--environment",
        choices=["development", "staging", "production"],
        default="development",
        help="Target environment",
    )
    parser.add_argument(
        "--config", default="deployment.json", help="Deployment configuration file"
    )

    args = parser.parse_args()

    print("🌸 Dahlia Deployment Manager")

    manager = DeploymentManager(args.config)

    success = False
    if args.action == "build":
        success = manager.build_application()
    elif args.action == "docker":
        success = manager.build_docker_image()
    elif args.action == "deploy":
        success = manager.deploy_container(args.environment)
    elif args.action == "health":
        success = manager.health_check(args.environment)
    elif args.action == "full":
        success = manager.full_deployment(args.environment)

    manager.export_deployment_log("deployment_log.json")

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
