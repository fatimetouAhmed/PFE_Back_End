from fastapi import APIRouter,Depends
from auth.authConfig import recupere_userid,create_user,Surveillant,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from sqlalchemy import select, literal_column,column,and_,create_engine
from datetime import datetime
from models.anne import Evaluation,Salle,Historiques,SurveillanceSuperviseur,Notifications,Matiere,Etudiant
#from models.anne import Evaluation,salles,historiques,Surveillance,notifications,Matiere
import json
async def write_data_case_etudiant(image1: str, id_etu: int, user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    date = datetime.now()
    surveillant = user_id
    id_sal = 0
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==surveillant).all()
    id_sal=salle[0][0]
    etudiant = session.query(Etudiant.id, Etudiant.nom, Etudiant.prenom,Etudiant.matricule).filter(Etudiant.id == id_etu).all()
    # print(etudiant[0][0],etudiant[0][1],etudiant[0][2])
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(Evaluation.id_sal == id_sal).all()
    # print(evaluation[0][0],evaluation[0][1],evaluation[0][2])
    salleNom = session.query(Salle.nom).filter(Salle.id == id_sal).all()
    # matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    surveillantNom = session.query(User.prenom,User.nom).join(Surveillant).filter(Surveillant.user_id == surveillant).all()
    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    # print(matiere[0][0])
    # description = "Attention étudiant " + str(etudiant[0][2]) + " " + str(etudiant[0][1]) + " n'a pas d'examen en ce moment "+\
    # " et tente d'entrer dans la salle " + str(evaluation[0][1]) + " pour passer  " + str(evaluation[0][2]) + " dans la matière " + \
    #               str(matiere[0][0]) + " au moment " + str(date) + ", le surveillant " + str(surveillant) 
    description="Attention étudiant"
    donnees = {
        "description": description,
        "matricule":etudiant[0][3],
        "etudiant": etudiant[0][2]+" "+etudiant[0][1],
        "evaluation": evaluation[0][2],
        "salle": salleNom[0][0],
        "matiere": matiere[0][0],
        "date": str(date),
        "surveillant": surveillantNom[0][0]+" "+surveillantNom[0][1],
        "status":"Non inscrie"
    }

    # Convertir le dictionnaire en chaîne JSON
    donnees_json = json.dumps(donnees, ensure_ascii=False)
    # con.execute(Historiques.__table__.insert().values(
    #     description=description,
    #     #id_exam=row3[2]
    #     id_exam=evaluation[0][1]
    # ))

    con.execute(Notifications.__table__.insert().values(
        content=donnees_json,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=evaluation[0][1],
        image=image1
    ))
    #print(row3[1])
    return donnees_json

async def write_data_case_etudiant_diplome_licence(image1: str, id_etu: int, user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    date = datetime.now()
    surveillant = user_id
    id_sal = 0
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==surveillant).all()
    id_sal=salle[0][0]
    etudiant = session.query(Etudiant.id, Etudiant.nom, Etudiant.prenom,Etudiant.matricule).filter(Etudiant.id == id_etu).all()
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(and_(Evaluation.id_sal == id_sal,date >= Evaluation.date_debut, date <= Evaluation.date_fin)).all()
    salleNom = session.query(Salle.nom).filter(Salle.id == id_sal).all()
    surveillantNom = session.query(User.prenom,User.nom).join(Surveillant).filter(Surveillant.user_id == surveillant).all()
    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    description="Attention le diplômé(e)"
    donnees = {
        "description": description,
        "matricule":etudiant[0][3],
         "etudiant": etudiant[0][2]+" "+etudiant[0][1],
        "evaluation": evaluation[0][2],
        "salle": salleNom[0][0],
        "matiere": matiere[0][0],
        "date": str(date),
        "surveillant": surveillantNom[0][0]+" "+surveillantNom[0][1],
        "status":"Diplômé en Licence"
    }

    # Convertir le dictionnaire en chaîne JSON
    donnees_json = json.dumps(donnees, ensure_ascii=False)
    con.execute(Notifications.__table__.insert().values(
        content=donnees_json,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=evaluation[0][1],
        image=image1
    ))
    return donnees_json
