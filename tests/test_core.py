# Refactored for pytest while maintaining class-based tests

class TestERPSystem:

    def setup_method(self, method):
        from erp.core.erp_system import initialize_erp_system
        self.erp_system = initialize_erp_system()

    def test_sales_process(self):
        result = self.erp_system.process("sales", {"order_id": "2001"})
        assert result == "Sales processed for Order ID: 2001"

    def test_hr_process(self):
        result = self.erp_system.process("hr", {"employee_id": "E100"})
        assert result == "HR processed for Employee ID: E100"

    def test_invalid_module(self):
        result = self.erp_system.process("nonexistent", {})
        assert result == "Module 'nonexistent' not found."
