from abc import ABC, abstractmethod

class ERPModule(ABC):
    """Abstract ERP Module interface."""
    @abstractmethod
    def process(self, data: dict) -> str:
        pass

class SalesModule(ERPModule):
    def process(self, data: dict) -> str:
        order_id = data.get("order_id", "unknown")
        return f"Sales processed for Order ID: {order_id}"

class InventoryModule(ERPModule):
    def process(self, data: dict) -> str:
        product_id = data.get("product_id", "unknown")
        return f"Inventory updated for Product ID: {product_id}"

class HRModule(ERPModule):
    def process(self, data: dict) -> str:
        employee_id = data.get("employee_id", "unknown")
        return f"HR processed for Employee ID: {employee_id}"

class FinanceModule(ERPModule):
    def process(self, data: dict) -> str:
        invoice_id = data.get("invoice_id", "unknown")
        return f"Finance processed for Invoice ID: {invoice_id}"

class ManufacturingModule(ERPModule):
    def process(self, data: dict) -> str:
        order_id = data.get("order_id", "unknown")
        return f"Manufacturing processed for Order ID: {order_id}"
