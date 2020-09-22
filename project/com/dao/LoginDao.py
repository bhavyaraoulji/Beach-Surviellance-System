import pymysql

class LoginDao:

    def LogDAO(self, loginUsername, loginPasswrd):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='bsh'
        )

        cursor1 = connection.cursor()

        cursor1.execute(
            "Select * from loginmaster WHERE loginUsername = '{}' and loginPasswrd ='{}' ").__format__(loginUsername,loginPasswrd)

        tpl = cursor1.fetchone()
        connection.commit()
        cursor1.close()
        return tpl


    def RegDisplay(self):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='bsh'
        )

        cursor1 = connection.cursor()

        cursor1.execute(
            " SELECT * FROM mvc_demo ")
        tupl = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()

        return tupl