"""

Progetto: Gestione Ricette

Obiettivo: Il progetto si propone di realizzare un sistema per gestire un insieme di ricette, consentendo agli utenti di eseguire operazioni di aggiunta, eliminazione, ricerca,
visualizzazione e analisi delle ricette. Attraverso questo programma, gli utenti potranno gestire facilmente una lista di ricette, ognuna con vari ingredienti e tempi di 
preparazione. Inoltre, il sistema offrirà la possibilità di effettuare ricerche avanzate e generare statistiche utili, come per esempio visionare la frequenza di un 
determinato ingrediente o la ricetta più complessa (maggior minutaggio).

Funzionalità principali:

**Aggiunta di una nuova ricetta**: Gli utenti possono inserire nuove ricette specificando il nome, gli ingredienti e il minutaggio, utilizzando la funzione aggiungi_ricetta().

**Eliminazione di una ricetta**: È possibile rimuovere ricette esistenti dalla lista, cercandole per nome tramite la funzione elimina_ricetta().

**Visualizzazione di tutte le ricette**: Consente di migliorare la visualizzazione di tutte le ricette presenti nella lista, con dettagli su nome, ingredienti e tempo di 
preparazione, attraverso la funzione visualizza_ricette().

**Ricerca avanzata di ricette**: Gli utenti possono cercare ricette in base al nome, a ingredienti specifici o al tempo di preparazione, utilizzando la funzione cerca_ricette(), 
che permette di filtrare i risultati in base ai criteri scelti dall'utente tramite ricerca_ricetta().

Statistiche sugli ingredienti:

    **ingrediente_frequenza()**       : mostra la frequenza con la quale si ripete un determinato ingrediente.
    **ricetta_con_piu_ingredienti()** : identifica e visualizza la ricetta con il maggior numero di ingredienti.
    **ricetta_con_piu_minutaggio(**)  : mostra la ricetta che richiede il maggior tempo di preparazione.
    **statistiche_ingredienti()**     : fornisce un'analisi degli ingredienti più e meno comuni.
    **statistiche_durata()**          : analizza la durata delle ricette, mostrando la durata minima, media e massima.
    
Filtraggio avanzato delle ricette:

    **filtraggio_avanzato()**  : permette di cercare ricette che richiedono un tempo di preparazione inferiore a un certo minutaggio e che contengono un determinato ingrediente.
    **filtraggio_avanzato2()** : consente di filtrare ricette che contengono due ingredienti specifici.
    
Questo progetto è concepito per facilitare la gestione delle ricette da parte di appassionati di cucina o di chiunque desideri organizzare e analizzare facilmente una 
collezione di ricette.

"""

from collections import Counter                                                     # Importa Counter dal modulo collections, che e' utile per contare gli elementi in una sequenza.
import pandas as pd                                                                 # Importa la libreria pandas, utile per la manipolazione dei dati.                                                                         


# Definisce una funzione che permette di aggiungere una nuova ricetta nella lista. (Start2impact -> Registrazione di un nuovo elemento)
def aggiungi_ricetta(lista):
            
    """
    Aggiunge una nuova ricetta alla lista delle ricette se non è già presente.

    Args:
        lista (list): Lista che contiene tutte le ricette.

    Returns: 
        Lista aggiornata con la nuova ricetta se presente, 
        altrimenti restituisce la lista originale.
    """
     
    nome = input("Inserisci il nome della ricetta: ")                                   # Chiede all'utente di inserire il nome della ricetta.
   
    for ricetta in lista:                                                               # Controlla se la ricetta esiste già nella lista per evitare duplicati.
        if ricetta['nome'].lower() == nome.lower():                                     # Se la ricetta è già presente, notifica l'utente e restituisce la lista originale.
            print(f"La ricetta '{nome}' è già presente nella lista.")
            return lista                                                                # Restituisce la lista originale se la ricetta è duplicata
    
    ingredienti = input("Inserisci gli ingredienti separati da virgole: ").split(',')   # Chiede all'utente di inserire gli ingredienti.
    while True:                                                                         # Ciclo Infinito
        try:
            minutaggio = int(input("Inserisci il minutaggio necessario (in minuti): ")) # Chiede all'utente di inserire il minutaggio della ricetta.
            if minutaggio > 0:
                break                                                                   # Esce dal ciclo solo se il minutaggio è valido (positivo).
            else:
                print("Il minutaggio deve essere un numero maggiore di 0. Riprova.")    # Messaggio di errore se il minutaggio è <= 0.
        except ValueError:
            print("Inserisci un numero valido per il minutaggio. Riprova.")
    
    nuova_ricetta = {                                                                   # Crea un nuovo dizionario con i dettagli della ricetta
        'nome': nome,                                                                   # Assegna il nome alla ricetta.
        'ingredienti': [ingrediente.strip() for ingrediente in ingredienti],            # Assegna gli ingredienti alla ricetta e rimuove eventuali spazi inutili dagli ingredienti.
        'minutaggio': minutaggio                                                        # Assegna il minutaggio alla ricetta.
    } 
    
    lista.append(nuova_ricetta)                                                         # Aggiunge il nuovo dizionario alla lista delle ricette
    print(f"La ricetta '{nome}' è stata aggiunta con successo.")                        # Notifica l'utente che la ricetta è stata aggiunta con successo.
    
    return lista                                                                        # Restituisce la lista aggiornata                                                                           
                     
