from hashlib import sha1

class ueseHashlib: 
    
    
    def __init__(self):
        pass
    
    
    def encrypt_sha1(self,lenguage):
        """
        funcion que recibe un str con el nombre del idioma que habla el pais y 
        se encripta con SHA1
        """
        result = sha1(lenguage.encode()).hexdigest()
        return result
