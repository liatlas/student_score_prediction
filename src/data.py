from pathlib import Path
import shutil
import kagglehub

DATASET = "enter your dataset here"

def download_kaggle_dataset(force = False):
    """
    call to download from a kaggle dataset
    files are downloaded to .cache/kaggle/datasets
    are copied to the project/data directory
    the folders in .cache/kaggle/datasets are deleted
    """
    dest = Path("../data/").resolve()
    
    if list(dest.glob("*.csv")) and not force:
        return dest

    cache_path = Path(kagglehub.data_download(DATASET))

    for csv in cache_path.rglob("*.csv"):
        shutil.copy(csv, dest / csv.name)

    shutil.rmtree(cache_path.parents[2], ignore_errors=True)

    return dest