#______________________________________________________________________________________________________________________________________

# Definisce una funzione che consente di eliminare una ricetta dalla lista.
def elimina_ricetta(lista):
    
    """
    Elimina una ricetta dalla lista basata sul nome fornito dall'utente.

    Args:
        lista (list): Lista che contiene tutte le ricette.

    Returns:
        Lista aggiornata senza la ricetta eliminata se presente, 
        altrimenti restituisce la lista originale.
    """
    
    nome = input("Inserisci il nome della ricetta da eliminare: ").lower()              # Chiede all'utente di inserire il nome della ricetta da eliminare, convertendolo in minuscolo per uniformità.
    for ricetta in lista:                                                               # Cicla attraverso la lista delle ricette per trovare quella con il nome corrispondente.
        if ricetta['nome'].lower() == nome:                                             # Confronta il nome della ricetta in minuscolo con l'input dell'utente.
            lista.remove(ricetta)                                                       # Rimuove la ricetta dalla lista
            print(f"Ricetta '{nome}' eliminata.")                                       # Notifica l'utente che la ricetta è stata eliminata.
            return lista                                                                # Restituisce la lista aggiornata dopo l'eliminazione.
        
    print(f"Ricetta '{nome}' non trovata.")                                             # Se la ricetta non viene trovata, notifica l'utente.
    return lista                                                                        # Restituisce la lista originale se la ricetta non è trovata

#______________________________________________________________________________________________________________________________________ 

