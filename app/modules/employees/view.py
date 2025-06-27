from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget


class EmployeesView(QTabWidget):
    SECTION_TITLE = "العاملون"

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        for i in (1, 2):
            tab_name = f"تبويب {i} {self.SECTION_TITLE}"
            self.addTab(self._create_tab(f"محتوى {tab_name}"), tab_name)

    def _create_tab(self, text: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(text))
        return widget
