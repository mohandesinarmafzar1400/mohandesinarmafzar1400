import mysql.connector
#Create Database dbfootball With User & Password Clint
ur="root"
pw="Razi0023161469"

def CreateDB(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    #Variable For Check to Database Exists
    Exists = False
    for x in mycursor:
        
        if (x[0] == "dbfootball"):
            Exists = True
            break
    if not Exists:
        mycursor.execute("CREATE DATABASE DBFootBall")
        return True
    else :
        return False

#Create Table
def CreateT(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw,
    database="dbfootball"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")
    #Exists = [Country,Competitions,Teams,(Player)]
    Exists = [False,False,False]
    for x in mycursor:
        
        if (x[0] == "country"):
            Exists[0] = True
        elif (x[0] == "competitions"):
            Exists[1] = True
        elif (x[0] == "teams"):
            Exists[2] = True
    result=[]
    #Create Table countries
    if not Exists[0]:
        mycursor.execute("CREATE TABLE countries (id INT NOT NULL AUTO_INCREMENT UNIQUE key, country_id VARCHAR(10) PRIMARY KEY, \
            country_name VARCHAR(100), country_logo VARCHAR(255))")
        #
        result.append("True")
    else :
        result.append("True")
    #Create Table Competitions
    if not Exists[1]:
        mycursor.execute("CREATE TABLE competitions (id INT NOT NULL AUTO_INCREMENT UNIQUE key , country_id VARCHAR(10) PRIMARY KEY, \
            country_name VARCHAR(100), league_id VARCHAR(10), league_name VARCHAR(100),league_season VARCHAR(11), \
            league_logo VARCHAR(255),country_logo VARCHAR(255))")
        result.append("True")
    else :
        result.append("True")
    #Create Table Team
    if not Exists[2]:
        mycursor.execute("CREATE TABLE teams (id INT NOT NULL AUTO_INCREMENT UNIQUE key , team_key VARCHAR(10) PRIMARY KEY, \
            team_name VARCHAR(100), team_badge VARCHAR(255), coach_name VARCHAR(100))")
        result.append("True")
    else :
        result.append("True")
    return result
    # #Create Table Player    
    # if not Exists[1]:
    #     mycursor.execute("CREATE TABLE Player (id INT NOT NULL AUTO_INCREMENT UNIQUE key , player_id VARCHAR(15) PRIMARY KEY, \
    #         player_image VARCHAR(255), player_name VARCHAR(100), player_number VARCHAR(2),player_type VARCHAR(50),\
    #         player_type VARCHAR(2),player_match_played VARCHAR(5),player_goals VARCHAR(5),player_goals VARCHAR(3),\
    #         player_red_cards VARCHAR(2),player_injured VARCHAR(5),player_substitute_out VARCHAR(3),\
    #         player_substitutes_on_bench VARCHAR(2),player_assists VARCHAR(2),team_name VARCHAR(50),\
    #         team_key VARCHAR(15))")
    #     result.append("True")
    # else :
    #     result.append("True")

#Drop Database dbfootball
def DropDB(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw,
    database="dbfootball"
    )   
    Exists = False
    #For Exists Database Or Not
    result = False
    #For The Final Result
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        if (x[0] == "dbfootball"):
            EXists = True
            break
    #Check DataBase Exists
    if EXists:
        mycursor.execute("DROP DATABASES dbfootball")
        result = True
    #The result is whether can drop or not
    return result


res_CDB = CreateDB(ur,pw)
if res_CDB:
    res_CT = CreateT(ur,pw)
    if res_CDB == True and res_CT == ['True','True','True']:
        print("Create DB and tables")
    else :
        print("Can't Create Table")
else :
    print("Fail Create DB")