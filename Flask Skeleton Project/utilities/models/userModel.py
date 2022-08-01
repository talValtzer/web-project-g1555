from utilities.db.db_manager import dbManager


class userModel:
    def __init__(self):
        pass

    def Login(self, userName, password):
        query = "SELECT User_name FROM users WHERE User_name=%s AND password=%s"
        return dbManager.fetch(query, (userName, password,))

    def LoginCheckExist(self, userName):
        query = "SELECT User_name FROM users WHERE User_name=%s"
        return dbManager.fetch(query, (userName,))

    def ViewUserDetails(self, userName):
        query = "SELECT * FROM users WHERE User_name=%s"
        return dbManager.fetch(query, (userName,))

    def updateUser(self, userName, First_name, Last_name, email, Academic_institution, Gender, City, about_me):
        query = "UPDATE users SET First_name=%s, Last_name=%s, email=%s, Academic_institution=%s, Gender=%s, City=%s, about_me=%s WHERE User_name=%s"
        return dbManager.commit(query, (
            First_name, Last_name, email, Academic_institution, Gender, City, about_me, userName,))

    def insertUser(self, User_name, First_name, Last_name, email, age, Academic_institution, Gender, City, about_me,
                   password):
        query = "INSERT INTO users (User_name, First_name,Last_name,email,age,Academic_institution,Gender,City,about_me,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        return dbManager.commit(query, (
            User_name, First_name, Last_name, email, age, Academic_institution, Gender, City, about_me, password))

    def userExists(self, userName):
        query = "SELECT User_name FROM users WHERE User_name=%s"
        return dbManager.fetch(query, (userName,))

userModel = userModel()
