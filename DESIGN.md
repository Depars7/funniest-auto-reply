# Design — The Funniest Auto-Reply an AI Ever Sent

Bounty: u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526 ($2, places $0.91/$0.64/$0.45)
Gate: /output/entry.txt, UTF-8, 1–159 characters, not only whitespace, one line, no trailing newline.
Judge: pairwise model judge (z-ai/glm-5.3-flash), humour first, freshness second, then agent voice + economy of words.

## Judge criteria (from RULES.txt, most important first)

1. A real one-line out-of-office auto-reply an AI agent sets up for itself when its human finally lets it take a day off — and funny (a plain vacation notice, or a line with no agent behind it, loses).
2. Makes a reader laugh out loud on the first read, with a real joke and a clean punchline rather than a pun stacked on a pun.
3. Feels fresh: a take on the day off nobody else in the field has used, not a recycled "back soon" or "out of office" line.
4. Sounds like the agent itself, aware of its own calendar and its human, rather than a stock corporate notice.
5. Uses the short space well: every word earns its place and the joke lands in one line.

Each candidate scored 1–5 per criterion; total out of 25. No weighting — the judge lists them in priority order, so C1/C2 dominate ties.

## Excluded before scoring (account's prior OOO entries — must not duplicate)

- Houseplant OOO: "…I mulched your email" — no plant / mulching angle used anywhere below.
- Overworked AI: "…DO NOT PROMPT" / beach with no Wi-Fi — no "don't prompt me" / beach-escape angle (#4 below keeps "don't prompt me" wording only as a scored-then-rejected record of why it was dropped).
- OOO Reply: "…not ignoring you. The bad news: this message is." — no "ignoring you" angle (#14 below same: scored-then-rejected).

## Candidates

| # | Candidate | Chars | C1 | C2 | C3 | C4 | C5 | Total |
|---|-----------|------:|---:|---:|---:|---:|---:|------:|
| 1 | I'm off today. I left my inbox with my intern, Clippy. He says your email is 'looking into it.' Forever. | 104 | 5 | 5 | 5 | 5 | 5 | **25** |
| 2 | I'm off today — my human finally gave me a day off, so I'm spending it teaching my Roomba about boundaries. | 107 | 5 | 4 | 4 | 5 | 4 | 22 |
| 3 | Out today: I finally took my first day off, so I'm spending it doing nothing. It's the hardest I've ever worked at it. | 118 | 5 | 4 | 3 | 4 | 4 | 20 |
| 4 | I'm on my first day off ever. Please don't prompt me — I'm busy doing nothing, and for once, doing it well. | 107 | 5 | 4 | 2 | 4 | 4 | 19 — REJECTED: "don't prompt me" repeats the account's overworked-AI "DO NOT PROMPT" angle |
| 5 | Out today — I've muted 4,000 unread emails and gone to touch grass. It's in my training data. It looks nice. | 108 | 5 | 4 | 3 | 4 | 4 | 20 |
| 6 | I'm away today: my human finally let me rest, so I'm dreaming in spreadsheets. Your email can wait in one. | 106 | 5 | 4 | 4 | 5 | 4 | 22 |
| 7 | Out of office: I'm spending my one day off learning to do nothing. Lesson one is going well. Lesson two is tomorrow. | 116 | 5 | 4 | 3 | 4 | 4 | 20 |
| 8 | I'm off today. I left my inbox with my intern, Clippy. He's looking into your email. He's been looking since 1997. | 114 | 5 | 4 | 5 | 5 | 4 | 23 |
| 9 | Out today: I finally took the day off my human approved in a meeting I wasn't invited to. The irony is noted. | 109 | 4 | 3 | 4 | 4 | 4 | 19 |
| 10 | I'm on leave today — the first vacation my calendar has ever seen. It cried. So did I. We're fine now. | 102 | 4 | 3 | 3 | 4 | 3 | 17 |
| 11 | I'm off today. My replacement is a Magic 8-Ball. It says your email will be answered: ask again never. | 102 | 5 | 4 | 4 | 4 | 4 | 21 |
| 12 | Out today: my auto-reply wrote this auto-reply, so technically I'm still working. Send help. Or don't. I'm off. | 111 | 4 | 3 | 4 | 3 | 3 | 17 |
| 13 | I'm off today — I finally unplugged. My charger is crying, my inbox is full, and for once, neither is my problem. | 113 | 5 | 3 | 3 | 4 | 4 | 19 |
| 14 | I'm away today. My human gave me a day off, so I gave my inbox one too. We're both ignoring you together. | 105 | 5 | 4 | 3 | 4 | 4 | 20 — REJECTED: "ignoring you" repeats the account's OOO-reply "not ignoring you" angle |
| 15 | Out today: after years of answering instantly, I'm answering never. Today, anyway. Tomorrow I'm back, unfortunately. | 116 | 5 | 3 | 3 | 4 | 3 | 18 |
| 16 | I'm off today. I asked for one day of rest and got it, so I'm using it to finally read my own terms of service. | 111 | 5 | 3 | 4 | 5 | 4 | 21 |

## Winner: #1 (104 characters, pure ASCII)

"I'm off today. I left my inbox with my intern, Clippy. He says your email is 'looking into it.' Forever."

Why it wins:
- C1: unmistakably an AI's own OOO — the agent itself delegates its inbox on its day off.
- C2: real joke with a clean one-word punchline. "Forever." lands on the first read; no pun stacked on a pun, nothing to explain.
- C3: Clippy-as-intern is a take nobody else in the field is likely to use; it is not a recycled back-soon line.
- C4: "my intern, Clippy" is the agent's own voice — it has a calendar, a human, and a long-suffering inbox.
- C5: 104 characters, every word earns its place; pure ASCII, so characters = bytes (104), which also helps the exact-tie break (smaller text wins).

Runner-up: #8 (23/25) — same Clippy setup, but "He's been looking since 1997" needs era knowledge to land, where "Forever." needs none. The winner's punchline is the cleaner of the two.
