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
    !git clone https://github.com/sinalephie/labs.git > /dev/null 2>&1
  from labs.lab import pd,plt,sp,np,math,potenza,moltiplica,somma,fit,excel,mediapesata,compatibilità,stampa,suona,std,chi2retta,media,pearson,stdmedia,massimirelativi,minimirelativi,chi2,curve_fit,posterioriretta,importa,guida,ufloat,correlated_values,guarda,stile

    ```

* ## **Altri (Jupyter Notebook, Vscode, Xcode...)**

    ```python
	import urllib.request, zipfile, os,shutil
    try: 
    	urllib.request.urlretrieve('https://codeload.github.com/sinalephie/labs/zip/refs/heads/main', 'labs.zip'); 
    	if os.path.exists('labs'): 
        		shutil.rmtree('labs')
    	zipfile.ZipFile('labs.zip', 'r').extractall('labs1'); os.remove('labs.zip'); shutil.move('labs1/labs-main', 'labs'); shutil.rmtree('labs1')
    except: pass
  from labs.lab import pd,plt,sp,np,math,potenza,moltiplica,somma,fit,excel,mediapesata,compatibilità,stampa,suona,std,chi2retta,media,pearson,stdmedia,massimirelativi,minimirelativi,chi2,curve_fit,posterioriretta,importa,guida,ufloat,correlated_values,guarda,stile

    ```
  in questo modo si ha sempre l'ultimo aggiornamento delle varie funzioni



# Come usare le funzioni
loading
