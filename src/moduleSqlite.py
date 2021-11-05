import sqlite3
import os 

class connectionSqlite():
    
    def __init__(self):
        """
            Se crea el directorio db_Sqlite donde se alamcena la b
        """
        os.makedirs("./db_Sqlite", exist_ok=True)
        try:
            self.con = sqlite3.connect("./db_Sqlite/dataBase.db")
        except Exception as err:
            print('no hay conexion')
            print(err)
        

    def openSQL(self):
        '''
        #la instancia cursor para ejecutar declaraciones SQLite
        '''
        self.con = sqlite3.connect('./db_Sqlite/dataBase.db')
        self.cursor = self.con.cursor()


    def closeSQL(self):
        """
        funcion para cerrar la base de datos
        """
        self.con.close()


    def newTableSQL(self):
        """
        funcion para crear la base de datos
        """
        try:
            self.openSQL()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tabla (id INTEGER PRIMARY KEY AUTOINCREMENT, region TEXT, city TEXT, language TEXT, time REAL)")
            self.con.commit()
        except Exception as error:
            print ("Error creando tabla", error)
        finally:
            self.closeSQL()
            

    def insertRow(self, fila):
        """
        funcion para insertar una fila, recibe una lista como parametro 
        """        
        try:
            self.openSQL()
            self.cursor.execute(f"INSERT INTO tabla (region, city, language, time) VALUES (?, ?, ? ,?)", fila)
            self.con.commit()
        except Exception as error:
            print ("Error insertando fila", error)
        finally:
            self.closeSQL()
            

    def viewRows(self):
        """
        funcion para consultar la base de datos,retorna la consulta
        """          
        try:
            self.openSQL()
            self.cursor.execute(f"SELECT * FROM tabla")
            rows = self.cursor.fetchall()
            return rows        
        except Exception as error:
            print ("Error mostrando filas", error)
        finally:
            self.closeSQL()
            
            
    def run_sql(self,df):
        """
        funcion principal para el manejo de db, recibe como parametro un DataFrame:
            -genera db
            -inserta filas
            -hace la consulta de la db y imprime las filas alamcenadas en db
        """  
        
        print('Inicia la escritura del resultado en sqlite')
        self.newTableSQL()  # genera db
        for i in df.index:            
            #lee los datos almacenados en la fila i
            region=df.loc[i,'Region']
            city=df.loc[i,'City Name']
            languaje=df.loc[i,'Languaje']
            time=df.loc[i,'Time']
            #inserta filas
            self.insertRow([region,city,languaje,time])     
        print('Termina la escritura del resultado en sqlite')
        viewdb=input('Desea consultar la base de datos: \n\tSi -> Y \n\tNo -N\n')
        if viewdb=='Y' or viewdb=='y' or viewdb=='si':
            print("\n\n----------- db sqlite ----------------")
            for i in self.viewRows():
                print(i)
        else:
            pass
            
        return
    