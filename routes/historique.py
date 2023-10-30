from fastapi import APIRouter,Depends
from auth.authConfig import recupere_userid,create_user,Surveillant,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from sqlalchemy import select, literal_column,column,and_
from datetime import datetime
from models.anne import Evaluation,Salle,Historiques,SurveillanceSuperviseur,Notifications,Matiere,Etudiant
#from models.anne import Evaluation,salles,historiques,Surveillance,notifications,Matiere


async def write_data_case_etudiant(image1: str, id_etu: int, user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    date = datetime.now()
    id_super = 0
    surveillant = user_id
    id_sal = 0
    salle = []
    matiere_examun = []
    etudiant = []
    a = 0
    # print("image", image1)
    # print("id_etu", id_etu)
    # print("user_id", user_id)
    Session = sessionmaker(bind=con)
    session = Session()
    # salle_query = session.query(Surveillance.id_sal).filter(and_(date >= Surveillance.date_debut, date <= Surveillance.date_fin, Surveillance.id_surv == user_id))
    salle_query = session.query(SurveillanceSuperviseur.id_sal).filter( SurveillanceSuperviseur == user_id)
    
    salle = salle_query.all()

    if salle:
        a = salle[0][0]
        q2 = session.query(Evaluation.id_mat, Salle.nom, Evaluation.id, Evaluation.type).join(Evaluation).filter(Salle.id == a)
        r2 = q2.all()
        r2 = q2.all()
    for row in r2:
        mat_id = row[0]
        a = mat_id
        result = {
            "id_sal": row[0],
            "libelle": row[1],
            "id_exam": row[2],
            "type": row[3],
            
        }
        salle.append(result)
        print(result)
        q3 = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == a)
        r3 = q3.all()            
        for row2 in r3:
                result = {
                    "libelle": row2[0],
                }
                matiere_examun.append(result)

        q4 = session.query(Etudiant.id, Etudiant.nom, Etudiant.prenom).filter(Etudiant.id == id_etu)
        r4 = q4.all()
        for row1 in r4:
            result = {
                "id_etu": row1[0],
                "nom": row1[1],
                "prenom": row1[2],
            }
            etudiant.append(result)

        q5 = session.query(Surveillant.superviseur_id).filter(Surveillant.user_id == user_id)
        r5 = q5.all()
        for row0 in r5:
            id_super = row0[0]
       
    print("id_super")

    description = "Attention étudiant " + str(row1[1]) + " " + str(row1[2]) + " n'a pas d'examen en ce moment "+\
    " et tente d'entrer dans la salle " + str(row[1]) + " pour passer l'examen " + str(row[3]) + " dans la matière " + \
                  str(row2[0]) + " au moment " + str(date) + ", le surveillant " + str(surveillant) + " de la salle N°" + str(id_sal)

    con.execute(Historiques.__table__.insert().values(
        description=description,
        #id_exam=row3[2]
        id_exam=row[2]
    ))

    con.execute(Notifications.__table__.insert().values(
        content=description,
        date=date,
        superviseur_id=id_super,
        is_read=False,
        id_exam=row[2],
        image=image1
    ))
    #print(row3[1])
    return description




async def write_data(image1:str,user_id: int = Depends(recupere_userid),user: User = Depends(check_survpermissions)):
    date=datetime.now()
    id_super=0
    surveillant = user_id
    id_sal = 0
    salle = []
    matiere_examun = []
    a = 0
    Session = sessionmaker(bind=con)
    session = Session()
    q1 = select(column('id_sal')).select_from(SurveillanceSuperviseur).where(SurveillanceSuperviseur.id_sup == surveillant )
    r1 = con.execute(q1)
    for row1 in r1:
        id_sal = row1[0]
        salle_id = row1[0]
        a = salle_id
        # print(a)

    q2 = session.query(Evaluation.id_mat, Salle.nom,Evaluation.id,Evaluation.type).join(Evaluation).filter(Salle.id == a and Evaluation.date_debut<=date and Evaluation.date_fin>=date )
    r2 = q2.all()
    for row2 in r2:
        mat_id = row2[0]
        a = mat_id
        result = {
            "id_sal": row2[0],
            "libelle": row2[1],
            "id_exam": row2[2],
            "type": row2[3],
            
        }
        salle.append(result)

    q3 = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == a)
    r3 = q3.all()
    for row3 in r3:
        mat_id = row3[0]
        a = mat_id
        result = {
            "libelle": row3[0],
        }
        matiere_examun.append(result)
        # print(matiere_examun)
    q5= session.query(Surveillant.superviseur_id).filter(Surveillant.user_id == user_id )
    r5=q5.all()

    for row in r5:
        id_super =row[0]
    # print("supervieur",id_super)
    if salle and matiere_examun:
        description = "Attention, quelqu'un n'est pas reconnu par l'application, et cette personne essaie d'entrer dans " + str(salle[0]["libelle"]) +" pour passer l'examen "\
            + str(salle[0]["type"]) + " dans la matière " + \
                        str(matiere_examun[0]["libelle"]) + " au moment "+ str(date) + ", le surveillant "+ str(surveillant) +" de la salle N°" + str(id_sal)
    else:
        description = "Some default description when data is unavailable"

    # description = "Attention, quelqu'un n'est pas reconnu par l'application, et cette personne essaie d'entrer dans " + str(salle[0]["libelle"]) +" pour passer l'examen "\
    #     + str(salle[0]["type"]) + " dans la matière " + \
    #                 str(matiere_examun[0]["libelle"]) + " au moment "+ str(date) + ", le surveillant "+ str(surveillant) +" de la salle N°" + str(id_sal)

    con.execute(Historiques.__table__.insert().values(
        description=description,
        id_exam=salle[0]["id_exam"]
    ))
    # print("photo  : "+image1)
    # print("examun" + str(salle[0]["id_exam"]))
    con.execute(Notifications.__table__.insert().values(
        content=description,
        date=date,
        superviseur_id=id_super,
        is_read=False,
        id_exam=salle[0]["id_exam"],
        image=image1,
    ))
    print("description", description)
    print("date",date )
    print("superviseur_id",id_super )
    print("salleexam", salle[0]["id_exam"])
    print("image1",image1 )
    return description


