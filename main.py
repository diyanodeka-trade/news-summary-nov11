import os
from pathlib import Path

NEWS = """**Iran (Reuters):** Oil rose as Iran said no uranium would leave; 37 ships hit.

**Ukraine (Reuters):** Russia and Ukraine agreed to a prisoner swap after talks in Abu Dhabi.

**Ebola (Al Jazeera):** 11,042 cases, 5,387 dead; Bundibugyo strain, deadliest outbreak.

**Kenya (Reuters):** Kenya's last Ebola patient discharged, starting a 42-day countdown.

**COP31 (Al Jazeera):** Guterres told Antalya climate crisis is "outrunning us" after record emissions.

**Israel (DW):** The Knesset met after the Oct 27 vote; Netanyahu has 53, Eisenkot 48.

**Gaza (Al Jazeera):** Strikes hit a tent camp, killing five, as the UN appealed for tents.

**Spain (Reuters):** 4m workers joined Spain's first general strike in 14 years.

**Spy arrest (CNN):** A 41-year-old soldier was arrested near Gloucester for spying for Russia with NATO.

**Yemen (Al Jazeera):** 190 Houthis were killed or wounded in six provinces; WHO counts 1,771 dead since August.

**Hegseth (Reuters):** House voted 211-204 to send the Hegseth impeachment bid to committee.

**Mississippi (AP):** Colom won the Senate seat as Hyde-Smith conceded, first Democratic win since 1982.

**Iran operatives (NPR):** US indicted three Iran-backed operatives behind nearly 20 attacks in Europe and the US.

**Wall Street (AP):** Stocks rebounded as CoreWeave jumped 24.7%; the S&P rose 1.3%, STOXX 600 hit a record.

**Nvidia (Reuters):** Huang was engulfed in a chip-spy scandal as his affair helped ship $7.5bn of chips to China.

**China-US (Reuters):** Wang Yi called Rubio talks "positive and constructive" ahead of APEC in Shenzhen.

**Indonesia (Reuters):** MSCI will drop Barito Pacific as Jakarta fell over 40% this year, the world's worst.

**Fed (Reuters):** Waller put a 50bp Dec hike on the table, lifting the dollar to a 19-month high.

**Sudan (G7):** G7 demanded an end to outside support for Sudan's forces as famine risk grows in Darfur.

**Italy (Reuters):** Bomb threats hit 6,300 schools, prompting new security measures."""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    p = Path(out_dir) / "entry.txt"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(NEWS, encoding="utf-8")

if __name__ == "__main__":
    main()
