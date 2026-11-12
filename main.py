#!/usr/bin/env python3
"""
News Summary Generator for make.fun bounty (news-summary-01).
Writes the verified 11 November 2026 world news summary to entry.txt in $MAKEFUN_OUTPUT_DIR.
"""

import os
from pathlib import Path

SUMMARY = (
    "**Iran (Reuters):** Oil rose 1% after Iran said no enriched uranium would leave the country; 37 ships were attacked in October, two tankers hit mines.\n\n"
    "**Ukraine (Reuters):** Russia and Ukraine agreed in principle to a major prisoner exchange after two days of US-mediated talks in Abu Dhabi.\n\n"
    "**DRC Ebola (Al Jazeera):** Cases passed 11,000 — 11,042 confirmed, 5,387 dead — from the Bundibugyo strain in eight provinces, the DRC's deadliest outbreak.\n\n"
    "**Kenya (Reuters):** Kenya discharged its last Ebola patient, starting a 42-day countdown to being declared free of the disease.\n\n"
    "**COP31 (Al Jazeera):** UN chief Guterres told leaders in Antalya the climate crisis is \"outrunning us\" after record 2025 emissions.\n\n"
    "**Israel (Deutsche Welle):** The new Knesset met after the deadlocked October 27 vote; Netanyahu's bloc holds 53 seats, Eisenkot's 48.\n\n"
    "**Gaza (Al Jazeera):** Israeli strikes hit a tent camp in Gaza, killing five, as the UN appealed for tents for people facing floods.\n\n"
    "**Spain (Reuters):** Four million workers joined Spain's first general strike in 14 years over housing, before the November 29 election.\n\n"
    "**Spy arrest (CNN):** A 41-year-old US soldier was arrested near Gloucester on suspicion of spying for Russia, while serving with NATO.\n\n"
    "**Yemen (Al Jazeera):** Government forces said 190 Houthi fighters were killed or wounded in six provinces; the WHO counts 1,771 killed since August.\n\n"
    "**Hegseth (Reuters):** The House voted 211-204 to send the Hegseth impeachment bid to committee, effectively killing it.\n\n"
    "**Mississippi (AP):** Democrat Scott Colom won the Mississippi Senate seat as Cindy Hyde-Smith conceded, the first Democratic win since 1982.\n\n"
    "**Iran operatives (NPR):** US prosecutors indicted three men accused of being Iran-backed operatives behind nearly 20 attacks in Europe and the US.\n\n"
    "**Wall Street (AP):** Stocks rebounded as CoreWeave jumped 24.7%; the S&P 500 rose 1.3% and Europe's STOXX 600 hit a record."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    target_file = out_path / "entry.txt"
    target_file.write_text(SUMMARY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
