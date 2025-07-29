from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from scraper_wrapper import run_scraper
import os
from flask import send_from_directory, abort

app = Flask(__name__)
app.config['VERSION'] = '1.0.1' # Change this every time you want to force refresh

app.secret_key = 'your_secret_key'  # Required for flashing messages

OUTPUT_DIR = "../based_output"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            output_file = run_scraper(url)
            if output_file:
                flash(f"Scraping completed. Download file below.", "success")
                return render_template('index.html', filename=os.path.basename(output_file))
            else:
                flash("Scraping failed or no data found.", "error")
        else:
            flash("Please enter a valid URL.", "error")
    return render_template('index.html')


@app.route('/download/<foldername>')
def download_file(foldername):
    base_output_dir = os.path.abspath('../based_output')
    folder_path = os.path.join(base_output_dir, foldername)

    print(f"Downloading from folder: {folder_path}")

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return abort(404)

    # Find the actual file inside the folder (e.g., output.txt)
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            return send_from_directory(folder_path, file, as_attachment=True)

    print("No file found in folder.")
    return abort(404)

if __name__ == '__main__':
    app.run(debug=True)
