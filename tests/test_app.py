from app import app

client = app.test_client()


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"
def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json()["version"] == "1.0.0"
def test_environment():
    response = client.get("/environment")

    assert response.status_code == 200
    assert response.get_json()["environment"] == "development"