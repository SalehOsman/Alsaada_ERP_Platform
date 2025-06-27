from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal


class SidebarWidget(QWidget):
    """Vertical sidebar emitting navigation signals."""

    navigate = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self._buttons: dict[str, QPushButton] = {}
        sections = [
            ("dashboard", "الرئيسية"),
            ("employees", "العاملون"),
            ("finance", "المالية"),
            ("equipment", "المعدات"),
            ("projects", "المشاريع"),
            ("daily_ops", "العمليات اليومية"),
            ("notes", "الملاحظات"),
            ("settings", "الإعدادات"),
        ]

        for key, text in sections:
            button = QPushButton(text)
            button.clicked.connect(lambda _=False, k=key: self.navigate.emit(k))
            layout.addWidget(button)
            self._buttons[key] = button

        layout.addStretch()
        layout.addWidget(QLabel("إجراءات سريعة"))
