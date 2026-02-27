import copy
from urllib.parse import quote

import pytest
from fastapi.testclient import TestClient

from src import app as app_module
from src import data


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities dictionary before each test."""
    # copy from the canonical default; we avoid depending on the app's
    # snapshot so tests remain decoupled from implementation details.
    app_module.activities = copy.deepcopy(data.DEFAULT_ACTIVITIES)
    yield


@pytest.fixture
def client():
    return TestClient(app_module.app)


# --- tests ---------------------------------------------------------------

def test_root_redirect(client):
    # disable automatic redirects so we can inspect the status code
    resp = client.get("/", follow_redirects=False)
    assert resp.status_code == 307
    assert resp.headers["location"] == "/static/index.html"


def test_list_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)


def test_signup_success(client):
    name = quote("Chess Club")
    resp = client.post(f"/activities/{name}/signup", params={"email": "new@school.edu"})
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")
    # ensure the participant was actually added
    assert "new@school.edu" in app_module.activities["Chess Club"]["participants"]


def test_signup_missing_activity(client):
    name = quote("Nonexistent")
    resp = client.post(f"/activities/{name}/signup", params={"email": "x@school.edu"})
    assert resp.status_code == 404


def test_signup_already_signed(client):
    name = quote("Chess Club")
    # michael is already signed up in initial snapshot
    resp = client.post(f"/activities/{name}/signup", params={"email": "michael@mergington.edu"})
    assert resp.status_code == 400


def test_unregister_success(client):
    name = quote("Chess Club")
    resp = client.delete(f"/activities/{name}/unregister", params={"email": "daniel@mergington.edu"})
    assert resp.status_code == 200
    assert "Unregistered" in resp.json().get("message", "")
    assert "daniel@mergington.edu" not in app_module.activities["Chess Club"]["participants"]


def test_unregister_missing_activity(client):
    name = quote("Foo")
    resp = client.delete(f"/activities/{name}/unregister", params={"email": "x@school.edu"})
    assert resp.status_code == 404


def test_unregister_not_signed(client):
    name = quote("Chess Club")
    # someone not in the list
    resp = client.delete(f"/activities/{name}/unregister", params={"email": "not@here.edu"})
    assert resp.status_code == 400
