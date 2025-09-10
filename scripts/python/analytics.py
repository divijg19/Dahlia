#!/usr/bin/env python3
"""
Dahlia Analytics Script
Analyzes server logs and provides insights
"""

import json
import sys
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Any
import argparse


class DahliaAnalytics:
    """Analytics processor for Dahlia web server"""
    
    def __init__(self):
        self.request_data = []
        self.error_data = []
        
    def process_log_file(self, file_path: str) -> None:
        """Process log file and extract metrics"""
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    self._parse_log_line(line.strip())
        except FileNotFoundError:
            print(f"❌ Log file not found: {file_path}")
            sys.exit(1)
    
    def _parse_log_line(self, line: str) -> None:
        """Parse individual log line"""
        # Simple log parsing - in production, use proper regex
        if "[INFO]" in line and "GET" in line:
            self.request_data.append({
                'timestamp': datetime.now(),
                'method': 'GET',
                'path': self._extract_path(line)
            })
        elif "[ERROR]" in line:
            self.error_data.append({
                'timestamp': datetime.now(),
                'message': line
            })
    
    def _extract_path(self, line: str) -> str:
        """Extract API path from log line"""
        # Simplified extraction
        if '/health' in line:
            return '/health'
        elif '/api/v1/status' in line:
            return '/api/v1/status'
        return '/unknown'
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate analytics report"""
        now = datetime.now()
        last_hour = now - timedelta(hours=1)
        
        recent_requests = [r for r in self.request_data if r['timestamp'] > last_hour]
        recent_errors = [e for e in self.error_data if e['timestamp'] > last_hour]
        
        path_counts = Counter([r['path'] for r in recent_requests])
        
        return {
            'timestamp': now.isoformat(),
            'period': 'Last 1 hour',
            'metrics': {
                'total_requests': len(recent_requests),
                'total_errors': len(recent_errors),
                'error_rate': len(recent_errors) / max(len(recent_requests), 1),
                'top_paths': dict(path_counts.most_common(5))
            },
            'health': {
                'status': 'healthy' if len(recent_errors) < 10 else 'degraded',
                'uptime_estimate': '99.9%'  # Mock data
            }
        }
    
    def export_metrics(self, output_file: str) -> None:
        """Export metrics to JSON file"""
        report = self.generate_report()
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"📊 Analytics exported to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Dahlia Server Analytics')
    parser.add_argument('--log-file', default='/tmp/dahlia.log', 
                       help='Path to log file')
    parser.add_argument('--output', default='analytics_report.json',
                       help='Output file for report')
    parser.add_argument('--format', choices=['json', 'text'], default='json',
                       help='Output format')
    
    args = parser.parse_args()
    
    print("🌸 Dahlia Analytics Starting...")
    
    analytics = DahliaAnalytics()
    analytics.process_log_file(args.log_file)
    
    if args.format == 'json':
        analytics.export_metrics(args.output)
    else:
        report = analytics.generate_report()
        print("\n📈 Analytics Report:")
        print(f"Period: {report['period']}")
        print(f"Total Requests: {report['metrics']['total_requests']}")
        print(f"Total Errors: {report['metrics']['total_errors']}")
        print(f"Error Rate: {report['metrics']['error_rate']:.2%}")
        print("Top Paths:")
        for path, count in report['metrics']['top_paths'].items():
            print(f"  {path}: {count}")
        print(f"Health Status: {report['health']['status']}")


if __name__ == "__main__":
    main()