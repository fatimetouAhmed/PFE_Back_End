from pydantic import BaseModel

class Creneau_jours(BaseModel):
   id_jour:int
   id_creneau:int
   id_mat:int