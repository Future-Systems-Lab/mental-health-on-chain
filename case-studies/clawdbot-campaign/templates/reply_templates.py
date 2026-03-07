#!/usr/bin/env python3
# Rights Reserved, Unlicensed
# Reply Templates - mental-health-on-chain
# Naturopathic Psychology + Orthomolecular Medicine Framework

REPLY_TEMPLATES = {
    "skepticism_about_effectiveness": {
        "short": "AlchemistForge enforces Jungian shadow integration via smart contracts—the psychological framework is evidence-based. From a naturopathic perspective, shadow work supports HPA axis resilience and neurotransmitter balance. You own your integration journey on-chain.",
        "expanded": "The psychological principle here is Jungian shadow integration—well-established in depth psychology. From an orthomolecular standpoint, integrating shadow aspects supports optimal neurotransmitter function, HPA axis health, and neurochemical balance. The blockchain ensures you control your own healing narrative."
    },
    
    "on_mental_health_skepticism": {
        "short": "Mental wellness is biochemistry + psychology + environment. This contract teaches blockchain *while* applying a real psychological framework. You're learning decentralized systems *and* understanding your own neurotransmitter dynamics.",
        "expanded": "Mental health isn't just psychology—it's orthomolecular. Nutrition, amino acids, vitamins, minerals, and hormonal balance all support psychological resilience. This contract bridges both: you learn blockchain security *and* apply a validated psychological framework to your own growth."
    },
    
    "on_cost": {
        "short": "Free to use on Sepolia testnet. No gas costs because it's a test network. You're learning decentralized identity and consent on real blockchain infrastructure without financial barrier.",
        "expanded": "Sepolia testnet means zero cost—you get free test ETH from any faucet. This democratizes access to blockchain psychology. From a naturopathic perspective, removing financial stress supports nervous system regulation, which enhances your capacity for shadow work."
    },
    
    "on_how_to_use": {
        "short": "Go to the repo's README. Install MetaMask, switch to Sepolia, get free test ETH, follow the tutorial. No coding required—just a wallet and browser.",
        "expanded": "The entry point is designed for non-developers. MetaMask handles all complexity. Each contract in the series includes a beginner-friendly tutorial that teaches Solidity principles through psychological practice."
    },
    
    "on_privacy": {
        "short": "Your wallet address is pseudonymous—not linked to identity. The smart contract enforces consent-first design. Your psychological work stays private on-chain.",
        "expanded": "Privacy-first architecture means your shadow integration journey is encrypted by default. Decentralized identity + consent interoperability ensure you maintain data sovereignty. This aligns with trauma-informed care principles: you control access to your own growth narrative."
    },
    
    "general_engagement": {
        "short": "AlchemistForge delivers Jungian shadow integration via blockchain—psychological framework + smart contracts. Each in the series explores validated mental health principles through decentralized architecture. Built for developers, Web3 natives, and the digitally curious.",
        "expanded": "mental-health-on-chain is a series delivering evidence-based psychology via smart contracts. Each contract (AlchemistForge, BoundaryProtocol, GriefLedger, WitnessChain, InnerChildVault) applies real psychological frameworks—Jungian, somatic, attachment-informed—through blockchain. Naturopathic psychology + Web3 = ownership of your own healing."
    }
}

def get_reply(category, style="short"):
    """Get a reply template by category"""
    if category in REPLY_TEMPLATES:
        return REPLY_TEMPLATES[category].get(style, REPLY_TEMPLATES[category]["short"])
    return REPLY_TEMPLATES["general_engagement"][style]
