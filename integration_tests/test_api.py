# Refactored for pytest using FastAPI's TestClient
# This file has been moved to the integration_tests directory to segregate integration tests

import json
from fastapi.testclient import TestClient
from erp.app import app

class TestERPApi:

    def setup_method(self, method):
        self.client = TestClient(app)

    def test_index(self):
        response = self.client.get("/")
        assert response.status_code == 200
        # FastAPI returns a JSON-encoded string for plain str responses.
        # Using response.text to check for the expected welcome message.
        assert "Welcome to the ERP Framework API" in response.text

    def test_sales_api(self):
        payload = {"order_id": "3001"}
        response = self.client.post(
            "/api/process/sales",
            json=payload
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "Sales processed for Order ID: 3001"

    def test_invalid_module_api(self):
        response = self.client.post(
            "/api/process/nonexistent",
            json={}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "Module 'nonexistent' not found."
