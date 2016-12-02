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
        query = "INSERT INTO `topplayers`(`playerID`, `playerName`, `playerScore`) VALUES('','','');"
        cursor.execute(query)
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
texti = con.Display()
for x in texti:
    print(x)

#SET SQL_SAFE_UPDATES = 0;


#drop procedure if exists AddPlayer $$

#create procedure AddPlayer(player_name varchar(10),player_points int)
#begin
#	declare lowest_points int;
    
#	insert into TopPlayers(playerName,playerPoints)values(player_name,player_points);
    
#    select min(playerPoints) into lowest_points from TopPlayers;
    
#    if count(playerName) > 9 then
#    delete from TopPlayers where playerPoints = lowest_points;
#    end if;
#end $$


#drop procedure if exists DisplayTopScore $$

#create procedure DisplayTopScore()
#begin
#	select * from TopPlayers order by playerPoints desc;
#end $$

#delimiter ;
