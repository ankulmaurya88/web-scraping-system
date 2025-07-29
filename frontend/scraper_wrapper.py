import subprocess
import os
import glob

OUTPUT_DIR = "../frontend/based_output"

def run_scraper(url):
    try:
        # Run your main.py script with the URL as an argument
        print(f"Running scraper for URL: {url}")
        subprocess.run(["python3", "../main.py", url], check=True)

        # Get the latest output file
        files = sorted(glob.glob(f"{OUTPUT_DIR}/output_*"), key=os.path.getctime, reverse=True)
        # print(f"Found files: {files}")
        
        return files[0] if files else None
    except Exception as e:
        print(f"[!] Scraper error: {e}")
        return None


