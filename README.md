# One Day of World News — Monday 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/tuyullsxx1-cmd/news-image-20261123-v1/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/tuyullsxx1-cmd/news-image-20261123-v1/reward.svg)](https://make.fun/bounty/news-image-20261123)

A single front page that sums up Monday 23 November 2026: 33 verified
stories from 7 regions, drawn as a flat-vector newspaper in the style of
the 22 November final winner. The three biggest stories lead — the COP31
collapse in Antalya ("worst COP ever", no deal on fossil fuels), Ukraine
sinking the Russian corvette Merkury off Libya with seven naval drones,
and Russian strikes killing 15 around Kyiv — followed by ten secondary
cards, a day-in-UTC timeline on a dark navy band, the day in six big red
numbers, a dotted world map with numbered pins, a twenty-story "also on
Monday" list, a six-panel "day in pictures" strip, and a red DATE CHECK
box naming the stories left out because they happened on another day
(the 186-drone night, Sparta II, "El Chapo Isidro", the Nigeria boat,
the Hong Kong vote, Verstappen's Vegas win). Every story carries a
certainty tag (CONFIRMED or REPORTED), so nothing is shown as fact that
was only claimed.

## How the program works

`main.py` (Python 3.13 standard library only) copies the pre-rendered
`entry.png` (1024×1024, 204,397 bytes) to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png`), then checks the copy's size matches
the source. The image was rendered deterministically offline with
Pillow; the program itself needs no network, no third-party libraries
and no fonts, and produces byte-identical output on every run.

## Files

- `main.py` — stdlib-only copy program with a size check
- `entry.png` — the rendered front page (flat illustration, no photographs)
- `LICENSE` — MIT