async def write_data_case_etudiant_diplome_master(image1: str, id_etu: int, user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    date = datetime.now()
    surveillant = user_id
    id_sal = 0
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==surveillant).all()
    id_sal=salle[0][0]
    etudiant = session.query(Etudiant.id, Etudiant.nom, Etudiant.prenom,Etudiant.matricule).filter(Etudiant.id == id_etu).all()
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(and_(Evaluation.id_sal == id_sal,date >= Evaluation.date_debut, date <= Evaluation.date_fin)).all()
    salleNom = session.query(Salle.nom).filter(Salle.id == id_sal).all()
    surveillantNom = session.query(User.prenom,User.nom).join(Surveillant).filter(Surveillant.user_id == surveillant).all()
    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    description="Attention le diplômé(e)"
    donnees = {
        "description": description,
        "matricule":etudiant[0][3],
         "etudiant": etudiant[0][2]+" "+etudiant[0][1],
        "evaluation": evaluation[0][2],
        "salle": salleNom[0][0],
        "matiere": matiere[0][0],
        "date": str(date),
        "surveillant": surveillantNom[0][0]+" "+surveillantNom[0][1],
        "status":"Diplômé en Master"
    }

    # Convertir le dictionnaire en chaîne JSON
    donnees_json = json.dumps(donnees, ensure_ascii=False)
    con.execute(Notifications.__table__.insert().values(
        content=donnees_json,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=evaluation[0][1],
        image=image1
    ))
    return donnees_json

async def write_data_case_etudiant_salle_different(image1: str, id_etu: int,id_salle:int, user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    date = datetime.now()
    surveillant = user_id
    id_sal = 0
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salleEvaluation = session.query(Salle.nom).filter(Salle.id == id_salle).all()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==surveillant).all()
    id_sal=salle[0][0]
    etudiant = session.query(Etudiant.id, Etudiant.nom, Etudiant.prenom,Etudiant.matricule).filter(Etudiant.id == id_etu).all()
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(and_(Evaluation.id_sal == id_sal,date >= Evaluation.date_debut, date <= Evaluation.date_fin)).all()
    salleNom = session.query(Salle.nom).filter(Salle.id == id_sal).all()
    surveillantNom = session.query(User.prenom,User.nom).join(Surveillant).filter(Surveillant.user_id == surveillant).all()
    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    description="Attention etudiant a une évaluation mais n êtes pas dans cette salle"
    donnees = {
        "description": description,
        "matricule":etudiant[0][3],
        "etudiant": etudiant[0][2]+" "+etudiant[0][1],
        "evaluation": evaluation[0][2],
        "salle": salleNom[0][0],
        "matiere": matiere[0][0],
        "date": str(date),
        "surveillant": surveillantNom[0][0]+" "+surveillantNom[0][1],
        "status":"Salle différent",
        "salleevaluation":salleEvaluation[0][0]
    }

    # Convertir le dictionnaire en chaîne JSON
    donnees_json = json.dumps(donnees, ensure_ascii=False)
    con.execute(Notifications.__table__.insert().values(
        content=donnees_json,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=evaluation[0][1],
        image=image1
    ))
    return donnees_json
async def write_data(image1:str,user_id: int = Depends(recupere_userid),user: User = Depends(check_survpermissions)):
    date=datetime.now()
    surveillant = user_id
    print('--------------------------------------')
    print()
    Session = sessionmaker(bind=con)
    session = Session()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==surveillant).all()
    id_sal=salle[0][0]
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(Evaluation.id_sal == id_sal).all()
    # print(evaluation[0][0],evaluation[0][1],evaluation[0][2])
    salleNom = session.query(Salle.nom).filter(Salle.id == id_sal).all()
    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    surveillantNom = session.query(User.prenom,User.nom).join(Surveillant).filter(Surveillant.user_id == surveillant).all()
    message="Attention person a essaie entrer dans la salle"
    # description = "Attention, quelqu'un n'est pas reconnu par l'application, et cette personne essaie d'entrer dans la salle " + str(evaluation[0[0]]) +" pour passer l'evaluation "\
    #         + str(salle[0]["type"]) + " dans la matière " + \
    #                     str(matiere[0][0]) + " au moment "+ str(date) + ", le surveillant "+ str(surveillant) +" de la salle N°" + str(id_sal)
    donnees = {
        "description": message,
        "matricule":"Inconue",
        "etudiant":"Inconue",
        "evaluation": evaluation[0][2],
        "salle": salleNom[0][0],
        "matiere": matiere[0][0],
        "date": str(date),
        "surveillant": surveillantNom[0][0]+" "+surveillantNom[0][1],
        "status":"Inconue"
    }
    print(donnees)
    donnees_json = json.dumps(donnees, ensure_ascii=False)
    # con.execute(Historiques.__table__.insert().values(
    #     description=description,
    #     id_exam=salle[0]["id_exam"]
    # ))

    con.execute(Notifications.__table__.insert().values(
        content=donnees_json,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=evaluation[0][1],
        image=image1,
    ))

    return donnees_json


