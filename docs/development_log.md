# سجل التطوير والتعديلات – Alsaada ERP Platform

---

## 2025-06-27

---

**إنشاء نقطة التشغيل الرئيسية للتطبيق**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\run.py**
    - تجهيز ملف التشغيل الأساسي ليستدعي النافذة الرئيسية فقط ويضبط اتجاه الواجهة RTL ويفتح التطبيق بحجم الشاشة الكامل.

---

**تطوير النافذة الرئيسية للتطبيق**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\main_window.py**
    - بناء MainWindow التي تجمع جميع العناصر الرئيسية (الهيدر، الشريط الجانبي، الفوتر، منطقة المحتوى الديناميكية)، مع دعم التوسعة وسهولة استدعاء أي قسم من خلال AppRouter.

---

**إعداد مدير التوجيه المركزي للأقسام**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\app_router.py**
    - إنشاء AppRouter لتحميل وعرض كل قسم من أقسام النظام ديناميكيًا عند الحاجة، واعتماد فصل كامل بين الأقسام وطرق تحميلها، مع بنية مرنة لإضافة أو حذف أي قسم مستقبلاً بسهولة.

---

**إنشاء واجهة قسم العاملين (العرض فقط)**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\employees\view.py**
    - بناء QTabWidget خاص بقسم العاملين مع تبويبين فرعيين: "تبويب 1 العاملين" و"تبويب 2 العاملين"، وكل تبويب يعرض محتوى Placeholder يوضح أنه تابع لقسم العاملين.

---

**إنشاء واجهة قسم المالية (العرض فقط)**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\finance\view.py**
    - نفس المنهجية: بناء QTabWidget بقسم المالية، مع تبويبين ("تبويب 1 المالية"، "تبويب 2 المالية") ومحتوى توضيحي داخل كل تبويب.

---

**إعداد ملفات التنسيقات الأساسية للواجهة**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\main.qss**
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\sidebar.qss**
    - تجهيز ملفات QSS مستقلة لكل جزء (بدون خلط مع الكود البرمجي) وجاهزة لتخصيص أي نمط أو لون لاحقًا.

---

**تهيئة ملفات التوثيق والسجل**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\docs\development_log.md**
    - تجهيز ملف سجل التطوير لتوثيق جميع الخطوات والتحسينات أولًا بأول، مع الالتزام بكتابة المسارات الكاملة والشرح الدقيق لكل خطوة.

---

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان  
التاريخ: 2025-06-27**

---

**أي تعديل لاحق يجب توثيقه بنفس الطريقة، مع ذكر المسار الكامل ووصف دقيق للتغيير.**

---

> **ملحوظة:**  
> أي قسم جديد أو تعديل مستقبلي يجب توثيقه بنفس النمط (تاريخ - مسار الملف - وصف التعديل).

**مسطر تجريبة:**  

## 2025-06-27

---

**إضافة صفحة دليل المكونات**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\component_guide\view.py**
    - إنشاء صفحة تستعرض المكونات الأساسية للتطبيق (أزرار، جداول، حقول، حوارات، تبويبات، تسميات وأيقونات) مع دعم العربية واتجاه RTL.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\component_guide\__init__.py**
    - تصدير الواجهة الجديدة.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\app_router.py**
    - إضافة مسار "component_guide" لعرض الصفحة الجديدة.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - إظهار "دليل المكونات" في الشريط الجانبي.

**تحسين الإعدادات وإدارة المظهر**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\style_manager.py**
    - إضافة مدير أنماط بسيط للتحكم في الألوان والخط والوضع الليلي.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\settings\view.py**
    - استبدال تبويب 1 بتبويب "المظهر" يتيح تغيير الألوان والخط والحجم والوضع الليلي مع تطبيق فوري.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\main_window.py**
    - استدعاء StyleManager لتطبيق المظهر عند تشغيل التطبيق.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-07-03

---

**تعديل القيم الافتراضية للخطوط**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\style_manager.py**
    - ضبط الخط الافتراضي ليكون Cairo والحجم 10 (صغير).
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\theme_manager.py**
    - مزامنة القيم الافتراضية للخط والحجم مع StyleManager.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-07-02

