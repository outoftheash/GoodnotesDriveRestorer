#Written by outoftheash on Github
#GoodnotesBackupGen

import os
import json
import shutil
from pathlib import Path

def run_cross_platform():
    root_dir = Path.cwd()
    
    # STEP 1: Rename all .goodnotes.zip files to .goodnotes
    print("Step 1: Renaming .goodnotes.zip files...")
    count = 0
    for path in root_dir.rglob("*.goodnotes.zip"):
        new_path = path.with_suffix('') # Strips the .zip extension
        
        # Resolve conflicts if the destination file already exists
        if new_path.exists():
            if new_path.is_dir():
                shutil.rmtree(new_path)
            else:
                new_path.unlink()
                
        path.rename(new_path)
        print(f"  -> Renamed: {path.name}")
        count += 1
    print(f"Renamed {count} files.\n")

    # STEP 2: Natively map directories and generate .goodnotesmeta
    print("Step 2: Generating .goodnotesmeta directly...")
    items = []
    
    # Recursively find all subdirectories inside the root folder
    for path in root_dir.rglob("*"):
        if path.is_dir():
            # Get the path relative to the main folder and force forward slashes
            rel_path = path.relative_to(root_dir).as_posix()
            
            # Ignore hidden OS folders (like .git, .Trash, or Mac's __MACOSX)
            if rel_path.startswith('.') or '__MACOSX' in rel_path:
                continue
                
            items.append({
                "color": "blue",
                "symbol": "none",
                "path": rel_path
            })

    # Wrap the parsed folders into the final JSON structure GoodNotes requires
    output = {
        "compatibilityVersion": 1,
        "items": items
    }

    # Compress the JSON by removing spaces and escape the forward slashes
    json_str = json.dumps(output, separators=(',', ':'))
    json_str = json_str.replace('/', '\\/')

    # Save the final .goodnotesmeta file safely in UTF-8
    with open(".goodnotesmeta", "w", encoding="utf-8") as f:
        f.write(json_str)
        
    print("  -> Successfully created .goodnotesmeta!\n")
    print("All steps complete! You can now zip this main directory and import it to your iPad.")

if __name__ == "__main__":
    run_cross_platform()
