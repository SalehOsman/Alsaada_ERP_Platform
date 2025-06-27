# sidebar.py
# حل ذكي: الأيقونات باللون الأساسي عند أول تحميل، ثم تعود للألوان الصحيحة مع أول تفاعل
# صالح عثمان – 2025-06-30

from __future__ import annotations

from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QGraphicsDropShadowEffect, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal, QEvent, QPropertyAnimation, QObject, QSettings, QSize
from PySide6.QtGui import QIcon, QColor, QFont
from ..core.theme_manager import ThemeManager

try:
    import qtawesome as qta
except Exception:
    qta = None

class SidebarWidget(QWidget):
    """Collapsible sidebar with navigation buttons."""

    navigate = Signal(str)
    PIN_KEY = "sidebar_pinned"

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("SidebarWidget")
        self._collapsed_width = 60
        self._expanded_width = 200
        self._icon_size_collapsed = 36
        self._icon_size_expanded = 24
        self._padding_lr = 14
        self.settings = QSettings("AlsaadaERP", "AlsaadaERP")
        self.pinned = self.settings.value(self.PIN_KEY, False, bool)
        self.setFixedWidth(self._expanded_width if self.pinned else self._collapsed_width)
        self.setProperty("collapsed", not self.pinned)
        self.setMouseTracking(True)
        self._initialized = False  # لمعالجة أول تهيئة بصرية

        # شادو يسار القائمة فقط
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(32)
        self.shadow.setOffset(-12, 0)
        self.shadow.setColor(QColor(0, 0, 0, 130))
        self.setGraphicsEffect(self.shadow)

        # إطار رئيسي لضبط الخلفية يدويًا
        self.frame = QFrame(self)
        self.frame.setObjectName("SidebarMainFrame")
        self.frame.setGeometry(0, 0, self._collapsed_width, self.height())

        # layout داخلي
        layout = QVBoxLayout(self.frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._buttons: dict[str, QPushButton] = {}
        self._section_keys = []
        icon_dir = Path(__file__).resolve().parents[2] / "styles" / "icons"
        sections = [
            ("dashboard", "الرئيسية", "fa5s.tachometer-alt", icon_dir / "dashboard.svg"),
            ("component_guide", "دليل المكونات", "fa5s.puzzle-piece", icon_dir / "guide.svg"),
            ("employees", "العاملون", "fa5s.users", icon_dir / "employees.svg"),
            ("finance", "المالية", "fa5s.chart-line", icon_dir / "finance.svg"),
            ("equipment", "المعدات", "fa5s.tools", icon_dir / "equipment.svg"),
            ("projects", "المشاريع", "fa5s.project-diagram", icon_dir / "projects.svg"),
            ("daily_ops", "العمليات اليومية", "fa5s.calendar-alt", icon_dir / "daily_ops.svg"),
            ("notes", "الملاحظات", "fa5s.sticky-note", icon_dir / "notes.svg"),
            ("settings", "الإعدادات", "fa5s.cog", icon_dir / "settings.svg"),
        ]

        for idx, (key, text, fa_name, icon) in enumerate(sections):
            button = QPushButton("", self.frame)
            button.setLayoutDirection(Qt.LeftToRight)
            button.setCursor(Qt.PointingHandCursor)
            button._fa_name = fa_name
            button._icon_path = icon
            button.setToolTip(text)
            button.setCheckable(True)
            button.installEventFilter(self)
            button._label = text
            button.setMinimumHeight(52)
            button.setMaximumHeight(60)
            button.setFont(QFont("Cairo", 12))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.clicked.connect(lambda _=False, k=key: self._on_button_clicked(k))
            # عند التهيئة: كل الأيقونات باللون الأساسي
            if qta:
                button.setIcon(qta.icon(fa_name, color=ThemeManager.palette["primary"]))
            else:
                button.setIcon(QIcon(str(icon)))
            button.setIconSize(QSize(self._icon_size_collapsed, self._icon_size_collapsed))
            button.setProperty("active", key == "dashboard")
            button.setChecked(key == "dashboard")
            self._buttons[key] = button
            self._section_keys.append(key)
            layout.addWidget(button)

        layout.addStretch()
        self.pin_btn = QPushButton("", self.frame)
        self.pin_btn.setCheckable(True)
        self.pin_btn.setChecked(self.pinned)
        self.pin_btn.setMinimumHeight(45)
        self.pin_btn.setMaximumHeight(52)
        self.pin_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pin_btn.clicked.connect(self._toggle_pinned)
        # لون أيقونة الدبوس الأساسي فقط (حتى التفاعل)
        if qta:
            self.pin_btn.setIcon(qta.icon("fa5s.thumbtack", color=ThemeManager.palette["primary"]))
        else:
            icon_dir = Path(__file__).resolve().parents[2] / "styles" / "icons"
            self.pin_btn.setIcon(QIcon(str(icon_dir / "pin.svg")))
        layout.addWidget(self.pin_btn)

        self._animation = QPropertyAnimation(self, b"minimumWidth")
        self._animation.setDuration(200)

        self._active_key = "dashboard"

        # الوضع الافتراضي – يبدأ دائماً مغلق (collapsed) إذا لم يكن مثبّتاً
        if self.pinned:
            self.expand()
        else:
            self.collapse()

        self.update()
        self.frame.update()
        self.repaint()
        self.frame.repaint()

    def resizeEvent(self, event):
        self.frame.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        # عند أول حدث تفاعل (hover)، فعّل collapse() لإعادة الألوان والتنسيقات الديناميكية
        if not self._initialized and (event.type() == QEvent.Enter):
            self._initialized = True
            self.collapse()  # تعيد تعيين الألوان الصحيحة فور أول تفاعل
            self.update()
            self.frame.update()
            self.repaint()
            self.frame.repaint()
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
        fa_color = ThemeManager.palette["primary"]
        name = "unpin.svg" if self.pinned else "pin.svg"
        if qta:
            fa_name = "fa5s.times" if self.pinned else "fa5s.thumbtack"
            self.pin_btn.setIcon(qta.icon(fa_name, color=fa_color))
        else:
            self.pin_btn.setIcon(QIcon(str(icon_dir / name)))

    def expand(self) -> None:
        if self.width() == self._expanded_width:
            return
        self.setMaximumWidth(self._expanded_width)
        self._animation.stop()
        self._animation.setStartValue(self.width())
        self._animation.setEndValue(self._expanded_width)
        self._animation.start()
        self.setProperty("collapsed", False)
        self._refresh_sidebar_style(collapsed=False)
        self._update_selection()
        self.update()
        self.frame.update()
        self.repaint()
        self.frame.repaint()

    def collapse(self) -> None:
        if self.width() == self._collapsed_width:
            return
        self.setMaximumWidth(self._collapsed_width)
        self._animation.stop()
        self._animation.setStartValue(self.width())
        self._animation.setEndValue(self._collapsed_width)
        self._animation.start()
        self.setProperty("collapsed", True)
        self._refresh_sidebar_style(collapsed=True)
        self._update_selection()
        self.update()
        self.frame.update()
        self.repaint()
        self.frame.repaint()

    def _refresh_sidebar_style(self, collapsed: bool):
        """Update frame styling and shadow after collapsing or expanding."""
        self.shadow.setColor(QColor(0, 0, 0, 130))
        self.style().polish(self)
        self.frame.update()

    def _update_selection(self):
        """Refresh button states and icons based on selection."""
        collapsed = self.property("collapsed")
        if not any(btn.property("active") for btn in self._buttons.values()):
            self._buttons[self._active_key].setProperty("active", True)

        for key, btn in self._buttons.items():
            is_active = bool(btn.property("active"))
            btn.setGraphicsEffect(None)
            btn.setText("" if collapsed else btn._label)
            if not collapsed and is_active:
                shadow = QGraphicsDropShadowEffect(btn)
                shadow.setBlurRadius(14)
                shadow.setOffset(0, 0)
                shadow.setColor(QColor(0, 0, 0, 120))
                btn.setGraphicsEffect(shadow)

            icon_color = ThemeManager.palette["secondary"] if (collapsed or is_active) else ThemeManager.palette["primary"]
            if qta:
                btn.setIcon(qta.icon(btn._fa_name, color=icon_color))
            else:
                btn.setIcon(QIcon(str(btn._icon_path)))
            btn.setIconSize(QSize(
                self._icon_size_collapsed if collapsed else self._icon_size_expanded,
                self._icon_size_collapsed if collapsed else self._icon_size_expanded,
            ))
            btn.style().polish(btn)

        # زر الدبوس – اللون الأساسي في جميع الحالات
        if qta:
            self.pin_btn.setIcon(qta.icon("fa5s.thumbtack", color=ThemeManager.palette["primary"]))
        else:
            icon_dir = Path(__file__).resolve().parents[2] / "styles" / "icons"
            self.pin_btn.setIcon(QIcon(str(icon_dir / "pin.svg")))

    def _on_button_clicked(self, key: str) -> None:
        for k, b in self._buttons.items():
            active = k == key
            b.setChecked(active)
            b.setProperty("active", active)
        self._active_key = key
        self._update_selection()
        self.navigate.emit(key)
