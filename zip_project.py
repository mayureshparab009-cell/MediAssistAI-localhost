import os
import zipfile

def zip_project():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    zip_name = "MediAssistAI.zip"
    zip_path = os.path.join(root_dir, zip_name)
    
    # Exclude patterns
    exclude_folders = {"node_modules", "venv", ".venv", "__pycache__", ".git", "dist", "build"}
    exclude_files = {zip_name, "mediassist.db"}
    
    print(f"Creating ZIP archive at: {zip_path}")
    
    count = 0
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(root_dir):
            # Prune directories in-place to prevent walking excluded folders
            dirs[:] = [d for d in dirs if d not in exclude_folders]
            
            for file in files:
                if file in exclude_files or file.endswith('.pyc') or file.endswith('.pyo'):
                    continue
                    
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, root_dir)
                
                zipf.write(full_path, rel_path)
                print(f"  Added: {rel_path}")
                count += 1
                
    print(f"Zip completed successfully! Added {count} files.")
    print(f"Saved to: {zip_path}")

if __name__ == "__main__":
    zip_project()