# Definisce una funzione che permetta di migliorare la visualizzazione delle ricette. (Start2impact -> Visualizzazione di tutti gli elementi)
def visualizza_ricette(lista):
    
    """
    Mostra tutte le ricette presenti nella lista, formattando nome, ingredienti e minutaggio.

    Args:
        lista (list): Lista che contiene tutte le ricette.

    Returns:
        None: Stampa le ricette
    """
    
    for ricetta in lista:                                                               # Cicla attraverso ogni ricetta nella lista
        print(f"Nome: {ricetta['nome']}")                                               # Stampa il nome della ricetta
        print(f"Ingredienti: {', '.join(ricetta['ingredienti'])}")                      # Stampa gli ingredienti uniti in una stringa, separati da virgole                   
        print(f"Minutaggio: {ricetta['minutaggio']} minuti")                            # Stampa il minutaggio della ricetta
        print("-" * 40)                                                                 # Stampa una linea di separazione per rendere l'output più leggibile

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di cercare ricette basate su uno o piu' attributi 
def cerca_ricette(lista, nome=None, ingrediente=None, minutaggio=None):
    
    """
    Cerca ricette nella lista in base a nome, ingrediente o minutaggio fornito.

    Args:
        lista (list): Lista che contiene tutte le ricette.
        nome (str, optional): Nome della ricetta da cercare.
        ingrediente (str, optional): Ingrediente da cercare nelle ricette.
        minutaggio (int, optional): Minutaggio per filtrare le ricette.

    Returns:
        None: Stampa le ricette che soddisfano i criteri di ricerca oppure un messaggio se non ci sono risultati.
    """
    
    risultati = []                                                                                          # Crea una lista vuota per memorizzare le ricette che soddisfano i criteri di ricerca.
    for ricetta in lista:                                                                                   # Itera attraverso ogni ricetta nella lista.
        if nome and nome.lower() not in ricetta['nome'].lower():                                            # Controlla se è specificato un nome e se il nome della ricetta non corrisponde, salta la ricetta.
            continue
        if ingrediente and all(ingrediente.lower() not in ingr.lower() for ingr in ricetta['ingredienti']): # Controlla se è specificato un ingrediente e se non è presente negli ingredienti della ricetta, salta la ricetta.
            continue
        if minutaggio and ricetta['minutaggio'] != minutaggio:                                              # Controlla se è specificato un minutaggio e se non corrisponde a quello della ricetta, salta la ricetta.
            continue
        risultati.append(ricetta)                                                                           # Se tutte le condizioni sono soddisfatte, aggiunge la ricetta alla lista dei risultati.
    
    if risultati:                                                                                           # Se ci sono risultati, stampali.
            visualizza_ricette(risultati)                                                                   # Visualizza le ricette che corrispondono ai criteri di ricerca.
    else:                                                                                                   
        print("Nessuna ricetta trovata che soddisfi i criteri.")                                            # Se non ci sono risultati, stampa un messaggio di avviso.

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di interagire con l'utente per acquisire criteri di ricerca. (Start2impact -> Ricerca di elementi)
def ricerca_ricetta(lista): 
    
    """
    Consente all'utente di cercare una ricetta per nome, ingrediente o minutaggio.
    Args:
        lista (list): Lista che contiene tutte le ricette.
    Returns:
        None: Stampa i risultati della ricerca o un messaggio di errore se l'input non è valido.
    """
    print("Criteri di ricerca disponibili:")                                                             # Stampa le opzioni di ricerca disponibili per l'utente.
    print("1. Nome")                                                                                        
    print("2. Ingrediente")
    print("3. Minutaggio")
    scelta = input("Scegli il criterio di ricerca (1/2/3): ")                                            # Chiede all'utente di scegliere un criterio di ricerca tra le opzioni disponibili.
    if scelta == '1':                                                                                    # Se l'utente ha scelto di cercare per nome, richiede il nome della ricetta e chiama la funzione cerca_ricette.
        nome = input("Inserisci il nome della ricetta da cercare: ")                                     # Input per il nome della ricetta
        cerca_ricette(lista, nome=nome)                                                                  # Chiamata alla funzione di ricerca con il nome specificato.
    elif scelta == '2':                                                                                  # Se l'utente ha scelto di cercare per ingrediente, richiede l'ingrediente e chiama la funzione cerca_ricette.
        ingrediente = input("Inserisci l'ingrediente da cercare: ")                                      # Input per l'ingrediente
        cerca_ricette(lista, ingrediente=ingrediente)                                                    # Chiamata alla funzione di ricerca con l'ingrediente specificato
    elif scelta == '3':  # Ricerca per minutaggio
        while True:
            try:
                minutaggio = int(input("Inserisci il minutaggio della ricetta da cercare: "))           # Inserisce un numero da tastiera
                if minutaggio < 0:
                    print("Il minutaggio deve essere un numero positivo. Riprova.")
                    continue                                                                            # Ripeti il ciclo se il numero è negativo
                break                                                                                   # Esci dal ciclo se il numero è valido
            except ValueError:                                                                          # Gestisce il caso in cui venga inserita una parola
                print("Per favore inserisci un numero valido. Riprova.")                                     
        cerca_ricette(lista, minutaggio=minutaggio)                                                     # Chiamata alla funzione di ricerca con il minutaggio specificato.
    else:                                                                                                  
        print("Scelta non valida. Per favore, scegli 1, 2 o 3.")                                         # Se l'input non è valido (non è 1, 2 o 3), stampa un messaggio di errore.

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di visualizzare con quale frequenza si presenta un determinato ingrediente (Start2impact -> Statistiche sugli elementi)
def ingrediente_frequenza(lista):
    
    """
    Chiede all'utente di inserire un ingrediente e determina quante volte appare tra tutte le ricette.

    Args:
        lista (list): Lista che contiene tutte le ricette.

    Returns:
        None: Stampa i risultati della ricerca o un messaggio se l'ingrediente non è stata trovato.
    """
    
    if not lista:                                                                                               # Controlla se la lista è vuota
        print("La lista delle ricette è vuota.")                                                                # Se sì, stampa un messaggio.
        return None                                                                                             # La funzione termina se non ci sono ricette.
    
    tutti_ingredienti = []                                                                                      # Inizializza una lista vuota per raccogliere tutti gli ingredienti.
    
    for ricetta in lista:                                                                                       # Itera attraverso ogni ricetta nella lista
        tutti_ingredienti.extend([ingrediente.lower() for ingrediente in ricetta['ingredienti']])               # Converte tutti gli ingredienti in minuscolo per la ricerca
    
    ingrediente_cercato = input("Inserisci l'ingrediente di cui vuoi conoscere la frequenza: ").strip().lower() # Richiede all'utente di inserire l'ingrediente da cercare e lo converte in minuscolo
    conteggi = Counter(tutti_ingredienti)                                                                       # Conta la frequenza di ogni ingrediente (tutti in minuscolo).
    frequenza_ingrediente = conteggi.get(ingrediente_cercato, 0)                                                # Ottiene la frequenza dell'ingrediente cercato (0 se non trovato)
    
    if frequenza_ingrediente > 0:
        print(f"L'ingrediente '{ingrediente_cercato}' appare {frequenza_ingrediente} volte nelle ricette.")     # Stampa il risultato.
    else:
        print(f"L'ingrediente '{ingrediente_cercato}' non è presente in nessuna ricetta.")                      # Se l'input non è valido, stampa un messaggio.        

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di visualizzare la ricetta con più ingredienti (Start2impact -> Statistiche sugli elementi)
def ricetta_con_piu_ingredienti(lista): 
    
    """
    Determina e restituisce la ricetta con il maggior numero di ingredienti.

    Args:
        lista (list): Lista che contiene tutte le ricette.

    Returns:
        dict or None: Restituisce un dizionario contenente la ricetta con il maggior numero di ingredienti,
                      o None se la lista è vuota.
    """
    
    if not lista:                                                          # Controlla se la lista è vuota
        print("La lista delle ricette è vuota.")                           # Se sì, stampa un messaggio.
        return None                                                        # La funzione restituisce None se non ci sono ricette.
    
    ricetta_max_ingredienti = None                                         # Inizializza una variabile per tenere traccia della ricetta con il maggior numero di ingredienti.
    max_ingredienti = 0                                                    # Inizializza una variabile per tenere traccia del numero massimo di ingredienti.
    for ricetta in lista:                                                  # Scorre ogni ricetta nella lista fornita.
        numero_ingredienti = len(ricetta['ingredienti'])                   # Calcola il numero di ingredienti della ricetta corrente.
        if numero_ingredienti > max_ingredienti:                           # Se il numero di ingredienti della ricetta corrente è maggiore del massimo attuale                                                          # Se il numero di ingredienti è maggiore di quello attualmente massimo, aggiorna
            max_ingredienti = numero_ingredienti                           # Aggiorna la variabile di massimo.
            ricetta_max_ingredienti = ricetta                              # Aggiorna la ricetta corrispondente
    
    return ricetta_max_ingredienti                                         # Restituisce la ricetta con il maggior numero di ingredienti.

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di visualizzare la ricetta che richiede maggior minutaggio per la preparazione (Start2impact -> Statistiche sugli elementi)
def ricetta_con_piu_minutaggio(lista):
    
    """
    Determina e visualizza la ricetta con il maggior minutaggio.

    Args:
        lista (list): Lista che contiene tutte le ricette, dove ogni ricetta è rappresentata come un dizionario 
        con chiavi 'nome', 'ingredienti' e 'minutaggio'.

    Returns:
        dict or None: Restituisce un dizionario contenente la ricetta con il maggior minutaggio,
                      o None se la lista è vuota.
    """
    
    if not lista:                                                                                           # Controlla se la lista è vuota
        print("La lista delle ricette è vuota.")                                                            # Se sì, stampa un messaggio.
        return None                                                                                         # La funzione restituisce None se non ci sono ricette.
    
    ricetta_max_minutaggio = None                                                                           # Inizializza una variabile per tenere traccia della ricetta con il maggior minutaggio.
    max_minutaggio = 0                                                                                      # Inizializza una variabile per tenere traccia del minutaggio massimo.
    for ricetta in lista:                                                                                   # Scorre ogni ricetta nella lista fornita.
        minutaggio = ricetta['minutaggio']                                                                  # Estrae il minutaggio della ricetta corrente.
        if minutaggio > max_minutaggio:                                                                     # Se il minutaggio della ricetta corrente è maggiore di quello attualmente massimo
            max_minutaggio = minutaggio                                                                     # Aggiorna la variabile massimo
            ricetta_max_minutaggio = ricetta                                                                # Aggiorna la ricetta corrispondente.
    
    return ricetta_max_minutaggio                                                                           # Restituisce la ricetta con il maggior minutaggio.

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di visualizzare gli ingredienti più e meno usati (Start2impact -> Statistiche sugli elementi)
def statistiche_ingredienti(lista):
    
    """
    Analizza e stampa statistiche sugli ingredienti delle ricette.

    Args:
        lista (list): Lista che contiene tutte le ricette, 
                      dove ogni ricetta è rappresentata come un dizionario 
                      con chiavi 'nome', 'ingredienti' e 'minutaggio'.

    Returns:
        None:Stampa i risultati della ricerca o un messaggio di errore se la lista è vuota.
    """
    
    if not lista:                                                                                           # Controlla se la lista è vuota
        print("La lista delle ricette è vuota.")                                                            # Se sì, stampa un messaggio.
        return None                                                                                         # La funzione restituisce None se non ci sono ricette.

 
    tutti_ingredienti = []                                                                                  # Inizializza una lista per raccogliere tutti gli ingredienti.
    for ricetta in lista:                                                                                   # Scorre ogni ricetta nella lista fornita 
        tutti_ingredienti.extend(ricetta['ingredienti'])                                                    # Aggiunge gli ingredienti alla lista "tutti_ingredienti" utilizzando il metodo extend.

    conteggi = Counter(tutti_ingredienti)                                                                   # Conta la frequenza di ogni ingrediente usando Counter.
    ingredienti_comuni = conteggi.most_common(5)                                                            # Estrae i 5 ingredienti più comuni dalla lista dei conteggi.
    frequenza_minima = min(conteggi.values())                                                               # Trova la frequenza minima tra gli ingredienti.
    ingredienti_meno_comuni = [ingrediente for ingrediente, frequenza in conteggi.items() if frequenza == frequenza_minima]  # Crea una lista di tutti gli ingredienti che hanno la frequenza minima.

    print("Ingredienti più comuni:")  
    for ingrediente, frequenza in ingredienti_comuni:
        print(f"{ingrediente}: {frequenza} occorrenze")                                                     # Stampa gli ingredienti più comuni e il loro conteggio.
        
    print("-" * 40)                                                                                         # Stampa una linea di separazione per migliorare la leggibilità.
     
    print(f"Ingredienti meno comuni: {', '.join(ingredienti_meno_comuni)} (frequenza: {frequenza_minima})") # Stampa gli ingredienti meno comuni e la loro frequenza minima.

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di visualizzare il minutaggio minimo, massimo e la media sul totale (Start2impact -> Statistiche sugli elementi)
def statistiche_durata(lista):
    
    """
    Analizza e stampa statistiche sulla durata delle ricette.

    Args:
        lista (list): Lista che contiene tutte le ricette, 
                      dove ogni ricetta è rappresentata come un dizionario 
                      con chiavi 'nome', 'ingredienti' e 'minutaggio'.

    Returns:
        None: Stampa i risultati della ricerca o un messaggio di errore se la lista è vuota.
    """
    
    if not lista:                                                                                           # Controlla se la lista è vuota
        print("La lista delle ricette è vuota.")                                                            # Se sì, stampa un messaggio.
        return None                                                                                         # La funzione restituisce None se non ci sono ricette.

    df = pd.DataFrame(lista)                                                                                # Crea un DataFrame da pandas usando la lista di ricette.
                                                                                                            # Estrae le statistiche sul minutaggio delle ricette.
    min_durata = df['minutaggio'].min()                                                                     # Trova la durata minima.
    media_durata = df['minutaggio'].mean()                                                                  # Calcola la durata media.
    max_durata = df['minutaggio'].max()                                                                     # Trova la durata massima.

    print(f"Durata minima: {min_durata} minuti")                                                            # Stampa i risultati delle statistiche sulla durata.
    print(f"Durata media: {media_durata:.2f} minuti")                                                       # Stampa la media formattata a due decimali.
    print(f"Durata massima: {max_durata} minuti")                                                           # Stampa i risultati delle statistiche sulla durata.
 
