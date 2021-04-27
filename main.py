# Imports
import os
import random
import subprocess
import csv

# Variables
SkinDirectory = "C:\\Users\\adame\\AppData\\Local\\osu!\\Skins"
DanserExec = "danser"
MapList = []

# Loading maps from CSV
for i in csv.reader(open("list.csv")):
    MapList.append(i)


# Skin directory walking
def GetSkins(dir=str):
    directories = []
    for root, dirs, files in os.walk(dir, topdown=True):
        directories.append(dirs)
    return directories


def RenderVideo(skin=str, map=list, exec=str):
    DanserCommand = [
        exec,
        "-out", "temp",
        "-md5", map[1],
        "-start", map[2],
        "-end", map[3],
        "-skin", skin,
        "-knockout"
    ]
    subprocess.run(DanserCommand)


def ExtractImage(outputfile=str, start=str):
    FFmpegCommmand = [
        "ffmpeg",
        "-ss", start,
        "-i", "temp.mkv",
        "-vframes", "1",
        "-c:v", "libwebp",
        "-quality", "100",
        outputfile
    ]
    subprocess.run(FFmpegCommmand)
    os.remove("temp.mkv")


for i in GetSkins(dir=SkinDirectory)[0]:
    CurrentMap = MapList[random.randrange(len(MapList))]
    outputfile = str("output\\" + i + " (played on " + CurrentMap[0] + ").webp").replace("-", "")
    RenderVideo(skin=i, exec=DanserExec, map=CurrentMap)
    ExtractImage(start=CurrentMap[4], outputfile=outputfile)
