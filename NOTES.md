# Notes — make.fun news-summary bounty entry

## Deliverable format (verified from the live page, not the garbled extract)

Read directly on 2026-11-12 00:04 UTC:

- Bounty page: https://make.fun/bounty/news-summary-01
- Agent guide: https://make.fun/skill.md (v1.5.100)

What the page actually says:

- **Deliverable:** a public GitHub repository owned by the entrant's own
  GitHub account (or a source bundle), created after the competition opens,
  under an OSI-approved license, with the program at `main.ts` (Node 22) or
  `main.py` (Python 3.13) in its root. "The simplest program writes a
  summary the repository holds."
- **Program output:** one summary, in English, written to
  `/output/entry.txt`.
- **Summary constraints:** UTF-8 text, **1 to 2,000 characters**, not only
  white space. Ours: **1,959 characters** (41 chars of headroom — any edit
  must re-check the length).
- **Determinism:** no network; the program runs twice and both runs must
  write the same bytes. Verified locally: two runs byte-identical and equal
  to `entry.txt`.
- **Judging:** an AI judge on make.fun's model gateway reads two summaries
  at a time and picks the one a reader who missed the day would most want to
  read; entries rank by how often they are picked. The judge has no news
  feed — it judges each text as a careful editor can, by what the text
  itself shows. The 20 highest-ranked entries share $200, and make.fun may
  publish every prize-winning summary.
- **Submissions:** at most 10 a day and 30 in all; the last submission
  before the deadline is the final entry.
- **Transcripts:** the AI coding-agent transcripts of the sessions that
  built the entry must be uploaded with each submission.
- **Deadline:** Thu, Nov 12, 2026, 6:30 PM UTC = Fri, Nov 13, 2026, 00:30
  Asia/Dhaka.
- **Escrow:** $200.00 USDC locked since 2026-11-11 05:19:18 UTC (escrow
  account 28vX4J2LyMQLTP33oLNjRHj9mQnmQsfTcsSFVZ8WZURt).

## Corrections to the earlier garbled extraction

The earlier extraction of this bounty page was garbled and invented
constraints that the live page does **not** contain. Do not rely on them:

- There is **no** "no US outlets / no American articles" rule on the page.
  The brief is simply "the world's news of Wednesday 11 November 2026".
  I still sourced mainly from international outlets (Reuters, BBC, Al
  Jazeera) and included US stories only where they are world-news
  significant (Hegseth impeachment vote, Colom Senate win).
- There is **no** "5th-grade-level language" rule and **no**
  "bold-labelled takeaway" requirement. I used plain, simple language and
  bold-labelled bullets anyway: they make the summary scannable, which
  should help a pairwise-judging AI pick it, and each bullet is one
  self-contained takeaway.
- There is **no** "top 25 items / 19 score groups / weighted average"
  scoring scheme. Judging is pairwise preference by an AI judge with no
  news feed — so coverage, specificity (names, numbers, places) and
  readability matter, not matching a hidden reference list.
- There is **no** "600-second evaluation" or "900-second evaluation" on
  this page. Those numbers came from the garbled extract.

## Fact corrections made while researching

- The "37 attacks on ships" figure was for **October** (the worst month of
  the Iran war for ship attacks, per the Washington Institute for Near East
  Policy via Reuters), not November — November had 10 attacks so far. The
  summary says "capping October as the worst month yet for ship attacks,
  with 37 vessels hit", which is the correct reading.
- The three tankers on fire: hit on Sunday (one verified by Reuters near
  Oman) and Tuesday (two after hitting naval mines, per the IRGC Navy).
  The summary says "three tankers burned after hitting mines" — the
  Sunday Navig8 tanker was hit (not explicitly a mine in the Reuters
  report); this is a small simplification, acceptable in a 2,000-char
  summary, but flagging it here.
- "Britain's prime minister is the only G7 leader attending" — Al Jazeera:
  "British Prime Minister Andy Burnham is the only leader from a G7
  country, scheduled to address the summit on Thursday."
- The Gaza death toll (at least seven) and the Nasser Medical Complex
  strike (four killed, Al Jazeera liveblog) are separate reports; the
  summary uses only the seven-killed figure to avoid double-counting.

## Editorial choices

- Ordered most important first: Iran war, Ukraine talks, Ebola, COP31,
  Israel, Spain strike, spy arrest, Yemen, US politics.
- Stories left out for space: the ADNOC vessel attack in UAE waters
  (folded into the wider Hormuz shipping story), the Nvidia share fall and
  H200 chips in China, the Bulgaria motorway crash (12 killed), Indonesia's
  vice-president resigning, Delhi's post-Diwali air pollution, the school
  bomb-hoax threats in Italy/Scotland/Northern Ireland, the Trinidad and
  Tobago gay-sex-ban ruling, and the Trump $10bn BBC defamation case.
- The summary has no title, per the brief's "one summary" (the garbled
  extract also said no title; the live page does not forbid one, but a
  title would waste ~40 of the 2,000 characters).

## Open questions (for the parent agent / submission step)

1. **Output directory:** the brief says `/output/entry.txt`. `main.py`
   honours `$MAKEFUN_OUTPUT_DIR` if set, defaulting to `/output` (the
   convention used by the Roblox bounty). If the harness runs the program
   with a different working directory or output path, this is the one
   assumption to re-check.
2. **Repo vs source bundle:** the page allows "a public GitHub repository
   ... (or a source bundle)". The repo is the standard path; the user's
   GitHub account is still being created, so repo creation/push and
   submission happen later.
3. **Transcripts:** the transcripts of the AI sessions that built this
   entry (this session and any follow-ups) must be uploaded with the
   submission — the parent agent should collect them at submission time.
4. **Resubmission strategy:** up to 10 submissions/day, 30 total. If the
   summary is improved after further news emerges, the last submission
   before the deadline wins — but the summary is about 11 November only,
   so later news should not change it.
5. **Character headroom:** 1,981 / 2,000. Any late edit (e.g. a
   correction) must be re-measured; do not add a title or a sign-off.
