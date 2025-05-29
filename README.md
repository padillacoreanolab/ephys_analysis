# ephys_analysis
This repository holds code to conduct ephys analysis on data files that come from trodes and phy files. It also has code to extract behavior data from Boris and ECU data and some tools to manipulate behavioral epochs. 



.vscode settings: 

changed through the settings tab under workspace we changed the following setting (File>Preference>Settings or Ctrl+,)

Jupyter: Notebook File Root
${workspaceFolder}

this means that the parent folder opened in VSCode is the workspaceFolder which is set as the working directory 

**note: where a jupyternotebook lives is not necessarily where
it is being run, those are two different things. 

- This is important because it is brittle to have imports be relative to where the jupyter notebook file is stored for importing local modules and extremely important for [pickling and unpickling](https://stackoverflow.com/a/2121918). Eg, if you wanted to move notebooks, or have notebooks be portable from computer to computer

## Installation

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Developer installation

## How to run tests like a real coder

### Download test data

We're going to use this small recording from trodes:
https://docs.spikegadgets.com/en/latest/basic/BasicUsage.html

There is a helper script that downloads it and unzips it into `tests/test_data/`.

```
python -m tests.utils download_test_data
```

please open terminal and run in this directory

```
python -m tests.util
cd diff_fam_social_memory_ephys/lfp
python -m unittest discover
```

## How to run single files as modules

For example, to turn a dataset into a test:

```
python -m tests.utils create /Volumes/SheHulk/cups/data/11_cups_p4.rec/11_cups_p4_merged.rec
```

This is nice because it allows all imports to be relative to the root directory.




### dropbox
1. install rclone on your local computer: https://rclone.org/downloads/
2. run on personal computer 
```
rclone.exe authorize "dropbox"
```

crtl + click on link that terminal spits out and press agree, terminal will now spit out a token key, finish step 3 before copying and pasting it into the hipergator terminal

3. open terminal in hipergator and run the following lines: 
```
module load rclone
rclone config
```

- n) New remote
- name your dropbox
- Storage > 13 (type 13 (which is dropobx) and hit enter) 
- leave client_id and client_secret blank (aka press enter) 
- type n and click enter (No) for edit advanced config
- type n and click enter (No) for web broswer question
- copy and paste config token from local terminal into hipergator terminal
- click y and hit enter for default settings to finish

if authentication breaks press choose: e) Edit existing remote 
4. find data on dropbox
```
rclone ls pc-dropbox:"Padilla-Coreano Lab/path/to/data"
```
5. copy data from dropdox
source = pc-dropbox
path ="path/to/folder"
run dry run first to confirm path and size of download 

example of destination path
dest:path = ./data 
```
rclone copy source:path dest:path --progress --dry-run
```
then run it for reals
```
rclone copy source:path dest:path --progress
```

example real command:
```
rclone copy pc-dropbox:"Padilla-Coreano Lab/2024/Cum_SocialMemEphys_pilot2/Only_Subjects (phase 5)/sorted" ./only_subjects_spike_data --progress  --dry-run
```

or to upload data to dropbox: 

```
rclone copy ./r4_predictions pc-dropbox:"Padilla-Coreano Lab/2024/Cum_SocialMemEphys_pilot2/SLEAP/only_subject_mp4s/r4_predictions" --progress --dry-run
```
