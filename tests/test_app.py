from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    assert "Chess Club" in resp.json()

def test_signup_and_unregister():
    # Signup
    resp = client.post("/activities/Chess Club/signup?email=tester@mergington.edu")
    assert resp.status_code == 200
    # Duplicate signup
    resp2 = client.post("/activities/Chess Club/signup?email=tester@mergington.edu")
    assert resp2.status_code == 400
    # Unregister
    resp3 = client.delete("/activities/Chess Club/signup?email=tester@mergington.edu")
    assert resp3.status_code == 200
    # Unregister again (should fail)
    resp4 = client.delete("/activities/Chess Club/signup?email=tester@mergington.edu")
    assert resp4.status_code == 404
