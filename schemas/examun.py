from pydantic import BaseModel
from datetime import datetime
class Evaluations(BaseModel):
   type:str
   date_debut:datetime
   date_fin:datetime
   id_mat:int
   id_sal:int