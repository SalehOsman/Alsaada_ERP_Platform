from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QPushButton,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QDialogButtonBox,
    QTabWidget,
    QScrollArea,
    QStyle,
    QToolButton,
)
from PySide6.QtCore import Qt

from ...core.theme_manager import ThemeManager


class ComponentGuideView(QScrollArea):
    SECTION_TITLE = "دليل المكونات"

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWidgetResizable(True)
        container = QWidget()
        self.setWidget(container)
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignTop)
        # Use golden ratio spacing between demo blocks
        layout.setSpacing(int(ThemeManager.spacing * 1.618))

        layout.addWidget(self._create_palette_preview())
        layout.addWidget(self._create_buttons())
        layout.addWidget(self._create_inputs())
        layout.addWidget(self._create_table())
        layout.addWidget(self._create_tabs())
        layout.addWidget(self._create_labels())
        layout.addWidget(self._create_icons())
        layout.addStretch()

    def _create_palette_preview(self) -> QGroupBox:
        box = QGroupBox("لوحة الألوان")
        l = QHBoxLayout(box)
        for key in [
            "primary",
            "primary_light",
            "primary_dark",
            "secondary",
            "secondary_light",
            "secondary_dark",
            "success",
            "warning",
            "error",
        ]:
            lbl = QLabel(key)
            lbl.setObjectName(f"color_{key}")
            lbl.setProperty("class", "color-preview")
            lbl.setFixedSize(62, 38)  # width:height ≈ golden ratio
            l.addWidget(lbl)
        l.addStretch()
        return box

    def _create_buttons(self) -> QGroupBox:
        box = QGroupBox("الأزرار")
        l = QVBoxLayout(box)
        default_btn = QPushButton("افتراضي")
        default_btn.setObjectName("defaultButton")
        l.addWidget(default_btn)

        primary = QPushButton("أساسي")
        primary.setObjectName("primaryButton")
        l.addWidget(primary)
        secondary = QPushButton("ثانوي")
        secondary.setObjectName("secondaryButton")
        l.addWidget(secondary)
        icon_btn = QPushButton("مع أيقونة")
        icon_btn.setIcon(self.style().standardIcon(QStyle.SP_DesktopIcon))
        l.addWidget(icon_btn)
        dialog_btn = QPushButton("حوار")
        dialog_btn.clicked.connect(self._show_dialog)
        l.addWidget(dialog_btn)
        return box

    def _create_inputs(self) -> QGroupBox:
        box = QGroupBox("حقول الإدخال")
        l = QVBoxLayout(box)
        l.addWidget(QLineEdit("نص افتراضي"))
        spin = QSpinBox()
        l.addWidget(spin)
        combo = QComboBox()
        combo.addItems(["خيار 1", "خيار 2", "خيار 3"])
        l.addWidget(combo)
        chk = QPushButton("زر تبديل")
        chk.setCheckable(True)
        l.addWidget(chk)
        return box

    def _create_table(self) -> QGroupBox:
        box = QGroupBox("جدول")
        l = QVBoxLayout(box)
        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["عمود 1", "عمود 2", "عمود 3"])
        for r in range(3):
            for c in range(3):
                table.setItem(r, c, QTableWidgetItem(f"{r+1}-{c+1}"))
        l.addWidget(table)
        return box

    def _create_tabs(self) -> QGroupBox:
        box = QGroupBox("التبويبات")
        l = QVBoxLayout(box)
        tabs = QTabWidget()
        tabs.addTab(QLabel("محتوى التبويب الأول"), "الأول")
        tabs.addTab(QLabel("محتوى التبويب الثاني"), "الثاني")
        l.addWidget(tabs)
        return box

    def _create_labels(self) -> QGroupBox:
        box = QGroupBox("التسميات")
        l = QVBoxLayout(box)
        lbl1 = QLabel("نص عادي")
        l.addWidget(lbl1)
        primary = QLabel("لون أساسي")
        primary.setObjectName("primaryLabel")
        l.addWidget(primary)
        secondary = QLabel("لون ثانوي")
        secondary.setObjectName("secondaryLabel")
        l.addWidget(secondary)
        return box

    def _create_icons(self) -> QGroupBox:
        box = QGroupBox("أيقونات")
        l = QVBoxLayout(box)
        tool = QToolButton()
        tool.setText("أيقونة")
        tool.setIcon(self.style().standardIcon(QStyle.SP_DesktopIcon))
        l.addWidget(tool)
        return box

    def _show_dialog(self) -> None:
        dialog = QDialog(self)
        dialog.setWindowTitle("مربع حوار")
        dialog_layout = QVBoxLayout(dialog)
        dialog_layout.addWidget(QLabel("مثال لمربع حوار"))
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        dialog_layout.addWidget(buttons)
        dialog.exec()

