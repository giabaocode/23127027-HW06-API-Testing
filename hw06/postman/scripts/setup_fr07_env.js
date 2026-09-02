// Automated environment generator for FR-07 Shopping Cart
// Uses legitimate SUT registration and login APIs to retrieve fresh tokens for test isolation.
const http = require('http');
const fs = require('fs');
const path = require('path');
const jwt = require('jsonwebtoken');

const BASE_URL = 'http://localhost:3000';
const SECRET_KEY = 'super_secret_key_that_should_not_be_here';
const ENV_FILE = path.join(__dirname, '../environments/fr07-environment.json');

function postJson(urlPath, data) {
    return new Promise((resolve, reject) => {
        const payload = JSON.stringify(data);
        const req = http.request(BASE_URL + urlPath, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(payload),
                'X-Student-Id': '23127027'
            }
        }, (res) => {
            let body = '';
            res.on('data', chunk => body += chunk);
            res.on('end', () => {
                try {
                    resolve({ status: res.statusCode, data: JSON.parse(body) });
                } catch (e) {
                    resolve({ status: res.statusCode, data: body });
                }
            });
        });
        req.on('error', reject);
        req.write(payload);
        req.end();
    });
}

async function getOrRegisterUserToken(emailPrefix) {
    const email = `${emailPrefix}_${Date.now()}_${Math.floor(Math.random()*10000)}@eshop.local`;
    const password = 'Password123!';
    await postJson('/api/register', { name: 'User ' + emailPrefix, email, password });
    const loginRes = await postJson('/api/login', { email, password });
    if (!loginRes.data.token) {
        throw new Error(`Failed to login user ${email}: ${JSON.stringify(loginRes.data)}`);
    }
    return loginRes.data.token;
}

async function main() {
    console.log('Generating isolated test tokens via legitimate SUT APIs...');
    const envValues = [
        { key: 'baseUrl', value: BASE_URL, enabled: true },
        { key: 'studentId', value: '23127027', enabled: true }
    ];

    // Single user tokens for AI tests
    const userKeys = [
        'token_user_01', 'token_user_02', 'token_user_03',
        'token_user_07', 'token_user_08', 'token_user_09', 'token_user_10', 'token_user_11',
        'token_user_12', 'token_user_13', 'token_user_14', 'token_user_15', 'token_user_16',
        'token_user_17', 'token_user_18', 'token_user_19', 'token_user_20', 'token_user_21',
        'token_user_22', 'token_user_23', 'token_user_24', 'token_user_25', 'token_user_26',
        'token_user_27', 'token_user_28', 'token_user_29', 'token_user_30',
        'token_user_37', 'token_user_38',
        'token_user_a', 'token_user_b',
        'token_user_stu1', 'token_user_stu2', 'token_user_stu3', 'token_user_stu4', 'token_user_stu5'
    ];

    for (const key of userKeys) {
        process.stdout.write(`  Registering ${key}... `);
        const token = await getOrRegisterUserToken(key);
        envValues.push({ key, value: token, enabled: true });
        console.log('OK');
    }

    // Expired token generation using local test setup
    const expiredToken = jwt.sign({ id: 9999, role: 'customer' }, SECRET_KEY, { expiresIn: '-1h' });
    envValues.push({ key: 'token_expired', value: expiredToken, enabled: true });
    console.log('  Generated legitimate expired token: OK');

    const envData = {
        id: 'f7a1b2c3-d4e5-6789-0abc-ef0000000000',
        name: 'FR-07 Cart Execution Environment',
        values: envValues,
        _postman_variable_scope: 'environment'
    };

    fs.mkdirSync(path.dirname(ENV_FILE), { recursive: true });
    fs.writeFileSync(ENV_FILE, JSON.stringify(envData, null, 2), 'utf-8');
    console.log(`Saved environment with ${envValues.length} variables to ${ENV_FILE}`);
}

main().catch(err => {
    console.error('Setup failed:', err);
    process.exit(1);
});
