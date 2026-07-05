"""Test configuration for Call Center Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "call-center-agent", "category": "Customer Service"}
