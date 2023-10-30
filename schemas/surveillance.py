from pydantic import BaseModel
from datetime import datetime
class Surveillances(BaseModel):
   id_sup:int
   id_sal:str
   id_eval:int