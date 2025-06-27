from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QStyle
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
            ("dashboard", "الرئيسية", QStyle.SP_DesktopIcon),
            ("component_guide", "دليل المكونات", QStyle.SP_FileDialogListView),
            ("employees", "العاملون", QStyle.SP_ComputerIcon),
            ("finance", "المالية", QStyle.SP_DriveHDIcon),
            ("equipment", "المعدات", QStyle.SP_DriveNetIcon),
            ("projects", "المشاريع", QStyle.SP_DirIcon),
            ("daily_ops", "العمليات اليومية", QStyle.SP_FileDialogDetailedView),
            ("notes", "الملاحظات", QStyle.SP_FileDialogInfoView),
            ("settings", "الإعدادات", QStyle.SP_FileDialogDetailedView),
        ]

        for key, text, icon in sections:
            button = QPushButton(text)
            button.setIcon(self.style().standardIcon(icon))
            button.clicked.connect(lambda _=False, k=key: self.navigate.emit(k))
            layout.addWidget(button)
            self._buttons[key] = button

        layout.addStretch()
        layout.addWidget(QLabel("إجراءات سريعة"))
