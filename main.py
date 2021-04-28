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
    subprocess.run(DanserCommand, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def ExtractImage(outputdir=str, start=str):
    FFmpegCommmand = [
        "ffmpeg", "-y",
        "-ss", start,
        "-i", "temp.mkv",
        "-vframes", "1",
        "-c:v", "libwebp",
        "-quality", "100",
        (outputdir + "_4k.webp")
    ]
    FFmpegCommmandLowRes = [
        "ffmpeg", "-y",
        "-ss", start,
        "-i", "temp.mkv",
        "-vf", "scale=960:540:flags=lanczos",
        "-vframes", "1",
        "-c:v", "libwebp",
        "-quality", "70",
        (outputdir + "_540p.webp")
    ]
    subprocess.run(FFmpegCommmand, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(FFmpegCommmandLowRes, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove("temp.mkv")


for i in GetSkins(dir=SkinDirectory)[0]:
    CurrentMap = MapList[random.randrange(len(MapList))]
    outputdir = SkinDirectory + "\\" + i + "\\"
    if not os.path.isfile(outputdir + "_4k.webp") or not os.path.isfile(outputdir + "_540p.webp"):
        print("Rendering " + i + " on " + CurrentMap[0])
        RenderVideo(skin=i, exec=DanserExec, map=CurrentMap)
        print("Generating image...")
        ExtractImage(start=CurrentMap[4], outputdir=outputdir)
    else:
        print("Skipping " + i + " as it was already generated")
