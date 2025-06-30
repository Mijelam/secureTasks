#  Vulnerability Log – SecureTasks

---

## Vulnerability #1 – Missing CSRF Token in Form

-  **Location**: Task creation form (to be defined)
-  **Description**: The form does not include the `{% csrf_token %}` tag, which is required in Django to protect against CSRF attacks.
-  **Risk**: CSRF (Cross-Site Request Forgery)
-  **Impact**: An attacker could trick a logged-in user into submitting unintended requests, potentially altering or creating tasks without consent.
-  **Status**:  Pending fix
-  **Note**: This vulnerability was introduced intentionally for learning purposes.
