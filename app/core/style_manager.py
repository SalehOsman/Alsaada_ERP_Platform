from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import Qt


class StyleManager:
    """Simple style manager for colors, fonts and theme."""

    primary_color: str = "#f47824"
    secondary_color: str = "#333333"
    font_family: str = "Arial"
    font_size: int = 12
    dark_mode: bool = False

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

        palette.setColor(QPalette.Button, QColor(cls.primary_color))
        palette.setColor(QPalette.ButtonText, Qt.white)
        app.setPalette(palette)

        font = QFont(cls.font_family, cls.font_size)
        app.setFont(font)
        app.setStyleSheet(
            f"QWidget{{font-family:'{cls.font_family}';font-size:{cls.font_size}pt;}}"
        )
