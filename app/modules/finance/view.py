from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget


class FinanceView(QTabWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.addTab(self._create_tab('محتوى التبويب 1'), 'تبويب 1')
        self.addTab(self._create_tab('محتوى التبويب 2'), 'تبويب 2')

    def _create_tab(self, text: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(text))
        return widget
