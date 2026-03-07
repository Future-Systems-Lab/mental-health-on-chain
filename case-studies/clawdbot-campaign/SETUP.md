# ClawdBot Campaign Setup Guide

## Overview
Autonomous marketing and engagement for mental-health-on-chain via clawdbot.

## Quick Start

### 1. Clone Repo
```bash
git clone https://github.com/Future-Systems-Lab/mental-health-on-chain.git
cd mental-health-on-chain/case-studies/clawdbot-campaign
```

### 2. Configure API Keys
```bash
cp .env.example .env
# Edit .env with your API keys:
# - Dev.to API key
# - Twitter/X OAuth (4 keys)
# - Discord bot token
# - GitHub PAT
# - Telegram bot token
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Campaign
```bash
python3 campaign_orchestrator.py
```

### 5. View Metrics
```bash
tail -f logs/campaign.log
cat logs/metrics.json
```

### 6. Deploy as systemd Service (Production)
```bash
sudo cp clawdbot-campaign.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable clawdbot-campaign.service
sudo systemctl start clawdbot-campaign.service
```

## Cost
**$0/month** — All APIs are free tier. Runs on existing server resources.

## Legal
- See DISCLAIMER.md (educational use only, not medical advice)
- See PRIVACY_POLICY.md (no PHI collected)

## Support
File issues at: https://github.com/Future-Systems-Lab/mental-health-on-chain/issues
