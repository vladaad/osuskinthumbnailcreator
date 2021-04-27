# osuskinthumbnailcreator
A thumbnail creator for osu! skins made possible with Danser and ffmpeg

You will need:
 - Danser 0.5.0 or newer
 - ffmpeg with libwebp and libx264

Put the maps you want to use with this (they are randomly chosen) into list.csv in this format:

Map name,MD5,Danser -start,Danser -end,ffmpeg -ss

For example:

Banana Street [Vanilla's Banana],6BB216A240A977F7218BD80D72F15B7D,45,46,1.2
