import firebase

url = "https://flickering-fire-1661.firebaseio.com/" # URL to Firebase database
token = "ZpSWTZaRaODNivf2S3Vil0a50BAPjx1ZhGsVbL2S" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

print "Reading from my database."
meow = firebase.get('/sighpie') # get the value from the node age
print meow
firebase.delete('/','age')