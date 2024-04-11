from requests import Session

def create_account(email, password):
    with Session() as session:
        api_key = ''
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}'
        data = {
            'clintType': 'CLIENT_TYPE_WEB',
            'email': email,
            'password': password,
            'returnSecureToken': True
    
        }
        response = session.post(url, json={'email': email, 'password': password})
        print(response.text)
    

if __name__ == '__main__':
    email = 'qwertyy0@gmail.com'
    password = 'qwerty'
    create_account(email, password)