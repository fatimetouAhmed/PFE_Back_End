from pydantic import BaseModel
from datetime import datetime
class Jours(BaseModel):
   libelle:str
   date:datetime