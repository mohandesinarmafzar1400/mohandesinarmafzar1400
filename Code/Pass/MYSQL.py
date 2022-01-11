import mysql.connector
#Variable For Test
ur="root"
pw="Razi0023161469"
#Create Database dbfootball and Tables With User & Password Clint
def Create_DBT():              #(ur,pw,num)
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
def Drop_DB():
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )   
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS dbfootball")
#For persons (For Page Recovry Password)    
def update(pas,uname):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE dbfootball")
    #Check Person With Uname Is Exists Or Not
    res = Check_PCE("persons",uname)
    if not res :
        statement="UPDATE persons SET ps = '{}' WHERE uname = \'{}\'".format(pas,uname)
        print(statement)
        mycursor.execute(statement)
        mydb.commit()
    return ( not res )
    
def Insert_Iteams(table_name,*args):
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
        Create_DBT()
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
                if (Check_PCE("countries",args[0])):
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
                if (Check_PCE("persons",args[0])):
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
def Check_PCE(table_name,val):
    mydb = mysql.connector.connect(
    host="localhost",
    user=ur,
    password=pw,
    )
    Check = mydb.cursor()
    Check.execute("SHOW DATABASES LIKE \'dbfootball\'")
    #Check Exists Database Or Not
    Exists_DB = [x for x in Check]
    if len(Exists_DB) == 0:
        Create_DBT()
        return True
    Check.execute("USE dbfootball")
    #if not 
    if (' ' in val):
        val='\'{}\''.format(val)
    else :
        val='\'{}\''.format(val)
    #Defining Variable For Work
    if (table_name == "persons"):
        statement_final = "SELECT uname FROM persons WHERE uname = {}".format(val)
    elif (table_name == "countries"):
        statement_final = "SELECT country_id FROM countries WHERE country_id = {}".format(val)
    #Elif For Othe Tables
    Check.execute(statement_final)
    
    for x in Check:
        if len(x) == 1:
            return False
    else :
        return True


#Select Iteam Form Table Countries
def Select_IC(table_name, val):
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
        Create_DBT()
    mycursor.execute("USE dbfootball")
    #if not 
    if (table_name == "countries"):
        statement_final = "SELECT * FROM countries"
        mycursor.execute(statement_final)
        temp = mycursor.fetchall()
        return temp
    elif (table_name == "persons"):
        statement_final = "SELECT * FROM persons where uname = \'{}\'".format(val)
        mycursor.execute(statement_final)
        for i in mycursor:
            return i
    #Elif For Othe Tables
    
    

#Drop_DB()    
#Check_PCE("persons","123")
#Create_DBT()
# Check_PCE("persons","123")
# #A=Select_IC("persons","amir")
# #print(A)
# Insert_Iteams("persons","uname","ps","fname","lname","gender","amir",str(hash(123)),"amir","rezai","Male")
# Insert_Iteams("persons","uname","ps","fname","lname","gender","reza",str(hash(123)),"zahra","zahrai","Female")
# Insert_Iteams("persons","uname","ps","fname","lname","gender","amir mahdi",str(hash(123)),"Mahdi","Mahdi zade","Male")
# Insert_Iteams("persons","uname","ps","fname","lname","gender","Amirmahdi",str(hash(123)),"Samira","Samirai","Female")

#Insert_Iteams("countries","country_id","country_name","country_logo","am  ir1123","Razi 21","amirmah di")
#Insert_Iteams("persons","uname","ps","fname","lname","amir1138","1","2","3","4") 


#PPPAAASSSSSSS 11