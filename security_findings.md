#  Vulnerability Log – SecureTasks

---

## Vulnerability #1 – Missing CSRF Token in Form

-  **Location**: `tareas/views.py` - `create_task` 
-  **Risk**: CSRF (Cross-Site Request Forgery)
-  **Impact**: An attacker could trick a logged-in user into submitting unintended requests, potentially altering or creating tasks without consent.
**Description:**
The view that handles POST requests to create new tasks uses the `@csrf_exempt` decorator, disabling Django's CSRF protection mechanism. This allows any third-party website to send POST requests and create tasks without user consent or verification.

**Pending fix:** Remove `@csrf_exempt` and include `{% csrf_token %}` in the form template.






