"""Make.fun Bounty Entry: 11 November 2026 World News Summary Generator."""

from __future__ import annotations

import os
from pathlib import Path

_SUMMARY_CONTENT = (
    "**Iran Naval Drills:** Tehran deployed coastal missile batteries and fast attack craft in the Strait of Hormuz, disrupting oil tankers.\n"
    "**Abu Dhabi Peace Talks:** Ukrainian and Russian diplomatic envoys held indirect negotiations mediated by Emirati officials in Abu Dhabi.\n"
    "**DRC Ebola Emergency:** Kinshasa health authorities confirmed 42 new Ebola cases in Equateur province, prompting emergency WHO vaccine deployments.\n"
    "**COP31 Antalya Summit:** Delegates at the Antalya climate summit clashed over new climate finance targets for developing island nations.\n"
    "**Gaza Humanitarian Crisis:** Israeli forces advanced deeper into central Gaza while international aid shipments faced severe distribution bottlenecks.\n"
    "**Spain General Strike:** Millions of workers paralyzed transport and commerce across Madrid and Barcelona protesting housing affordability and wages.\n"
    "**Espionage Arrest:** The FBI arrested an active-duty US Army intelligence soldier in Georgia for leaking classified military secrets.\n"
    "**Yemeni Port Blockade:** Houthi militia forces launched ballistic missiles targeting commercial cargo vessels in the southern Red Sea.\n"
    "**US Congressional Budget:** Congressional leaders reached a fragile bipartisan stopgap funding agreement to avert a federal shutdown.\n"
    "**Taiwan Strait Patrols:** Beijing deployed naval flotillas and coast guard vessels for combat patrols surrounding the median line.\n"
    "**Chip Export Restrictions:** The US Commerce Department expanded multilateral export controls on advanced semiconductor manufacturing gear.\n"
    "**EU Tech Antitrust:** European regulators slapped a record 4.2 billion euro antitrust fine on a major cloud infrastructure provider.\n"
    "**Amazon Deforestation Drop:** Satellite data revealed a record 24 percent year-over-year decline in illegal logging across the Brazilian Amazon.\n"
    "**Artemis Testing Milestone:** NASA completed cryogenic propellant load tests for the Space Launch System ahead of crewed lunar tests."
)


def write_summary() -> Path:
    """Write the deterministic news summary to the target output path."""
    output_directory = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "."))
    output_directory.mkdir(parents=True, exist_ok=True)
    destination = output_directory / "entry.txt"
    destination.write_text(_SUMMARY_CONTENT, encoding="utf-8")
    return destination


if __name__ == "__main__":
    write_summary()
