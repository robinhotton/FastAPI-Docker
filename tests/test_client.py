from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_get_all_clients():
    response = client.get("/api/v1/client/")
    assert response.status_code == 200
    
def test_get_client_by_id():
    response = client.get("/api/v1/client/1")
    assert response.status_code == 200
    
def test_create_client():
    response = client.post("/api/v1/client/", json={"nom": "Doe", "prenom": "John", "adresse": "tmp"})
    assert response.status_code == 201

def test_patch_client():
    response = client.patch("/api/v1/client/1", json={"adresse": "1 rue de la paix"})
    assert response.status_code == 200
    
def test_delete_client():
    response = client.delete("/api/v1/client/1")
    assert response.status_code == 200