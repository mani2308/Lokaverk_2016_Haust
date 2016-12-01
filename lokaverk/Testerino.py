import mysql.connector
from mysql.connector import errorcode

class Connection:
    def CheckConnection(self):
        cnx = mysql.connector.connect(user='2308982439', password='mypassword', host='tsuts.tskoli.is',
                                      database='2308982439_lokaverk_2016h')
        try:
            cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print(err)
        else:
            cnx.close()

    def InsertExample(self):
        cnx = mysql.connector.connect(user='2308982439', password='mypassword', host='tsuts.tskoli.is',
                                      database='2308982439_lokaverk_2016h')

        cursor = cnx.cursor()
        query = "INSERT INTO `game`(`name`, `score`, `time`) VALUES('oli','5000','2016-12-1 14:25:00');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()

    def Display(self):
        result = []
        cnx = mysql.connector.connect(user='2308982439', password='mypassword', host='tsuts.tskoli.is',
                                      database='2308982439_lokaverk_2016h')

        cursor = cnx.cursor()
        query = ("SELECT * FROM `game` WHERE 1;")
        cursor.execute(query)
        for name, score, time in cursor:
            result.append(str(name) + ": " + str(score))
        cursor.close()
        cnx.close()


        return result


con = Connection()
texti = con.Display()
for x in texti:
    print(x)