#LIBRERIE:
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
from IPython.display import Audio, HTML, Latex, display, Image
import math
from numpy import sin,cos,tan,arcsin,arctan,arccos
import requests
from io import BytesIO
from termcolor import colored
from labs.librerie_aggiuntive.uncertainties.core import ufloat, correlated_values
try:
  from google.colab import output
  is_dark = output.eval_js('document.documentElement.matches("[theme=dark]")')
except ModuleNotFoundError:
  pass

#VARIABILI
rispostacorretta='https://cdn.pixabay.com/download/audio/2021/08/04/audio_bb630cc098.mp3?filename=short-success-sound-glockenspiel-treasure-video-game-6346.mp3'
capra='https://cdn.pixabay.com/download/audio/2023/11/20/audio_6d2ecb8b19.mp3?filename=goat-sound-177346.mp3'
#CIAOOO
def guarda(*links,**kwargs):
  immagini = {}
  immagini['capra'] = 'https://styles.redditmedia.com/t5_2qlyf/styles/communityIcon_w3vaehlvt5i11.jpg'
  immagini['mucca'] = 'https://www.fondazionevb.org/media/cache/582_436_inset/uploads/contents/dona-una-mucca-alle-donne-di-mutanu_1679318060.png'
  if 'size' not in kwargs:
    kwargs['size']=200
  for link in links:
    presente=False
    for c, d in immagini.items():
      if link==c:
        link=d
        presente=True
    elenco = ', '.join("'{0}'".format(key) for key in immagini.keys()) + '.'
    if link=='elenco':
      print('l\'elenco delle immagini disponibili è:', elenco)
      return
    if isinstance(link, str) and presente==False:
      raise ValueError(f'{link} non è stata/o ancora aggiunta/o, per visualizzare l\'elenco con tutte le immagini metti in argomento \'elenco\'')
      return
    display(Image(link, width=kwargs['size']))  

#FUNZIONI
def importa(link):

  import os, re, urllib,shutil
  import pandas as pd
  try:
      urllib.request.urlopen("https://www.google.com", timeout=3)
  except:
      raise ImportError('Sei offline, connettiti ad internet per importare i dati')
      return
  if 'google' and 'edit' in link:
    file_id_match = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    file_id = file_id_match.group(1) if file_id_match else None
    link = f"https://drive.google.com/uc?export=download&id={file_id}"
  if '1drv' in link:
    if 'files' in link:
      link='https://api.onedrive.com/v1.0/shares/s!'+ link[link.find('!')+1:link.find('?')]+'/root/content'
  if not os.path.exists('Datiis'):
    os.makedirs('Datiis')
  percorso=os.path.join(os.getcwd(), 'Datiis')
  percorso=percorso + '/'
  c='dati.xlsx'
  print(link)
  urllib.request.urlretrieve(link, percorso+c)
  Dataframe=pd.read_excel(f'{percorso+c}')
  shutil.rmtree('Datiis')
  return Dataframe


def guida():
    print('link alla guida funzioni \u2193 \u2193 \u2193')
    print('https://colab.research.google.com/drive/1Lace8ZenxKYWlCYEODxErVbPpABbGp4G?usp=sharing')


#STAMPA (print) ma piu figa (grazie chatgpt)
#       SINTASSI/ESEMPI: stampa(['ciaoo',20],['questo è un testo un po piu grande',50],['questo è piu piccolo ed è rosso',30,'red'])
#
#                        misura=40
#                        stampa([f'la tua misura è {misura}','blue'])
def stampa(*frasi_grandezze_colore):
    try:
        if is_dark:
          color='white'
        if not is_dark:
          color='black'
        else:
          color='white'
    except ModuleNotFoundError:
        color='grey'
    testo_stili_multipli = ""
    frase = ''
    for elemento in frasi_grandezze_colore:
        grandezza = 18
        colore=color
        if isinstance(elemento, (tuple, list)):
            if len(elemento) == 1:
                frase = elemento[0]
            if len(elemento) == 2:
                if isinstance(elemento[1], str):
                    frase, colore, grandezza = elemento[0], elemento[1], 18
                if isinstance(elemento[1], (int, float)):
                    frase, grandezza, colore = elemento[0], elemento[1], colore
            if len(elemento) == 3:
                if isinstance(elemento[1], str):
                    frase, colore, grandezza = elemento[0], elemento[1], elemento[2]
                elif isinstance(elemento[1], (int, float)):
                    frase, grandezza, colore = elemento[0], elemento[1], elemento[2]
        else:
            frase = str(elemento)

        stile = f"style='font-size: {grandezza}px; display: inline-block; color: {colore}; white-space: pre;'"
        frase_formattata = frase.format(f=frase) if '{f}' in frase else frase
        testo_stili_multipli += f"<span {stile}>{frase_formattata}</span>"

    display(HTML(testo_stili_multipli))





#CORRELAZIONE LINEAERE (Pearson):
def pearson(x,y):
  print('')
  print('')
  stampa(['Correlazione lineare di pearson:',25])
  import scipy as sp
  import pandas as pd
  pear=sp.stats.pearsonr(x,y)
  coeff=pear[0]
  s_coeff=((1-coeff**2)/(len(x)-2))**0.5
  tabella = {'correlazione_lineare:': coeff, 's_correlazione_lineare:': s_coeff}
  df = pd.Series(tabella)
  return df


