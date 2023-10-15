from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
# from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
from models.anne import Annees,Departement,Formation
annee_router=APIRouter()
@annee_router.get("/")
async def read_data():
    query = Annees.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"id": row.id,
                  "annee_debut": row.annee_debut,
                  "annee_fin": row.annee_fin}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results

@annee_router.get("/annee_universitaire")
async def read_data():
    query = Annees.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        # Assurez-vous que row.annee_debut et row.annee_fin sont des objets datetime
        annee_debut = row.annee_debut if isinstance(row.annee_debut, datetime) else datetime.strptime(row.annee_debut, "%Y-%m-%dT%H:%M:%S")
        annee_fin = row.annee_fin if isinstance(row.annee_fin, datetime) else datetime.strptime(row.annee_fin, "%Y-%m-%dT%H:%M:%S")
        
        result = {
            "annee_debut": datetime.strftime(annee_debut, "%Y"),  # Convertit la date en année
            "annee_fin": datetime.strftime(annee_fin, "%Y")  # Convertit la date en année
        }
        results.append(result)
    
    return results

@annee_router.get("/departements")
async def read_data():
    query = Departement.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "nom": row.nom_departement}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
@annee_router.get("formations/{id}")
async def read_data_by_id(id:int,):
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les étudiants avec leurs matières
    result_proxy = session.query(Formation.nom)\
               .join(Departement, Departement.id == Formation.dep_id)\
               .filter(Departement.id==id)
    results = []
    for row in result_proxy:
        result = {
                 "nom": row.nom,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results

