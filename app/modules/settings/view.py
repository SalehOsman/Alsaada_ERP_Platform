from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget,
    QComboBox,
    QPushButton,
    QColorDialog,
    QCheckBox,
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from ...core.style_manager import StyleManager
from ...core.theme_manager import ThemeManager


class SettingsView(QTabWidget):
    SECTION_TITLE = "الإعدادات"

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.addTab(self._create_appearance_tab(), "المظهر")
        self.addTab(self._create_tab("محتوى تبويب 2 الإعدادات"), "تبويب 2 الإعدادات")

    def _create_tab(self, text: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(text))
        return widget

    def _create_appearance_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        btn_primary = QPushButton("تغيير اللون الأساسي")
        btn_primary.clicked.connect(lambda: self._choose_color("primary"))
        layout.addWidget(btn_primary)

        btn_secondary = QPushButton("تغيير اللون الثانوي")
        btn_secondary.clicked.connect(lambda: self._choose_color("secondary"))
        layout.addWidget(btn_secondary)

        font_combo = QComboBox()
        font_combo.addItems(["Arial", "Times New Roman", "Cairo", "Amiri"])
        font_combo.setCurrentText(StyleManager.font_family)
        font_combo.currentTextChanged.connect(self._font_changed)
        layout.addWidget(font_combo)

        size_combo = QComboBox()
        size_combo.addItems(["كبير", "متوسط", "صغير"])
        size_label_map = {16: "كبير", 12: "متوسط", 10: "صغير"}
        size_combo.setCurrentText(size_label_map.get(StyleManager.font_size, "متوسط"))
        size_combo.currentTextChanged.connect(self._size_changed)
        layout.addWidget(size_combo)

        mode_chk = QCheckBox("الوضع الداكن")
        mode_chk.setChecked(StyleManager.dark_mode)
        mode_chk.stateChanged.connect(self._mode_changed)
        layout.addWidget(mode_chk)

        layout.addStretch()
        return widget

    # slots
    def _adjust_color(self, hex_color: str, factor: float) -> str:
        """Return a lightened or darkened version of a hex color."""
        h = hex_color.lstrip("#")
        r = int(h[0:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:6], 16)
        r = max(0, min(255, int(r * factor)))
        g = max(0, min(255, int(g * factor)))
        b = max(0, min(255, int(b * factor)))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _choose_color(self, which: str) -> None:
        current = ThemeManager.palette.get(which, "#ffffff")
        color = QColorDialog.getColor(QColor(current), self)
        if color.isValid():
            hex_color = color.name()
            if which == "primary":
                ThemeManager.update(
                    primary=hex_color,
                    primary_light=self._adjust_color(hex_color, 1.2),
                    primary_dark=self._adjust_color(hex_color, 0.8),
                    primary_disabled=self._adjust_color(hex_color, 1.4),
                    accent=hex_color,
                    accent_light=self._adjust_color(hex_color, 1.2),
                )
            elif which == "secondary":
                ThemeManager.update(
                    secondary=hex_color,
                    secondary_light=self._adjust_color(hex_color, 1.2),
                    secondary_dark=self._adjust_color(hex_color, 0.8),
                    secondary_disabled=self._adjust_color(hex_color, 1.4),
                )

    def _font_changed(self, font: str) -> None:
        if font:
            StyleManager.font_family = font
            StyleManager.apply()

    def _size_changed(self, text: str) -> None:
        size_map = {"كبير": 16, "متوسط": 12, "صغير": 10}
        StyleManager.font_size = size_map.get(text, 12)
        StyleManager.apply()

    def _mode_changed(self, state: int) -> None:
        StyleManager.dark_mode = state == Qt.Checked
        ThemeManager.switch_mode(StyleManager.dark_mode)
        StyleManager.apply()
