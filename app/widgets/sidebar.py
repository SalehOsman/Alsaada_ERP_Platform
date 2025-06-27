# sidebar.py
# الغرض: ودجت الشريط الجانبي المتجاوب مع توسع تلقائي عند المرور بالماوس
# المؤلف: صالح عثمان
# تاريخ التعديل: 2025-06-28

from __future__ import annotations

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QStyle
from PySide6.QtCore import Signal, QEvent, QPropertyAnimation, QObject
=======
from PySide6.QtCore import Qt, Signal, QEvent, QPropertyAnimation, QObject



class SidebarWidget(QWidget):
    """ودجت شريط جانبي يظهر أيقونات فقط ويتوسع عند المرور بالماوس."""

    navigate = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._collapsed_width = 60
        self._expanded_width = 200
        self.setFixedWidth(self._collapsed_width)
        self.setMouseTracking(True)

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
            button = QPushButton("", self)
            button.setIcon(self.style().standardIcon(icon))
            button.setToolTip(text)
            button.clicked.connect(lambda _=False, k=key: self.navigate.emit(k))
            button.installEventFilter(self)
            button._label = text  # type: ignore[attr-defined]
            layout.addWidget(button)
            self._buttons[key] = button

        layout.addStretch()
        layout.addWidget(QLabel("إجراءات سريعة"))

        self._animation = QPropertyAnimation(self, b"minimumWidth")
        self._animation.setDuration(150)

    # ------------------------------------------------------------------
    # الأحداث
    # ------------------------------------------------------------------
    def eventFilter(self, obj: QObject, event: QEvent) -> bool:  # type: ignore[name-defined]
        if isinstance(obj, QPushButton) and event.type() == QEvent.Enter:
            self.expand()
        return super().eventFilter(obj, event)

    def enterEvent(self, event: QEvent) -> None:
        self.expand()
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.collapse()
        super().leaveEvent(event)

    # ------------------------------------------------------------------
    # التحويل بين الوضعين
    # ------------------------------------------------------------------
    def expand(self) -> None:
        """توسيع الشريط الجانبي وإظهار أسماء الأقسام."""
        if self.width() == self._expanded_width:
            return
        self.setMaximumWidth(self._expanded_width)
        self._animation.stop()
        self._animation.setStartValue(self.width())
        self._animation.setEndValue(self._expanded_width)
        self._animation.start()
        for btn in self._buttons.values():
            btn.setText(btn._label)

    def collapse(self) -> None:
        """إرجاع الشريط الجانبي إلى وضع الأيقونات فقط."""
        if self.width() == self._collapsed_width:
            return
        self.setMaximumWidth(self._collapsed_width)
        self._animation.stop()
        self._animation.setStartValue(self.width())
        self._animation.setEndValue(self._collapsed_width)
        self._animation.start()
        for btn in self._buttons.values():
            btn.setText("")
