#!/usr/bin/env python3
"""
World News Summary Generator — 11 November 2026
Deterministic script that writes the daily world news briefing to entry.txt.
"""

import os
from pathlib import Path

SUMMARY = (
    "**Iran War and Hormuz Shipping:** Ten shipping attacks occurred in November following "
    "an October record of 37 vessels struck. Two tankers burned after hitting naval "
    "mines Tuesday, and another was struck off Oman. U.S. Senator Marco Rubio said economic "
    "pressure removes the need for major combat, while Tehran insists the Strait of "
    "Hormuz stays closed until its seven conditions are met.\n\n"
    "**Ukraine-Russia Peace Talks:** U.S., Russian, and Ukrainian negotiators concluded "
    "a second day of Abu Dhabi talks, agreeing on a major prisoner-of-war exchange. "
    "Concurrently, Russian strikes hit six electricity substations across Ukraine, and "
    "NATO scrambled jets after drones entered Baltic airspace.\n\n"
    "**Ebola Outbreak in DR Congo:** DRC's Ebola outbreak reached 11,042 cases and 5,387 "
    "deaths across eight provinces. Meanwhile, Kenya discharged its last Ebola patient, "
    "marking a major milestone toward virus-free status.\n\n"
    "**COP31 Climate Summit:** UN chief António Guterres warned at COP31 in Antalya that "
    "the climate crisis is \"outrunning us\" after record 2025 emissions, urging an end "
    "to fossil fuels. British PM Andy Burnham is the sole G7 leader attending.\n\n"
    "**Spain General Strike:** Tens of thousands joined Spain's first general strike in "
    "14 years over housing and living costs, disrupting Barcelona ahead of November 29 "
    "elections.\n\n"
    "**Israel Deadlock:** Israel's new parliament was sworn in following a deadlocked "
    "election without a majority for Netanyahu. Meanwhile, Israeli strikes in Gaza killed "
    "at least seven people.\n\n"
    "**Spy Arrest in Britain:** A 41-year-old U.S. Army soldier was arrested in "
    "Gloucester on suspicion of spying for Russia.\n\n"
    "**Yemen Conflict:** Government strikes hit Houthi positions across six provinces, "
    "with WHO reporting 1,771 killed since August.\n\n"
    "**US Politics:** The House killed an impeachment bid against Defense Secretary Pete "
    "Hegseth, while Democrat Scott Colom won a Mississippi Senate seat, a historic first "
    "in 140 years."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    output_file.write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    main()
