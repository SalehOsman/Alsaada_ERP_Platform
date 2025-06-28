"""
اسم الملف: run.py
الغرض: نقطة التشغيل الأساسية لتطبيق منصة السعادة ERP - فتح الواجهة الرئيسية باستخدام PyWebview.
المؤلف: صالح عثمان
تاريخ الإنشاء: 2024-06-29
آخر تعديل: 2024-06-29
شرح: هذا السكريبت يُشغّل نافذة التطبيق ويعرض صفحة main.html من مجلد templates.
"""

import webview
import os

# مسار صفحة الواجهة الرئيسية (HTML)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PAGE = os.path.join(BASE_DIR, "web", "templates", "main.html")

if __name__ == '__main__':
    # فتح نافذة التطبيق مع تفعيل دعم RTL
    webview.create_window(
        title="منصة السعادة ERP",
        url=MAIN_PAGE,
        width=1200,
        height=800,
        resizable=True
    )
    webview.start()
