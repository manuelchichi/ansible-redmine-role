import requests

def test_get_redmine_main_page(host):
     all_variables = host.ansible.get_variables()
     result = host.ansible('debug','var=redmine_url')
     response = requests.get("http://" + result['redmine_url'] + ":8083")
     
     assert response.status_code == 200
     assert 'Redmine' in str(response.content)
