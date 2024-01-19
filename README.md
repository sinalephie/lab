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
Successivamente per **importare le funzioni** cosi come le librerie basta copiare questa riga sul proprio progetto, quando vengono create nuove funzioni bisognerà dichiararle

```
from lab.funzioni_e_librerie import pd,plt,sp,np,Audio,HTML,math,requests,BytesIO,colored,potenza,moltiplica,somma,fit,excel,mediapesata,compatibilità,stampa,suona,rispostacorretta,std,chi2retta,media,pearson,stdmedia,massimirelativi,minimirelativi,chi2,curve_fit,posterioriretta,importa,guida
```
