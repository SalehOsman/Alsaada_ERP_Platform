from importlib import import_module
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QStackedWidget


class AppRouter(QObject):
    """Handles navigation between application modules."""

    def __init__(self, stack: QStackedWidget) -> None:
        super().__init__()
        self._stack = stack
        self._pages: dict[str, object] = {}
        self._map = {
            "dashboard": "app.modules.dashboard.view.DashboardView",
            "employees": "app.modules.employees.view.EmployeesView",
            "finance": "app.modules.finance.view.FinanceView",
            "equipment": "app.modules.equipment.view.EquipmentView",
            "projects": "app.modules.projects.view.ProjectsView",
            "daily_ops": "app.modules.daily_ops.view.DailyOpsView",
            "notes": "app.modules.notes.view.NotesView",
            "component_guide": "app.modules.component_guide.view.ComponentGuideView",
            "settings": "app.modules.settings.view.SettingsView",
        }

    def navigate(self, name: str) -> None:
        if name not in self._map:
            return
        if name not in self._pages:
            module_path, class_name = self._map[name].rsplit(".", 1)
            module = import_module(module_path)
            view_class = getattr(module, class_name)
            widget = view_class()
            self._pages[name] = widget
            self._stack.addWidget(widget)
        self._stack.setCurrentWidget(self._pages[name])
