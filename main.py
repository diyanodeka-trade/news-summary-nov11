"""Entry for make.fun bounty "Write the best summary of 11 November's world news".

Writes one summary of the world's news of Wednesday 11 November 2026 to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the summary is a fixed string; no network, no randomness,
no clock. Two runs write identical bytes. Standard library only.
"""

import os

SUMMARY = '**Iran war:** Tehran said the ball is in Washington\'s court on its terms for restarting talks, and the Strait of Hormuz stays shut until they are met. Three tankers burned after hitting mines, capping October as the worst month yet for ship attacks, with 37 vessels hit.\n**Ukraine talks:** American, Russian and Ukrainian officials held a second day of peace talks in Abu Dhabi, the first three-way meeting since February, and agreed a large prisoner swap — but ended with no breakthrough as Russia kept striking Ukraine\'s power grid. NATO scrambled jets after drones strayed into Baltic airspace.\n**Ebola:** Congo confirmed 11,042 cases and 5,387 deaths in an Ebola outbreak now the second largest ever recorded. Kenya discharged its last patient, a big step toward being virus-free.\n**Climate summit:** World leaders met in Antalya for COP31, where UN chief António Guterres warned the climate crisis is "outrunning us" and 2025 emissions hit a record high. The United States skipped the talks for a second year, and Britain\'s prime minister is the only G7 leader attending.\n**Israel:** A new parliament was sworn in after a deadlocked election left Benjamin Netanyahu without a majority and no government in place. Israeli strikes killed at least seven people in Gaza.\n**Spain strike:** The country\'s first general strike in 14 years shut down transport and brought clashes in Barcelona, as unions protested housing costs and the cost of living ahead of elections on 29 November.\n**Spy arrest:** Britain arrested a 41-year-old US soldier serving with a NATO unit on suspicion of spying for Russia.\n**Yemen:** Government forces struck Houthi positions across six provinces. The WHO counts 1,771 people killed since August and more than 300,000 displaced.\n**US politics:** The House blocked an effort to impeach Defense Secretary Pete Hegseth, and Democrat Scott Colom won a Mississippi Senate seat — the first Black person from the state elected to the Senate in over 140 years.\n'

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SUMMARY)

if __name__ == "__main__":
    main()
