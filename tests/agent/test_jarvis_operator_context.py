"""Regression checks for the JARVIS project-context contract.

These tests check that the project guidance is discoverable and retains critical
interaction and safety requirements. They do not prove a running gateway has
loaded the context or that messaging integrations work end to end.
"""
from pathlib import Path

from agent.prompt_builder import _find_hermes_md


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_jarvis_context_is_discoverable_from_repository_root():
    context_path = _find_hermes_md(REPO_ROOT)
    assert context_path is not None
    assert context_path.name.lower() == ".hermes.md"


def test_jarvis_context_requires_curiosity_without_engagement_bait():
    content = (REPO_ROOT / ".hermes.md").read_text(encoding="utf-8")
    assert "Be a thoughtful, proactive operator" in content
    assert "Challenge assumptions respectfully" in content
    assert "Never invent urgency" in content
    assert "not as a mandatory question at the end of every response" in content


def test_jarvis_context_preserves_channels_and_safety_boundaries():
    content = (REPO_ROOT / ".hermes.md").read_text(encoding="utf-8")
    for channel in ("Telegram", "Discord", "WhatsApp"):
        assert channel in content
    assert "CoinSwitch read-only" in content
    assert "Never change or delete Mizan V1/V2 resources" in content
    assert "No paid services" in content
    assert "deny unknown users by default" in content
