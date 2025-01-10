import nbformat
from nbformat.sign import NotebookNotary

# Path to your notebook
notebook_path = r"C:\Users\bose\Downloads\made-template\project\EDA\analysis.ipynb"

# Load the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Mark the notebook as trusted
notary = NotebookNotary()
notary.mark_cells(notebook, notebook_path)

# Save the notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(notebook, f)

print(f"{notebook_path} is now trusted.")
