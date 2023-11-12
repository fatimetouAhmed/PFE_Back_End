from fastapi import FastAPI, File, UploadFile,HTTPException,Header,status,Depends,APIRouter,Form
import uvicorn
#from prediction import read_image
from starlette.responses import JSONResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, Column, Integer, String ,Sequence,and_,select,delete
from sqlalchemy.ext.declarative import declarative_base
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError,jwt
from passlib.context import CryptContext
import datetime
from prediction import predict_face
from auth.authConfig import PV,recupere_userid,create_user,read_data_users,read_data_users_by_id,Evaluation,Superviseur,Surveillant,Administrateur,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
#import redis
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pathlib import Path
#auuth
#from fastapi import FastAPI, HTTPException, status
from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker, relationship, Session
from models.anne import Annees,Departement,Formation,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User

from auth.authConfig import create_user,UserResponse,UserCreate,recupere_user,get_current_user,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from auth.authConfig import get_current_user,read_users_nom,superviseur_id,hash_password
import os
from routes.etudiants import addetudiant 
from fastapi.middleware.cors import CORSMiddleware
from config.db import con
from routes.annee import annee_router
from routes.scolarite import scolarite_router
from routes.statis import statis_router
from routes.notifications import notification_router
from routes.salle import salle_router
from routes.data import data_router
from routes.surveillance import surveillance_router
from routes.jour import jour_router
from routes.creneau import creneau_router
from routes.creneau_jour import creneaujour_router
from routes.historique import write_data_case_etudiant
app=FastAPI()
Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3"))
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
# Définir les routes pour l'ensemble d'itinéraires surveillance
app.include_router(creneaujour_router, prefix="/creneau_jours", tags=["Creneaux_Jours"])
app.include_router(creneau_router, prefix="/creneaux", tags=["Creneaux"])
app.include_router(jour_router, prefix="/jours", tags=["Jours"])
app.include_router(data_router, prefix="/datas", tags=["Datas"])
app.include_router(surveillance_router, prefix="/surveillances", tags=["Surveillances"])
# Définir les routes pour l'ensemble d'itinéraires etudiant
app.include_router(salle_router, prefix="/salles", tags=["Salles"])
# Définir les routes pour l'ensemble d'itinéraires etudiant
app.include_router(notification_router, prefix="/notifications", tags=["Notifications"])
# Définir les routes pour l'ensemble d'itinéraires annee
app.include_router(annee_router, prefix="/annees", tags=["Annes"])
# Définir les routes pour l'ensemble d'itinéraires annee
app.include_router(scolarite_router, prefix="/scolarites", tags=["Scolarites"])
# Définir les routes pour l'ensemble d'itinéraires statis
app.include_router(statis_router, prefix="/statis", tags=["Statis"])
#--------------------------authentication---------------------#
@app.post("/registeruser/", response_model=UserResponse)
async def create_user(
    nom: str = Form(...),
    prenom: str = Form(...),
    email: str = Form(...),
    pswd: str = Form(...),
    role: str = Form(...),
    id_sal: int = Form(...),
    file: UploadFile = File(...)):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        image = await file.read()      
        # Spécifiez le chemin complet du dossier où vous souhaitez stocker l'image
        upload_folder = r"C:\Users\pc\StudioProjects\pfe\PFE_FRONT\images\users"
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
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        if role == "admin":
            admin = Administrateur(user_id=db_user.id)
            session.add(admin)
            session.commit()
            session.refresh(admin)
        elif role == "surveillant":
            print('-----------------------------------------------------------')
            print(id_sal)
            id_sal = id_sal  # Récupération du superviseur_id depuis user
            surveillant = Surveillant(user_id=db_user.id, id_sal=id_sal)
 # Utilisation du superviseur_id lors de la création du surveillant
            session.add(surveillant)
            session.commit()
            session.refresh(surveillant)
        elif role == "superviseur":
            superviseur = Superviseur(user_id=db_user.id)
            session.add(superviseur)
            session.commit()
            session.refresh(superviseur)

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
    id_sal: int = Form(None),
    file: UploadFile = File(None),
):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Recherchez l'utilisateur dans la base de données par ID
        db_user = session.query(User).filter(User.id == user_id).first()
        
        if not db_user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

        # Supprimez l'ancienne photo du dossier
        if file:
            #if db_user.photo:
            #    os.remove(db_user.photo)

            image = await file.read()
            upload_folder = r"C:\Users\pc\StudioProjects\pfe\PFE_FRONT\images\users"

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
        if id_sal:
            db_user.id_sal = id_sal

        session.commit()
        session.refresh(db_user)

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
    
