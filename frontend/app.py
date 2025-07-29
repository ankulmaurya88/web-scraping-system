from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from scraper_wrapper import run_scraper

from flask import send_from_directory, abort
import shutil

app = Flask(__name__)
app.config['VERSION'] = '1.0.1' # Change this every time you want to force refresh

app.secret_key = 'your_secret_key'  # Required for flashing messages


# BASE_OUTPUT_DIR = os.path.abspath("based_output")


base_output_dir = os.path.abspath('../frontend/based_output')  # in your Flask route

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            output_file = run_scraper(url)
            if output_file:
                # flash(f"Scraping completed. Download file below.", "success")
                return render_template('index.html', filename=os.path.basename(output_file))
            else:
                flash("Scraping failed or no data found.", "error")
        else:
            flash("Please enter a valid URL.", "error")
    return render_template('index.html')


# @app.route('/download/based_output/<foldername>', methods=['GET'])
# def download_file(foldername):
#     base_output_dir = os.path.abspath('../frontend/based_output')
#     folder_path = os.path.join(base_output_dir, foldername)

#     print(f"Downloading from folder: {folder_path}")

#     if not os.path.exists(folder_path):
#         print("Folder does not exist.")
#         return abort(404)

#     # Find the actual file inside the folder (e.g., output.txt)
#     for file in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file)
#         if os.path.isfile(file_path):
#             return send_from_directory(folder_path, file, as_attachment=True)

#     print("No file found in folder.")
#     return abort(404)



@app.route('/download/based_output/<foldername>/<filename>', methods=['GET'])
def download_file(foldername, filename):
    base_output_dir = os.path.abspath('frontend/based_output')  # this should match your actual path
    folder_path = os.path.join(base_output_dir, foldername)
    file_path = os.path.join(folder_path, filename)

    print(f"Trying to download: {file_path}")

    if not os.path.exists(file_path):
        print("File does not exist.")
        return abort(404)

    return send_from_directory(folder_path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
