import pyrebase

config = {
    "apiKey": "AIzaSyCsw51LzI3LqiJr1wPvdsQ_EGMv51cWuZA",
    "authDomain": "ep-database-d7dce.firebaseapp.com",
    "databaseURL": "https://ep-database-d7dce.firebaseio.com",
    "projectId": "ep-database-d7dce",
    "storageBucket": "ep-database-d7dce.appspot.com",
    "messagingSenderId": "260192294729"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

print db.get()

#db.update({"ep-database-d7dce/seated":false})
#firebase.FirebaseApplication('https://ep-database-d7dce.firebaseio.com/seated').put(false)