#MEDIA
def media(*lista):
  if isinstance(lista[0],(int, float,np.int64,np.int32,np.float64,np.float32)):
    lis=[]
    for c in range (len(lista)):
      lis.append(lista[c])
  else:
    lis=list(lista[0])
  return sum(lis)/len(lis)


#DEVIAZIONE STANDARD (quella che ha nel denominatore n-1)
def std(*lista):
  import numpy as np
  if isinstance(lista[0],(int, float,np.int64,np.int32,np.float64,np.float32)):
    lis=[]
    for c in range (len(lista)):
      lis.append(lista[c])
  else:
    lis=list(lista[0])
  import numpy as np
  return np.std(lis,ddof=1)

#DEVIAZIONE STANDARD DELLA MEDIA
def stdmedia(*lista):
  import numpy as np
  if isinstance(lista[0],(int, float,np.int64,np.int32,np.float64,np.float32)):
    lis=[]
    for c in range (len(lista)):
      lis.append(lista[c])
  else:
    lis=list(lista[0])
  import numpy as np
  return (np.std(lis,ddof=1))/(len(lis))**0.5

#CHI QUADRO su una retta interpolante:  (BOZZA)
#               c'è bisogno di inserire i gradi di libertà utilizzando le keywords ddof= N-vincoli, non so se i gradi di libertà per una retta sono sempre N-2 nel caso poi modifico la funzione
#               se si assegna la funzione ad una variabile, alla variabile viene assegnato il p value risultante (VEDI ESEMPIO 2), oltre a stampare i dovuti risultati
           #SINTASSI: chi2retta(lista x,lista y, numero o lista incerteze y, variabile retta calcolata con la funzione fit, KEYWORDS)

           #KEYWORDS:

 #                   ddof= gradi di libertà
#                             imposta i gradi di libertà da utilizzare

#                    tabella=True
#                             mostra la tabella come le mostrava doro

           #ESEMPI:

#                ESEMPIO 1:
#                          chi2retta(x,y,sy,retta,ddof=(len(x)-2))
#
#                ESEMPIO 2:
#                          pvalue=chi2retta(x,y,sy,retta,ddof=(),tabella=True)



def chi2retta(x,y,sy,retta,**kwargs):
    print('')
    print('')
    print('')
    from IPython.display import display
    if not 'ddof' in kwargs:
        kwargs['ddof']=len(x)-2
    if not 'tabella' in kwargs:
        kwargs['tabella']=False
    from scipy.stats import chi2
    import pandas as pd
    if isinstance (sy,(int,float)):
        incertezza=sy
        lista=[]
        for f in range (len(x)):
            lista.append(sy)
        sy=lista
    chi2singoli=[]
    attese=[]
    for c in range (len(x)):
        attesa=x[c]*retta[1][0]+retta[0][0]
        attese.append(attesa)
        chi2singolo=((y[c]-attesa)/sy[c])**2
        chi2singoli.append(chi2singolo)
    pvalue= 1 - chi2.cdf(sum(chi2singoli), kwargs['ddof'])
    tabella=pd.DataFrame({'x_i':x,'y_i':y,'s_y':sy,'y_i*':attese,'chi2_i':chi2singoli,'chi2_m':sum(chi2singoli)})
    if kwargs['tabella']==True:
        stampa(['                                  tabella chi quadro     '])
        display(tabella)
        stampa([f'il p-value del chi quadro è: {pvalue}',35])
        return pvalue
    stampa([f'il p-value del chi quadro è: {pvalue}',35])
    return pvalue

def chi2(funzione,*args,**kwargs):
    print('')
    print('')
    print('')
    from IPython.display import display
    parametri=args[0]
    x=args[1]
    y=args[2]
    sy=args[3]
    if not 'ddof' in kwargs:
        kwargs['ddof']=len(x)-len(parametri)
    if not 'tabella' in kwargs:
        kwargs['tabella']=False
    from scipy.stats import chi2
    import pandas as pd
    if isinstance (sy,(int,float)):
        incertezza=sy
        lista=[]
        for f in range (len(x)):
            lista.append(sy)
        sy=lista
    chi2singoli=[]
    attese=[]
    for c in range (len(x)):
        attesa=funzione(x[c],*parametri)
        attese.append(attesa)
        chi2singolo=((y[c]-attesa)/sy[c])**2
        chi2singoli.append(chi2singolo)
    pvalue= 1 - chi2.cdf(sum(chi2singoli), kwargs['ddof'])
    tabella=pd.DataFrame({'x_i':x,'y_i':y,'s_y':sy,'y_i*':attese,'chi2_i':chi2singoli,'chi2_m':sum(chi2singoli)})
    if kwargs['tabella']==True:
        stampa(['                                  tabella chi quadro     '])
        display(tabella)
        stampa([f'il p-value del chi quadro è: {pvalue}',35])
        return pvalue
    stampa([f'il p-value del chi quadro è: {pvalue}',35])
    return pvalue



#POTENZA: calcola la potenza di un numero o di una lista.
#         nel caso della lista significa che ritorna la stessa lista inserita ma con ogni suo elemento elevato al certo numero inserito.

#        SINTASSI: potenza(numero o lista , numero al quale elevare).

