import pyrebase

firebaseConfig={'apiKey': "AIzaSyDoibaOR8IBIGglUl_Msm_NHcoBdt8FAdg",

    'authDomain': "final-project-d1529.firebaseapp.com",

    'projectId': "final-project-d1529",

    'databaseURL': "gs://final-project-d1529.appspot.com",

    'storageBucket': "final-project-d1529.appspot.com",

    'messagingSenderId': "360651356513",

    'appId': "1:360651356513:web:62ba94007a2c4c9391ed20"
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

# File named f1.txt is to be uploaded in Cloud
file = "f1.txt"
# In cloud The file is stored as P.txt
storage.child("P.txt").put(file)

storage = firebase.storage()
# From cloud the File named P.txt is downloaded as f2.txt
storage.child("P.txt").download("f2.txt")


# Replace it in appropriate position of the code
'''
storage = firebase.storage()
file = "password.txt"
storage.child("P.txt").put(file)
storage = firebase.storage()
file = "data.txt"
storage.child("D.txt").put(file)


storage = firebase.storage()
storage.child("P.txt").download("password.txt")
storage = firebase.storage()
storage.child("D.txt").download("data.txt")
'''