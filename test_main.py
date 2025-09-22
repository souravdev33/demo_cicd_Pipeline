import pytest
from fastapi.testclient import TestClient
from main import api 

client = TestClient(api)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


def test_add_ticket():
    ticket = {
        "id": 1,
        "flight_name": "Air Bangladesh",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    }
    response = client.post("/ticket", json=ticket)
    assert response.status_code == 200
    assert response.json() == ticket


def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(ticket["id"] == 1 for ticket in data)


def test_update_ticket():
    updated_ticket = {
        "id": 1,
        "flight_name": "Air India",
        "flight_date": "2025-11-01",
        "flight_time": "16:00",
        "destination": "Delhi"
    }
    response = client.put("/ticket/1", json=updated_ticket)
    assert response.status_code == 200
    assert response.json() == updated_ticket


def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    deleted_ticket = response.json()
    assert deleted_ticket["id"] == 1

    response = client.get("/ticket")
    assert all(ticket["id"] != 1 for ticket in response.json())