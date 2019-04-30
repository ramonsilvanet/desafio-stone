from app import app as testapp
import pytest, base64, json

valid_credentials = base64.b64encode(b'stone:pagamentos').decode('utf-8')

@pytest.fixture
def client():
    testapp.config['TESTING'] = True
    client = testapp.test_client()        
    yield client

def test_get_index_should_be_404_not_found(client):
    response = client.get('/')
    assert response.status_code == 404

def test_get_token_should_be_403_when_credentials_are_missing(client):
    response = client.get('/token')
    assert response.status_code == 403

def test_get_token_should_be_success_when_credentials_are_correct(client):
    
    response = client.get('/token', 
                headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status_code == 200 
    token = json.loads(response.data.decode('utf-8'))["token"]
    assert not token is None

def test_post_job_without_name(client):
    response = client.get('/token', 
                headers={'Authorization': 'Basic ' + valid_credentials})
    token = json.loads(response.data.decode('utf-8'))["token"] + ":"        
    valid_token = base64.b64encode(token.encode('utf-8')).decode('utf-8')
    response = client.post('/job',
                headers={'Authorization': 'Basic ' + valid_token})
    assert response.status_code == 400

def test_create_job_should_be_403_when_give_no_credentials(client):
    response = client.post('/job',                
                data=json.dumps({'job_name': 'countdown', 'meta': {'seconds': 5} }),
                content_type='application/json')
    assert response.status_code == 403

def test_create_job_should_be_405_when_try_http_get(client):
    response = client.get('/job')                
    assert response.status_code == 405

def test_create_job(client):
    response = client.get('/token', 
                headers={'Authorization': 'Basic ' + valid_credentials})
    token = json.loads(response.data.decode('utf-8'))["token"] + ":"        
    valid_token = base64.b64encode(token.encode('utf-8')).decode('utf-8')
    
    response = client.post('/job',
                headers={'Authorization': 'Basic ' + valid_token},
                data=json.dumps({'job_name': 'countdown', 'meta': {'seconds': 5} }),
                content_type='application/json')
    assert response.status_code == 201
    payload = json.loads(response.data.decode('utf-8'))

    assert not payload["id"] is None
    assert not payload["message"] == b"Job created !!!"

def test_get_job_should_be_403_when_give_no_credentials(client):
    response = client.get('/job/aaaaa')                
    assert response.status_code == 403


def test_get_job_status_shouold_be_404_when_give_wrong_id(client):
    response = client.get('/job/aaaaa', headers={'Authorization': 'Basic ' + valid_credentials})                
    assert response.status_code == 404
    payload = json.loads(response.data.decode('utf-8'))
    assert payload["error"] == "Not Found"

def test_get_job_status_shouold_be_success_when_give_correct_id(client):
    response = client.post('/job',
                headers={'Authorization': 'Basic ' + valid_credentials},
                data=json.dumps({'job_name': 'countdown', 'meta': {'seconds': 5} }),
                content_type='application/json')
    
    payload = json.loads(response.data.decode('utf-8'))
    job_id = payload["id"]
    
    endpoint = "/job/{}".format(job_id)
    response = client.get(endpoint, headers={'Authorization': 'Basic ' + valid_credentials})                
    assert response.status_code == 200
    
    payload = json.loads(response.data.decode('utf-8'))
    
    assert payload["id"] == job_id
    assert payload["meta"]["seconds"] == 5
    assert payload["status"] == "finished"
    assert not payload["created_at"] is None
    assert payload["started_at"] is None
    assert payload["finished_at"] is None
    