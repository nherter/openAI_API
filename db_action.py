import sqlite3

class DatabaseThat:
    def __init__(self, filename):
        self.__filename = filename  # Private Variable für den Dateinamen
        self.__conn = None  # Private Variable für die Verbindung
        self.__cursor = None  # Private Variable für den Cursor

    def open_database(self):
        """Öffnet die Datenbank, erstellt die Tabelle (falls nicht vorhanden) und speichert Verbindung und Cursor."""
        self.__conn = sqlite3.connect(self.__filename)
        self.__cursor = self.__conn.cursor()
        
        # Tabelle erstellen, falls sie nicht existiert
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS deine_tabelle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            modell TEXT,
            prompt_cost INTEGER,
            response_cost INTEGER,
            vendor TEXT)
        """)
        self.__conn.commit()

    def add_token_usage(self, modell, promt_cost, response_cost, vendor):
        """Fügt eine neue Zeile in die Tabelle ein."""
        self.__cursor.execute("""
        INSERT INTO deine_tabelle (modell, prompt_cost, response_cost, vendor)
        VALUES (?, ?, ?, ?)
        """, (modell, promt_cost, response_cost, vendor))
        self.__conn.commit()

    def show_all_usages(self):
        """Gibt alle Einträge in der Tabelle aus."""
        self.__cursor.execute("SELECT * FROM deine_tabelle")
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)

    def close_database(self):
        """Schließt die Verbindung zur Datenbank."""
        if self.__cursor:
            self.__cursor.close()
        if self.__conn:
            self.__conn.close()
    
    def total_token_cost(self):
        """Summiert alle kosten"""
        self.__cursor.execute("SELECT prompt_cost, response_cost FROM deine_tabelle")
        rows = self.__cursor.fetchall()

        total_cost_prompt = 0
        total_cost_response = 0

        for row in rows:
          total_cost_prompt += row[0]
          total_cost_response += row[1]

        total_cost = total_cost_prompt + total_cost_response
        print(f"""
        Prompt cost: {total_cost_prompt} 
        Response cost: {total_cost_response}
        Total: {total_cost}
        """)

        price_per_token = 0,15/1000000

        price_in_dollor = total_cost * price_per_token
        
        # Das geht nicht iwie mit dem Dollar
        print(f"The total cost in Dollor are {total_cost * price_per_token}$")


    def __del__(self):
        """Automatisch aufgerufen, wenn das Objekt gelöscht wird. Schließt die Datenbankverbindung."""
        self.close_database()