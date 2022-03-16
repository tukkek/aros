# A Rando of Sorrow

AROS is an opinionated *Castlevania: Aria of Sorrow* randomizer: instead of allowing for several options like most randomizers, it tries to deliver high-quality on a vision for a roguelite metroidvania instead. Being open-source, modifications and suggestions are very welcome - there are also multiple other traditional randomizers for the game availabe for those who would enjoy a more flexible approach instead.

**What does AROS do?**

(Keep in mind that this project is in development and these features are more of a wishlist at the moment).

- **Starts the game in a save room in any area of the castle**, vastly increasing routing opportunities,  while leaning more on Aria of Sorrow's [metroidvania gameplay](https://en.wikipedia.org/wiki/Metroidvania).
- **Has s simple meta-game** that allows you to focus on just enjoying the game: each area of the castle is guaranteed to have exactly one progression ability, so players can easily know when an area is "cleared". To accomplish this goal in a balanced manner (and to increase routing possibilities), multiple copies of some progression items can be found around the castle - finding one means no more progression items in the area.
- **Scales enemies**, according to a player's likely route throughout the castle - so that players aren't heavily penalized for starting in a late-game area or find themselves steam-rolling early areas later on.
- Aims for **longer runs**. The base game can be beat by many experienced players in around an hour, other randomizers in an hour or two. AROS runs should be a littie more involved, at two hours or more for a run.
- **Makes the game harder**. This is done by lowering the availability of items, souls and experience gain. This isn't meant to make the game ultra hard, just to balance it for players who have or will play it often.

**What does AROS not do?**

- For now, only supports the normal ending. A balanced, polished normal ending comes before the good ending.
- Similarly, for now, the Cemetery, Forbidden Zone and Chaotic Realm are not featured in the routing logic.
- AROS tries to perfect one possible vision for the game. This comes at the cost of flexibility and scope.

# Setup

1. Install [Python](https://www.python.org/downloads/windows/). Use the advanced installation mode to select a full install and also for Python to be added to your system's `PATH `.
2. Produce a ROM of the US version of *Castlevania: Aria of Sorrow* (MD5: `e7470df4d241f73060d14437011b90ce`).
3. Rename your ROM to `rom.gba` (or just `rom` if file-name extensions are hidden in your file browser).
4. Run either `aros.windows.bat` or `aros.unix.sh` if you are on an Unix system (like Linux or MacOS).
5. A new file will be created in the AROS folder, as well as a text file containing spoilers for the seed.
6. If you haven't yet, install [a GBA emulator](https://www.emulatorgames.net/emulators/gameboy-advance/).
7. Have fun!

You can also run the script in step #4, via a termainl emulator, with the `--help` flag to see more options.

# Credits

**ԠДD ЯԐSPԐҚ** for:

* Abyssonym, creator of [the original Aria of Sorrow randomizer](https://github.com/abyssonym/aos_rando/)
* LagoLunatic, creator of [the DSVania Editor](https://github.com/LagoLunatic/DSVEdit)
* Smiling Jack, (alleged) yanker of jawbones.

Zero respect for: vampires that sparkle when exposed to sunlight `¯\_(ツ)_/¯ `