#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di avere Doppio Filtro: 1) Per minutaggio. 2) Per Ingrediente (Start2impact -> Filtraggio Avanzato)
def filtraggio_avanzato(lista):
    
    """
    Filtra e visualizza le ricette in base a un doppio criterio: 
    minutaggio massimo e presenza di un ingrediente specifico.

    Args:
        lista (list): Lista che contiene tutte le ricette, 
                      dove ogni ricetta è rappresentata come un dizionario 
                      con chiavi 'nome', 'ingredienti' e 'minutaggio'.

    Returns:
        None: Stampa i risultati della ricerca o un messaggio se la ricetta non è stata trovata.
    """
    
    while True:                                                                                             # Ciclo infinito per ottenere un input valido per il minutaggio massimo.
        try:
            max_minutaggio = int(input("Inserisci il massimo minutaggio (in minuti): "))                    # Richiede all'utente di inserire il massimo minutaggio e converte l'input in un intero.
            if max_minutaggio <= 0:                                                                         # Verifica se il minutaggio è un valore positivo(>0).
                raise ValueError("Il minutaggio non può essere negativo o uguale a 0.")
            break                                                                                           # Esce dal ciclo se l'input è valido
        except ValueError as e:
            print(f"Errore: {e}. Per favore, inserisci un numero intero valido.")                           # Stampa un messaggio di errore se l'input non è valido.
     
    ingrediente = input("Inserisci l'ingrediente da cercare: ").lower()                                     # Richiede all'utente di inserire un ingrediente da cercare, convertendolo in minuscolo per uniformità.                                   
    ricette_filtrate = []                                                                                   # Inizializza una lista per memorizzare le ricette che soddisfano i criteri.                                                                                
    for ricetta in lista:                                                                                   # Scorre ogni ricetta nella lista fornita.                                                                                
        if ricetta['minutaggio'] <= max_minutaggio:                                                         # Verifica se il minutaggio della ricetta è inferiore o uguale al massimo specificato.                                                           
            ingredienti_lower = [ingrediente_item.lower() for ingrediente_item in ricetta['ingredienti']]   # Crea una lista di ingredienti in minuscolo per la ricetta corrente convertiti in minuscolo.
            if ingrediente in ingredienti_lower:                                                            # Verifica se l'ingrediente (in minuscolo) è presente nella lista di ingredienti (anch'essa in minuscolo).
                ricette_filtrate.append(ricetta)                                                            # Aggiunge la ricetta alla lista dei risultati filtrati se soddisfa i criteri.
    
    if ricette_filtrate:                                                                                    # Controlla se ci sono ricette filtrate da mostrare.                                                                         
        for ricetta in ricette_filtrate:
            visualizza_ricette(ricette_filtrate)                                                            # Stampa le ricette filtrate chiamando la funzione di visualizzazione.
    else:
        print(f"Nessuna ricetta trovata con meno di {max_minutaggio} minuti e contenente '{ingrediente}'.") # Stampa un messaggio se non ci sono ricette che soddisfano i criteri di filtraggio.

