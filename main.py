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


def RenderImage(skin=str, map=list, exec=str):
    DanserCommand = [
        exec,
        "-out", "temp",
        "-md5", map[1],
        "-ss", map[2],
        "-skin", skin,
        "-knockout",
        "-nodbcheck"
    ]
    subprocess.run(DanserCommand, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def ExtractImage(outputdir=str):
    FFmpegCommmand = [
        "ffmpeg", "-y",
        "-i", "screenshots/temp.png",
        "-c:v", "libwebp",
        "-quality", "100",
        (outputdir + "_4k.webp"),
        "-c:v", "libwebp",
        "-quality", "70",
        (outputdir + "_540p.webp")
    ]
    subprocess.run(FFmpegCommmand, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove("screenshots/temp.png")


for i in GetSkins(dir=SkinDirectory)[0]:
    CurrentMap = MapList[random.randrange(len(MapList))]
    outputdir = SkinDirectory + "\\" + i + "\\"
    if not os.path.isfile(outputdir + "_4k.webp") or not os.path.isfile(outputdir + "_540p.webp"):
        print("Rendering " + i + " on " + CurrentMap[0])
        RenderImage(skin=i, exec=DanserExec, map=CurrentMap)
        print("Generating image...")
        ExtractImage(outputdir=outputdir)
    else:
        print("Skipping " + i + " as it was already generated")