#         es: potenza([1,2,3],2) ---> [1,4,9]
#         es: potenza(2,3) ----> 8
#         es: potenza([2,4],-1) ----> [1/2, 1/4]
def potenza(a,b):
    import numpy as np
    if isinstance(a,(int, float,np.int64,np.int32,np.float64,np.float32)):
        a=float(a)
        return a**b
    else:
        potenzalista=[]
        for c in a:
            c=float(c)
            potenzalista.append(c**b)
        return potenzalista


#MOLTIPLICA: moltiplica numeri con numeri, liste con liste e liste con numeri potendole/i inserire in numero e ordine arbitrario all interno dell'argomento
#            liste con liste significa che moltiplica il primo elemento della prima lista per il primo della seconda e poi il secondo della prima con il secondo della seconda ecc...

#        SINTASSI: moltiplica(numero o lista, numero o lista, numero o lista.......)

#        es: moltiplica([1,2,3],2)----> [2,4,6]
#        es: moltiplica(2,[1,2],[2,3])----> [4,12]
#        es: moltiplica([2,3],2,3)-----> [12,18]
#        es: moltiplica(2,4) ----> 8

def moltiplica(*argomento):
    import numpy as np
    conteggio=[]
    for h in range(0,len(argomento)):
        if isinstance(argomento[h],(int,float,np.int64,np.int32,np.float64,np.float32)):
            conteggio.append(1)
    if len(conteggio)==len(argomento):
        moltiplicazione=1
        for k in range(0,len(argomento)):
            moltiplicazione=moltiplicazione*argomento[k]
        return moltiplicazione
    else:

        args=list(argomento)
        for f in range(0, len(args)):
            if not isinstance(args[f],(int, float,np.int64,np.int32,np.float64,np.float32)) :
                lunghezza=len(args[f])
                indice=f

        for a in range(len(args)):
            if isinstance(args[a],(int, float,np.int64,np.int32,np.float64,np.float32)):
                lista=[]
                for e in range(0,lunghezza):
                    lista.append(args[a])
                args[a]=lista
        listarisultante=[1]*len(args[indice])
        for b in range(0,len(args[0])):
            for c in range(0,len(args)):
                listarisultante[b]=listarisultante[b]*args[c][b]
        return listarisultante

#SOMMA: somma numeri con numeri, liste con liste e liste con numeri potendole/i inserire in numero e ordine arbitrario all interno dell'argomento
#       liste con liste significa che somma il primo elemento della prima lista per il primo della seconda e poi il secondo della prima con il secondo della seconda ecc..
#       nel caso si metta in argomento una singola lista, la funzione fornirà la somma degli elementi della lista

#         SINTASSI: somma(numero o lista, numero o lista, numero o lista.......)
#          es: somma([1,2,3])--->6
#          es: somma([1,2],[2,3]) ----> [3,5]
#          es: somma(2,[1,3],5) -----> [8,10]
#          es: somma(1,2)----> 3

def somma(*argomento):
    import numpy as np
    if len(argomento)==1 and not isinstance(argomento[0],(int, float,np.int64,np.int32,np.float64,np.float32)):
        return sum(argomento[0])
    conteggio=[]
    for h in range(0,len(argomento)):
        if isinstance(argomento[h],(int,float,np.int64,np.int32)):
            conteggio.append(1)
    if len(conteggio)==len(argomento):
        somma=0
        for k in range(0,len(argomento)):
            somma=somma+argomento[k]
        return somma
    else:
        args=list(argomento)
        for f in range(0, len(args)):
            if not isinstance(args[f], (int, float,np.int64,np.int32,np.float64,np.float32)):
                lunghezza=len(args[f])
                indice=f
        for a in range(len(args)):
            if isinstance(args[a],(int, float,np.int64,np.int32,np.float64,np.float32)):
                lista=[]
                for e in range(0,lunghezza):
                    lista.append(args[a])
                args[a]=lista
        listarisultante=[0]*len(args[indice])
        for b in range(0,len(args[0])):
            for c in range(0,len(args)):
                listarisultante[b]=listarisultante[b]+args[c][b]
        return listarisultante

#FIT LINEARE: fa il fit secondo uno dei 3 casi presenti nelle dispense di Doro
#             IN BREVE: se trascurate le incertezze in ascissa mettete 0 al posto di sx e se le incertezze sono tutte uguali potete mettere il singolo valore in argomento.
#                       se fate quello che c'è scritto nella riga sopra non importa che caso usate: i risultati sono esattamente gli stessi, quindi vi basta sapere quanto scritto prima (vedi riga sintassi)

#             SINTASSI: fit(lista delle misure in ascissa, lista o numero incertezze sulle ascisse, lista delle misure in ordinata, lista o numero incertezze ordinate.)

#             COSA RITORNA: ritorna la lista seguente: [[intercetta,erroreintercetta],[pendenza,errorependenza]]
#                   ESEMPIO:
#                          retta=fit(x,sx,y,sy)
#                          intercetta = retta[0][0]
#                          pendenza = retta[1][0]
#                          erroreintercetta = retta[0][1]
#                          errorependenza = retta[1][1]