#______________________________________________________________________________________________________________________________________

# Definisce una funzione che permetta di visualizzare la/e ricetta/e attraverso il filtro di due Ingredienti (Start2impact -> Filtraggio Avanzato)
def filtraggio_avanzato2(lista):
   
    """
    Filtra e visualizza le ricette che contengono due ingredienti specifici.

    Args:
        lista (list): Lista che contiene tutte le ricette, 
                      dove ogni ricetta è rappresentata come un dizionario 
                      con chiavi 'nome', 'ingredienti' e 'minutaggio'.

    Returns:
        None:Stampa i risultati della ricerca o un messaggio  se la ricetta non è stata trovata.
    """
    
    ingrediente1 = input("Inserisci il primo ingrediente da cercare: ").strip().lower()                     # Richiede all'utente di inserire il primo ingrediente e lo converte in minuscolo.
    ingrediente2 = input("Inserisci il secondo ingrediente da cercare: ").strip().lower()                   # Richiede all'utente di inserire il secondo ingrediente e lo converte in minuscolo.
    ricette_filtrate = []                                                                                   # Inizializza una lista per memorizzare le ricette che soddisfano i criteri.
    for ricetta in lista:                                                                                   # Scorre ogni ricetta nella lista fornita
        ingredienti_lower = [ingrediente_item.lower() for ingrediente_item in ricetta['ingredienti']]       # Converte gli ingredienti della ricetta in minuscolo per il confronto 
        if ingrediente1 in ingredienti_lower and ingrediente2 in ingredienti_lower:                         # Verifica se entrambe le condizioni siano soddisfatte
            ricette_filtrate.append(ricetta)                                                                #Aggiunge la ricetta alla lista dei risultati filtrati se soddisfa i criteri.
    
    if ricette_filtrate:                                                                                    # Controlla se ci sono ricette filtrate da mostrare.
        for ricetta in ricette_filtrate:
            visualizza_ricette(ricette_filtrate)                                                            # Stampa le ricette filtrate chiamando la funzione di visualizzazione.
    else:
        print(f"Nessuna ricetta trovata contenente entrambi '{ingrediente1}' e '{ingrediente2}'.")          # Stampa un messaggio se non ci sono ricette che soddisfano i criteri di filtraggio.