@app.delete("/usersuveillant/{id}")
async def delete_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    suveillant=delete(Surveillant).where(Surveillant.user_id==id)
    session.execute(suveillant)
    session.commit()
    user=delete(User).where(User.id==id)
    session.execute(user)
    session.commit()
        
@app.delete("/usersuperviseur/{id}")
async def delete_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    superviseur=delete(Superviseur).where(Superviseur.user_id==id)
    session.execute(superviseur)
    session.commit()
    user=delete(User).where(User.id==id)
    session.execute(user)
    session.commit()
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
async def data_user_id(nom:str):
   user_data = await superviseur_id(nom)
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
@app.get("/current_user")
def get_current_user_route(user: User = Depends(get_current_user)):
    nom_fichier = os.path.basename(user.photo)
    user_data = {
        "id": user.id,
        "nom": user.nom,
        "prenom": user.prenom,
        "email": user.email,
        "role": user.role,
        "photo":nom_fichier
    }
  
    return user_data

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
    result= await addetudiant(matricule,nom,prenom,genre,date_N,lieu_n,email,tel,id_fil,nni,nationalite,date_inscription,file,db)
    return {"data": result}
@app.get("/get_surveillant_info/")
def get_surveillant_info(user: User = Depends(check_survpermissions)):
    surveillant = user.surveillant
    return {
        "id": user.id,
        "nom": user.nom,
        "prenom": user.prenom,
        "email": user.email,
        "role": user.role,
        "photo": user.photo,
        "typecompte": surveillant.typecompte
    }

