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
    ([pk] INTEGER PRIMARY KEY, [radius] REAL, [disEarth] REAL, [disSun] REAL, [lum] REAL, [visEarth] TEXT, [madeOf] TEXT, [thumbnail] BLOB)
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
        # print("\n\tLogin Successfull")
    else:
        makeUserLoggedIn.fetchError = True
        # print("\n\tIncorrect Password")



# lst = ["/home/tesla/RedShift/images/thumbnails/6/saturnv2.jpg"]
# lst2 = [l.split("/") for l in lst]
# lth = len(lst2[0])
# print(lth)
# print(lst2[0][7])




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
    # print(fName)
    # print(lth)
    print(thumbName)
    os.system(f"mv {parent}/images/thumbnails/{pk}/{thumbName} {parent}/images/thumbnails/{pk}/{pk}.jpg")

    newThumbPath = f"{parent}/images/thumbnails/{pk}/{pk}.jpg"

    # os.system(f"mv {pk}.jpg")
    try:
        c.execute(
            '''
            INSERT INTO homeInfo
            VALUES(?,?,?)
            ''',(pk,name,newThumbPath)
        )
        dBconnect.commit()
        addObjInfoToDB.fetchError = False
        print(pk,name,newThumbPath)
    except:
        addObjInfoToDB.fetchError = True


# os.system(f"mkdir {curDir}/images/thumbnails/")

c.execute(
    '''
    SELECT * FROM homeInfo
    '''
)

print("\n----------------------\n\t TABLE:::\n------------------------")
getUserInfo = pd.DataFrame(c.fetchall(),columns=['pk', 'objectName', 'thumbnail'])
print(getUserInfo)





# inpk = int(input("pk: "))
# inName = input("Obj Nmae: ")
# inThumb = input("Thumb: ")


# try:
#     c.execute(
#         '''
#         INSERT INTO homeInfo(pk, objectName, thumbnail)
#         VALUES (?,?,?)
#         ''', (inpk,inName,inThumb)
#     )
# except:
#     print("PK already exists!")

dBconnect.commit()



# dBconnect.close()


# c.execute(
#     '''
#     SELECT * FROM homeInfo
#     '''
# )


# getVal = pd.DataFrame(c.fetchall(),columns=['pk','objectName','thumbnail'])
# print(getVal)