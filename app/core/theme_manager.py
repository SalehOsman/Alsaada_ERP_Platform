from __future__ import annotations

from pathlib import Path
from PySide6.QtWidgets import QApplication


class ThemeManager:
    """Central manager for theme colors and styling."""

    # Base palette
    palette: dict[str, str] = {
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
    }

    font_family: str = "Arial"
    font_size: int = 12

    radius_small: int = 4
    radius_medium: int = 8
    spacing: int = 8

    @classmethod
    def apply(cls, app: QApplication | None = None) -> None:
        """Apply current palette and style sheets to the application."""
        app = app or QApplication.instance()
        if not app:
            return
        style_dir = Path(__file__).resolve().parents[2] / "styles"
        qss_path = style_dir / "main.qss"
        if qss_path.exists():
            with open(qss_path, "r", encoding="utf-8") as f:
                qss_template = f.read()
            variables = {
                **cls.palette,
                "font_family": cls.font_family,
                "font_size": cls.font_size,
                "radius_small": cls.radius_small,
                "radius_medium": cls.radius_medium,
                "spacing": cls.spacing,
            }
            app.setStyleSheet(qss_template.format(**variables))

    @classmethod
    def update(cls, **kwargs: str) -> None:
        """Update palette values then reapply styles."""
        for key, value in kwargs.items():
            if key in cls.palette:
                cls.palette[key] = value
            elif hasattr(cls, key):
                setattr(cls, key, value)
        cls.apply()
