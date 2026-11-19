# Sum up 19 November's world news in one image

Entry for make.fun bounty `news-image-20261119` ($250, ends Sat 21 Nov 2026 00:00 UTC).
`main.py` (Python 3.13, standard library only, no network) copies the
image held in this repository to `/output/entry.png`. Running it twice
writes the same bytes.

## The image

A 1024x1024 front-page collage, headed "19 NOVEMBER 2026 — THURSDAY •
THE WORLD IN ONE IMAGE", with four labelled panels:

1. **Summit in Shenzhen** — US, China and Russia meet. The first-ever
   US–China–Russia trilateral summit, held in Shenzhen on 19 November
   2026, with nuclear arms and the Ukraine war on the table.
   Sources: Associated Press via The Manila Times, "Trump meets Xi and
   Putin in China with nuclear arms and two wars on the table";
   SBS News, 19 Nov 2026.
2. **Tankers on fire** — Strait of Hormuz. Three oil tankers caught fire
   after hitting mines east of the Strait of Hormuz.
   Source: NDTV, "3 Oil Tankers Catch Fire After Hitting Mines East Of
   Strait Of Hormuz: Iran", Thursday 19 November 2026.
3. **GTA VI is out** — Vice City returns worldwide. Grand Theft Auto VI
   began its global rollout on 19 November 2026, to near-perfect reviews.
   Sources: Associated Press, "'Grand Theft Auto VI' launches worldwide
   to near-perfect reviews", 19 Nov 2026; Jagran Josh, 19 Nov 2026.
4. **Voyager 1** — One light-day from Earth. NASA's Voyager 1 probe was
   reported on 19 November 2026 to have reached one light-day from Earth.
   Sources: The Manila Times / Associated Press, 19 Nov 2026;
   Jagran Josh, 19 Nov 2026.

The image is an original AI-generated illustration with labels overlaid
in code (DejaVu Sans). The summit panel shows generic leaders at a
summit table, so its label names the countries, not individual likenesses.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see LICENSE.
