# GoodNotes Google Drive Backup Restorer

## The Problem

When you use GoodNotes' Auto Backup feature with Google Drive, GoodNotes uploads individual `.goodnotes` files arranged in a folder hierarchy. If you try to download a folder to a PC via Google Drive web Google Drive automatically turns `.goodnotes` files to `.goodnotes.zip` files (e.g., `Notebook.goodnotes` -> `Notebook.goodnotes.zip`) during Google Drive's zipping process. There is a missing `.goodnotesmeta` file that is not created by GoodNotes' Auto Backup feature, which shows the structure of all the files.

Without `.goodnotesmeta`, GoodNotes will refuse to bulk-import the folder structure. Furthermore, GoodNotes cannot read the altered `.goodnotes.zip` files. Attempting to import the raw Google Drive download will fail.

## The Solution
This Python script repairs a downloaded Google Drive Auto Backup so it can be restored exactly like a native GoodNotes Manual Backup. 

It automates the following steps:
1. Recursively scans all subfolders and renames any `*.goodnotes.zip` files back to proper `*.goodnotes` packages.
2. Natively maps out your exact folder hierarchy across Windows, macOS, or Linux.
3. Parses that hierarchy to mathematically recreate the missing `.goodnotesmeta` file with the exact JSON syntax and escaping GoodNotes requires.

## Prerequisites
* Python 3 installed.
* Your extracted Google Drive backup folder.

## Usage Instructions

**1. Prepare your files**
Download your GoodNotes backup from Google Drive and extract/unzip it into a standard folder on your computer. 

**2. Run the script**
Place `build_goodnotes.py` into the **root** of that extracted folder (the same directory containing your top-level subject folders like "Math", "Work", etc.). 

Open your terminal or command prompt in that directory and run:
```bash
python3 build_goodnotes.py
```
*(Note: On some systems, the command may just be `python build_goodnotes.py`)*

**3. Cleanup (Important)**
Before zipping your backup, you must remove any files that do not belong in a native GoodNotes backup. Delete the following from your folder:
* `build_goodnotes.py` (the script itself)
* Any `.pdf` files or other files like images (only `.goodnotes` files and folders should remain, alongside the newly created `.goodnotesmeta` file).

**4. Create the final GoodNotes Backup**
Select **all** the items inside your root folder (your subfolders, standalone `.goodnotes` files, and the `.goodnotesmeta` file). 
* Right-click the selected items and compress/zip them (e.g., *Compress to ZIP file* on Windows, or *Compress* on macOS).
* Name the resulting file something like `GoodNotes_Restored_Backup.zip`. 

This newly generated `.zip` file is now structurally identical to a native backup generated directly by the GoodNotes app.

**5. Import to iPad**
Transfer `GoodNotes_Restored_Backup.zip` to your iPad (via iCloud Drive, Google Drive app, or AirDrop). 
Open GoodNotes, tap **+ (New) > Import**, and select the `.zip` file. GoodNotes will process the `.goodnotesmeta` file and instantly restore all your notebooks with their exact folder structure perfectly intact.
