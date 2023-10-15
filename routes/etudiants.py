from fastapi import APIRouter,Depends,Form
from auth.authConfig import recupere_userid,create_user,read_data_users,Superviseur,Surveillant,Administrateur,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
import os
from config.db import con

from sqlalchemy import create_engine, update
from auth.authConfig import create_user,UserResponse,UserCreate,read_users_nom,superviseur_id,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from auth.authConfig import get_current_user
#from schemas.etudiant import EtudiantBase
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
#from models.etudiant import Etudiant
#from models.semestre_etudiant import Etudiants
from sqlalchemy.orm import sessionmaker, relationship, Session
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pathlib import Path
from datetime import datetime
from models.anne import Etudiant


async def addetudiant(matricule: str= Form(...),nom: str= Form(...),
  
    prenom: str= Form(...),
    genre: str= Form(...),
    date_N: datetime= Form(...),
    lieu_n: str= Form(...),
    email: str= Form(...),
    tel: int = Form(...),
    id_fil:int= Form(...),
    nni:int= Form(...),

    nationalite: str = Form(...),
    date_inscription: datetime = Form(...),file: UploadFile = File(...),db: Session = Depends(get_db)):
    try:
        image = await file.read()      
        # Spécifiez le chemin complet du dossier où vous souhaitez stocker l'image
        upload_folder = r"C:\Users\hp\Desktop\PFE\PFE_FRONT\images\etudiants"
       
        # Assurez-vous que le dossier existe, sinon, créez-le
        os.makedirs(upload_folder, exist_ok=True)      
        # Générez un nom de fichier unique (par exemple, basé sur le timestamp)
        unique_filename = f"{datetime.now().timestamp()}.jpg"   
        # Construisez le chemin complet du fichier
        file_path = os.path.join(upload_folder, unique_filename)  
        file_path_str = str(file_path).replace("\\", "/")
        print(file_path_str)
        # Enregpistrez l'image dans le dossier spécifié
        with open(file_path, "wb") as f:
            f.write(image)
        print(file_path_str)    
        # date_N = datetime.strptime('2023-09-01T22:56:45.274Z', '%Y-%m-%dT%H:%M:%S.%fZ')
        # date_insecription = datetime.strptime('2023-09-01T22:56:45.274Z', '%Y-%m-%dT%H:%M:%S.%fZ')

        # Create a new Etudiant object
        etudiant = Etudiant(
            matricule=matricule,
            nom=nom,
            prenom=prenom,
            photo=str(file_path_str),
            genre=genre,
            date_n=date_N,
            lieu_n=lieu_n,
            email=email,
            tel=tel,
            nni=nni,
            id_fil=id_fil,
            nationnalite=nationalite,
            date_inscription=date_inscription,
        )

        # Add the Etudiant object to the session and commit the changes
        db.add(etudiant)
        db.commit()

        return file_path_str
    except Exception as e:
        return {"error": str(e)}