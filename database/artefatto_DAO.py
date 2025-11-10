from database.DB_connect import ConnessioneDB
from database.museo_DAO import MuseoDAO
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    cnx = ConnessioneDB.get_connection()
    artefatti = list()
    if  cnx is not None:
        cursor = cnx.cursor()
        query = """ SELECT * 
                    FROM artefatto
                    WHERE epoca = COALESCE(%s, epoca)
                          and museo = COALESCE(%s, museo)"""
        cursor.execute(query)
        for row in cursor:
            artefatti.append(row)

        cursor.close()
        cnx.close()

    else:
        print("Impossibile connetersi")

    cnx = ConnessioneDB.get_connection()
    epoche = list()
    if cnx is not None:
        cursor = cnx.cursor()
        query2 = """ SELECT DISTINCT epoca 
                     FROM artefatto
                """
        cursor.execute(query2)
        for row in cursor:
            epoche.append(row)

        cursor.close()
        cnx.close()

    else:
        print("Impossibile connetersi")







