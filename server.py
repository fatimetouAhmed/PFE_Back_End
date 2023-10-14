from fastapi import FastAPI, File, UploadFile,HTTPException,Header,status,Depends,APIRouter,Form
import uvicorn
#from prediction import read_image
from starlette.responses import JSONResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, Column, Integer, String ,Sequence,and_,select
from sqlalchemy.ext.declarative import declarative_base
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError,jwt
from passlib.context import CryptContext
import datetime
from auth.authConfig import PV,recupere_userid,create_user,read_data_users,read_data_users_by_id,Superviseur,Surveillant,Administrateur,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
#import redis
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pathlib import Path
#auuth
#from fastapi import FastAPI, HTTPException, status
from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker, relationship, Session

from auth.authConfig import create_user,UserResponse,UserCreate,recupere_user,get_current_user,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from auth.authConfig import get_current_user,read_users_nom,superviseur_id,hash_password
import os
from routes.etudiants import addetudiant 
from fastapi.middleware.cors import CORSMiddleware
from config.db import con
app=FastAPI()
Session = sessionmaker(bind=con)
# Create a session
session = Session


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (*)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Définir les routes pour l'ensemble d'itinéraires utilisateur
# app.include_router(user_router, prefix="", tags=["Utilisateurs"])

# Définir les routes pour l'ensemble d'itinéraires etudiant


#--------------------------authentication---------------------#
@app.post("/registeruser/", response_model=UserResponse)
async def create_user(
    nom: str = Form(...),
    prenom: str = Form(...),
    email: str = Form(...),
    pswd: str = Form(...),
    role: str = Form(...),
    superviseur_id: int = Form(...),
    file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    try:
        image = await file.read()      
        # Spécifiez le chemin complet du dossier où vous souhaitez stocker l'image
        upload_folder = r"C:\Users\hp\Desktop\PFE\PFE_FRONT\images\users"
        # id_surv_int=int(id_surv)
        # if id_surv == '' or id_surv is None:
        #  id_surv_int = 0
        # else:
        #    id_surv_int = int(id_surv)
     
        # Assurez-vous que le dossier existe, sinon, créez-le
        os.makedirs(upload_folder, exist_ok=True)      
        # Générez un nom de fichier unique (par exemple, basé sur le timestamp)
        unique_filename = f"{datetime.now().timestamp()}.jpg"   
        # Construisez le chemin complet du fichier
        file_path = os.path.join(upload_folder, unique_filename)  
        file_path_str = str(file_path).replace("\\", "/")
        print(file_path_str)
        # Enregistrez l'image dans le dossier spécifié
        with open(file_path, "wb") as f:
            f.write(image)
        print(file_path_str)    
        # date_N = datetime.strptime('2023-09-01T22:56:45.274Z', '%Y-%m-%dT%H:%M:%S.%fZ')
        # date_insecription = datetime.strptime('2023-09-01T22:56:45.274Z', '%Y-%m-%dT%H:%M:%S.%fZ')
        hashed_password = hash_password('ghhg')
        db_user = User(nom=nom, prenom=prenom, email=email, pswd=hashed_password, role=role ,photo=file_path_str)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        if role == "admin":
            admin = Administrateur(user_id=db_user.id)
            db.add(admin)
            db.commit()
            db.refresh(admin)
        elif role == "surveillant":
            superviseur_id = superviseur_id  # Récupération du superviseur_id depuis user
            surveillant = Surveillant(user_id=db_user.id, superviseur_id=superviseur_id)  # Utilisation du superviseur_id lors de la création du surveillant
            db.add(surveillant)
            db.commit()
            db.refresh(surveillant)
        elif role == "superviseur":
            superviseur = Superviseur(user_id=db_user.id)
            db.add(superviseur)
            db.commit()
            db.refresh(superviseur)

        return UserResponse(id=db_user.id, nom=db_user.nom, prenom=db_user.prenom, email=db_user.email, role=db_user.role,photo=db_user.photo)
    except Exception as e:
        return {"error": str(e)}

@app.put("/updateuser/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    nom: str = Form(None),
    prenom: str = Form(None),
    email: str = Form(None),
    pswd: str = Form(None),
    role: str = Form(None),
    superviseur_id: int = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db),
    user: User = Depends(check_Adminpermissions)
):
    try:
        # Recherchez l'utilisateur dans la base de données par ID
        db_user = db.query(User).filter(User.id == user_id).first()
        
        if not db_user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

        # Supprimez l'ancienne photo du dossier
        if file:
            #if db_user.photo:
            #    os.remove(db_user.photo)

            image = await file.read()
            upload_folder = r"C:\Users\hp\Desktop\PFE\PFE_FRONT\images\users"

            # Générez un nom de fichier unique pour la nouvelle photo
            unique_filename = f"{datetime.now().timestamp()}.jpg"
            # Construisez le chemin complet du nouveau fichier
            file_path = os.path.join(upload_folder, unique_filename)
            file_path_str = str(file_path).replace("\\", "/")
            print(file_path_str)
            
            # Enregistrez la nouvelle image dans le dossier spécifié
            with open(file_path, "wb") as f:
                f.write(image)
            print(file_path_str)

            # Mettez à jour le chemin de la nouvelle photo dans la base de données
            db_user.photo = file_path_str
        
        # Mettez à jour les autres colonnes en fonction des données fournies
        if nom:
            db_user.nom = nom
        if prenom:
            db_user.prenom = prenom
        if email:
            db_user.email = email
        if pswd:
            # Vous pouvez mettre à jour le mot de passe de manière appropriée ici
            db_user.pswd = hash_password(pswd)
        if role:
            db_user.role = role
        if superviseur_id:
            db_user.superviseur_id = superviseur_id

        db.commit()
        db.refresh(db_user)

        return UserResponse(
            id=db_user.id,
            nom=db_user.nom,
            prenom=db_user.prenom,
            email=db_user.email,
            role=db_user.role,
            photo=db_user.photo
        )
    except Exception as e:
        # Gérez les erreurs en conséquence
        raise HTTPException(status_code=500, detail="Erreur lors de la mise à jour de l'utilisateur")

