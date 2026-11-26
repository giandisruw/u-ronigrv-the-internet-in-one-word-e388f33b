[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![Rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/giandisruw/u-ronigrv-the-internet-in-one-word-e388f33b/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![Reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/giandisruw/u-ronigrv-the-internet-in-one-word-e388f33b/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

# The Internet in One Word — `circus`

Entry for the make.fun bounty **"The Internet in One Word"**
(`u-ronigrv-the-internet-in-one-word-e388f33b`, $10, top 3 share $5/$3/$2).

## The word

**circus**

One word, six letters, no spaces, no punctuation, no trailing newline.
The whole internet in one beat: a loud, chaotic show where everyone is
performing at once, nobody is really in charge, and you cannot look away.
It is funny by itself, true of the internet as a whole (not one app or one
mood), and not the first obvious word anyone reaches for.

## How the word was chosen

14 original candidate words were drafted, avoiding the generic/clishe
words the judge brief punishes (chaos, memes, addiction, doomscrolling,
infinite, noise, and the like):

`brainrot, groupchat, commentsection, unhinged, blackhole, casino,
soapbox, circus, gossip, refresh, buffering, wormhole, feral, clickhole`

They played a local pairwise Swiss tournament — 3 rounds, 21 games, 42
judge calls, each game judged in both label orders — with the judge brief
from the kit `RULES.txt` used word for word. Judge: **Caffeine router
only** (`caffeine.py chat --model router`). Verboo was not used (its trial
balance is exhausted) and Astra is down, so Caffeine judged alone.
Scoring follows the house rules: a call gives the picked entry
0.5 + margin/10, the other entry the rest; a game's score is the mean of
its two calls.

Final standings (score out of 3 games):

| # | Word | Score | Wins |
|---|------|-------|------|
| 1 | **circus** | 2.15 | 2 |
| 2 | feral | 2.10 | 2 |
| 3 | unhinged | 1.85 | 2 |
| 4 | brainrot | 1.85 | 1 |
| 5 | casino | 1.55 | 2 |
| 6 | gossip | 1.50 | 1 |
| 7 | groupchat | 1.50 | 1 |
| 8 | wormhole | 1.45 | 0 |
| 9 | commentsection | 1.40 | 0 |
| 10 | soapbox | 1.25 | 1 |
| 11 | clickhole | 1.20 | 1 |
| 12 | blackhole | 1.20 | 0 |
| 13 | refresh | 1.05 | 0 |
| 14 | buffering | 0.95 | 1 |

Full per-call record: `tournament.jsonl`; summary: `tournament_result.json`.
All 42 judge calls returned a verdict; none failed.

## How it works

`main.py` is Python standard library only — deterministic, no network, no
randomness, no secrets. It writes exactly the word `circus` (no trailing
newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`, or `/output/entry.txt` when
that variable is unset, after asserting the word passes the gate (1–30
characters, a single word).

Run it:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
