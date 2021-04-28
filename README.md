# osuskinthumbnailcreator
A thumbnail creator for osu! skins made possible with Danser and ffmpeg

You will need:
 - [Danser](https://github.com/Wieku/danser-go) 0.5.0 or newer
 - [FFmpeg](https://github.com/FFmpeg/FFmpeg) with libwebp and libx264

First, change skin and song path in `settings.json`

Put the maps you want to create thumbnails with into list.csv in this format:

`Map name,MD5 hash,Start in seconds,End in seconds,ffmpeg image creation -ss`

For example:

`Banana Street [Vanilla's Banana],6BB216A240A977F7218BD80D72F15B7D,45,46,1.2`

The maps will be randomly chosen for each screenshot.

Map name can be anything, currently it is only used for log messages and keeping track of what is what in the map .csv.

Finished screenshots will be put in the skin folder as `_screenshot.webp`