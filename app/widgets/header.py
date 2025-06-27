from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt


class HeaderWidget(QWidget):
    """Simple header with logo, names and contact info."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        logo = QLabel("شعار")
        company_name = QLabel("شركة السعادة")
        app_name = QLabel("منصة السعادة لإدارة الموارد")
        contact = QLabel("معلومات الاتصال")

        layout.addWidget(logo)
        layout.addWidget(company_name)
        layout.addStretch()
        layout.addWidget(app_name, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(contact)