#______________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________

# Lista con all'interno tutte le ricette.
lista_ricette= [
    
     # Ogni ricetta è un dizionario con il nome della ricetta, una lista di ingredienti e il minutaggio richiesto.
    {'nome': 'Carbonara','ingredienti': ['Pasta','Uova','Pecorino','Parmigiano','Pepe Nero','Guanciale'],'minutaggio': 30} ,
    {'nome': 'Matriciana','ingredienti': ['Pasta','Sugo di Pomodoro','Pecorino','Pepe Nero','Guanciale'],'minutaggio': 45},
    {'nome': 'Pesto','ingredienti': ['Aglio','Basilico','Pinoli','Olio','Sale'],'minutaggio': 10},
    {'nome': 'Polpetta','ingredienti': ['Carne Macinata','Uova','Pane','Pepe Nero','Sale','Parmigiano'],'minutaggio': 20},
    {'nome': 'Margherita','ingredienti': ['Sugo di Pomodoro','Mozzarella','Basilico','Olioo'],'minutaggio': 15},
    {'nome': 'Lasagna', 'ingredienti': ['Pasta', 'Carne Macinata', 'Sugo di Pomodoro', 'Besciamella', 'Mozzarella', 'Parmigiano'], 'minutaggio': 90},
    {'nome': 'Risotto ai Funghi', 'ingredienti': ['Riso', 'Funghi', 'Brodo Vegetale', 'Vino Bianco', 'Cipolla', 'Parmigiano'], 'minutaggio': 40},
    {'nome': 'Tiramisu', 'ingredienti': ['Mascarpone', 'Uova', 'Caffè', 'Savoiardi', 'Zucchero', 'Cacao in Polvere'], 'minutaggio': 30},
    {'nome': 'Cacciatora', 'ingredienti': ['Pollo', 'Pomodoro', 'Cipolla', 'Olive', 'Vino Rosso', 'Rosmarino'], 'minutaggio': 60},
    {'nome': 'Frittata di Patate', 'ingredienti': ['Uova', 'Patate', 'Cipolla', 'Parmigiano', 'Sale', 'Pepe'], 'minutaggio': 30},
    {'nome': 'Caprese', 'ingredienti': ['Mozzarella', 'Pomodoro', 'Basilico', 'Olio d\'Oliva', 'Sale'], 'minutaggio': 10},
    {'nome': 'Zuppa di Legumi', 'ingredienti': ['Legumi Misti', 'Brodo Vegetale', 'Carota', 'Cipolla', 'Sedano', 'Pomodoro'], 'minutaggio': 50},
    {'nome': 'Pollo al Limone', 'ingredienti': ['Pollo', 'Limone', 'Olio d\'Oliva', 'Aglio', 'Rosmarino', 'Sale', 'Pepe'], 'minutaggio': 40},
    {'nome': 'Pancakes', 'ingredienti': ['Farina', 'Latte', 'Uova', 'Zucchero', 'Lievito in Polvere', 'Burro'], 'minutaggio': 20},
    {'nome': 'Couscous alle Verdure', 'ingredienti': ['Couscous', 'Zucchine', 'Peperoni', 'Pomodorini', 'Cipolla', 'Olio d\'Oliva'], 'minutaggio': 30},
    {'nome': 'Spaghetti Aglio e Olio', 'ingredienti': ['Spaghetti', 'Aglio', 'Peperoncino', 'Olio d\'Oliva', 'Prezzemolo'], 'minutaggio': 20},
    {'nome': 'Sgombro al Forno', 'ingredienti': ['Sgombro', 'Limone', 'Rosmarino', 'Olio d\'Oliva', 'Sale', 'Pepe'], 'minutaggio': 25},
    {'nome': 'Involtini di Melanzane', 'ingredienti': ['Melanzane', 'Ricotta', 'Pomodoro', 'Mozzarella', 'Basilico'], 'minutaggio': 45},
    {'nome': 'Torta di Mele', 'ingredienti': ['Mele', 'Farina', 'Zucchero', 'Uova', 'Burro', 'Lievito in Polvere'], 'minutaggio': 60},
    {'nome': 'Gnocchi al Pesto', 'ingredienti': ['Gnocchi di Patate', 'Pesto', 'Parmigiano'], 'minutaggio': 20},
    {'nome': 'Boeuf Bourguignon', 'ingredienti': ['Manzo', 'Vino Rosso', 'Carota', 'Cipolla', 'Funghi', 'Bacon', 'Brodo di Carne'], 'minutaggio': 120},
    {'nome': 'Falafel', 'ingredienti': ['Ceci', 'Aglio', 'Cipolla', 'Prezzemolo', 'Coriandolo', 'Cumino', 'Farina'], 'minutaggio': 45},
    {'nome': 'Moussaka', 'ingredienti': ['Melanzane', 'Carne Macinata', 'Pomodoro', 'Cipolla', 'Besciamella', 'Parmigiano'], 'minutaggio': 90},
    {'nome': 'Chili con Carne', 'ingredienti': ['Carne Macinata', 'Fagioli', 'Pomodoro', 'Peperoni', 'Cipolla', 'Spezie'], 'minutaggio': 60},
    {'nome': 'Zuppa di Cipolle', 'ingredienti': ['Cipolla', 'Brodo di Carne', 'Pane', 'Formaggio Gruyère', 'Burro'], 'minutaggio': 50},
    {'nome': 'Insalata di Tonno', 'ingredienti': ['Tonno in scatola', 'Pomodori', 'Cetrioli', 'Olive', 'Cipolla', 'Olio d\'Oliva'], 'minutaggio': 15},
    {'nome': 'Tacos', 'ingredienti': ['Tortillas', 'Carne Macinata', 'Lattuga', 'Pomodoro', 'Formaggio', 'Salsa'], 'minutaggio': 30},
    {'nome': 'Pasta al Pesto di Rucola', 'ingredienti': ['Pasta', 'Rucola', 'Noci', 'Parmigiano', 'Olio d\'Oliva', 'Aglio'], 'minutaggio': 20},
    {'nome': 'Ratatouille', 'ingredienti': ['Melanzane', 'Zucchine', 'Peperoni', 'Pomodoro', 'Cipolla', 'Aglio', 'Olio d\'Oliva'], 'minutaggio': 60},
    {'nome': 'Polpette di Ricotta', 'ingredienti': ['Ricotta', 'Farina', 'Uova', 'Parmigiano', 'Prezzemolo', 'Sale'], 'minutaggio': 30},
    {'nome': 'Pancetta alla Griglia', 'ingredienti': ['Pancetta', 'Sale', 'Pepe', 'Rosmarino', 'Olio d\'Oliva'], 'minutaggio': 20},
    {'nome': 'Frittelle di Zucchine', 'ingredienti': ['Zucchine', 'Farina', 'Uova', 'Parmigiano', 'Aglio', 'Prezzemolo'], 'minutaggio': 25},
    {'nome': 'Crostini al Pomodoro', 'ingredienti': ['Pane', 'Pomodori', 'Aglio', 'Basilico', 'Olio d\'Oliva', 'Sale'], 'minutaggio': 15},
    {'nome': 'Quiche Lorraine', 'ingredienti': ['Pasta Brisè', 'Panna', 'Uova', 'Bacon', 'Formaggio Gruyère', 'Cipolla'], 'minutaggio': 50},
    {'nome': 'Sgombro alla Griglia', 'ingredienti': ['Sgombro', 'Limone', 'Rosmarino', 'Olio d\'Oliva', 'Sale', 'Pepe'], 'minutaggio': 25},
    {'nome': 'Torta Salata con Spinaci e Ricotta', 'ingredienti': ['Pasta Brisè', 'Spinaci', 'Ricotta', 'Parmigiano', 'Uova', 'Noce Moscata'], 'minutaggio': 45}
    
    ]