---

**إضافة دعم أيقونات Font Awesome اختيارياً**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - استخدام مكتبة `qtawesome` لاستبدال الأيقونات المحلية عند توفرها مع إبقاء
      الأيقونات الحالية كخيار احتياطي.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\docs\README.md**
    - توضيح طريقة تفعيل الأيقونات الاحترافية عبر تثبيت `qtawesome`.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-06-28

---


**معالجة خطأ تطبيق الأنماط**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\main.qss**
    - تصحيح استخدام الأقواس المزدوجة ليعمل التنسيق مع ThemeManager بدون أخطاء.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\sidebar.qss**
    - تعديل الأقواس المزدوجة لضمان عدم تعطل التطبيق عند تحميل الأنماط.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-06-28

---
**تحديث سلوك وتصميم الشريط الجانبي**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - إعادة كتابة الودجت ليدعم الوضع المدمج مع توسع تلقائي عند المرور بالماوس.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\main_window.py**
    - إزالة تقسيم النسبة الذهبية وجعل عرض الشريط يعتمد على المحتوى.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\sidebar.qss**
    - تنسيقات جديدة لدعم التوسع والهوفر.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\main.qss**
    - تحديث التنسيقات العامة لتوافق التعديل الجديد.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-06-28

---

**تطوير شامل للشريط الجانبي**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - دعم أيقونات SVG حديثة، زر تثبيت، وحفظ حالة التثبيت مع تحسين التفاعل.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\style_manager.py**
    - ربط تطبيق الوضع الليلي بمدير الثيم لتحديث الأنماط تلقائيًا.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\theme_manager.py**
    - إضافة لوحات ألوان للوضعين الفاتح والداكن ولون Accent موحد.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\settings\view.py**
    - تحديث آلية تبديل الوضع الداكن لتعمل مع التعديلات الجديدة.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\sidebar.qss**
    - تأثيرات Hover وActive بتدرج لوني وفاصل مرئي للأقسام.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\icons**
    - إضافة مجموعة أيقونات SVG موحّدة.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-06-29

---

**تحسينات واجهة الشريط الجانبي**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - إضافة خاصية collapsed للتبديل بين الألوان تلقائيًا وتحديث التوسعة مع تحريك العرض.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\sidebar.qss**
    - تحديث الأنماط لتغيير الألوان حسب حالة الشريط وتهيئة تأثيرات hover/active.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\icons\settings.svg**
    - استبدال الأيقونة بأيقونة ترس حديثة.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\icons\pin.svg**
    - استبدال أيقونة التثبيت بدبوس مكتبي.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\icons\unpin.svg**
    - استبدال أيقونة الفك بدبوس مشطوب.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\icons\equipment.svg**
    - استبدال الأيقونة بأيقونة مفتاح إنجليزي.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\icons\finance.svg**
    - استبدال الأيقونة برمز حقيبة نقود.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-06-30

---

**تصحيح ألوان وحجم أيقونات الشريط الجانبي**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - تفعيل تحديث خلفية الوضع المصغر وإضافة متغيرات حجم الأيقونة.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\styles\sidebar.qss**
    - ضبط حجم الأيقونات تلقائيًا وتحديث التاريخ.
- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\core\theme_manager.py**
    - إضافة متغيرات icon_size_expanded و icon_size_collapsed لدعم التحكم في حجم الأيقونات.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-07-01

---

**تحسين وظائف تبويب المظهر في الإعدادات**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\modules\settings\view.py**
    - تهيئة القوائم المنسدلة بقيم المظهر الحالية وإضافة حساب تلقائي لتدرجات الألوان عند اختيار اللون الأساسي أو الثانوي.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---

## 2025-07-03

---

**إضافة تأثير شادو للقسم الفعال في الشريط الجانبي عند الفتح**

- **D:\Alsaada-ERP\Alsaada_ERP_Platform\app\widgets\sidebar.py**
    - تطبيق QGraphicsDropShadowEffect على الزر النشط عند توسعة الشريط وإزالته
      عن باقي الأزرار.

**جميع التعديلات الحالية تمت بواسطة: صالح عثمان**

---
