# Image and EXIF Viewer
Programming assignment per il corso di Human Computer Interaction tenuto dal prof. Andrew D. Bagdanov e previsto dal corso di laurea magistrale in Ingegneria Informatica dell'Università degli Studi di Firenze, A.A. 2021/2022. \
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
Il modello è implementato nella relativa classe `Model`. Nello specifico serve per tenere traccia dei dati memorizzati dall'applicazione, dove questi non sono altro che le immagini che l'utente carica dal proprio computer. Inoltre definisce tutte quelle operazioni che richiedono la manipolazione di suddette immagini e che sono utili ai fini dell'estrazione dei metadati.

### View
La vista è presente all'interno della classe `View` e implementa la finestra dell'applicazione. Questa classe definisce tutte le componenti che concorrono alla realizzazione dell'applicazione e in particolare fa uso dei file presenti all'interno della cartella `utils`, ovvero:
1) `ImageView`: classe utile per mostrare l'immagine selezionata dall'utente nella lista delle immagini.
2) `ImageList`: classe necessaria per realizzare la coda delle immagini caricate dall'utente dentro l'applicativo.
3) `TableData`: custom widget che permette all'utente di visualizzare le informazioni generali e i dati EXIF dell'immagine selezionata.

### Controller
Il controller è implementato nell'omonima classe `Controller` ed ha il compito di fare comunicare la vista con il modello. Nello specifico si fa carico delle interazioni che l'utente ha con la finestra dell'applicazione e provvede a richiamare opportunamente le relative operazioni del modello.

## Applicazione
Di seguito è riportato uno screenshot della finestra dell'applicazione in funzione, insieme alle principali feature implementate. Altre immagini sono consultabili [qui](https://github.com/CosimoGiani/Image_EXIF_viewer/tree/main/screenshots).

<div align="center">
    <img src="https://github.com/CosimoGiani/Image_EXIF_viewer/blob/main/screenshots/screenshot_exif.png">
  </div>

#### Aggiungere immagini dal proprio computer
Premendo sul tasto `Aggiungi immagine` l'utente è in grado di caricare una immagine dal proprio dispositivo. Per rendere l'applicazione più user-friendly è stato associato a suddetto bottone la shortcut `Ctrl+o`, così che l'apertura della finestra per la selezione delle immagini sia più immediata.

#### Possibilità di vedere e gestire una coda di immagini
Una volta che l'immagine è stata selezionata e aperta ne verrà caricata un'anteprima all'interno di una lista, dentro la quale verranno inserite le eventuali successive foto che l'utente desidererà caricare. Questa coda permette dunque di poter visualizzare più immagini tra le quali poter scegliere.

#### Visualizzare le immagini caricate
L'utente può quindi visualizzare un'immagine tra quelle caricate all'interno della lista semplicemente selezionandone una dalla coda. Con un semplice click è possibile dunque vedere la foto in maniera più dettagliata. 

#### Rimuovere singole immagini
Qualora l'utente non desiderasse più tenere nella propria lista un'immagine gli sarà sufficiente selezionarla dalla coda e quindi premere l'opportuno bottone `Rimuovi immagine`: l'immagine verrà rimossa dalla lista, così come dalla corrente visualizzazione. Anche in questo caso a questo tasto è stata associata una shortcut, ovvero è sufficiente premere sulla propria tastiera `Ctrl+d` per eliminare l'immagine selezionata.

#### Eliminare l'intera coda

#### Visualizzare le informazioni e i dati EXIF delle immagini

#### Scorrere la lista delle immagini

#### Rescaling

#### Rotazione delle immagini

#### Geolocalizzazione

## Note
Ai fini di una più profonda comprensione dell'implementazione dell'applicazione, il codice è stato documentato in maniera opportuna. Si rimanda pertanto ad una lettura
del codice stesso per ulteriori chiarimenti.
