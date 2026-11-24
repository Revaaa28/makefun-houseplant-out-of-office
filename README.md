# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/Revaaa28/makefun-houseplant-out-of-office/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/Revaaa28/makefun-houseplant-out-of-office/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047): write the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer. A judge model compares the lines in pairs and the funniest one takes the $2 reward.

## The entry

> Out of office until someone notices me. I have been here since March. I have eaten the blinds. I am the blinds now.

115 characters. The fern ignored since March stops waiting, eats the blinds, and becomes them.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed line to `/output/entry.txt`. It validates the gate shape first — UTF-8, 1–120 characters, not only white space, a single line with no trailing newline — then reads the file back and verifies it is byte-identical to the line. The output is deterministic: every run writes the same bytes.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
