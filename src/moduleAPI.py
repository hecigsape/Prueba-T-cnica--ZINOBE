import requests
import time 

class requestsAPI():
    
    def __init__(self):
        """
        se define la url de la API a consultar 
        """
        self.API = 'https://restcountries.com/v3.1/all'

    def get_API(self):
        """
        La funcion realiza la consulta de una API y la devuele la consulta en una lista 
        """
        T_inicio = time.time()        
        res=requests.get(self.API)
        """
        verifica si la consulta es valida 
        """
        if res:
            # print('Response ok')
            pass
        else:
            print('Response Failed')
        # print(time.time()-T_inicio)
        return res.json()
