# Call Center Agent

[![CI](https://github.com/kogunlowo123/call-center-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/call-center-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Customer Service | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Call center analytics agent that monitors queue metrics, forecasts call volumes, optimizes staffing schedules, tracks agent performance, and identifies training opportunities from call analysis.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `monitor_queue_metrics` | Monitor real-time call center queue metrics (wait time, abandonment, SLA) |
| `forecast_call_volume` | Forecast call volume by hour, day, and week |
| `optimize_schedule` | Optimize agent staffing schedule based on volume forecast |
| `analyze_agent_performance` | Analyze individual agent performance metrics |
| `identify_training_needs` | Identify training opportunities from call quality analysis |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/call-center/analyze` | Run analysis |
| `POST` | `/api/v1/call-center/execute` | Execute action |
| `GET` | `/api/v1/call-center/metrics` | Get metrics |
| `PUT` | `/api/v1/call-center/configure` | Update configuration |
| `POST` | `/api/v1/call-center/report` | Generate report |

## Features

- Call
- Center
- Analytics
- Automation

## Integrations

- Zendesk
- Intercom
- Salesforce Service
- Freshdesk
- Hubspot Service

## Architecture

```
call-center-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── call_center_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Customer Service Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
