# theme_manager.py
# الغرض: إدارة وتطبيق سمات الألوان والخطوط على الواجهة
# المؤلف: صالح عثمان
# تاريخ التعديل: 2025-06-30

from __future__ import annotations

from pathlib import Path
import re
from PySide6.QtWidgets import QApplication


class ThemeManager:
    """مدير الثيم المركزي للألوان والتنسيقات."""

    light_palette: dict[str, str] = {
        "primary": "#f47824",
        "primary_light": "#ffa96b",
        "primary_dark": "#b35c1c",
        "primary_disabled": "#fbd3ba",
        "secondary": "#333333",
        "secondary_light": "#4f4f4f",
        "secondary_dark": "#1a1a1a",
        "secondary_disabled": "#777777",
        "success": "#28a745",
        "warning": "#ffc107",
        "error": "#dc3545",
        "sidebar_bg": "#f7f7f7",
        "sidebar_text": "#333333",
        "sidebar_hover_bg": "#e0e0e0",
        "sidebar_hover_bg_alt": "#ffffff",
        "sidebar_hover_text": "#000000",
        "sidebar_active_bg": "#f47824",
        "sidebar_active_text": "#ffffff",
        "accent": "#f47824",
        "accent_light": "#ffa96b",
    }

    dark_palette: dict[str, str] = {
        "primary": "#f47824",
        "primary_light": "#ffa96b",
        "primary_dark": "#b35c1c",
        "primary_disabled": "#fbd3ba",
        "secondary": "#dddddd",
        "secondary_light": "#bbbbbb",
        "secondary_dark": "#888888",
        "secondary_disabled": "#555555",
        "success": "#28a745",
        "warning": "#ffc107",
        "error": "#dc3545",
        "sidebar_bg": "#2c2c2c",
        "sidebar_text": "#f0f0f0",
        "sidebar_hover_bg": "#444444",
        "sidebar_hover_bg_alt": "#333333",
        "sidebar_hover_text": "#ffffff",
        "sidebar_active_bg": "#f47824",
        "sidebar_active_text": "#ffffff",
        "accent": "#f47824",
        "accent_light": "#ffa96b",
    }

    palette: dict[str, str] = dark_palette.copy()

    font_family: str = "Arial"
    font_size: int = 12

    radius_small: int = 4
    radius_medium: int = 8
    spacing: int = 8
    icon_size_expanded: int = 24
    icon_size_collapsed: int = 32

    dark_mode: bool = True

    @classmethod
    def switch_mode(cls, dark: bool) -> None:
        cls.dark_mode = dark
        cls.palette = cls.dark_palette.copy() if dark else cls.light_palette.copy()
        cls.apply()

    @classmethod
    def apply(cls, app: QApplication | None = None) -> None:
        app = app or QApplication.instance()
        if not app:
            return
        style_dir = Path(__file__).resolve().parents[2] / "styles"
        qss_contents: list[str] = []
        for name in ("main.qss", "sidebar.qss"):
            path = style_dir / name
            if path.exists():
                with open(path, "r", encoding="utf-8") as f:
                    qss_contents.append(f.read())
        if qss_contents:
            qss_template = "\n".join(qss_contents)
            variables = {
                **cls.palette,
                "font_family": cls.font_family,
                "font_size": cls.font_size,
                "radius_small": cls.radius_small,
                "radius_medium": cls.radius_medium,
                "spacing": cls.spacing,
                "icon_size_expanded": cls.icon_size_expanded,
                "icon_size_collapsed": cls.icon_size_collapsed,
            }
            pattern = re.compile(r"{([a-zA-Z0-9_]+)}")

            def replace(match: re.Match) -> str:
                return str(variables.get(match.group(1), match.group(0)))

            qss = pattern.sub(replace, qss_template)
            app.setStyleSheet(qss)

    @classmethod
    def update(cls, **kwargs: str) -> None:
        for key, value in kwargs.items():
            if key in cls.palette:
                cls.palette[key] = value
            elif hasattr(cls, key):
                setattr(cls, key, value)
        cls.apply()
