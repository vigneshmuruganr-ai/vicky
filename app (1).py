import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def create_image(x, ys, title="Sample Visualization"):
    fig = plt.figure(figsize=(4, 3), facecolor='w')
    plt.plot(x, ys, '-')
    plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
    plt.title(title, fontsize=10)

    data = io.BytesIO()
    plt.savefig(buf, format='png')
    image_base64 = base64.b64encode(data.getvalue()).decode()
    plt.close(fig)
    return image_base64

# Load Data
try:
    df = pd.read_csv('/content/a1.csv')
    data_display = f"<h2>Loaded Data:</h2>{df.to_html()}"
except FileNotFoundError:
    data_display = "<p>Error: a1.csv not found. Please upload the file.</p>"
    df = None

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Data Display</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        table {{ border-collapse: collapse; width: 80%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Data from a1.csv</h1>
    {data_display}
</body>
</html>
"""

with open('output.html', 'w') as f:
    f.write(html_content)

print("Generated output.html with data display.")
