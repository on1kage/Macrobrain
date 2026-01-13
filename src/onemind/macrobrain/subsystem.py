from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from onemind.kernel.core import KERNEL


@dataclass
class MacrobrainSubsystem:
    """
    FSM/KERNEL-facing adapter for Macrobrain.

    Minimal, fail-closed wiring:
    - describe(): deterministic metadata
    - execute(): NotImplementedError until explicitly wired
    - register_with_kernel(): registers singleton instance in KERNEL.subsystems
    """
    name: str = "macrobrain"
    version: str = "0.1"

    def describe(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "capabilities": ["macro_regime", "rates", "inflation", "growth", "stress"],
        }

    def execute(self, ctx: Any) -> Any:
        raise NotImplementedError("macrobrain.execute is not wired yet")


def register_with_kernel() -> MacrobrainSubsystem:
    sub = MacrobrainSubsystem()
    if sub.name not in KERNEL.subsystems:
        KERNEL.subsystems[sub.name] = sub
    return KERNEL.subsystems[sub.name]
