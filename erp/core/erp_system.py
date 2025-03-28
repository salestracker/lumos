from typing import Dict
from erp.domain.erp_modules import ERPModule, SalesModule, InventoryModule, HRModule, FinanceModule, ManufacturingModule

class ERPSystem:
    """
    Core ERP System adhering to clean architecture principles.
    Manages and orchestrates ERP modules (Domain Layer) while remaining decoupled
    from external frameworks and UI concerns.
    """
    def __init__(self):
        self._modules: Dict[str, ERPModule] = {}
    
    def register_module(self, name: str, module: ERPModule) -> None:
        self._modules[name] = module
        print(f"Module '{name}' registered.")
    
    def process(self, module_name: str, data: dict) -> str:
        if module_name in self._modules:
            return self._modules[module_name].process(data)
        else:
            return f"Module '{module_name}' not found."

def initialize_erp_system() -> ERPSystem:
    """
    Factory function to initialize the ERP system with default ERP modules.
    """
    system = ERPSystem()
    system.register_module("sales", SalesModule())
    system.register_module("inventory", InventoryModule())
    system.register_module("hr", HRModule())
    system.register_module("finance", FinanceModule())
    system.register_module("manufacturing", ManufacturingModule())
    return system

if __name__ == "__main__":
    erp_system = initialize_erp_system()
    # Demonstration of processing with default modules.
    print(erp_system.process("sales", {"order_id": "1234"}))
    print(erp_system.process("hr", {"employee_id": "emp001"}))
