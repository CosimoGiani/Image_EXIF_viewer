# Image and EXIF Viewer
Programming assignment per il corso di Human Computer Interaction tenuto dal prof. Andrew D. Bagdanov e previsto dal corso di laurea magistrale in Ingegneria Informatica 
dell'Università degli Studi di Firenze, A.A. 2021/2022. \
Il progetto consiste in una semplice applicazione che permette di visualizzare i dati EXIF delle immagini caricate dal proprio computer. \
\
Le immagini sono ovunque, in grandi quantità e in una grossa varietà di formati. Con la consapevolezza che questi numeri sarebbero continuati a crescere nel corso del 
tempo si è resa necessaria l'introduzione di uno standard comune per lo scambio dei metadati delle immagini digitali. \
Da qui la nascita di **EXIF** (Exchangeable Image File Format), una specifica per il formato di queste immagini.

## Tecnologie utilizzate
Il progetto è stato implementato in linguaggio `Python`. Nello specifico le dipendenze usate dall'applicazione sono le seguenti:
| Package        | Versione       |
| -------------- |:--------------:|
| **Python**     |       3.7      |
| **PyQt5**      |     >= 5.15    |
| **Pillow**     |      9.1.0     |

Altre versioni di queste librerie non sono state testate. Nonostante questo, con semplici accorgimenti l'applicazione dovrebbe comunque funzionare senza problemi.

## Implementazione
Per l'implementazione dell'applicazione è stato fatto uso di `Python`, congiuntamente al pattern architetturale **MVC** (**M**odel-**V**iew-**C**ontroller).\
La libreria `PyQt5` è servita per la realizzazione dell'interfaccia grafica, mentre `Pillow` ha reso possibile la lettura e l'estrazione del contenuto delle immagini
da file.

### Model
Il modello è implementato nell'omonima classe `Model`. Nello specifico serve per tenere traccia dei dati memorizzati dall'applicazione, dove questi non sono altro che
le immagini che l'utente carica dal proprio computer. Inoltre definisce tutte quelle operazioni che richiedono la manipolazione di suddette immagini e che sono utili
ai fini dell'estrazione dei metadati.

### View
La vista è presente all'interno della classe `View` e definisce la finestra dell'applicazione. Questa classe definisce tutte le componenti che concorrono alla realizzazione
dell'applicazione e in particolare fa uso dei file presenti all'interno della cartella `utils`, ovvero:
1) `ImageView`: classe utile per mostrare l'immagine selezionata dall'utente nella lista delle immagini.
2) `ImageList`: classe necessaria per realizzare la coda delle immagini caricate dall'utente dentro l'applicativo.
3) `TableData`: custom widget che permette all'utente di visualizzare le informazioni generali e i dati EXIF dell'immagine selezionata. 

### Controller

## Applicazione

## Note
Ai fini di una più profonda comprensione dell'implementazione dell'applicazione, il codice è stato documentato in maniera opportuna. Si rimanda pertanto ad una lettura
del codice stesso per ulteriori chiarimenti.
