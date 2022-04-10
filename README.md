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
| **PyQt5**      |     >= 5.15.0    |
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
* `ImageView`: classe utile per mostrare l'immagine selezionata dall'utente nella lista delle immagini.
* `ImageList`: classe necessaria per realizzare la coda delle immagini caricate dall'utente dentro l'applicativo.
* `TableData`: custom widget che permette all'utente di visualizzare le informazioni generali e i dati EXIF dell'immagine selezionata.

### Controller
Il controller è implementato nell'omonima classe `Controller` ed ha il compito di fare comunicare la vista con il modello. Nello specifico si fa carico delle interazioni che l'utente ha con la finestra dell'applicazione e provvede a richiamare opportunamente le relative operazioni del modello.

## Applicazione
Di seguito è riportato uno screenshot della finestra dell'applicazione in funzione, insieme alle principali feature implementate. Altre immagini sono consultabili [qui](https://github.com/CosimoGiani/Image_EXIF_viewer/tree/main/screenshots).

<div align="center">
    <img src="https://github.com/CosimoGiani/Image_EXIF_viewer/blob/main/screenshots/screenshot_exif.png">
  </div>

#### Aggiungere immagini dal proprio computer
Premendo sul tasto `Aggiungi immagine` l'utente è in grado di caricare un'immagine dal proprio dispositivo. Per rendere l'applicazione più user-friendly è stato associato a suddetto bottone la shortcut `Ctrl+o`, così che l'apertura della finestra per la selezione delle foto sia più immediata.

#### Possibilità di vedere e gestire una coda di immagini
Una volta che l'immagine è stata selezionata e aperta ne verrà caricata un'anteprima all'interno di una lista, dentro la quale verranno inserite le eventuali successive foto che l'utente desidererà caricare. Questa coda permette dunque di poter visualizzare più immagini tra le quali poter scegliere.

#### Visualizzare le immagini caricate
L'utente può quindi visualizzare un'immagine tra quelle caricate all'interno della lista semplicemente selezionandone una dalla coda. Con un semplice click è possibile dunque vedere la foto in maniera più dettagliata. 

#### Rimuovere singole immagini
Qualora l'utente non desiderasse più tenere nella propria lista un'immagine, gli sarà sufficiente selezionarla dalla coda e quindi premere il bottone `Rimuovi immagine`: questa verrà rimossa dalla lista, così come dalla corrente visualizzazione. Anche in questo caso a questo tasto è stata associata una shortcut, ovvero è sufficiente premere sulla propria tastiera `Ctrl+d` per eliminare l'immagine selezionata.

#### Eliminare l'intera coda
Prememendo sul bottone `Svuota tutto` sarà possibile per l'utente eliminare qualsiasi foto dalla lista delle immagini. La shortcut per questa operazione è il tasto `canc` della propria tastiera.

#### Visualizzare le informazioni e i dati EXIF delle immagini
Scopo di questo progetto è l'estrazione dei dati EXIF dalle immagini. A tal fine una volta che l'utente ha selezionato una foto dalla coda, questa gli risulterà visibile con maggior dettaglio, ma soprattutto l'applicazione provvederà a mostrare e organizzare i metadati estratti in apposite pagine tab. Nello specifico sono state implementate due pagine: una per le **Info generali**, ovvero le proprietà generali dell'immagine, e una per i **dati EXIF**. Qualora la quantità di metadati da mostrare risultasse eccessiva per la dimensione della finestra, la tab provvederà a fornire una pagina con una barra laterale per lo scorrimento. Anche in questo caso è stato deciso di implementare una shortcut per il passaggio da una tab all'altra: l'utente premendo il solo tasto `Tab` potrà comodamente alternare la vista di una delle due pagine senza dover necessariamente cliccare sulla tab di interesse per la visualizzazione delle informazioni.

#### Scorrere la lista delle immagini
Se l'utente ha caricato più di una immagine dentro l'applicazione può decidere di cambiare foto di cui visualizzare dettagli e informazioni selezionando semplicemente un'altra immagine dalla lista. In alternativa sono stati implementati due bottoni con i quali è possibile scorrere la coda verso sinistra, tasto `Freccia sinistra`, e verso destra, tasto `Freccia destra`, entrambi situati nella parte inferiore della finestra: una volta che un'immagine è stata selezionata dalla lista, l'utente sarà abilitato a cambiare la foto corrente premendo su uno di questi due bottoni. Per rendere l'applicazione più user-friendly a queste operazioni sono state associate rispettivamente le shortcut tasti freccia `sinistra` e `destra`.

#### Rescaling
Un'altra caratteristica che l'applicazione possiede è la capacità di scalare la sua dimensione in maniera opportuna: qualora l'utente decida di ridimensionare la finestra, l'interfaccia si adatterà di conseguenza e l'immagine correntemente visualizzata (se presente) scalerà appropriatamente.

#### Rotazione delle immagini
Una delle feature implementate prevede invece la possibilità di ruotare l'immagine correntemente selezionata: facendo ausilio dei tasti situati nella parte inferiore della finestra l'utente sarà in grado di ruotare l'immagine visualizzata di 90° in senso orario e antiorario. In questo caso le shortcut assegnate sono i tasti freccia `su` e `giù` rispettivamente per la rotazione oraria e antioraria. 

#### Geolocalizzazione
Se l'immagine selezionata tra i dati EXIF presenta informazioni relative alla geolocalizzazione GPS, l'applicazione permetterà all'utente di aprire il proprio browser con una pagine di Google Maps centrata alle coordinate GPS dell'immagine. Per questo motivo è stato implementato il bottone `Apri mappa`: cliccandolo, se i dati di geolocalizzazione sono presenti, sarà elaborata una query Google Maps che verrà aperta sul browser dell'utente; altrimenti se tali informazioni sono mancanti l'applicazione farà comparire un messaggio di errore. Anche in questo caso è stata associata al bottone una shortcut, ovvero `Ctrl+m`.

## Note
Ai fini di una più profonda comprensione dell'implementazione dell'applicazione, il codice è stato documentato in maniera opportuna. Si rimanda pertanto ad una lettura
del codice stesso per ulteriori chiarimenti.
