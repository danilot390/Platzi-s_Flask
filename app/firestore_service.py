import firebase_admin
import logging
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-390'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential,{
    'projectId' : project_id,
})

db = firestore.client()

def current_user(id):
    try:
        return db.collection('users').document(id).get().to_dict()
    except Exception as e:
        logging.error('Error retrieving user data: %s', str(e))
        return None

def get_user(username):
    try:
        # Get a reference to the 'users' collection and query for the specified username
        user_query = db.collection('users').where('username','==', username)

        # Get the query snapshot
        user_snapshots = user_query.get()

        # Check the number of matching documents
        if len(user_snapshots) == 1:
            return user_snapshots[0].to_dict()
        return None
    
    except Exception as e:
        logging.error('Error retrieving user data: %s', str(e))
        return None

def create_user(user):
    new_user = db.collection('users').document(str(user.id))
    new_user.set({
        'id': user.id,
        'username' : user.username,
        'password': user.password,
        })

def create_task(user_id, description):
    task_collection_ref = db.collection('users').document(user_id).collection('tasks')
    task_collection_ref.add({
        'description': description,
        'done': False
        })
    
def delete_task(user_id, task_id):
    task_ref = db.document('users/{}/tasks/{}'.format(user_id, task_id))
    #task_ref = db.collection('users').document(user_id).collection('tasks').document(task_id)
    task_ref.delete()


def get_tasks(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('tasks').get()