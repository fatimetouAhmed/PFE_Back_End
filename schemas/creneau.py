from pydantic import BaseModel
from datetime import time
class Creneaus(BaseModel):
   heure_debut:time
   heure_fin:time