from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QSizePolicy,
)
from PySide6.QtCore import Qt

from .core.app_router import AppRouter
from .core.style_manager import StyleManager
from .core.theme_manager import ThemeManager
from .widgets import HeaderWidget, SidebarWidget, FooterWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("منصة السعادة")
        self.setLayoutDirection(Qt.RightToLeft)
        StyleManager.apply()
        ThemeManager.apply()

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.header = HeaderWidget()
        main_layout.addWidget(self.header)

        body = QWidget()
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        self.sidebar = SidebarWidget()
        self.sidebar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        body_layout.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        self.stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body_layout.addWidget(self.stack)
        # Use golden ratio for sidebar vs main area (100:162 ≈ 1:1.618)
        body_layout.setStretch(0, 100)
        body_layout.setStretch(1, 162)

        main_layout.addWidget(body, 1)

        self.footer = FooterWidget()
        main_layout.addWidget(self.footer)

        self.router = AppRouter(self.stack)
        self.sidebar.navigate.connect(self.router.navigate)
        self.router.navigate("dashboard")
