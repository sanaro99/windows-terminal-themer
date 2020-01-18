# windows-terminal-themer
A GUI based theme manager for the new Windows Terminal

## Usage

Clone this repo

```
git clone https://github.com/pranavgoyanka/windows-terminal-themer.git
```
### Or 
Download it manually and save it to your computer

### Method 1 (Adding the scripts to PATH)

```
[Environment]::SetEnvironmentVariable("Path", "$env:Path;<PATH_TO_REPO_DIRECTORY>")
```
Where, <PATH_TO_REPO_DIRECTORY> is the location of the downloaded/cloned files

Example

```
[Environment]::SetEnvironmentVariable("Path", "$env:Path;E:\code\windows-terminal-themer\")
```

Now run

```
themergui.py
```

Select the shell from the CLI (GUI will be added for this in the future) and hit enter to change the settings

### Method 2 

Change directory of PowerShell to the location where you have the files downloaded/cloned

```
cd <PATH_TO_REPO_DIRECTORY>
```

Now run

```
themergui.py
```

Select the shell from the CLI (GUI will be added for this in the future) and hit enter to change the settings


#### To Do:
Improve what the GUI looks like