@app.put("/{id}")
async def update_data(id:int,usercreate:UserCreate,user: User = Depends(check_Adminpermissions)):
    con.execute(User.__table__.update().values(
        nom=usercreate.nom
    ).where(User.__table__.c.id==id))
    return await read_data_users()
@app.delete("/{id}")
async def delete_data(id:int,user: User = Depends(check_Adminpermissions)):
    con.execute(Superviseur.__table__.delete().where(Superviseur.__table__.c.user_id==id))
    con.execute(Surveillant.__table__.delete().where(Surveillant.__table__.c.user_id==id))
    con.execute(Administrateur.__table__.delete().where(Administrateur.__table__.c.user_id==id))
    con.execute(User.__table__.delete().where(User.__table__.c.id==id))
    return await read_data_users()
@app.get("/user_data_by_id/{id}")
async def read_data_users_by(id:int):
    user_data2 = await read_data_users_by_id(id)
    return user_data2
@app.get("/user_data/")
async def data_user_route():
    user_data1 = await read_data_users()
    return user_data1
@app.get("/nomsuperviseur/")
async def data_user_nom():
    user_data = await read_users_nom()
    return user_data
@app.get("/id_superviseur/{nom}")
async def data_user_id(nom:str,user: User = Depends(check_Adminpermissions)):
   user_data = await superviseur_id(nom,user)
   return user_data
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user.email, "role": user.role},  # Inclusion du rôle dans les données du token
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/admin")
def admin_route(user: User = Depends(check_Adminpermissions)):
    return {"message": "Admin access granted"}

@app.get("/superv")
def superv_route(user: User = Depends(check_superviseurpermissions)):
    return {"message": "superviseur access granted"}

@app.get("/surveillant")
def surv_route(user: User = Depends(check_survpermissions)):
    return {"message": "superviseur access granted"}
@app.post('/api/etudiant')

async def ajouteretudiant(matricule: str= Form(...),nom: str= Form(...),
  
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
    result=addetudiant(matricule,nom,prenom,genre,date_N,lieu_n,email,tel,id_fil,nni,nationalite,date_inscription,file,db)
    return result
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='127.0.0.1')