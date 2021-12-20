import mysql.connector
#Create Database dbfootball With User & Password Clint
ur="root"
pw="Razi0023161469"

def CreateDBT(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    #Variable Defining
    #Variable For Check to Database Exists
    Exists_DB = False
    Result_DB = False
    #Exists_Tables = [countrys,competitions,teams]
    Exists_Tables = [False,False,False]
    
    for x in mycursor:
        
        if (x[0] == "dbfootball"):
            Exists_DB = True
            break
    if not Exists_DB:
        mycursor.execute("CREATE DATABASE dbfootball")
        Result_DB = True

    if Result_DB:
        mycursor.execute("USE dbfootball")
        #Create Tables
        for x in mycursor:
            if (x[0] == "country"):
                Exists_Tables[0] = True
            elif (x[0] == "competitions"):
                Exists_Tables[1] = True
            elif (x[0] == "teams"):
                Exists_Tables[2] = True
        result=[]
        #Create Table countries
        if not Exists_Tables[0]:
            mycursor.execute("CREATE TABLE countries (id INT NOT NULL AUTO_INCREMENT UNIQUE key, country_id VARCHAR(10) PRIMARY KEY, \
                country_name VARCHAR(100), country_logo VARCHAR(255))")
            result.append("True")
        else :
            result.append("True")
        #Create Table competitions
        if not Exists_Tables[1]:
            mycursor.execute("CREATE TABLE competitions (id INT NOT NULL AUTO_INCREMENT UNIQUE key , country_id VARCHAR(10) PRIMARY KEY, \
                country_name VARCHAR(100), league_id VARCHAR(10), league_name VARCHAR(100),league_season VARCHAR(11), \
                league_logo VARCHAR(255),country_logo VARCHAR(255))")
            result.append("True")
        else :
            result.append("True")
        #Create Table team
        if not Exists_Tables[2]:
            mycursor.execute("CREATE TABLE teams (id INT NOT NULL AUTO_INCREMENT UNIQUE key , team_key VARCHAR(10) PRIMARY KEY, \
                team_name VARCHAR(100), team_badge VARCHAR(255), coach_name VARCHAR(100))")
            result.append("True")
        else :
            result.append("True")
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
        if result == ["True", "True", "True"]:
            return True
    else :
        return False


#Drop Database dbfootball
def DropDB(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )   
    Exists = False
    #For Exists Database Or Not
    result = False
    #For The Final Result
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        if (x[0] == "dbfootball"):
            Exists = True
            break
    #Check DataBase Exists
    if Exists:
        mycursor.execute("DROP DATABASES dbfootball")
        result = True
    else :
        result = False
    #The result is whether can drop or not
    return result