#Funzione Richiamata per Aggiungere una Nuova Ricetta a quelle gia presenti.
aggiungi_ricetta(lista_ricette)

print("-" * 40)

#Funzione Richiamata per Eliminare una Ricetta già presente nella lista.
elimina_ricetta(lista_ricette)

print("-" * 40)

#Funzione Richiamata per migliorare la visualizzazione di tutte le ricette.
visualizza_ricette(lista_ricette)

#Funzione Richiamata per ricercare una determinata ricetta in base a determinati criteri.
ricerca_ricetta(lista_ricette)

#Funzione Richiamata per visualizzare la frequenza con la quale si prensenta un determinato ingrediente
ingrediente_frequenza(lista_ricette)
print("-" * 40)

#Funzione Richiamata per mostrare la ricetta che contiene più ingredienti.
ricetta_max_ingredienti = ricetta_con_piu_ingredienti(lista_ricette)

if ricetta_max_ingredienti:
    print(f"La ricetta con il maggior numero di ingredienti è '{ricetta_max_ingredienti['nome']}' con {len(ricetta_max_ingredienti['ingredienti'])} ingredienti.")

print("-" * 40)

#Funzione Richiamata per mostrare la ricetta che richiede maggior Minutaggio.
ricetta_max_minutaggio = ricetta_con_piu_minutaggio(lista_ricette)

if ricetta_max_minutaggio:
    print(f"La ricetta con il maggior minutaggio è '{ricetta_max_minutaggio['nome']}' con {ricetta_max_minutaggio['minutaggio']} minuti.")

print("-" * 40)

#Funzione Richiamata per mostrare le ricette con piu'/meno minutaggio.
statistiche_ingredienti(lista_ricette)
print("-" * 40)

#Funzione Richiamata per mostrare le ricette con il minutaggio minore, maggiore e la media sul totale
statistiche_durata(lista_ricette)
print("-" * 40)

#Funzione Richiamata per mostrare le ricette con al suo interno un Doppio Filtro, ovvero il primo in base al minutaggio (Es: <=45 minuti)e il secondo per Ingrediente (Es: Aglio).
filtraggio_avanzato(lista_ricette)

#Funzione Richiamata per mostrare le ricette con al suo interno un Doppio Filtro, ovvero due Ingredienti (Es: Pasta & Spinaci).
filtraggio_avanzato2(lista_ricette)
