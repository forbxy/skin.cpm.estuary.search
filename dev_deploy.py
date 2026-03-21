import os
import sys
import shutil

REMOTE=True
def main():
    addon_id = "skin.cpm.estuary.search"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    is_remote = REMOTE or (len(sys.argv) > 1 and sys.argv[1].lower() == 'remote')

    if is_remote:
        target_dir = os.path.join("F:\\", "storage", ".kodi", "addons", addon_id)
    else:
        appdata = os.environ.get("APPDATA")
        if not appdata:
            print("APPDATA environment variable not found.")
            return
        target_dir = os.path.join(appdata, "Kodi", "addons", addon_id)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created target directory: {target_dir}")

    exclude_dirs = {'.git', '.vscode', '__pycache__', '.github', 'dist'}
    exclude_files = {'dev_deploy.py', 'dev_deploy.ps1', '.gitignore', 'build_package.py'}
    exclude_exts = {'.pyc', '.DS_Store', 'Thumbs.db', '.log'}

    print("Deploying files...")
    count = 0
    
    for root, dirs, files in os.walk(script_dir):
        # Modify dirs in-place to prune excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        rel_path = os.path.relpath(root, script_dir)
        
        for file in files:
            if file in exclude_files or any(file.endswith(ext) for ext in exclude_exts):
                continue
            
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, rel_path, file) if rel_path != "." else os.path.join(target_dir, file)
            
            dst_dir = os.path.dirname(dst_file)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                
            shutil.copy2(src_file, dst_file)
            count += 1
            
    print(f"Deployment complete! {count} files copied into {target_dir}")

if __name__ == "__main__":
    main()
