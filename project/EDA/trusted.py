import nbformat
from nbformat.sign import NotebookNotary

# Path to your notebook
notebook_path = r"C:\Users\bose\Downloads\made-template\project\EDA\analysis.ipynb"

# Load the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Add top-level metadata
notebook['metadata'] = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.13.1"
    },
    "trusted": True
}

# Save the updated notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(notebook, f)

print(f"Metadata added and notebook trusted: {notebook_path}")