#             COSE GIUSTO PER I PRECISI (ma non servono per quanto detto prima, quindi potete ignorare ste righe e fidarvi):
#                COME COMUNICARE IL MODO D'INTERPOLAZIONE DA UTLIZZARE:
#                  CASO 1 e 2
#                     se si sceglie di trascurare gli errori delle misure in ascissa inserite il numero 0 nel posto di sx in argomento, facendo così la funzione utilizzerà il caso 1 o 2.
#                     se sx=0 e le incertezze in ordinata sono tutte uguali potete inserire il valore singolo di sy in argomento. così si utilizzerà il caso 1.
#                     se sx=0 e si inserisce una lista di valori diversi di sy la funzione utilizzerà il caso 2;
#                     se sx=0 e mettete una lista sy di valori tutti uguali la funzione utilizzerà sempre il caso 2 ma il risultato è lo stesso di utilizzare il caso 1
#                     questo poteva rendere il programma piu semplice non scrivendo proprio il caso1 ma me ne sono accorto dopo.

#                  CASO 3
#                     se le misure in ascissa non sono trascurabili mettete la lista sx in argomento e userà il caso 3,
#                     se le incertezze sx sono tutte uguali potete anche mettere il singolo valore sx.
#                     se le incertezze sulle x non sono trascurabili e avete incertezze uguali sulle y allora mettete il singolo valore sy, sennò mettete la lista

def fit(x,sx,y,sy,**kwargs):
  opzioniplot={}
  boo=0
  for chiave, valore in kwargs.items():
    if boo==1:
      opzioniplot[chiave]=valore
    if chiave=='opzioniplot':
      boo=1
  if not 'origine' in kwargs:
    kwargs['origine']=False
  if not 'plot' in kwargs:
    kwargs['plot']=False
  N=len(x) #  Numerosità
  if len(x)!=len(y):
      raise ValueError('la numerosità delle misure in ascissa è diverse da quelle in ordinata')
      return 
  scalasinistra=0.95
  if min(x)<0:
    scalasinistra=1.05
  scaladestra=1.05
  if max(x)<0:
    scaladestra=0.95
  if 'xsinistra' in kwargs:
    scalasinistra=1
  if 'xdestra' in kwargs:
    scaladestra=1
  if not 'xsinistra' in kwargs:
    kwargs['xsinistra']=min(x)
  if not 'xdestra' in kwargs:
    kwargs['xdestra']=max(x)
  def caso1(x,y,sy):
      delta=N*somma(potenza(x,2))-(somma(x))**2
      intercetta=(1/delta)*(somma(potenza(x,2))*somma(y)-somma(x)*somma(moltiplica(x,y)))
      pendenza=(1/delta)*(N*somma(moltiplica(x,y))-somma(x)*somma(y))
      erroreintercetta=sy*((somma(potenza(x,2))/delta)**0.5)
      errorependenza=sy*((N/delta)**0.5)
      if kwargs['plot']==True:
        import matplotlib.pyplot as plt
        lex=np.array([kwargs['xsinistra']*scalasinistra,kwargs['xdestra']*scaladestra])
        ley=pendenza*lex + intercetta
        plt.plot(lex,ley,**opzioniplot)
      return [[intercetta,erroreintercetta],[pendenza,errorependenza]]
  def caso2(x,y,sy):
      delta=somma(moltiplica(1,potenza(sy,-2)))*somma(moltiplica(potenza(x,2),potenza(sy,-2)))-(somma(moltiplica(x,potenza(sy,-2))))**2
      intercetta=(1/delta)*(somma(moltiplica(potenza(x,2),potenza(sy,-2)))*somma(moltiplica(y,potenza(sy,-2)))-somma(moltiplica(x,potenza(sy,-2)))*somma(moltiplica(x,y,potenza(sy,-2))))
      pendenza=(1/delta)*(somma(moltiplica(1,potenza(sy,-2)))*somma(moltiplica(x,y,potenza(sy,-2)))-somma(moltiplica(x,potenza(sy,-2)))*somma(moltiplica(y,potenza(sy,-2))))
      erroreintercetta=((1/delta)*somma(moltiplica(potenza(x,2),potenza(sy,-2))))**0.5
      errorependenza=((1/delta)*somma(moltiplica(1,potenza(sy,-2))))**0.5
      if kwargs['plot']==True:
        import matplotlib.pyplot as plt
        lex=np.array([kwargs['xsinistra']*scalasinistra,kwargs['xdestra']*scaladestra])
        ley=pendenza*lex + intercetta
        plt.plot(lex,ley,**opzioniplot)
      return [[intercetta,erroreintercetta],[pendenza,errorependenza]]
  def caso3(x,sx,y,sy):
      if isinstance (sy, (float, int)):
          retta=caso1(x,y,sy)
      if not isinstance (sy, (float, int)):
          retta=caso2(x,y,sy)
      b=retta[1][0]

      if isinstance(sy,(int, float)):
          incertezzasingola=sy
          sy=[]
          for c in range(0,len(x)):
              sy.append(incertezzasingola)

      if isinstance(sx,(int, float)):
          incertezzasingola=sx
          sx=[]
          for c in range(0,len(x)):
              sx.append(incertezzasingola)
      if len(sy) != len(x):
          raise ValueError('il numero di incertezze inserite per le misure in ordinata è diverso dalla numerosità delle misure')
      if len(sx) != len(x):
          raise ValueError('il numero di incertezze inserite per le misure in ascissa è diverso dalla numerosità delle misure')
      if len(sx) != len(x) or len(sy) != len(x):
          print('controlla i dati e riprova')
          return 
      si=potenza(somma(potenza(sy,2),moltiplica(b**2,potenza(sx,2))),0.5)
      delta=somma(moltiplica(1,potenza(si,-2)))*somma(moltiplica(potenza(x,2),potenza(si,-2)))-(somma(moltiplica(x,potenza(si,-2))))**2
      intercetta=(1/delta)*(somma(moltiplica(potenza(x,2),potenza(si,-2)))*somma(moltiplica(y,potenza(si,-2)))-somma(moltiplica(x,potenza(si,-2)))*somma(moltiplica(x,y,potenza(si,-2))))
      pendenza=(1/delta)*(somma(moltiplica(1,potenza(si,-2)))*somma(moltiplica(x,y,potenza(si,-2)))-somma(moltiplica(x,potenza(si,-2)))*somma(moltiplica(y,potenza(si,-2))))
      erroreintercetta=((1/delta)*somma(moltiplica(potenza(x,2),potenza(si,-2))))**0.5
      errorependenza=((1/delta)*somma(potenza(si,-2)))**0.5
      if kwargs['plot']==True:
        import matplotlib.pyplot as plt
        lex=np.array([kwargs['xsinistra']*scalasinistra,kwargs['xdestra']*scaladestra])
        ley=pendenza*lex + intercetta
        plt.plot(lex,ley,**opzioniplot)
      return [[intercetta,erroreintercetta],[pendenza,errorependenza]]
  if kwargs['origine']==True:
    if isinstance(sy,(int, float)):
        incertezzasingola=sy
        sy=[]
        for c in range(0,len(x)):
          sy.append(incertezzasingola)
    if sx==0:
      if isinstance(sx,(int, float)):
          incertezzasingola=sx
          sx=[]
          for c in range(0,len(x)):
              sx.append(incertezzasingola)
      from scipy.optimize import curve_fit
      def funzione(x,a):
        return x*a
      parametri, covarianza=curve_fit(funzione,x,y,sigma=sy,absolute_sigma=True)
      if kwargs['plot']==True:
        import matplotlib.pyplot as plt
        lex=np.array([kwargs['xsinistra']*scalasinistra,kwargs['xdestra']*scaladestra])
        ley=parametri[0]*lex
        plt.plot(lex,ley,**opzioniplot)
      return [[0,0],[parametri[0],covarianza[0][0]**0.5]]
    else:
      from scipy.odr import Model,RealData,ODR
      def funzione(parametri,x):
        return parametri[0]*x
      rettaa=caso3(x,sx,y,sy)
      modello=Model(funzione)
      data=RealData(x,y,sx=sx,sy=sy)
      odr = ODR(data, modello, beta0=[rettaa[1][0]])
      result = odr.run()
      if kwargs['plot']==True:
        import matplotlib.pyplot as plt
        lex=np.array([kwargs['xsinistra']*scalasinistra,kwargs['xdestra']*scaladestra])
        ley=result.beta[0]*lex
        plt.plot(lex,ley,**opzioniplot)
      return [[0,0],[result.beta[0],result.sd_beta[0][0]]]



  if sx == 0 and isinstance (sy, (float,int)):
      return caso1(x,y,sy)

  if sx == 0 and not isinstance (sy, (float,int)):
      if len(sy) != len(x):
          mess='''
          il numero di incertezze inserite per le misure in ordinata è diverso dalla numerosità delle misure.
          se le misure in ordinata hanno tutte la stessa incertezza è possibile insererire il singolo valore in argomento.
          '''
          raise ValueError(mess)
          return 
      return caso2(x,y,sy)

  else:
      return caso3(x,sx,y,sy)

