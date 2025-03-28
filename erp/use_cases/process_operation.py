from erp.core.erp_system import ERPSystem

class ProcessOperationUseCase:
    """
    Use Case for processing an ERP operation.
    Acts as an interactor between interface adapters (e.g., web controllers) and the core ERP system,
    ensuring that business rules (domain logic) remain isolated.
    """
    def __init__(self, erp_system: ERPSystem):
        self.erp_system = erp_system

    def execute(self, module: str, data: dict) -> str:
        return self.erp_system.process(module, data)
