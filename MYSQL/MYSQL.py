import mysql.connector
#Variable For Test
ur="root"
pw="Razi0023161469"
#Create Database dbfootball and Tables With User & Password Clint
def Create_DBT(ur, pw):              #(ur,pw,num)
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )
    mycursor = mydb.cursor()
    #Create DataBase
    mycursor.execute("CREATE DATABASE IF NOT EXISTS dbfootball")
    #Change DataBase
    mycursor.execute("USE dbfootball")
    #Create Table Countries
    mycursor.execute("CREATE TABLE IF NOT EXISTS countries (id INT NOT NULL AUTO_INCREMENT UNIQUE, country_id VARCHAR(10) PRIMARY KEY, \
    country_name VARCHAR(100), country_logo VARCHAR(255))")
    #Create Table Perosns
    mycursor.execute("CREATE TABLE IF NOT EXISTS persons (id INT NOT NULL AUTO_INCREMENT UNIQUE, uname VARCHAR(255) PRIMARY KEY, \
    ps VARCHAR(100), fname VARCHAR(50), lname VARCHAR(50), gender VARCHAR(6))")
    
#Drop Database dbfootball
def Drop_DB(ur,pw):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )   
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS dbfootball")
    

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
        Create_DBT(ur, pw)
    mycursor.execute("USE dbfootball")
    #if not 

    #Defining Variable For Work
    args = list(args)
    statement_cols = "INSERT INTO {} (".format(table_name)    
    statement_vals = "VALUES ("
    vals=[]
    statement_final = ""
    #For Country Insert_Iteams
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
                if (Check_PCE(ur,pw,"countries",args[0])):
                    #If Exists Country In Table Countriies With Primary Key That As Input 
                    vals.append( (args[ i ], args [ i + 1 ], args[ i + 2 ]) )
                else :
                    #Do Noting
                    pass
        statement_final = statement_cols + statement_vals
    #For Cersons Insert_Iteams
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
                if (Check_PCE(ur,pw,"persons",args[0])):
                    #If Exists Person In Table Persons With Primary Key That As Input 
                    vals.append( (args[ i ], args [ i + 1 ], args[ i + 2 ], args[ i + 3 ], args[ i + 4 ]) )
                else :
                    #Do Noting
                    pass
        statement_final = statement_cols + statement_vals
    #Elif For Othe Tables
    mycursor.executemany(statement_final,vals)
    mydb.commit()

#Check Person Or Country Exists
def Check_PCE(ur,pw,table_name,val):
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
        Create_DBT(ur, pw)
    mycursor.execute("USE dbfootball")
    #if not 
    val='\'{}\''.format(val)
    #Defining Variable For Work
    if (table_name == "persons"):
        statement_final = "SELECT uname FROM persons WHERE uname = {}".format(val)
    elif (table_name == "countries"):
        statement_final = "SELECT country_id FROM countries WHERE country_id = '{}'".format(val)
    #Elif For Othe Tables
    mycursor.execute(statement_final)
    for x in mycursor:
        if len(x) == 1:
            return False
    else :
        return True


#Select Iteam Form Table Countries
def Select_IC(ur,pw):
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
        Create_DBT(ur, pw)
    mycursor.execute("USE dbfootball")
    #if not 
    
    statement_final = "SELECT * FROM countries"

    #Elif For Othe Tables
    mycursor.execute(statement_final)
    #Defining Variable For Work
    temp = mycursor.fetchall()
    return temp

#Drop_DB(ur,pw)    
#Create_DBT(ur,pw)
#Select_Iteams(ur,pw,"persons","uname","123")
#Insert_iteams(ur, pw, "persons","uname","ps","fname","lname","gender","2324 1221213","Raz i321","amirm ahdi","Ra zi","m ale")
#Insert_iteams(ur, pw, "countries","country_id","country_name","country_logo","amir1123","Razi321","amirmahdi")
#Insert_iteams(ur, pw,"persons","uname","ps","fname","lname","gender","amir1138","1","2","3","4")