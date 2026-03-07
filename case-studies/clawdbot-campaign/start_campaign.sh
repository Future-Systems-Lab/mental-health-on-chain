#!/bin/bash

# Rights Reserved, Unlicensed
# Start mental-health-on-chain Campaign

cd /opt/clawdbot

echo "Installing Python dependencies..."
pip install -q -r requirements.txt

echo ""
echo "=========================================="
echo "🧠⛓️  mental-health-on-chain Campaign"
echo "=========================================="
echo ""
echo "✅ Campaign Orchestrator: Starting"
echo "✅ Dashboard: http://localhost:8501"
echo "✅ Telegram: Connected"
echo "✅ GitHub: Tracking Future-Systems-Lab/mental-health-on-chain"
echo ""
echo "Contract: 0xE092336F8f5082e57CcBb341A110C20ad186A324"
echo "Network: Sepolia Testnet"
echo ""
echo "Starting services..."
echo ""

python campaign_orchestrator.py &
CAMPAIGN_PID=$!

streamlit run dashboard.py --server.port=8501 &
DASHBOARD_PID=$!

echo "Campaign PID: $CAMPAIGN_PID"
echo "Dashboard PID: $DASHBOARD_PID"
echo ""
echo "Press Ctrl+C to stop"

wait
