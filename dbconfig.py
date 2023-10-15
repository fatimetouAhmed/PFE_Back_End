from PIL import Image
from io import BytesIO
import deepface
from deepface import DeepFace
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer, String ,Sequence ,ForeignKey ,Date ,DateTime, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import relationship, mapper, sessionmaker
import os

from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from config.db import con
#from models.departement import Departements
#from models.filiere import Filieres
#from models.matiere import Matiere
from models.anne import Etudiant
#from models.etudiermat import Etudiant
#from models.etudiermat import etudiermats
#from models.etudiermat import Matiere
#from models.semestre_etudiant import Semestres
#from models.semestre_etudiant import semestre_etudiants
# from models.semestre_etudiant import Etudiants
#from models.examun import examuns
#from routes.historique import write_data_case_etudiant
from fastapi import APIRouter,Depends
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from datetime import datetime, timedelta

Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=con)
# Create a session
session = Session()



Base.metadata.create_all(con)
def get_etudiant(photo: str):
    # print(photo)
    # Retrieve the student's ID after verifying the image
    etudiants = session.query(Etudiant.id).filter(Etudiant.photo == photo).all()
    id_etu = etudiants[0][0]
    print(id_etu)
    return  id_etu
  