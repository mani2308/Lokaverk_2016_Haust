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

    def InsertExample(self, player_name, score):
        cnx = mysql.connector.connect(user='2308982439', password='mypassword', host='tsuts.tskoli.is',
                                      database='2308982439_lokaverk_2016h')

        cursor = cnx.cursor()
        query = "Call AddPlayer('" + player_name + "', " + str(score) + ");" #kallar i functionid AddPlayer sem eydir
        cursor.execute(query)                                                #notandanum sem er med minnstu stigin.
        cnx.commit()
        cursor.close()
        cnx.close()

    def Display(self):
        result = []
        cnx = mysql.connector.connect(user='2308982439', password='mypassword', host='tsuts.tskoli.is',
                                      database='2308982439_lokaverk_2016h')

        cursor = cnx.cursor()
        query = ("SELECT * FROM `topplayers` WHERE 1;")
        cursor.execute(query)
        for playerID, playerName, playerScore in cursor:
            result.append(str(playerName) + ": " + str(playerScore))
        cursor.close()
        cnx.close()

        return result


con = Connection()