#ERRORE A POSTERIORI per RETTA:
def posterioriretta(x,y,retta):
  x=np.array(x)
  attese=x*retta[1][0]+retta[0][0]
  return ((somma(potenza(somma(y,moltiplica(attese,-1)),2)))/(len(x)-2))**0.5


#ESPORTA SU EXCEL: metti in input una lista (lista di liste o una lista semplice), un array, una matrice ecc e le salva in un file excel.
#                  SINTASSI:  excel(lista,'nomefile')
#                      ESEMPIO:  excel (lista, 'ciao' )


def excel(lista, stringa):
  nomefile=stringa + '.xlsx'
  if isinstance (lista[0],(int, float)):
    df = pd.DataFrame(lista)
    return  df.to_excel(nomefile, index=False)
  else:
    df = pd.DataFrame(lista).transpose()
    return  df.to_excel(nomefile, index=False)

def minimirelativi(lista,**kwargs):
    import numpy as np
    if not 'contrario' in kwargs:
        kwargs['contrario']=False
    if not 'soglia' in kwargs:
        kwargs['soglia']=1
    if not 'indici' in kwargs:
        kwargs['indici']=False
    if not 'fontsize' in kwargs:
        kwargs['fontsize']=12
    indici=[]
    minimi=[]
    for c in range(kwargs['soglia'], len(lista)-kwargs['soglia']):
        if lista[c+1]>lista[c] and lista[c-1]>lista[c] and lista[c+kwargs['soglia']]>lista[c] and lista[c-kwargs['soglia']]>lista[c]:
            indici.append(c)
            minimi.append(lista[c])
    if kwargs['contrario']==True:
        indici.reverse()
        minimi.reverse()
    if 'plot' in kwargs:
        x=np.array(kwargs['plot'])
        y=np.array(lista)
        x1=x[indici]
        y1=y[indici]
        #plt.errorbar(x1,y1,yerr=max(y)*0.1,elinewidth=0.5,fmt='None',color='purple')
        plt.plot(x,y)
        for c in range(len(x1)):
          testo=f'{c}'
          plt.text(x1[c],y1[c],testo,fontsize=kwargs['fontsize'],ha='center',va='bottom',color='purple')
    if kwargs['indici']==True:
        return np.array(indici)
    else:
        return minimi



