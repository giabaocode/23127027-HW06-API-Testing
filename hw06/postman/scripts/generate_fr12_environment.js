/**
 * Generate Postman Environment for FR-12 Access Control Test Suite.
 */
const path = require('path');
const fs = require('fs');

const jwtPath = path.resolve(__dirname, '../../../backend/node_modules/jsonwebtoken');
const jwt = require(jwtPath);

const SECRET_KEY = "super_secret_key_that_should_not_be_here";

// Generate tokens
const adminToken = jwt.sign({ id: 1, name: "Admin User", email: "admin@eshop.com", role: "admin" }, SECRET_KEY);
const userToken = jwt.sign({ id: 2, name: "Test User", email: "test@eshop.com", role: "user" }, SECRET_KEY);
const expiredAdminToken = jwt.sign({ id: 1, role: "admin", exp: Math.floor(Date.now() / 1000) - 3600 }, SECRET_KEY);
const forgedToken = jwt.sign({ id: 1, role: "admin" }, "completely_wrong_secret_key_12345");
const missingRoleToken = jwt.sign({ id: 10, name: "No Role User" }, SECRET_KEY);
const uppercaseRoleToken = jwt.sign({ id: 1, role: "ADMIN" }, SECRET_KEY);

// alg=none token
const b64 = (obj) => Buffer.from(JSON.stringify(obj)).toString("base64url");
const unsignedAlgNoneToken = b64({ alg: "none", typ: "JWT" }) + "." + b64({ id: 1, username: "admin", role: "admin" }) + ".";

// future nbf token
const futureNbfToken = jwt.sign({ id: 1, role: "admin", nbf: Math.floor(Date.now() / 1000) + 3600, exp: Math.floor(Date.now() / 1000) + 7200 }, SECRET_KEY);

// whitespace role token
const whitespaceRoleToken = jwt.sign({ id: 1, role: " admin " }, SECRET_KEY);

// array role token
const arrayRoleToken = jwt.sign({ id: 1, role: ["admin"] }, SECRET_KEY);

const env = {
    id: "fr12-env-23127027",
    name: "FR-12 Access Control Environment",
    values: [
        { key: "baseUrl", value: "http://localhost:3000", enabled: true },
        { key: "studentId", value: "23127027", enabled: true },
        { key: "adminToken", value: adminToken, enabled: true },
        { key: "userToken", value: userToken, enabled: true },
        { key: "expiredAdminToken", value: expiredAdminToken, enabled: true },
        { key: "forgedToken", value: forgedToken, enabled: true },
        { key: "missingRoleToken", value: missingRoleToken, enabled: true },
        { key: "uppercaseRoleToken", value: uppercaseRoleToken, enabled: true },
        { key: "unsignedAlgNoneToken", value: unsignedAlgNoneToken, enabled: true },
        { key: "futureNbfToken", value: futureNbfToken, enabled: true },
        { key: "whitespaceRoleToken", value: whitespaceRoleToken, enabled: true },
        { key: "arrayRoleToken", value: arrayRoleToken, enabled: true }
    ],
    _postman_variable_scope: "environment"
};

const outputPath = path.resolve(__dirname, '../environments/fr12-environment.json');
fs.writeFileSync(outputPath, JSON.stringify(env, null, 2), 'utf-8');
console.log(`Saved FR-12 environment to ${outputPath}`);
