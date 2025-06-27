from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import Qt

from .theme_manager import ThemeManager


class StyleManager:
    """إدارة الخطوط وتطبيق الوضع الليلي."""

    font_family: str = "Cairo"
    font_size: int = 10
    dark_mode: bool = True

    @classmethod
    def apply(cls, app: QApplication | None = None) -> None:
        app = app or QApplication.instance()
        if not app:
            return
        palette = app.palette()
        if cls.dark_mode:
            palette.setColor(QPalette.Window, QColor("#222222"))
            palette.setColor(QPalette.WindowText, Qt.white)
        else:
            palette.setColor(QPalette.Window, Qt.white)
            palette.setColor(QPalette.WindowText, Qt.black)

        app.setPalette(palette)

        font = QFont(cls.font_family, cls.font_size)
        app.setFont(font)
        ThemeManager.font_family = cls.font_family
        ThemeManager.font_size = cls.font_size
        ThemeManager.apply()
