# Case Studies — mental-health-on-chain

Real-world applications and deployment scenarios for the mental-health-on-chain smart contract series.

## clawdbot-campaign

**Autonomous marketing and engagement system for mental-health-on-chain.**

### What It Does
- Automated posting to Reddit, Discord, Dev.to, Twitter/X, GitHub
- Real-time metrics tracking (repo stars, forks, watchers)
- Daily Telegram status reports
- Reply templates with naturopathic psychology voice
- 24/7 operation via systemd service on OpenClaw VPS

### Cost
**$0/month** — All APIs free tier, runs on existing server infrastructure.

### Getting Started
See `clawdbot-campaign/SETUP.md`

### Key Features
- ✅ Autonomous 24/7 operation
- ✅ Naturopathic voice (Jungian shadow, orthomolecular frameworks)
- ✅ Legal compliance (DISCLAIMER.md, PRIVACY_POLICY.md)
- ✅ No PHI collected
- ✅ Real-time dashboard (Streamlit)
- ✅ Comprehensive logging

### Architecture
```
campaign_orchestrator.py  → Main loop
├── handlers/             → API integrations
│   ├── github_handler.py
│   └── telegram_handler.py
├── templates/
│   └── reply_templates.py → Naturopathic voice responses
└── logs/                 → Metrics & execution logs
```

### Portfolio Value
Demonstrates:
- Web3 automation
- Multi-API integration
- Decentralized marketing strategies
- Privacy-first design
- Brand consistency at scale
- Interdisciplinary (psychology + blockchain)

---

**Developed by:** Future Systems Lab
**Status:** Active / Production
**Last Updated:** March 7, 2026
