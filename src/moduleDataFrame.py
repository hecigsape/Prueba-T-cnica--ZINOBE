import os 
import pandas as pd 
import time 
from .encryptsSHA1 import ueseHashlib

class newDataFrame():
    
    
    def __init__(self):
        self.uese_Hashlib = ueseHashlib()
        pass
    
    
    def writeDataFrame(self,res):
        """
        la funcion writeDataFrame tiene como parametro de entrada la respuesta 
        de la consulta API devuelve un dataframe con los datos de Region,
        City Name,Languaje,Time.
        """
        df = pd.DataFrame(columns=['Region','City Name','Languaje','Time'])
        s_time = time.time_ns()
        start_time=time.time_ns()

        for i in res:
            '''
            #se puso un retardo de un nanosegundo, debido a que el tiempo que 
            toma la  de escritura de la tabla es muy corto y el delta se toma 
            como cero, el retardo se puso con el fin de cumplir con lo propuesto
            : "Con funciones de la libreria pandas muestre el tiempo total, 
            el tiempo promedio, el tiempo minimo y el maximo que tardo en
            procesar toda las filas de la tabla".
            '''
            time.sleep(1e-9)  

            try:
                region=i['region']
                city=i['name']['common']
                lg=list(i['languages'].values())[0]            
                language=self.uese_Hashlib.encrypt_sha1(lg)
                nueva_fila = { 'Region':region , 'City Name':city,'Languaje':language} # creamos un diccionario
                end_time=time.time_ns()-start_time
                nueva_fila.update({'Time': end_time*1e-6})
                df = df.append(nueva_fila, ignore_index=True)
                start_time=time.time_ns()

            except:
                pass
        T_time = (time.time_ns()-s_time)*1e-6  
        # print(f"Total Time: {T_time} Miliseconds")
        print(df)
        print(type(df))

        self.viewInfo_DF(df)
        return  df
    
    
    def viewInfo_DF(self,df):
        '''
        Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio,
        el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
        '''
        print(f"Timepo total: {df.Time.sum()} Miliseconds")
        print(f"Timepo promedio: {df.Time.mean()} Miliseconds")
        print(f"Timepo minimo: {df.Time.min()} Miliseconds")
        print(f"Timepo maximo: {df.Time.max()} Miliseconds")


        return     
    
    
    def saveDF_to_json(self,df):
        """
        La funcion escribe el DataFrame de entrada en formato json
        """
        os.makedirs("./db_Json", exist_ok=True)
        df.to_json('./db_Json/data.json')
        return 