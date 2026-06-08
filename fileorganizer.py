import os
import shutil
from flask import Flask, render_template_string, request

app = Flask(__name__)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple File Organizer</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; padding: 20px;">
    <h2>📁 Simple File Organizer</h2>
    <p>Enter a folder path to sort its files instantly.</p>
    
    <form method="POST">
        <input type="text" name="folder_path" placeholder="Paste folder path here" style="width: 100%; padding: 10px; margin-bottom: 10px;" required>
        <button type="submit" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; cursor: pointer; width: 100%;">Organize Now</button>
    </form>

    {% if message %}
        <p style="margin-top: 20px; color: {% if 'Error' in message %}red{% else %}green{% endif %}; font-weight: bold;">
            {{ message }}
        </p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
       
        folder = request.form.get("folder_path").strip()

      
        if os.path.exists(folder):
         
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)

             
                if os.path.isdir(file_path):
                    continue

                if file.lower().endswith((".jpg", ".png", ".jpeg", ".gif")):
                    category = "Images"
                elif file.lower().endswith((".pdf", ".docx", ".txt", ".xlsx")):
                    category = "Documents"
                else:
                    category = "Others"

                
                target_folder = os.path.join(folder, category)
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, file))

            message = "Success! Your files have been sorted."
        else:
            message = "Error: That folder path does not exist."

    return render_template_string(HTML_TEMPLATE, message=message)


if __name__ == "__main__":
    app.run(debug=True)
