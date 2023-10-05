import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

def get_user():
    return db.collection('users').get()

def get_tasks(user_id):
    return db.collection('users').document(user_id).collection('tasks').get()