# Prerequisiti 
* ## se siete su Google Colab siete apposto
* ## Altrimenti
	Le librerie necessarie sono:
	
	* ciao
	* ciao
	* ciao
# Come importare il modulo e le varie funzioni
* ## **Google Colab**
  
	nella prima riga di ogni progetto:
    ```python
    !git clone https://github.com/sinalephie/lab.git > /dev/null 2>&1
    from labs.lab import pd,plt,sp,np,Audio,HTML,math,requests,BytesIO,colored,potenza,moltiplica,somma,fit,excel,mediapesata,compatibilità,stampa,suona,rispostacorretta,std,chi2retta,media,pearson,stdmedia,massimirelativi,minimirelativi,chi2,curve_fit,posterioriretta,importa,guida

    ```

* ## **Altri (Jupyter Notebook, Vscode, Xcode...)**

    ```python
	import urllib.request, zipfile, os,shutil
	try:
	urllib.request.urlretrieve('https://codeload.github.com/sinalephie/lab/zip/refs/heads/main', 'lab.zip'); 
	if os.path.exists('lab'): shutil.rmtree('lab'); zipfile.ZipFile('lab.zip', 'r').extractall('lab1'); os.remove('lab.zip'); shutil.move('lab1/lab-main', 'lab'); shutil.rmtree('lab1')
	except: pass
	from labs.lab import pd,plt,sp,np,Audio,HTML,math,requests,BytesIO,colored,potenza,moltiplica,somma,fit,excel,mediapesata,compatibilità,stampa,suona,rispostacorretta,std,chi2retta,media,pearson,stdmedia,massimirelativi,minimirelativi,chi2,curve_fit,posterioriretta,importa,guida

    ```
  in questo modo si ha sempre l'ultimo aggiornamento delle varie funzioni



# Come usare le funzioni
loading
