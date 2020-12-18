import requests

def test_get_redmine_main_page():
     response = requests.get("http://myprojects.example.com:8082")
     
     assert response.status_code == 200
     assert 'Redmine' in str(response.content)
