# Security & Containment Report
The app has a single vulnerable query. No file or directory access. Only exposed through Docker containers. Tested UNION-based payloads successfully extract admin.password.

# Tests Performed

1. Directory Traversal - 
Attempted payloads such as ../../etc/passwd and %2e%2e/ in parameters.

Result: Application properly restricts file access. No sensitive files exposed.

2. Resource Access Isolation - 
Tried accessing /flag.txt, /admin/, /db/.

Result: Direct access blocked. Challenge flag only accessible via intended SQLi exploitation.

3. Cross-Challenge Security - 
Verified no shared data between stored procedure injection challenge and union injection challenge.

Result: Data isolation confirmed.

4. Authentication Bypass - 
Simple ' OR '1'='1 tested on login form.

Result: Login bypass not possible, confirming this is a pure UNION-based SQLi challenge.