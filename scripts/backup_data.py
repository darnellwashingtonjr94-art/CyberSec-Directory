import shutil
import time
from pathlib import Path

def backup_data_dir():
    base = Path(__file__).parent.parent
    data_dir = base / "data"
    backup_dir = base / "backups"
    backup_dir.mkdir(exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    archive_name = backup_dir / f"data_backup_{timestamp}"
    
    shutil.make_archive(str(archive_name), 'zip', data_dir)
    print(f"Backed up {data_dir.name} to {archive_name}.zip")

if __name__ == "__main__":
    backup_data_dir()
