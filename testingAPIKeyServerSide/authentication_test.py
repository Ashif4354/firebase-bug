from requests import Session

def create_account(email, password):
    with Session() as session:
        url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyCDFcFc8f2VdQ9zCV2gPdZDlQppwx87OvU'
        data = {
            'clintType': 'CLIENT_TYPE_WEB',
            'email': email,
            'password': password,
            'returnSecureToken': True
    
        }
        response = session.post(url, json={'email': email, 'password': password})
        return response.status_code
    

if __name__ == '__main__':
    email = 'qwerty@gmail.com'
    password = 'qwerty'
    create_account(email, password)