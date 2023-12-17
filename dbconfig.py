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

from sqlalchemy import  Column, Integer, ForeignKey,create_engine
from sqlalchemy.orm import relationship, mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from config.db import con
from models.anne import Annees,Departement,Formation,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User
from routes.historique import write_data_case_etudiant,write_data_case_etudiant_diplome_master,write_data_case_etudiant_diplome_licence,write_data_case_etudiant_salle_different
from fastapi import APIRouter,Depends
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from datetime import datetime, timedelta
from models.anne import Etudiant ,Evaluation,Surveillant
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3").connect())
session = Session()



# Base.metadata.create_all(con)
def get_etudiant(photo: str):
    # print(photo)
    # Retrieve the student's ID after verifying the image
    etudiants = session.query(Etudiant.id).filter(Etudiant.photo == photo).all()
    id_etu = etudiants[0][0]
    # print(id_etu)
    return  id_etu
async def get_infoexamun(imagepath,image1: str,id_etu:int,user_id: int = Depends(recupere_userid),user: User = Depends(check_survpermissions)):
             engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
             Session = sessionmaker(bind=engine)
             session = Session()
  #temps actuel
             now = datetime.now()
            #  print("user",user_id)
             #filere de l'etudiant 
             etudiant=session.query(Etudiant.date_inscription,Formation.nom).\
                      join(Filiere, Filiere.id == Etudiant.id_fil). \
                     join(Semestre, Semestre.id == Filiere.semestre_id). \
                    join(Niveau, Niveau.id == Semestre.niveau_id). \
                    join(Formation, Formation.id == Niveau.formation_id).filter(Etudiant.id == id_etu).all()
             print(etudiant[0][0])
             date1 = etudiant[0][0]
             date2 = now
             difference = date2 - date1

                # Calculer la différence en années
