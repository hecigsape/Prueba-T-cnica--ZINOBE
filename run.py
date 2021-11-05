"""
Se integran los modulos creados para cumplir con los objetivos propuestos.

Desarrolle una aplicacion en python que genere la tabla anterior teniendo 
las siguientes consideraciones:

    -De https://restcountries.com/ obtenga el nombre del idioma que habla el 
        pais y encriptelo con SHA1
    -En la columna Time ponga el tiempo que tardo en armar la fila 
        (debe ser automatico)
    -La tabla debe ser creada en un DataFrame con la libreria PANDAS
    -Con funciones de la libreria pandas muestre el tiempo total, el tiempo 
        promedio, el tiempo minimo y el maximo que tardo en procesar toda las 
        filas de la tabla.
    -Guarde el resultado en sqlite.
    -Genere un Json de la tabla creada y guardelo como data.json
"""
from src.moduleAPI import requestsAPI
from src.moduleDataFrame import newDataFrame
from src.moduleSqlite import connectionSqlite

if __name__ == "__main__":

            
    requests_API=requestsAPI()
    new_DataFrame=newDataFrame()
    connection_Sqlite=connectionSqlite()
    
    res=requests_API.get_API()
    df=new_DataFrame.writeDataFrame(res)
    new_DataFrame.saveDF_to_json(df)
    connection_Sqlite.run_sql(df)
    
    