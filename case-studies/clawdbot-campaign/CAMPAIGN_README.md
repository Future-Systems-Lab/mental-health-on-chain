# mental-health-on-chain Campaign Automation

## Overview

Autonomous marketing and engagement for mental-health-on-chain smart contract series via clawdbot.

**Status:** Active
**Network:** Sepolia Testnet
**Repository:** Future-Systems-Lab/mental-health-on-chain
**Contract:** 0xE092336F8f5082e57CcBb341A110C20ad186A324

## Architecture
```
campaign_orchestrator.py     → Main scheduler
├── handlers/
│   ├── github_handler.py    → Repo metrics tracking
│   ├── telegram_handler.py  → Daily status reports
│   └── [reddit, discord, devto, twitter handlers]
├── templates/
│   └── reply_templates.py   → Naturopathic voice responses
├── dashboard.py             → Streamlit real-time metrics
└── logs/
    ├── campaign.log         → Execution logs
    ├── metrics.json         → Campaign metrics
    └── github_metrics.json  → GitHub stats
```

## Services

### Campaign Orchestrator
- Autonomous posting (Reddit, Discord, Dev.to, Twitter)
- Comment monitoring & reply
- GitHub metrics tracking
- Telegram daily updates

### Dashboard (Streamlit)
- Real-time GitHub stats (stars, forks, watchers)
- Channel status
- Campaign health metrics
- Quick links to contract & repo

### Telegram Reporter
- Daily summary (10 AM UTC)
- Campaign milestones
- Engagement alerts
- GitHub metrics snapshot

## Running Locally
```bash
cd /opt/clawdbot
pip install -r requirements.txt
python campaign_orchestrator.py
```

## Running in Docker
```bash
docker-compose up -d campaign dashboard
```

### Access Dashboard
http://localhost:8501

## Environment Variables

See `.env` file for all API keys configured.

## Replies Use Your Voice

All replies reflect naturopathic psychology + orthomolecular medicine.
See `templates/reply_templates.py`.

## DISCLAIMER

**Educational only. Not medical advice. Not a substitute for licensed professionals.**

## Metrics Tracked

- GitHub stats (stars, forks, watchers)
- Campaign channels active
- Engagement & mentions
- **No PHI. No personal health data.**