# Accédez aux jours, heures, minutes, etc. si nécessaire
             difference_jours = difference.days

                # Définir la valeur représentant 5 ans en jours
             cinq_ans_en_jours = 5 * 365
             six_ans_en_jours = 6 * 365

        
             if(etudiant[0][1]=="Licence"):
                # Vérifier si la différence est supérieure à 5 ans
                if difference_jours > cinq_ans_en_jours:
                    timestamp = datetime.now().timestamp()
                    notification_filename = f"{timestamp}.jpg"
                    notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
                    notification_path = os.path.join(notification_folder, notification_filename)
                    os.rename(imagepath, notification_path)

                    # Nouveau chemin de l'image
                    image_etu_path = notification_path.replace("\\", "/") 
                    return await write_data_case_etudiant_diplome_licence(image_etu_path,id_etu, user_id, user)
                else:
                    # print('hello')
                    fil=session.query(Etudiant.id_fil).filter(Etudiant.id == id_etu).all()
                    print("etudiant",fil[0][0])
                    #recuperation des matires de filiere de l'etudiant
                    subquery = session.query(Matiere.id).filter(Matiere.id_fil == fil[0][0])
                    print("matiere",subquery)
                    #recuperation de salle de surveillance de cette utilisateur a ce moment
                    #  salle=session.query(SurveillanceSuperviseur.id_sal).filter(and_(now >= Surveillance.date_debut, now <= Surveillance.date_fin, Surveillance.id_surv==user_id)).all()
                    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==user_id).all()
                    #  id_sal=salle[0][0]
                    
                    exams = session.query(Evaluation.id,Evaluation.id_sal).filter(and_(now >= Evaluation.date_debut, now <= Evaluation.date_fin,Evaluation.id_mat.in_(subquery))).all()
                    
                    #timestamp = datetime.now().timestamp()

                    if not exams:
                            timestamp = datetime.now().timestamp()
                            notification_filename = f"{timestamp}.jpg"
                            notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
                            notification_path = os.path.join(notification_folder, notification_filename)
                            os.rename(imagepath, notification_path)

                    # Nouveau chemin de l'image
                            image_etu_path = notification_path.replace("\\", "/")        
                
        
                            #return "pas d'examen a ce moment"
                            return await write_data_case_etudiant(image_etu_path,id_etu, user_id, user)
                    else:
                            for exam in exams:
                                if exam.id_sal != salle[0][0]:
                                                    timestamp = datetime.now().timestamp()
                                                    notification_filename = f"{timestamp}.jpg"
                                                    notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
                                                    notification_path = os.path.join(notification_folder, notification_filename)
                                                    os.rename(imagepath, notification_path)

                                                    # Nouveau chemin de l'image
                                                    image_etu_path = notification_path.replace("\\", "/") 
                                                    return await write_data_case_etudiant_salle_different(image_etu_path,id_etu,exam.id_sal, user_id, user)
                                    # return "Vous avez une évaluation mais n'êtes pas dans cette salle. Votre évaluation est dans la salle " + str(exam.id_sal)
                            return "Rentrez"
                        
             else :
                if(etudiant[0][1]=="Master"):
                    # Vérifier si la différence est supérieure à 5 ans
                    if difference_jours > six_ans_en_jours:
                        timestamp = datetime.now().timestamp()
                        notification_filename = f"{timestamp}.jpg"
                        notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
                        notification_path = os.path.join(notification_folder, notification_filename)
                        os.rename(imagepath, notification_path)

                        # Nouveau chemin de l'image
                        image_etu_path = notification_path.replace("\\", "/") 
                        return await write_data_case_etudiant_diplome_master(image_etu_path,id_etu, user_id, user)
                    else:
                        # print('hello')
                        fil=session.query(Etudiant.id_fil).filter(Etudiant.id == id_etu).all()
                        print("etudiant",fil[0][0])
                        #recuperation des matires de filiere de l'etudiant
                        subquery = session.query(Matiere.id).filter(Matiere.id_fil == fil[0][0])
                        print("matiere",subquery)
                        #recuperation de salle de surveillance de cette utilisateur a ce moment
                        #  salle=session.query(SurveillanceSuperviseur.id_sal).filter(and_(now >= Surveillance.date_debut, now <= Surveillance.date_fin, Surveillance.id_surv==user_id)).all()
                        salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==user_id).all()
                        #  id_sal=salle[0][0]
                        
                        exams = session.query(Evaluation.id,Evaluation.id_sal).filter(and_(now >= Evaluation.date_debut, now <= Evaluation.date_fin,Evaluation.id_mat.in_(subquery))).all()
                        
                        #timestamp = datetime.now().timestamp()

                        if not exams:
                                timestamp = datetime.now().timestamp()
                                notification_filename = f"{timestamp}.jpg"
                                notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
                                notification_path = os.path.join(notification_folder, notification_filename)
                                os.rename(imagepath, notification_path)

                        # Nouveau chemin de l'image
                                image_etu_path = notification_path.replace("\\", "/")        
                    
            
                                #return "pas d'examen a ce moment"
                                return await write_data_case_etudiant(image_etu_path,id_etu, user_id, user)
                        else:
                                for exam in exams:
                                    if exam.id_sal != salle[0][0]:
                                                        timestamp = datetime.now().timestamp()
                                                        notification_filename = f"{timestamp}.jpg"
                                                        notification_folder = "C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications"
                                                        notification_path = os.path.join(notification_folder, notification_filename)
                                                        os.rename(imagepath, notification_path)

                                                        # Nouveau chemin de l'image
                                                        image_etu_path = notification_path.replace("\\", "/") 
                                                        return await write_data_case_etudiant_salle_different(image_etu_path,id_etu,exam.id_sal, user_id, user)
                                        # return "Vous avez une évaluation mais n'êtes pas dans cette salle. Votre évaluation est dans la salle " + str(exam.id_sal)
                                return "Rentrez"


                            
            
        