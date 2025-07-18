{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fa022a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os\n",
    "import glob\n",
    "import subprocess\n",
    "\n",
    "def convert_vid_sleap(input_folder, vid_type):\n",
    "    \"\"\"\n",
    "    This assumes all videos are in the same folder. Converts videos to be used for sleap tracking without issues \n",
    "    i.e. an mp4 with some other specifications of this command -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23\n",
    "    saves all videos with original name plus _converted at the end. \n",
    "\n",
    "    Args (2 required, 3 total)\n",
    "        input_folder: str, where your videos exist\n",
    "        vid_type: str {'.mp4' or '.h264', whatever the original video type is}\n",
    "        output_folder: str, optional, where you would like the videos to be saved, \n",
    "            if not specified the input_folder is used\n",
    "    \"\"\"\n",
    "    if output_folder is None:\n",
    "        output_folder = input_folder\n",
    "    data_path = input_folder + '\\*'\n",
    "    videos = glob.glob(data_path)\n",
    "    video = [glob.glob(f'*{vid_type}') for video in videos]\n",
    "    commands = []\n",
    "    for video in (videos):\n",
    "        video_dir, video_name = os.path.split(video)\n",
    "        new_name = os.path.join(output_folder, video_name.replace(vid_type, '_converted.mp4'))\n",
    "        if not os.path.exists(new_name):\n",
    "            command =  f'ffmpeg -y -i \"{video}\" -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23 \"{new_name}\"' \n",
    "            commands.append(command)\n",
    "    i = 0\n",
    "    for command in commands:\n",
    "       subprocess.Popen(command, shell=True).wait()\n",
    "       i +=1\n",
    "       print(i, 'out of', len(commands), 'videos converted')\n",
    "\n",
    "def convert_h264_trodes(input_folder, vid_type = None):\n",
    "    \"\"\"\n",
    "    This assumes all videos are in .rec folders (typical trodes output folder structure).\n",
    "    Converts videos to be used for sleap tracking without issues \n",
    "    i.e. an mp4 with some other specifications of this command -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23\n",
    "    saves all videos with original name plus _converted at the end and saved in their original .rec folder. \n",
    "\n",
    "    Args (1 required, 2 total)\n",
    "        input_folder: str, where your videos exist\n",
    "        vid_type: str, optional, {'.mp4' or '.h264', whatever the original video type is}\n",
    "            if not specified, .h264 files are assumed\n",
    "    \"\"\"\n",
    "    if vid_type is None:\n",
    "        vid_type = '.h264'\n",
    "    rec_folders = glob.glob(os.path.join(input_folder, '*.rec'))\n",
    "    commands = []\n",
    "    for rec_folder in rec_folders:\n",
    "        videos = glob.glob(os.path.join(rec_folder, f'*{vid_type}'))\n",
    "        for video in (videos):\n",
    "            video_dir, video_name = os.path.split(video)\n",
    "            new_name = os.path.join(video_dir, video_name.replace(vid_type, '_converted.mp4'))\n",
    "            if not os.path.exists(new_name):\n",
    "                print(new_name)\n",
    "                command =  f'ffmpeg -y -i \"{video}\" -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23 \"{new_name}\"' \n",
    "                commands.append(command)\n",
    "    i = 0\n",
    "    for command in commands:\n",
    "       subprocess.Popen(command, shell=True).wait()\n",
    "       i +=1\n",
    "       print(i, 'out of', len(commands), 'videos converted')"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
