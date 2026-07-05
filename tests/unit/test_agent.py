"""Call Center Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_monitor_queue_metrics():
    """Test Monitor real-time call center queue metrics (wait time, abandonment, SLA)."""
    tools = AgentTools()
    result = await tools.monitor_queue_metrics(queue="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_forecast_call_volume():
    """Test Forecast call volume by hour, day, and week."""
    tools = AgentTools()
    result = await tools.forecast_call_volume(horizon_days=1, granularity="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_schedule():
    """Test Optimize agent staffing schedule based on volume forecast."""
    tools = AgentTools()
    result = await tools.optimize_schedule(period="test", constraints="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_agent_performance():
    """Test Analyze individual agent performance metrics."""
    tools = AgentTools()
    result = await tools.analyze_agent_performance(agent_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.call_center_agent_agent import CallCenterAgentAgent
    agent = CallCenterAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
