with open('cleanup_backup.py', 'w') as f:
    f.write('''import os
from pathlib import Path

def dangerous_cleanup():
    root_dir = Path.cwd()
    print(f"WARNING: Deleting everything in {root_dir} that is not .goodnotes or .goodnotesmeta!")
    
    deleted_count = 0
    for path in root_dir.rglob("*"):
        if path.is_file():
            if path.suffix == '.goodnotes' or path.name == '.goodnotesmeta':
                continue
                
            try:
                path.unlink()
                print(f"Deleted: {path.name}")
                deleted_count += 1
            except Exception as e:
                print(f"Could not delete {path.name}: {e}")
                
    print(f"Cleanup complete. Deleted {deleted_count} files.")

if __name__ == '__main__':
    dangerous_cleanup()
''')
print("[file-tag: cleanup_backup.py]")