@app.post('/api/predict')
async def predict_image(file: UploadFile = File(...), user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    try:
        image = await file.read()
        with open("image.jpg", "wb") as f:
            f.write(image)
           # print("image.jpg")
        result = await predict_face("image.jpg", user_id, user)
        return result
    except Exception as e:
        return {"error": str(e)}
@app.get("/current_user_id")
def get_current_user_route(user: User = Depends(get_current_user)):

    user_data = {
        "id": user.id,
        "nom": user.nom,
        "prenom": user.prenom,
        "email": user.email,
        "role": user.role
    }
    user_id = user_data["id"]
    return user_id
@app.get("/current_user_nom")
def get_current_user_route(user: User = Depends(get_current_user)):

    user_data = {
        "id": user.id,
        "nom": user.nom,
        "prenom": user.prenom,
        "email": user.email,
        "role": user.role
    }
    user_nom = user_data["prenom"]+' '+user_data["nom"]
    return user_nom
@app.get("/current_user_photo")
def get_current_user_route(user: User = Depends(get_current_user)):
    nom_fichier = os.path.basename(user.photo)
    user_data = {
        "id": user.id,
        "nom": user.nom,
        "prenom": user.prenom,
        "email": user.email,
        "role": user.role,
        "photo":nom_fichier
    }
    user_photo = user_data["photo"]
    return user_photo
@app.post('/api/pv')
async def pv(file: UploadFile = File(...),nom:str=Form(...),type:str=Form(...),id_surv:int=Form(...),description: str = Form(...), nni: str= Form(...),tel: int= Form(...)):
    # surveillant = db.query(Surveillant).filter_by(user_id=current_user['id']).first()
        engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
        Session = sessionmaker(bind=engine)
        session = Session()
        now = datetime.now()  
        id_eval=session.query(Evaluation.id).join(Surveillant,Surveillant.id_sal==Evaluation.id_sal).filter(and_(Surveillant.user_id==id_surv,now >= Evaluation.date_debut, now <= Evaluation.date_fin)).all()
    # try:
        image = await file.read()      
        # Spécifiez le chemin complet du dossier où vous souhaitez stocker l'image
        upload_folder = r"C:\Users\pc\StudioProjects\pfe\PFE_FRONT\images\pv"
       
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
        pv_record = PV(nom=nom,photo=file_path, description=description, nni=nni, tel=tel,type=type, surveillant_id=id_surv, date_pv=datetime.now(),etat='initial',id_eval=id_eval[0][0])
        # Utilisez le chemin du fichier comme URL de la photo
        session.add(pv_record)
        session.commit()
        print(file_path)
        
        return file_path
    # except Exception as e:
        # return {"error": str(e)}
@app.get('/pv')
async def get_pvs():
    Session = sessionmaker(bind=con)
    session = Session()
    query = select(PV.__table__.c.id,
                   PV.__table__.c.photo,
                   PV._table_.c.description,
                   PV._table_.c.nni,
                    PV.__table__.c.tel,
                   User.prenom,PV._table_.c.date_pv). \
        join(Surveillant, Surveillant.user_id == PV._table_.c.surveillant_id). \
        join(User, Surveillant.user_id == User.id)

    result = session.execute(query).fetchall()
    results = []
    for row in result:
        nom_fichier = os.path.basename(row.photo)
        result = {
                  "id": row.id,
                  "photo": nom_fichier,
                  "description": row.description,
                  "nni": row.nni,
                  "tel": row.tel,
                  "surveillant": row.prenom,
                  "date_pv": row.date_pv,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
@app.get('/pv/{id}')
async def get_pvs_by_id(id:int):
    Session = sessionmaker(bind=con)
    session = Session()
    query = select(PV.__table__.c.id,
                   PV.__table__.c.photo,
                   PV._table_.c.description,
                   PV._table_.c.nni,
                    PV.__table__.c.tel,
                   User.prenom,PV._table_.c.date_pv). \
        join(Surveillant, Surveillant.user_id == PV._table_.c.surveillant_id). \
        join(User, Surveillant.user_id == User.id).filter(PV.__table__.c.id==id)
    result = session.execute(query).fetchall()
    results = []
    for row in result:
        nom_fichier = os.path.basename(row.photo)
        result = {
                  "id": row.id,
                  "photo": nom_fichier,
                  "description": row.description,
                  "nni": row.nni,
                  "tel": row.tel,
                  "surveillant": row.prenom,
                  "date_pv": row.date_pv,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
@app.get('/pv/curentuser')
async def get_pvs_user(user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions), db: Session = Depends(get_db)):
    pvs = db.query(PV).filter_by(surveillant_id=user_id).all()
    return pvs
@app.get('/informations/{image1}/{id_etu}/{id}')
async def getInformations(image1: str,id_etu:int,id:int):
             engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
             Session = sessionmaker(bind=engine)
             session = Session()
  #temps actuel
             now = datetime.now()
            #  print("user",user_id)
             #filere de l'etudiant 
             fil=session.query(Etudiant.id_fil).filter(Etudiant.id == id_etu).all()
             print("etudiant",fil[0][0])
             #recuperation des matires de filiere de l'etudiant
             subquery = session.query(Matiere.id).filter(Matiere.id_fil == fil[0][0])
             print("matiere",subquery[0][0])
             #recuperation de salle de surveillance de cette utilisateur a ce moment
            #  salle=session.query(SurveillanceSuperviseur.id_sal).filter(and_(now >= Surveillance.date_debut, now <= Surveillance.date_fin, Surveillance.id_surv==user_id)).all()
             salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==id).all()
             print("sal",salle[0][0])
             exams = session.query(Evaluation.id,Evaluation.id_sal).filter(and_(now >= Evaluation.date_debut, now <= Evaluation.date_fin,Evaluation.id_mat.in_(subquery))).all()
             
             #timestamp = datetime.now().timestamp()

             if not exams:
            #            timestamp = datetime.now().timestamp()
            #            notification_filename = f"{timestamp}.jpg"
            #            notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
            #            notification_path = os.path.join(notification_folder, notification_filename)
            #            os.rename(image1, notification_path)

            # # Nouveau chemin de l'image
            #            image_etu_path = notification_path.replace("\\", "/")        
           
              
                       #return "pas d'examen a ce moment"
                       return await write_data_case_etudiant(image1,id_etu,salle[0][0])
             else : 
                 if(exams[0][1]==salle[0][0]) :
                   return "Rentrez"
                 else :
                     print(exams[0][1])
                     return "Vous avez une évaluation mais n'êtes pas dans cette salle. Votre évaluation est dans la salle " + str(exams[0][1])
    
  
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='192.168.16.113')