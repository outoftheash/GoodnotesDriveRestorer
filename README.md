# GoodNotes Google Drive Backup Restorer

## The Problem

When you use GoodNotes' Auto Backup feature with Google Drive, GoodNotes uploads individual `.goodnotes` files arranged in a folder hierarchy, tracked by a hidden `.goodnotesmeta` file at the root.

If you try to download this backup folder to a PC via Google Drive web:

1. Google Drive automatically zips the folder. During this process, it often incorrectly appends `.zip` to your `.goodnotes` files (e.g., `Notebook.goodnotes.zip`).
2. The hidden `.goodnotesmeta` file is frequently lost or stripped during the download/extraction process.

Without `.goodnotesmeta`, GoodNotes on your iPad will refuse to bulk-import the folder structure. Furthermore, GoodNotes cannot read the altered `.goodnotes.zip` files. Attempting to import the raw Google Drive download will fail.

## The Solution

This Python script repairs a downloaded Google Drive Auto Backup so it can be restored exactly like a native GoodNotes Manual Backup.

It automates three steps:

1. Recursively scans all subfolders and renames any `*.goodnotes.zip` files back to proper `*.goodnotes` packages.
2. Uses the native Windows `tree` command to map out your exact folder hierarchy.
3. Parses that hierarchy to mathematically recreate the missing `.goodnotesmeta` file with the exact JSON syntax and escaping GoodNotes requires.

## Prerequisites

* Windows OS (uses the native Windows `tree` command).
* Python 3 installed.
* Your extracted Google Drive backup folder.

## Usage Instructions

**1. Prepare your files**
Download your GoodNotes backup from Google Drive and extract/unzip it into a standard folder on your PC.

**2. Run the script**
Place `build_goodnotes.py` into the **root** of that extracted folder (the same directory containing your top-level subject folders like "Math", "Work", etc.).

Open PowerShell or Command Prompt in that directory and run:

```bash
python build_goodnotes.py

```

**3. Cleanup**
The script will generate a temporary file named `GoodNotes_Tree.txt` and the necessary `.goodnotesmeta` file.
Before proceeding, you must **delete** the following two files from the folder so they are not included in your notebook library:

* `GoodNotes_Tree.txt`
* `build_goodnotes.py`

**4. Create the final GoodNotes Backup**
Select **all** the items inside your root folder (your subfolders, standalone `.goodnotes` files, and the newly generated `.goodnotesmeta` file).

* Right-click the selected items and choose **Compress to ZIP file** (or *Send to > Compressed (zipped) folder*).
* Name the resulting file something like `GoodNotes_Restored_Backup.zip`.

This newly generated `.zip` file is now structurally identical to a native backup generated directly by the GoodNotes app.

**5. Import to iPad**
Transfer `GoodNotes_Restored_Backup.zip` to your iPad (via iCloud Drive, Google Drive app, or AirDrop).
Open GoodNotes, tap **+ (New) > Import**, and select the `.zip` file. GoodNotes will process the `.goodnotesmeta` file and instantly restore all your notebooks with their exact folder structure perfectly intact.