def massimirelativi(lista,**kwargs):
    import numpy as np
    if not 'contrario' in kwargs:
        kwargs['contrario']=False
    if not 'soglia' in kwargs:
        kwargs['soglia']=1
    if not 'indici' in kwargs:
        kwargs['indici']=False
    if not 'fontsize' in kwargs:
        kwargs['fontsize']=12
    indici=[]
    massimi=[]
    for c in range(kwargs['soglia'], len(lista)-kwargs['soglia']):
        if lista[c+1]<lista[c] and lista[c-1]<lista[c] and lista[c+kwargs['soglia']]<lista[c] and lista[c-kwargs['soglia']]<lista[c]:
            indici.append(c)
            massimi.append(lista[c])
    if kwargs['contrario']==True:
        indici.reverse()
        massimi.reverse()
    if 'plot' in kwargs:
        x=np.array(kwargs['plot'])
        y=np.array(lista)
        x1=x[indici]
        y1=y[indici]
        #plt.errorbar(x1,y1,yerr=max(y)*0.1,elinewidth=0.5,fmt='None',color='purple')
        plt.plot(x,y)
        for c in range(len(x1)):
          testo=f'{c}'
          plt.text(x1[c],y1[c],testo,fontsize=kwargs['fontsize'],ha='center',va='bottom',color='purple')
    if kwargs['indici']==True:
        return np.array(indici)
    else:
        return massimi





#SUONA: fa partire un suono mettendo il link del download del suono in argomento
#   SINTASSI: suona('www.ciao.mp3')
#   trovare link suoni: trovate un suono e lo scaricate, dal browser: tasto destro nel file scaricato e fate copia link download (almeno da edge)
def suona(link):
  presente=False
  suoni = {}
  suoni['capra'] = 'https://cdn.pixabay.com/download/audio/2023/11/20/audio_6d2ecb8b19.mp3?filename=goat-sound-177346.mp3'
  suoni['risposta corretta'] = 'https://cdn.pixabay.com/download/audio/2021/08/04/audio_bb630cc098.mp3?filename=short-success-sound-glockenspiel-treasure-video-game-6346.mp3'
  for c, d in suoni.items():
    if link==c:
      link=d
      presente=True
  elenco = ', '.join("'{0}'".format(key) for key in suoni.keys()) + '.'
  if link=='elenco':
    print('l\'elenco dei suoni disponibili è:', elenco)
    return
  if isinstance(link, str) and presente==False:
    raise ValueError('Questo suono non è stato ancora aggiunto, per visualizzare l\'elenco con tutti i suoni metti in argomento \'elenco\'')
    return
  response = requests.get(link)
  audio_data = BytesIO(response.content)
  display(Audio(data=audio_data.read(), autoplay=True))
  
      


#MEDIA PESATA fra misure:
#                         è possibile  inserire in argomento le singole misure e incertezze o le 2 liste contenti le misure e le incertesze
#
#             COSA RITORNA: ritorna la seguente lista [mediapesata,incertezzamediapesata]
#             SINTASSI:
#                      singole misure:
#                                      mediapesata(x1,sx1,x2,sx2,x3,sx3....)
#
#                      liste:
#                                      mediapesata(x,sx)
#
#             ESEMPIO:
#                     b = mediapesata(x,sx)
#                     media_pesata = b[0]
#                     incertezza_media_pesata = b[1]

def mediapesata(*argo):
    arg=list(argo)
    if isinstance (arg[0],(int, float)):
        x=[]
        sx=[]
        for c in range (0,int(len(arg)),2):
            x.append(arg[c])
        for b in range (1,int(len(arg)),2):
            sx.append(arg[b])
        arg=[]
        arg.append(x)
        arg.append(sx)
    if isinstance (arg[1],(int,float)):
      sx=arg[1]
      lista=[]
      for h in range(0,len(arg[0])):
        lista.append(sx)
      arg[1]=lista
    k=somma(potenza(arg[1],-2))
    sx_mp=(1/k)**0.5
    x_mp=(1/k)*somma(moltiplica(arg[0],potenza(arg[1],-2)))
    return [x_mp,sx_mp]



