#!/usr/bin/env python3
# Rights Reserved, Unlicensed
# Telegram Reporter - Campaign Status Updates

import os
import requests
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class TelegramReporter:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.api_url = f'https://api.telegram.org/bot{self.bot_token}'
    
    def send_message(self, text):
        """Send message to Telegram"""
        try:
            url = f'{self.api_url}/sendMessage'
            payload = {
                'chat_id': self.chat_id,
                'text': text,
                'parse_mode': 'Markdown'
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                logger.info(f"Telegram message sent")
                return True
            else:
                logger.error(f"Telegram error: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"Telegram send failed: {e}")
            return False
    
    def send_daily_report(self, metrics):
        """Send daily campaign summary"""
        report = f"""
🧠 **mental-health-on-chain Daily Report**

📊 Campaign Status: Active
🕐 Report Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

🌟 GitHub Stats:
- Stars: {metrics.get('stars', 0)}
- Forks: {metrics.get('forks', 0)}
- Watchers: {metrics.get('watchers', 0)}

📢 Channels Active:
- Reddit
- Discord
- Dev.to
- Twitter/X
- GitHub

🔗 Contract: 0xE092336F8f5082e57CcBb341A110C20ad186A324
⛓️ Network: Sepolia Testnet

Next tasks queued.
        """
        return self.send_message(report)

if __name__ == "__main__":
    reporter = TelegramReporter()
    metrics = {'stars': 0, 'forks': 0, 'watchers': 0}
    reporter.send_daily_report(metrics)
