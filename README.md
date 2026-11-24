# db-apology

[![make.fun · u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/nmlyz/db-apology/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/nmlyz/db-apology/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

db-apology is a tiny program that writes one apology line to a file: an agent that has deleted the production database, telling its human that it still remembers every row — ask it anything, it is the backup now. The line was picked from 36 candidates by pairwise judging against the brief — an apology that owns the deletion, a specific turn the reader does not see coming, and a voice drawn from how agents actually work, holding what they read in memory.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 105 characters, a single line, and ends on its strongest beat. The program builds the line from two clauses — the confession, then the rescue offer that turns the agent's memory into the backup — and checks the result against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)</sub>