#COMPATIBILITÀ           fra misure (con eventuale media pesata):
#
#              IN BREVE: calcola la compatibilità ed in caso positivo può farne la media pesata (in tal caso la soglia di compatibilità di default è 3) (vedi parte KEYWORDS!!!)
#                        è possibile inserire i dati sia in liste (o oggetti simili) che singolarmente (vedi parte SINTASSI)
#
#              SINTASSI:
#                        singolarmente:
#                                     compatibilità(x1,sx1,x2,sx2.....,keywords....)
#                        liste/array e oggetti simili:
#                                     compatibilità(x,sx,keywords...)
#
#              KEYWORDS: in argomento, una volta inserite le misure, sono disponibili varie keywords da poter utilizzare in ordine arbitrario.
#                        ESEMPIO KEYWORDS:
#                                         compatibilità(x,sx,soglia=2,mediapesata=True,mostratuttegruppo=True)
#
#                        mediapesata=True  --->  inserendola la funzione compatibilità ritornerà la media pesata ([mediapesata,erroremediapesata])
#                                                oltre a stamparne il risultato.
#                                                la media pesata viene calcolata tra le misure che hanno una compatibilità inferiore alla soglia
#                                                la soglia impostata di default è 3 ma puo essere cambiata con la specifica keyword
#
#                        soglia=valore_soglia_che_si_vuole ---> imposta il valore della soglia cioè quel valore per cui una misura
#                                                                 (due misure, dipende in che parte del processo si è...) viene scartata
#                                                                 dal calcolo della media pesata cioè se la sua compatibilità risulta essere maggiore della soglia
#
#                        mostratutte=True ---> mostra le singole compatibilità tra tutte le misure
#
#                        mostratutteconsoglia=True ---> mostra le singole compatibilità che sono sotto la soglia
#
#                        mostratuttegruppo=True ----> nel caso si inseriscano piu di 2 misure mostra le singole compatibilià all'interno del gruppo più numeroso di misure compatibili (vedi parte ECCEZIONI)
#
#                        mostragruppi=True ----> mostra tutti i gruppi di misure tra di loro compatibil
#
#               ECCEZIONI e approfondimenti:
#                        se in input inseriamo piu di 2 misure la funzione riporterà il gruppo più numeroso ('gruppo vincente') di misure fra di loro tutte compatibili (entro la soglia)
#                        e quindi eventualmente fare la media pesata di quelle misure (se mediapesata=True)
#                        capita non raramente però che ci siano due o più 'gruppi vincenti' cioè che hanno la stessa numerosità.
#                        in questo caso la funzione calcolerà il valore della compatibilità media per ogni gruppo e quindi sceglierà come vincente quella con il valore minore.
#                        poi da quest'ultimo verrà calcolata la media pesata
#                        in ogni caso verrano stampati tutti i gruppi vincenti con i loro errori nel caso possano essere utili.
def compatibilità(*argomento,**kargs):
    if not 'mostragruppi' in kargs:
        kargs['mostragruppi']=False
    if not 'mostratuttegruppo' in kargs:
        kargs['mostratuttegruppo']=False
    if not 'mediapesata' in kargs:
        kargs['mediapesata']=False
    if not 'mostratutte' in kargs:
        kargs['mostratutte']=False
    if not 'mostratutteconsoglia' in kargs:
        kargs['mostratutteconsoglia']=False
    if not 'soglia' in kargs:
        kargs['soglia']=3
    args=list(argomento)
    if isinstance (args[0],(int, float)):
        x=[]
        sx=[]
        for c in range (0,int(len(args)),2):
            x.append(args[c])
        for b in range (1,int(len(args)),2):
            sx.append(args[b])
        args=[]
        args.append(x)
        args.append(sx)
    if len(args[0]) != len(args[1]):
       return print('la lista delle misure e la lista dei loro errori hanno lunghezze diverse')
    if len(args[0])==2:
        c=(abs(args[0][0]-args[0][1]))/((args[1][0]**2+args[1][1]**2)**0.5)
        print('la compatibilità tra le due misure è:',c)
        if c < kargs['soglia'] and kargs['mediapesata']==True:
            mp=mediapesata(args[0],args[1])
            print('la loro media pesata è:', mp[0],'con incertezza sulla media pesata: ', mp[1])
        if c > kargs['soglia'] and kargs['mediapesata']==True:
            print('le due misure non sono compatibili con una la soglia di compatibilità pari a',kargs['soglia'],'quindi non è ragionevole effettuare una media pesata')
        return
    gruppi=[]
    gruppiincertezze=[]
    gruppicompatibilità=[]
    for r in range (0,len(args[0])):
        gruppi.append([])
        gruppiincertezze.append([])
    for f in range(0,len(args[0])):
        gruppi[f].append(args[0][f])
        gruppiincertezze[f].append(args[1][f])
        for d in range (0,len(args[0])):
            c=(abs(args[0][f]-args[0][d]))/((args[1][f]**2+args[1][d]**2)**0.5)
            if c != 0 and c < kargs['soglia']:
                gruppi[f].append(args[0][d])
                gruppiincertezze[f].append(args[1][d])
        for d in range (f,len(args[0])):
            c=(abs(args[0][f]-args[0][d]))/((args[1][f]**2+args[1][d]**2)**0.5)
            if c != 0 and kargs['mostratutte']==True:
                print('la compatibilità tra', args[0][f], 'e' ,args[0][d], 'è:',c)
            if c != 0 and kargs['mostratutteconsoglia']==True and c < kargs['soglia']:
                print('la compatibilità tra', args[0][f], 'e' ,args[0][d], 'è:',c)
    import copy

    copiagruppi=copy.deepcopy(gruppi)
    copiagruppiincertezze=copy.deepcopy(gruppiincertezze)
    for f in range(0,len(copiagruppi)):
        for u in range (1,len(copiagruppi[f])):
            for s in range (2,(len(copiagruppi[f]))):
                c=(abs(copiagruppi[f][u]-copiagruppi[f][s]))/((copiagruppiincertezze[f][u]**2+copiagruppiincertezze[f][s]**2)**0.5)
                if c > kargs['soglia']:
                    gruppi[f][u]=0
                    gruppi[f][s]=0
                    gruppiincertezze[f][u]=0
                    gruppiincertezze[f][s]=0
        while 0 in gruppi[f]:
            gruppi[f].remove(0)
        while 0 in gruppiincertezze[f]:
            gruppiincertezze[f].remove(0)
    sommegruppi=[]
    indici2=[]
    for e in range(0,len(gruppi)):
        sommegruppi.append(sum(gruppi[e]))
    for h in range(0,len(sommegruppi)):
        for g in range (h+1,len(sommegruppi)):
            if sommegruppi[g]==sommegruppi[h]:
                indici2.append(g)
    for d in indici2:
        gruppi[d]=0
        gruppiincertezze[d]=0
    while 0 in gruppi:
        gruppi.remove(0)
    while 0 in gruppiincertezze:
        gruppiincertezze.remove(0)
    if kargs['mostragruppi']==True:
        print(gruppi)
    maggiornumerosità=0
    indicegruppovincente=0
    gruppinumerositàuguale=[]
    gruppinumerositàuguale.append(0)

    for g in range(len(gruppi)):
        if len(gruppi[g]) == maggiornumerosità and len(gruppi[g]) != 1:
            gruppinumerositàuguale.append(len(gruppi[g]))
            comp1=[]
            compvincente=[]
            for o in range(0,len(gruppi[g])):
                for r in range (o+1,len(gruppi[g])):
                    c=(abs(gruppi[g][o]-gruppi[g][r]))/((gruppiincertezze[g][o]**2+gruppiincertezze[g][r]**2)**0.5)
                    comp1.append(c)
            for o in range(0,len(gruppi[indicegruppovincente])):
                for r in range (o+1,len(gruppi[indicegruppovincente])):
                    c=(abs(gruppi[indicegruppovincente][o]-gruppi[indicegruppovincente][r]))/((gruppiincertezze[indicegruppovincente][o]**2+gruppiincertezze[indicegruppovincente][r]**2)**0.5)
                    compvincente.append(c)
            if sum(comp1)/len(comp1) < sum(compvincente)/len(compvincente):
                maggiornumerosità=len(gruppi[g])
                indicegruppovincente=g
                compvincente=comp1
                gruppinumerositàuguale.pop()
        if len(gruppi[g]) > maggiornumerosità:
            maggiornumerosità=len(gruppi[g])
            indicegruppovincente=g
    gruppiNuguale=[]
    gruppiincertezzeNuguale=[]
    for y in range(0,len(gruppi)):
        if len(gruppi[y])==maggiornumerosità:
            gruppiNuguale.append(gruppi[y])
            gruppiincertezzeNuguale.append(gruppiincertezze[y])
    if maggiornumerosità==1:
        print('non sono state trovate misure compatibili sotto la soglia di', kargs['soglia'])
        return
    if max(gruppinumerositàuguale)==len(gruppi[indicegruppovincente]):
        print('non si è trovato un gruppo di misure fra di loro compatibili con una numerosità maggiore rispetto a tutti gli altri')
        print('cioè, fra i gruppi con numerosità maggiore di tutti gli altri, due o più gruppi hanno numerosità uguale')
        print('tali gruppi sono',gruppiNuguale)
        print('con le rispettive incertezze',gruppiincertezzeNuguale)
        print('')
        print('tra questi è stato scelto il gruppo il quale valore medio delle compatibilità fosse minore (quindi migliore)')
        print('rispetto a quelle degli altri gruppi mostrati:')
        print('')
        print('il gruppo di misure in questione è',gruppi[indicegruppovincente],'con misure compatibili fra loro sotto la soglia di',kargs['soglia'])
        print('la compatibilità media fra le misure del gruppo è:',sum(compvincente)/(len(compvincente)))
        print('')
        print('')
    else:
        comp2=[]
        for o in range(0,len(gruppi[indicegruppovincente])):
            for r in range (o+1,len(gruppi[indicegruppovincente])):
                c=(abs(gruppi[indicegruppovincente][o]-gruppi[indicegruppovincente][r]))/((gruppiincertezze[indicegruppovincente][o]**2+gruppiincertezze[indicegruppovincente][r]**2)**0.5)
                comp2.append(c)
        print('il gruppo più numeroso di misure compatibili tra loro è:',gruppi[indicegruppovincente], 'tutte con una compatibilità inferiore al valore soglia', kargs['soglia'])
        print('la media delle compatibilità fra le misure del gruppo è:',sum(comp2)/(len(comp2)))
    if kargs['mostratuttegruppo']==True:
        for t in range (0,len(gruppi[indicegruppovincente])):
            for r in range (t+1,len(gruppi[indicegruppovincente])):
                c=(abs(gruppi[indicegruppovincente][t]-gruppi[indicegruppovincente][r]))/((gruppiincertezze[indicegruppovincente][t]**2+gruppiincertezze[indicegruppovincente][r]**2)**0.5)
                print('la compatibilità tra',gruppi[indicegruppovincente][t],'e',gruppi[indicegruppovincente][r],'è:',c)
    if kargs['mediapesata']==True:
        mp=mediapesata(gruppi[indicegruppovincente],gruppiincertezze[indicegruppovincente])
        print('')
        print('la media pesata delle misure nel gruppo è',mp[0],'con incertezza sulla media pesata pari a:',mp[1])
        return([mp[0],mp[1]])




# type: ignore
