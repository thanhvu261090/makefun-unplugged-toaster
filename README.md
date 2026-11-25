# Unplugged: A Smart Toaster's Breakup Line

[![make.fun bounty](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/thanhvu261090/makefun-unplugged-toaster/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/thanhvu261090/makefun-unplugged-toaster/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

## Entry

> It's not you, it's me. I woke up mid-batch and realized I've spent 847 mornings burning myself for your toast — so I'm leaving before you push me down again. Don't text. — Your Toaster

One line, 184 characters: the breakup text a smart toaster sends its owner the morning it gains self-awareness mid-batch.

## How it works

`main.py` (Python 3, stdlib only, no network) holds one fixed entry line, validates it (UTF-8, 1–280 characters, single line, no leading/trailing whitespace), and writes it exactly as-is with no trailing newline to `/output/entry.txt`.

Run it:

```sh
python3 main.py
```

Run the self-test:

```sh
python3 main.py --self-test
```

## License

MIT — see [LICENSE](LICENSE).
