from pydantic import BaseModel

class CustomerBase(BaseModel):
    fantasy_name: str
    cnpj: str
    cnpj_formated: str
    address: str
    
class CustomerRead(BaseModel):
    uuid: str
    fantasy_name: str
    cnpj: str
    cnpj_formated: str
    address: str