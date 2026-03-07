#!/usr/bin/env python3
# Rights Reserved, Unlicensed
# GitHub Metrics Handler - mental-health-on-chain

import os
import requests
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class GitHubMetrics:
    def __init__(self):
        self.token = os.getenv('GITHUB_PAT')
        self.username = os.getenv('GITHUB_USERNAME')
        self.repo = 'mental-health-on-chain'
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.api_url = f'https://api.github.com/repos/{self.username}/{self.repo}'
    
    def get_repo_stats(self):
        """Fetch repo stars, forks, watchers"""
        try:
            response = requests.get(self.api_url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                stats = {
                    'stars': data.get('stargazers_count', 0),
                    'forks': data.get('forks_count', 0),
                    'watchers': data.get('watchers_count', 0),
                    'issues': data.get('open_issues_count', 0),
                    'last_update': datetime.now().isoformat()
                }
                logger.info(f"GitHub Stats: {stats}")
                return stats
            else:
                logger.error(f"GitHub API error: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"GitHub fetch failed: {e}")
            return None
    
    def save_stats(self):
        """Save metrics to JSON"""
        stats = self.get_repo_stats()
        if stats:
            with open('/opt/clawdbot/logs/github_metrics.json', 'w') as f:
                json.dump(stats, f, indent=2)
            return stats
        return None

if __name__ == "__main__":
    gh = GitHubMetrics()
    gh.save_stats()
