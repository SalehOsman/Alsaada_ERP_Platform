# sidebar.py
# الغرض: ودجت الشريط الجانبي المتفاعل مع دعم التثبيت والوضع الليلي وتغيير الألوان ديناميكياً
# المؤلف: صالح عثمان
# تاريخ التعديل: 2025-06-30

from __future__ import annotations

from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QFrame,
    QGraphicsDropShadowEffect,
)
from PySide6.QtCore import Qt, Signal, QEvent, QPropertyAnimation, QObject, QSettings
from PySide6.QtGui import QIcon, QColor

try:
    import qtawesome as qta
except Exception:  # pragma: no cover - optional dependency
    qta = None


class SidebarWidget(QWidget):
    """ودجت شريط جانبي يظهر أيقونات فقط ويتوسع عند التفاعل."""

    navigate = Signal(str)
    PIN_KEY = "sidebar_pinned"

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._collapsed_width = 60
        self._expanded_width = 200
        self.settings = QSettings("AlsaadaERP", "AlsaadaERP")
        self.pinned = self.settings.value(self.PIN_KEY, False, bool)
        self.setFixedWidth(
            self._expanded_width if self.pinned else self._collapsed_width
        )
        self.setProperty("collapsed", not self.pinned)
        self.setMouseTracking(True)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(-3, 0)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self._buttons: dict[str, QPushButton] = {}
        icon_dir = Path(__file__).resolve().parents[2] / "styles" / "icons"
        sections = [
            (
                "dashboard",
                "الرئيسية",
                "fa5s.tachometer-alt",
                icon_dir / "dashboard.svg",
            ),
            (
                "component_guide",
                "دليل المكونات",
                "fa5s.puzzle-piece",
                icon_dir / "guide.svg",
            ),
            ("employees", "العاملون", "fa5s.users", icon_dir / "employees.svg"),
            ("finance", "المالية", "fa5s.chart-line", icon_dir / "finance.svg"),
            ("equipment", "المعدات", "fa5s.tools", icon_dir / "equipment.svg"),
            ("projects", "المشاريع", "fa5s.project-diagram", icon_dir / "projects.svg"),
            (
                "daily_ops",
                "العمليات اليومية",
                "fa5s.calendar-alt",
                icon_dir / "daily_ops.svg",
            ),
            ("notes", "الملاحظات", "fa5s.sticky-note", icon_dir / "notes.svg"),
            ("settings", "الإعدادات", "fa5s.cog", icon_dir / "settings.svg"),
        ]

        for key, text, fa_name, icon in sections:
            button = QPushButton("", self)
            button.setLayoutDirection(Qt.RightToLeft)
            if qta:
                button.setIcon(qta.icon(fa_name))
            else:
                button.setIcon(QIcon(str(icon)))
            button.setToolTip(text)
            button.setCheckable(True)
            button.clicked.connect(lambda _=False, k=key: self._on_button_clicked(k))
            button.installEventFilter(self)
            button._label = text  # type: ignore[attr-defined]
            layout.addWidget(button)
            self._buttons[key] = button

        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        layout.addWidget(divider)
        layout.addWidget(QLabel("اختصارات"))
        layout.addStretch()

        self.pin_btn = QPushButton("", self)
        self.pin_btn.setCheckable(True)
        self.pin_btn.setChecked(self.pinned)
        self._update_pin_icon()
        self.pin_btn.clicked.connect(self._toggle_pinned)
        layout.addWidget(self.pin_btn)

        self._animation = QPropertyAnimation(self, b"minimumWidth")
        self._animation.setDuration(200)

        if self.pinned:
            for btn in self._buttons.values():
                btn.setText(btn._label)
            self.setProperty("collapsed", False)
        else:
            for btn in self._buttons.values():
                btn.setText("")
            self.setProperty("collapsed", True)
        self.style().polish(self)
        self._update_button_shadows()

    # ------------------------------------------------------------------
    # أحداث التفاعل
    # ------------------------------------------------------------------
    def eventFilter(self, obj: QObject, event: QEvent) -> bool:  # type: ignore[name-defined]
        if isinstance(obj, QPushButton) and event.type() == QEvent.Enter:
            if not self.pinned:
                self.expand()
        return super().eventFilter(obj, event)

    def enterEvent(self, event: QEvent) -> None:
        if not self.pinned:
            self.expand()
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        if not self.pinned:
            self.collapse()
        super().leaveEvent(event)

    # ------------------------------------------------------------------
    # التحكم في التثبيت
    # ------------------------------------------------------------------
    def _toggle_pinned(self) -> None:
        self.pinned = self.pin_btn.isChecked()
        self._update_pin_icon()
        self.settings.setValue(self.PIN_KEY, self.pinned)
        if self.pinned:
            self.expand()
        else:
            self.collapse()

    def _update_pin_icon(self) -> None:
        icon_dir = Path(__file__).resolve().parents[2] / "styles" / "icons"
        name = "unpin.svg" if self.pinned else "pin.svg"
        if qta:
            fa_name = "fa5s.times" if self.pinned else "fa5s.thumbtack"
            self.pin_btn.setIcon(qta.icon(fa_name))
        else:
            self.pin_btn.setIcon(QIcon(str(icon_dir / name)))

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
        self.setProperty("collapsed", False)
        self.style().polish(self)
        for btn in self._buttons.values():
            btn.setText(btn._label)
        self._update_button_shadows()

    def collapse(self) -> None:
        """إرجاع الشريط الجانبي إلى وضع الأيقونات فقط."""
        if self.width() == self._collapsed_width:
            return
        self.setMaximumWidth(self._collapsed_width)
        self._animation.stop()
        self._animation.setStartValue(self.width())
        self._animation.setEndValue(self._collapsed_width)
        self._animation.start()
        self.setProperty("collapsed", True)
        self.style().polish(self)
        for btn in self._buttons.values():
            btn.setText("")
        self._update_button_shadows()

    # ------------------------------------------------------------------
    # إدارة الضغط على الأزرار
    # ------------------------------------------------------------------
    def _apply_shadow(self, button: QPushButton) -> None:
        """Apply drop shadow effect to the active button."""
        if not isinstance(button.graphicsEffect(), QGraphicsDropShadowEffect):
            effect = QGraphicsDropShadowEffect(button)
            effect.setBlurRadius(15)
            effect.setOffset(0, 0)
            effect.setColor(QColor(0, 0, 0, 100))
            button.setGraphicsEffect(effect)

    def _remove_shadow(self, button: QPushButton) -> None:
        """Remove shadow effect from a button."""
        if button.graphicsEffect():
            button.setGraphicsEffect(None)

    def _update_button_shadows(self) -> None:
        """Update shadows based on active state and sidebar mode."""
        expanded = not self.property("collapsed")
        for btn in self._buttons.values():
            if btn.isChecked() and expanded:
                self._apply_shadow(btn)
            else:
                self._remove_shadow(btn)

    def _on_button_clicked(self, key: str) -> None:
        for k, b in self._buttons.items():
            b.setChecked(k == key)
        self._update_button_shadows()
        self.navigate.emit(key)
