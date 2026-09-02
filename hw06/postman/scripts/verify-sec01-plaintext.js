/**
 * FR01-AI-037: SEC-01 Non-API Storage Verification Probe
 * Verifies whether password submitted during registration is stored in plaintext in SQLite DB.
 * Official SRS Oracle (README.md Line 278): stored password MUST NOT equal submitted plaintext password.
 * Student ID: 23127027
 */

const http = require('http');
const path = require('path');
const sqlite3 = require('sqlite3').verbose();

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';
const DB_PATH = path.resolve(__dirname, '../../../backend/database.sqlite');
const STUDENT_ID = '23127027';

const testEmail = `fr01_sec01_${Date.now()}@example.com`;
const submittedPassword = 'SecretPlaintextPassword123!';
const testName = 'SEC01 Verification Probe';

console.log('============================================================');
console.log('FR01-AI-037: SEC-01 NON-API DATABASE STORAGE VERIFICATION');
console.log('============================================================');
console.log(`Target URL:     ${BASE_URL}/api/register`);
console.log(`Database Path:  ${DB_PATH}`);
console.log(`X-Student-Id:   ${STUDENT_ID}`);
console.log(`Test Email:     ${testEmail}`);
console.log(`Submitted Pass: ${submittedPassword}`);
console.log('------------------------------------------------------------');

// Step 1: Send registration request
const postData = JSON.stringify({
    name: testName,
    email: testEmail,
    password: submittedPassword
});

const url = new URL(`${BASE_URL}/api/register`);
const options = {
    hostname: url.hostname,
    port: url.port || 3000,
    path: url.pathname,
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData),
        'X-Student-Id': STUDENT_ID
    }
};

const req = http.request(options, (res) => {
    let rawBody = '';
    res.on('data', (chunk) => { rawBody += chunk; });
    res.on('end', () => {
        console.log(`HTTP Registration Status: ${res.statusCode} ${res.statusMessage}`);
        console.log(`HTTP Response Body:       ${rawBody}`);

        // Step 2: Query SQLite database directly
        const db = new sqlite3.Database(DB_PATH, sqlite3.OPEN_READWRITE, (err) => {
            if (err) {
                console.error(`Database Connection Error: ${err.message}`);
                process.exit(1);
            }
        });

        db.get('SELECT id, name, email, password FROM users WHERE email = ?', [testEmail], (dbErr, row) => {
            if (dbErr) {
                console.error(`Database Query Error: ${dbErr.message}`);
                db.close();
                process.exit(1);
            }

            if (!row) {
                console.error(`Test row with email ${testEmail} not found in database!`);
                db.close();
                process.exit(1);
            }

            console.log('------------------------------------------------------------');
            console.log('DATABASE RECORD FOUND:');
            console.log(`User ID:         ${row.id}`);
            console.log(`Stored Email:    ${row.email}`);
            console.log(`Stored Password: ${row.password}`);
            console.log('------------------------------------------------------------');

            const isPlaintext = (row.password === submittedPassword);
            console.log(`COMPARISON: stored_password === submitted_plaintext: ${isPlaintext}`);

            if (isPlaintext) {
                console.log('SECURITY VERDICT: FAILED (SEC-01 VIOLATION CONFIRMED)');
                console.log('Finding: The password was stored directly as raw plaintext in SQLite.');
                console.log('Official Oracle: stored_password MUST NOT equal submitted_plaintext_password.');
            } else {
                console.log('SECURITY VERDICT: PASSED (SEC-01 SATISFIED)');
                console.log('Finding: The password in SQLite is transformed/hashed and does not match plaintext.');
            }

            // Step 3: Cleanup test row
            db.run('DELETE FROM users WHERE email = ?', [testEmail], (cleanErr) => {
                if (cleanErr) {
                    console.warn(`Cleanup warning: ${cleanErr.message}`);
                } else {
                    console.log(`Cleanup: Deleted test user ${testEmail}`);
                }
                db.close();
                console.log('============================================================');
            });
        });
    });
});

req.on('error', (e) => {
    console.error(`HTTP Request Error: ${e.message}`);
    process.exit(1);
});

req.write(postData);
req.end();
