import mysql.connector
#Variable For Test
ur="root"
pw="Razi0023161469"
#Create Database dbfootball and Tables With User & Password Clint
def CreateDBT(ur, pw):              #(ur,pw,num)
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS dbfootball")
    #Create Table countries
    
    mycursor.execute("USE dbfootball")
    
    #if num == 1 or num == 3:
    mycursor.execute("CREATE TABLE IF NOT EXISTS countries (id INT NOT NULL AUTO_INCREMENT UNIQUE, country_id VARCHAR(10) PRIMARY KEY, \
    country_name VARCHAR(100), country_logo VARCHAR(255))")
    #if num == 2 or num == 3:
    mycursor.execute("CREATE TABLE IF NOT EXISTS persons (id INT NOT NULL AUTO_INCREMENT UNIQUE, uname VARCHAR(255) PRIMARY KEY, \
    ps VARCHAR(100), fname VARCHAR(50), lname VARCHAR(50), gender VARCHAR(6))")
    # mycursor.execute("SHOW DATABASES")
    # #Variable Defining
    # #Variable For Check to Database Exists
    # Exists_DB = False
    # Result_DB = False
    # #Exists_Tables = [countrys,competitions,teams,Player]
    # #Exists_Tables = [False,False,False]
    # #Exists_Table = [country]
    # Exists_Table = False
    # result_Final = False
    # for x in mycursor:
        
    #     if (x[0] == "dbfootball"):
    #         Exists_DB = True
    #         break
    # if not Exists_DB:
    #     mycursor.execute("CREATE DATABASE dbfootball")
    #     Result_DB = True
    # print(Result_DB)
    # if Result_DB:
    #     mycursor.execute("USE dbfootball")
    #     #Create Table
    #     for x in mycursor:
    #         if (x[0] == "country"):
    #             Exists_Table = True

    #         """elif (x[0] == "competitions"):
    #             Exists_Tables[1] = True
    #         elif (x[0] == "teams"):
    #             Exists_Tables[2] = True"""

    #     #result=[]
        
    #     #Create Table countries
    #     if not Exists_Table:
    #         mycursor.execute("CREATE TABLE countries (id INT NOT NULL AUTO_INCREMENT UNIQUE, country_id VARCHAR(10) PRIMARY KEY, \
    #             country_name VARCHAR(100), country_logo VARCHAR(255))")
    #         result_Final = True
    #     #Create Table competitions
    #     # if not Exists_Tables[1]:
    #     #     mycursor.execute("CREATE TABLE competitions (id INT NOT NULL AUTO_INCREMENT UNIQUE, country_id VARCHAR(10) , \
    #     #         country_name VARCHAR(100), league_id VARCHAR(10), league_name VARCHAR(100),league_season VARCHAR(11), \
    #     #         league_logo VARCHAR(255),country_logo VARCHAR(255),FOREIGN KEY (country_id) REFERENCES countries(country_id))")
    #     #     result.append("True")
    #     # else :
    #     #     result.append("True")
    #     # #Create Table teams
    #     # if not Exists_Tables[2]:
    #     #     mycursor.execute("CREATE TABLE teams (id INT NOT NULL AUTO_INCREMENT UNIQUE key , team_key VARCHAR(10) PRIMARY KEY, \
    #     #         team_name VARCHAR(100), team_badge VARCHAR(255), coach_name VARCHAR(100))")
    #     #     result.append("True")
    #     # else :
    #     #     result.append("True")
    #     # #Create Table Player    
    #     # if not Exists[2]:
    #     #     mycursor.execute("CREATE TABLE players (id INT NOT NULL AUTO_INCREMENT UNIQUE key , player_id VARCHAR(15) PRIMARY KEY, \
    #     #         player_image VARCHAR(255), player_name VARCHAR(100), player_number VARCHAR(2),player_type VARCHAR(50),\
    #     #         player_match_played VARCHAR(5),player_goals VARCHAR(5),player_yellow_cards VARCHAR(2),\
    #     #         player_red_cards VARCHAR(2),player_injured VARCHAR(5),player_substitute_out VARCHAR(3),\
    #     #         player_substitutes_on_bench VARCHAR(2),player_assists VARCHAR(2),team_name VARCHAR(50),\
    #     #         team_key VARCHAR(15),FOREIGN KEY (team_key) REFERENCES teams(team_key))")
    #     #     result.append("True")
    #     # else :
    #     #     result.append("True")
    #     # if result == ["True", "True", "True"]:
    #     #     return True
    # return result_Final


#Drop Database dbfootball
def DropDB(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )   
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS dbfootball")
    
    # Exists = False
    # #For Exists Database Or Not
    # result = False
    # #For The Final Result
    # mycursor.execute("SHOW DATABASES")
    # for x in mycursor:
    #     if (x[0] == "dbfootball"):
    #         Exists = True
    #         break
    # #Check DataBase Exists
    # if Exists:
    #     mycursor.execute("drop databases dbfootball")
    #     result = True
    # else :
    #     result = False
    # #The result is whether can drop or not
    # return result

def Insert_iteams(ur,pw,table_name,*args):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw,
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES LIKE 'dbfootball'")
    #Check Exists Database Or Not
    Exists_DB = [x for x in mycursor]
    if len(Exists_DB) == 0:
        CreateDBT(ur, pw)
    mycursor.execute("USE dbfootball")
    #if not 
    #Defining Variable For Work
    args = list(args)
    statement_cols = "INSERT INTO {} (".format(table_name)    
    statement_vals = "VALUES ("
    vals=[]
    statement_final = ""
    if (table_name == "countries"):
        for i in range(3):
            if (i == 0):
                statement_cols += args[i]
                statement_vals += "%s"
            else:
                statement_cols += "," + args[i]
                statement_vals += ", %s"
        for i in range(3):
            args.pop(0)
        statement_cols += ") "
        statement_vals += ")"
        for i in range( 0 , len(args) , 3 ):
                vals.append( (args[ i ], args [ i + 1 ], args[ i + 2 ]) )
        statement_final = statement_cols + statement_vals
    #For persons
    elif (table_name == "persons"):
        for i in range(5):
            if (i == 0):
                statement_cols += args[i]
                statement_vals += "%s"
            else:
                statement_cols += "," + args[i]
                statement_vals += ", %s"
        for i in range(5):
            args.pop(0)
        
        statement_cols += ") "
        statement_vals += ")"
        for i in range( 0 , len(args) , 5 ):
                vals.append( (args[ i ], args [ i + 1 ], args[ i + 2 ], args[ i + 3 ], args[ i + 4 ]) )
        statement_final = statement_cols + statement_vals
    #Elif For Othe Tables
    mycursor.executemany(statement_final,vals)
    mydb.commit()
#CreateDBT(ur,pw)
#Insert_iteams(ur, pw, "persons","uname","ps","fname","lname","gender","232421213","Razi321","amirmahdi","Razi","male")
#Insert_iteams(ur, pw, "countries","country_id","country_name","country_logo","amir1123","Razi321","amirmahdi")