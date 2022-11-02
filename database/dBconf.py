import sys
import os
curDir = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(curDir)
sys.path.append(parent)


# from main import redirect

import sqlite3
import pandas as pd


dBconnect = sqlite3.connect('rsdxDB')
c = dBconnect.cursor()




#       Adding New Users to Database
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS userInfo
    ([userName] CHAR(32) PRIMARY KEY, [userPassword] CHAR(32))
    '''
)



#       Creating Table for elements to be displayed in the homepage

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS homeInfo
    ([pk] INTEGER PRIMARY KEY, [objectName] TEXT, [thumbnail] BLOB)
    '''
)

#       Creating Table to store short information

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS basicInfo
    ([pk] INTEGER PRIMARY KEY,[Objname] TEXT, [mass] TEXT, [radius] TEXT, [disEarth] TEXT, [madeOf] TEXT, [lum] TEXT, [visEarth] TEXT, [thumbnail] BLOB)
    '''
)


#       Creating Table to store Brief PostBody

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS broadInfo
    ([pk] INTEGER PRIMARY KEY, [postBody] TEXT)
    '''
)

#       Creating Table to store images

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS objImgs
    ([pk] INTEGER PRIMARY KEY, [img1] BLOB, [img2] BLOB, [img3] BLOB, [img4] BLOB)
    '''
)








def makeUserRegistered(un,pwd):
    makeUserRegistered.fetchError2 = 'False'
    try:
        c.execute(
            '''
            INSERT INTO userInfo(userName,userPassword)
            VALUES(?,?)
            ''', (un,pwd)
            )
        dBconnect.commit()
        makeUserRegistered.fetchError = False
    
    except:
        makeUserRegistered.fetchError = True


def makeUserLoggedIn(un,pwd):    
    try:
        c.execute(
            '''
            SELECT userPassword FROM userInfo
            WHERE userName = ?
            ''',(un,)
        )
    except:
        makeUserLoggedIn.fetchError = True


    getUserInfo = pd.DataFrame(c.fetchall(),columns=['userPassword'])
    pdpass = getUserInfo['userPassword'].to_string(index=False)
    if pwd == pdpass:
        makeUserLoggedIn.fetchError = False

    else:
        makeUserLoggedIn.fetchError = True




def addObjInfoToDB(name,mass,radius,disEarth,madeOf,lum,visible,brinfo,thumbPath):
    c.execute(
        '''
        SELECT COUNT(pk) from homeInfo
        '''
    )
    pk = c.fetchone()[0]
    os.system(f'''
    cd {parent}/images/thumbnails
    mkdir {pk}
    ''')
    os.system(f"cp {thumbPath} {parent}/images/thumbnails/{pk}")
    fName = os.listdir(f"{parent}/images/thumbnails/{pk}")
    fName = fName[0]
    lst = [f"{parent}/images/thumbnails/{pk}/{fName}"]
    lst2 = [l.split("/") for l in lst]
    lth = len(lst2[0])
    thumbName = lst2[0][lth-1]
    print(thumbName)
    os.system(f"mv {parent}/images/thumbnails/{pk}/{thumbName} {parent}/images/thumbnails/{pk}/{pk}.jpg")

    newThumbPath = f"{parent}/images/thumbnails/{pk}/{pk}.jpg"
    try:
        c.execute(
            '''
            INSERT INTO homeInfo
            VALUES(?,?,?)
            ''',(pk,name,newThumbPath)
        )
        dBconnect.commit()
        c.execute(
            '''
            INSERT INTO basicInfo
            VALUES(?,?,?,?,?,?,?,?,?)
            ''',(pk,name,mass,radius,disEarth,madeOf,lum,visible,newThumbPath)
        )
        dBconnect.commit()
        c.execute(
            '''
            INSERT INTO broadInfo
            VALUES(?,?)
            ''',(pk,brinfo)
        )
        dBconnect.commit()
        addObjInfoToDB.fetchError = False

    except:
        addObjInfoToDB.fetchError = True






def getPlanetInfo(pk):
    c.execute(
        '''
        SELECT * from basicInfo WHERE pk = ?
        ''',(pk,)
    )
    # [pk] INTEGER PRIMARY KEY,[Objname] TEXT, [mass] REAL, [radius] REAL,
    # [disEarth] REAL, [madeOf] TEXT, [lum] REAL, [visEarth] TEXT, [thumbnail] BLOB
    val = c.fetchone()
    getPlanetInfo.name = val[1]
    getPlanetInfo.mass = val[2]
    getPlanetInfo.radius = val[3]
    getPlanetInfo.dis = val[4]
    getPlanetInfo.madeof = val[5]
    getPlanetInfo.lum = val[6]
    getPlanetInfo.visible = val[7]
    getPlanetInfo.thumb = val[8]
    # print(name,mass,radius,dis,madeof,lum,visible,thumb)

    c.execute(
        '''
        SELECT * from broadInfo WHERE pk = ?
        ''',(pk,)
    )
    bval = c.fetchone()
    getPlanetInfo.body = bval[1]
 


c.execute(
    '''
    SELECT * FROM homeInfo
    '''
)

# print("\n----------------------\n\t TABLE:::\n------------------------")
# # getUserInfo = pd.DataFrame(c.fetchall(),columns=['pk', 'objectName', 'thumbnail'])
# # print(getUserInfo)
# record = c.fetchone()
# print(record[1])
# c.execute(
#     '''
#     SELECT * FROM basicInfo
#     '''
# )

# print("\n----------------------\n\t TABLE:::\n------------------------")
# getUserInfo = pd.DataFrame(c.fetchall(),columns=['pk', 'Objname', 'mass','radius','disEarth','madeOf','lum','visEarth','thumbnail'])
# print(getUserInfo)


dBconnect.commit()