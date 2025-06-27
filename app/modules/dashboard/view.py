from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class DashboardView(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("محتوى لوحة التحكم هنا"))
