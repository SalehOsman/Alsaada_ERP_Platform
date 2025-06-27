from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt


class FooterWidget(QWidget):
    """Simple footer displayed at the bottom."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        label = QLabel("© 2024 شركة السعادة")
        layout.addWidget(label, alignment=Qt.AlignCenter)
