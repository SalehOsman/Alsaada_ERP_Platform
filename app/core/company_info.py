from __future__ import annotations

"""Model representing company information used across the application.

This simple dataclass acts as a placeholder until the settings module
implements persistent storage for the company profile.

Author: OpenAI Codex
Last Modified: 2025-07-09
"""

from dataclasses import dataclass


@dataclass
class CompanyInfo:
    """Basic company details."""

    name: str = "شركة السعادة"
    app_name: str = "منصة السعادة لإدارة الموارد"
    contact: str = "معلومات الاتصال"
    logo_path: str | None = None


# Global instance used by widgets
company_info = CompanyInfo()
