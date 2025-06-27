from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QFrame,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from pathlib import Path

from ..core.company_info import company_info


class HeaderWidget(QWidget):
    """Header displaying company logo, name and contact information."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setMinimumHeight(72)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        logo_frame = QFrame()
        logo_frame.setObjectName("logoFrame")
        logo_layout = QVBoxLayout(logo_frame)
        logo_layout.setContentsMargins(4, 4, 4, 4)

        logo_label = QLabel()
        logo_label.setAlignment(Qt.AlignCenter)
        if company_info.logo_path and Path(company_info.logo_path).exists():
            pix = QPixmap(str(company_info.logo_path))
            logo_label.setPixmap(
                pix.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        else:
            logo_label.setText("شعار")

        logo_layout.addWidget(logo_label)

        shadow = QGraphicsDropShadowEffect(logo_frame)
        shadow.setBlurRadius(6)
        shadow.setOffset(0, 1)
        shadow.setColor(QColor(0, 0, 0, 60))
        logo_frame.setGraphicsEffect(shadow)

        company_name = QLabel(company_info.name)
        app_name = QLabel(company_info.app_name)
        app_name.setAlignment(Qt.AlignCenter)
        contact = QLabel(company_info.contact)

        layout.addWidget(logo_frame)
        layout.addWidget(company_name)
        layout.addStretch()
        layout.addWidget(app_name)
        layout.addStretch()
        layout.addWidget(contact)

        header_shadow = QGraphicsDropShadowEffect(self)
        header_shadow.setBlurRadius(10)
        header_shadow.setOffset(0, 2)
        header_shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(header_shadow)
