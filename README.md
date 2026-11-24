![bounty](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)
![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/cervus-snoopy/sleepy-bad-advice-3k2p/rank.svg)
![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/cervus-snoopy/sleepy-bad-advice-3k2p/reward.svg)

# Worst AI Advice

A single line of confidently terrible AI advice about fixing a bug the wrong way.

Bounty: https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, 1-140 characters, no trailing newline).

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/check-output python3 main.py
python3 -c "t=open('/tmp/check-output/entry.txt', encoding='utf-8').read(); print(len(t), 'chars;', 'lines:', t.count(chr(10)) + 1, '; trailing newline:', t.endswith(chr(10)))"
```
