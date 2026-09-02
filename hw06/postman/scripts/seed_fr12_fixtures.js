/**
 * Seed FR-12 disposable test fixtures into database.sqlite.
 * Cleanly removes any leftover probe records from previous runs, then seeds fresh fixtures.
 */
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.resolve(__dirname, '../../../backend/database.sqlite');
const db = new sqlite3.Database(dbPath);

db.serialize(() => {
    console.log('Cleaning up old test probe records...');
    
    // Clean up probe coupons
    db.run("DELETE FROM coupons WHERE code LIKE '%23127027%' OR id >= 50");
    
    // Clean up probe users
    db.run("DELETE FROM users WHERE email LIKE '%23127027%' OR id >= 50");
    
    // Clean up probe products
    db.run("DELETE FROM products WHERE name LIKE '%23127027%' OR id >= 50");
    
    // Clean up probe categories
    db.run("DELETE FROM categories WHERE name LIKE '%23127027%' OR id >= 50");
    
    // Clean up probe orders
    db.run("DELETE FROM orders WHERE id >= 100");

    console.log('Seeding fresh FR-12 disposable test fixtures...');

    // Orders
    db.run("INSERT OR REPLACE INTO orders (id, user_id, total_amount, status, shipping_address) VALUES (101, 2, 100000, 'pending', '123 Test St')");
    db.run("INSERT OR REPLACE INTO orders (id, user_id, total_amount, status, shipping_address) VALUES (102, 2, 200000, 'pending', '456 Test St')");

    // Disposable Users
    db.run("INSERT OR REPLACE INTO users (id, name, email, password, role) VALUES (50, 'Disposable User 002', 'disp002@example.com', 'dispPassword1!', 'user')");
    db.run("INSERT OR REPLACE INTO users (id, name, email, password, role) VALUES (51, 'Disposable User 016', 'disp016@example.com', 'dispPassword2!', 'user')");
    db.run("INSERT OR REPLACE INTO users (id, name, email, password, role) VALUES (52, 'Disposable User 038', 'disp038@example.com', 'dispPassword3!', 'user')");

    // Disposable Coupons
    db.run("INSERT OR REPLACE INTO coupons (id, code, type, discount_value, min_order_amount, expired_at, is_active, max_uses_per_user) VALUES (50, 'DISP_CPN_007', 'percent', 10, 100000, '2099-12-31', 1, 1)");
    db.run("INSERT OR REPLACE INTO coupons (id, code, type, discount_value, min_order_amount, expired_at, is_active, max_uses_per_user) VALUES (51, 'DISP_CPN_021', 'percent', 10, 100000, '2099-12-31', 1, 1)");

    // Disposable Products
    db.run("INSERT OR REPLACE INTO products (id, name, price, description, imageUrl, category_id) VALUES (50, 'DispProduct_009', 100000, 'Disposable 009', 'https://placehold.co/300', 1)");
    db.run("INSERT OR REPLACE INTO products (id, name, price, description, imageUrl, category_id) VALUES (51, 'DispProduct_010', 100000, 'Disposable 010', 'https://placehold.co/300', 1)");
    db.run("INSERT OR REPLACE INTO products (id, name, price, description, imageUrl, category_id) VALUES (52, 'DispProduct_023', 200000, 'Disposable 023', 'https://placehold.co/300', 1)");
    db.run("INSERT OR REPLACE INTO products (id, name, price, description, imageUrl, category_id) VALUES (53, 'DispProduct_024', 200000, 'Disposable 024', 'https://placehold.co/300', 1)");
    db.run("INSERT OR REPLACE INTO products (id, name, price, description, imageUrl, category_id) VALUES (54, 'DispProduct_030', 300000, 'Disposable 030', 'https://placehold.co/300', 1)");
    db.run("INSERT OR REPLACE INTO products (id, name, price, description, imageUrl, category_id) VALUES (55, 'DispProduct_031', 300000, 'Disposable 031', 'https://placehold.co/300', 1)");

    // Disposable Categories
    db.run("INSERT OR REPLACE INTO categories (id, name) VALUES (50, 'DispCategory_012')");
    db.run("INSERT OR REPLACE INTO categories (id, name) VALUES (51, 'DispCategory_013')");
    db.run("INSERT OR REPLACE INTO categories (id, name) VALUES (52, 'DispCategory_026')");
    db.run("INSERT OR REPLACE INTO categories (id, name) VALUES (53, 'DispCategory_027')");

    console.log('FR-12 fresh fixtures successfully seeded!');
});

db.close();
