# osuskinthumbnailcreator
A thumbnail creator for osu! skins made possible with Danser and ffmpeg

You will need:
 - [Danser](https://github.com/Wieku/danser-go) 0.5.1 or newer
 - [FFmpeg](https://github.com/FFmpeg/FFmpeg) with libwebp

First, change skin and song path in `settings.json` and in `main.py` itself

Put the maps you want to create thumbnails with into list.csv in this format:

`Map name,MD5 hash,Time of screenshot`

For example:

`Banana Street [Vanilla's Banana],6BB216A240A977F7218BD80D72F15B7D,45.2`

The maps will be randomly chosen for each screenshot.

Map name can be anything, currently it is only used for log messages and keeping track of what is what in the map .csv.

Finished screenshots will be put in the skin folder as `_4k.webp` and `_540p.webp`
