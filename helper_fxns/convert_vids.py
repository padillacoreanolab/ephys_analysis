import sys
import os
import glob
import subprocess

def convert_vid_folder_sleap(input_folder, vid_type):
    """
    This assumes all videos are in the same folder. Converts videos to be used for sleap tracking without issues 
    i.e. an mp4 with some other specifications of this command -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23
    saves all videos with original name plus _converted at the end. 

    Args (2 required, 3 total)
        input_folder: str, where your videos exist
        vid_type: str {'.mp4' or '.h264', whatever the original video type is}
        output_folder: str, optional, where you would like the videos to be saved, 
            if not specified the input_folder is used
    """
    if output_folder is None:
        output_folder = input_folder
    data_path = input_folder + '\*'
    videos = glob.glob(data_path)
    video = [glob.glob(f'*{vid_type}') for video in videos]
    commands = []
    for video in (videos):
        video_dir, video_name = os.path.split(video)
        new_name = os.path.join(output_folder, video_name.replace(vid_type, '_converted.mp4'))
        if not os.path.exists(new_name):
            command =  f'ffmpeg -y -i "{video}" -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23 "{new_name}"' 
            commands.append(command)
    i = 0
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True) # .Popen(command, shell=True).wait()
            i +=1
            print(i, 'out of', len(commands), 'videos converted')
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {command}")
            print(f"Error code: {e.returncode}")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")

def convert_h264_trodes(input_folder, vid_type = None):
    """
    This assumes all videos are in .rec folders (typical trodes output folder structure).
    Converts videos to be used for sleap tracking without issues 
    i.e. an mp4 with some other specifications of this command -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23
    saves all videos with original name plus _converted at the end and saved in their original .rec folder. 

    Args (1 required, 2 total)
        input_folder: str, where your videos exist
        vid_type: str, optional, {'.mp4' or '.h264', whatever the original video type is}
            if not specified, .h264 files are assumed
    """
    if vid_type is None:
        vid_type = '.h264'
    rec_folders = glob.glob(os.path.join(input_folder, '*.rec'))
    commands = []
    for rec_folder in rec_folders:
        videos = glob.glob(os.path.join(rec_folder, f'*{vid_type}'))
        for video in (videos):
            video_dir, video_name = os.path.split(video)
            new_name = os.path.join(video_dir, video_name.replace(vid_type, '_converted.mp4'))
            if not os.path.exists(new_name):
                print(new_name)
                command =  f'ffmpeg -y -i "{video}" -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23 "{new_name}"' 
                commands.append(command)
    i = 0
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True) # .Popen(command, shell=True).wait()
            i +=1
            print(i, 'out of', len(commands), 'videos converted')
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {command}")
            print(f"Error code: {e.returncode}")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")

def convert_other_sleap(input_folder, vid_type = None):
    """
    This assumes all videos are in recording type folders in an experimental folder structure. 
    ie. experiment_folder/rec/vid_to_convert. and input folder would be path/to/experiment/folder 
    Converts videos to be used for sleap tracking without issues 
    i.e. an mp4 with some other specifications of this command -c:v libx264 -pix_fmt yuv420p -preset superfast -crf 23
    saves all videos with original name plus _converted at the end and saved in their original .rec folder. 

    Args (1 required, 2 total)
        input_folder: str, where your videos exist
        vid_type: str, optional, {'.mp4' or '.h264', whatever the original video type is}
            if not specified, .h264 files are assumed
    """
    if vid_type is None:
        vid_type = '.h264'
    commands = []
    ###################################
    # FIXED WITH THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    long_path_str = r'\\?\\'
    # PATHS ON WINDOWS CAN ONLY BE 260 CHARACTERS LONG
    # WHEN USING THIS REAL STRING IN FRONT OF ANY PATH/STRING 
    # TO FLAG IT AS LONG. wINDOWS WILL THEN KNOW TO TREAT IT
    # IN THE CORRECT WAY.
    # OTHERWISE THE PATHS BECOME TOO LONG.
    # WINDOWS SUCKS SOMETIMES. 
    # BUT THIS IS A NIFTY TRICK TO REMEMBER TO BE ABLE TO
    # USE LONGER PATHS IN WINDOWS FROM PYTHON.
    ####################################
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(vid_type):
                video_path = os.path.join(root, file)
                new_path = os.path.join(root, file.replace(vid_type, '_converted.mp4'))
                if not os.path.exists(new_path):
                    ####################################
                    # I ADDED IT HERE TO THE COMMANDLINE STRING TO FIX IT.
                    command = (
                        f'ffmpeg -y -i "{long_path_str}{video_path}" -c:v libx264 -pix_fmt yuv420p '
                        f'-preset superfast -crf 23 "{long_path_str}{new_path}"'
                    )
                    ####################################
                    commands.append(command)
    i = 0
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True) # .Popen(command, shell=True).wait()
            i +=1
            print(i, 'out of', len(commands), 'videos converted')
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {command}")
            print(f"Error code: {e.returncode}")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")