from fastapi import APIRouter,Depends
from auth.authConfig import recupere_userid,create_user,Surveillant,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from sqlalchemy import select, literal_column,column,and_,create_engine
from datetime import datetime
from models.anne import Evaluation,Salle,Historiques,SurveillanceSuperviseur,Notifications,Matiere,Etudiant
#from models.anne import Evaluation,salles,historiques,Surveillance,notifications,Matiere


async def write_data_case_etudiant(image1: str, id_etu: int, user_id: int = Depends(recupere_userid), user: User = Depends(check_survpermissions)):
    date = datetime.now()
    surveillant = user_id
    id_sal = 0
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==id).all()
    id_sal=salle[0][0]
    etudiant = session.query(Etudiant.id, Etudiant.nom, Etudiant.prenom).filter(Etudiant.id == id_etu).all()
    # print(etudiant[0][0],etudiant[0][1],etudiant[0][2])
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(Evaluation.id_sal == id_sal).all()
    # print(evaluation[0][0],evaluation[0][1],evaluation[0][2])

    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()
    # print(matiere[0][0])
    description = "Attention étudiant " + str(etudiant[0][2]) + " " + str(etudiant[0][1]) + " n'a pas d'examen en ce moment "+\
    " et tente d'entrer dans la salle " + str(evaluation[0][1]) + " pour passer  " + str(evaluation[0][2]) + " dans la matière " + \
                  str(matiere[0][0]) + " au moment " + str(date) + ", le surveillant " + str(surveillant) 

    # con.execute(Historiques.__table__.insert().values(
    #     description=description,
    #     #id_exam=row3[2]
    #     id_exam=evaluation[0][1]
    # ))

    con.execute(Notifications.__table__.insert().values(
        content=description,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=evaluation[0][1],
        image=image1
    ))
    #print(row3[1])
    return description




async def write_data(image1:str,user_id: int = Depends(recupere_userid),user: User = Depends(check_survpermissions)):
    date=datetime.now()
    surveillant = user_id
    Session = sessionmaker(bind=con)
    session = Session()
    salle=session.query(Surveillant.id_sal).filter(Surveillant.user_id==id).all()
    id_sal=salle[0][0]
    evaluation = session.query(Evaluation.id_mat,  Evaluation.id, Evaluation.type).filter(Evaluation.id_sal == id_sal).all()
    # print(evaluation[0][0],evaluation[0][1],evaluation[0][2])

    matiere = session.query(Matiere.libelle).join(Evaluation).filter(Evaluation.id_mat == evaluation[0][0]).all()

    description = "Attention, quelqu'un n'est pas reconnu par l'application, et cette personne essaie d'entrer dans la salle " + str(evaluation[0[0]]) +" pour passer l'evaluation "\
            + str(salle[0]["type"]) + " dans la matière " + \
                        str(matiere[0][0]) + " au moment "+ str(date) + ", le surveillant "+ str(surveillant) +" de la salle N°" + str(id_sal)
    con.execute(Historiques.__table__.insert().values(
        description=description,
        id_exam=salle[0]["id_exam"]
    ))
    print("photo  : "+image1)
    print("examun" + str(salle[0]["id_exam"]))
    con.execute(Notifications.__table__.insert().values(
        content=description,
        date=date,
        surveillant_id=surveillant,
        is_read=False,
        id_exam=salle[0]["id_exam"],
        image=image1,
    ))

    return description


