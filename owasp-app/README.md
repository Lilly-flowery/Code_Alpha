## SQL Injection (SQLi) Fix

* **Vulnerable Component:** Login mechanism
* **Files & Directories Modified:** 
  * `routes/login.ts` (Fixed the insecure query implementation by replacing raw SQL concatenation with parameterized queries).
