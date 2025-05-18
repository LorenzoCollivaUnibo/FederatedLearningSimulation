# FederateLearningSimulation


Risultati degli esperimenti:

1 Risultati dell'esecuzione del codice di Federate Learning con 2 client che si suddividono equamente il dataset

n batch client 1:  234

n batch client 2:  235

<img src="test_accuracy_rounds1.png" width="500" height="300" />

Da questo grafico si evince un andamento relativamente costante nella metrica di accuracy, che aumenta per ogni round.
Un significativo miglioramento dell'accuracy avvviene dal 2° al 5° round, mente dal 5° al 10° round si evince un costante miglioramento ma con una curva meno pendente rispetto ai precenti round.
Nel complesso, dato il numero di client, e il numero di batch assegnati ad ogni client, permettono una fase di training efficace che si riflette poi nel modello globale.



2 Risultati dell'esecuzione del codice di Federate Learning con 5 client che si suddividono equamente il dataset

n_client:  5

client 0 num batch: 94

client 1 num batch: 94

client 2 num batch: 94

client 3 num batch: 94

client 4 num batch: 93

<img src="test_accuracy_rounds2.png" width="500" height="300" />

In questo esperimento si verifica un miglioramento dell'accuracy molto elevato per i primi due round, mentre per i successivi si verifica un costante, ma sempre più piccolo, miglioramento dell'accuracy che porta ad un risultato poco oltre al 94% come nell'esperimento precedente.
Si evince che con l'avanzare dei round l'accuracy aumenta sempre di meno rispetto al round precedente.


3 Risultati dell'esecuzione del codice di Federate Learning con 5 client che si suddividono randomicamente il dataset

n_client:  5

num_batch_train_elements:  469

client 0 num batch: 179

client 1 num batch: 86

client 2 num batch: 189

client 3 num batch: 3

client 4 num batch: 12

<img src="test_accuracy_rounds3.png" width="500" height="300" />

In questo esperimento invece si nota un andamento molto meno costante rispetto agli esperimenti precedenti, probablimente a causa del numero di batch assegnati in modo randomico ai client, portando alcuni di essi ad allenare quasi 200 batch mentre nel caso peggiore limitandosi al training di 3 batch. 
Questa suddivisione del dataset porta ad un risultato finale molto simile agli esperimenti precedenti, anche se con un andamento dell'accuracy, round per round, molto diverso rispetto ai precedenti, caratterizzato da picchi soprattutto per il 2°, 5°, 7° round, in termini di aumento dell'accuracy e gli altri round invece meno significativi (con però sempre un miglioramento anche se di poco dell'accuracy)








Di seguito riporto i grafici di 14 test con un numero di client che varia per ogni test:

<p float="left">
  <img src="chart1.png" width="500" height="300" />
  <img src="chart2.png" width="500" height="300" />
  <img src="chart3.png" width="500" height="300" />
  <img src="chart4.png" width="500" height="300" />
  <img src="chart5.png" width="500" height="300" />
  <img src="chart6.png" width="500" height="300" />
  <img src="chart7.png" width="500" height="300" />
  <img src="chart8.png" width="500" height="300" />
  <img src="chart9.png" width="500" height="300" />
  <img src="chart10.png" width="500" height="300" />
  <img src="chart11.png" width="500" height="300" />
  <img src="chart12.png" width="500" height="300" />
  <img src="chart13.png" width="500" height="300" />
  <img src="chart14.png" width="500" height="300" />
</p>

Dai grafici emerge che nell'apprendimento federato con pochi client i risultati sono molto simile e le curve di apprendimento sono più o meno costanti (ovviamente il test con 2 client resta sempre la curva più costante delle tre) e raggiungono alti tassi di accuratezza che si aggirano circa al 94%. Ciò che rende però interessanti questi test è che con l'aumentare del numero di client, per la seconda e terza versione, otteniamo risultati diversi. Nella seconda versione il numero di batch per client è equo tra tutti i client, e di conseguenza diminuisce sempre di più, all'aumentare del numero di client, mentre per la seconda versione del codice di simulazione di Federate Learning, il Set di dati è suddiviso randomicamente tra i vari client (più realistico) il che porta ad avere client con un numero elevato di batch, come 200/300 batch sui 469 batch totali per alcuni, ed altri client con anche 1 solo batch.  Al netto di questa suddivisione come si nota soiprattutto negli ultimi grafici, l'apprendimento del modello globale è più elevato quando sono presenti client con un elevato numero di batch, e di conseguenza la seconda versione di Federate Learning risulta come meno accurata rispetto alla terza, poichè con un numero elevato di client con un numero medio/basso di batch l'apprendimento del modello globale, e di conseguenza l'accuratezza del modello è peggiore rispetto, all'apprendimento con anche un solo client con un numero elevato di batch che consente una fase di training migliore e di conseguenza permette un update al center model più preciso ed efficace, dato che ogni client contribuisce con al calcolo dei nuovi weights in base al numero di batch che tratta (media pesata).
