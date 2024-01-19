* **Google Colab**

    ```bash
    !git clone https://github.com/sinalephie/lab.git > /dev/null 2>&1
    ```

* **Altri (Jupyter Notebook, Vscode, Xcode...)**

    Se avete GitHub installato (è buono averlo: [GitHub Desktop](https://desktop.github.com/)), dal terminale:

    ```bash
    pip install git+https://github.com/sinalephie/lab.git
    ```

    L'alternativa è eseguire queste righe:

    ```python
    import urllib.request, zipfile, os,shutil; urllib.request.urlretrieve('https://codeload.github.com/sinalephie/lab/zip/refs/heads/main', 'lab.zip')
	if os.path.exists('lab'): shutil.rmtree('lab'); zipfile.ZipFile('lab.zip', 'r').extractall('lab1'); os.remove('lab.zip'); shutil.move('lab1/lab-main', 'lab'); shutil.rmtree('lab1'

    ```
