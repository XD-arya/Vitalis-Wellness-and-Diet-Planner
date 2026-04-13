-- Insert new user (Arya Pore)
INSERT INTO users (name, email, password, age, height, weight) 
VALUES ('Arya Pore', 'aryapore@example.com', '1234567890', 25, 175.0, 70.0);

-- Get the auto-incremented user_id for Arya Pore
SET @user_id = LAST_INSERT_ID();

-- Insert 15 days of Health Logs (2026-03-29 to 2026-04-12)
INSERT INTO health_logs (user_id, date, water_intake, steps, sleep_hours) VALUES
(@user_id, '2026-03-29', 2.0, 6500,  7.5),
(@user_id, '2026-03-30', 2.5, 8200,  8.0),
(@user_id, '2026-03-31', 1.8, 5400,  6.5),
(@user_id, '2026-04-01', 3.0, 10100, 7.0),
(@user_id, '2026-04-02', 2.2, 7300,  7.5),
(@user_id, '2026-04-03', 2.8, 9500,  8.5),
(@user_id, '2026-04-04', 3.2, 11200, 8.0),
(@user_id, '2026-04-05', 2.1, 4800,  6.0),
(@user_id, '2026-04-06', 2.5, 8700,  7.5),
(@user_id, '2026-04-07', 2.9, 10500, 7.0),
(@user_id, '2026-04-08', 2.4, 7600,  6.5),
(@user_id, '2026-04-09', 3.5, 12400, 8.5),
(@user_id, '2026-04-10', 1.9, 5900,  6.0),
(@user_id, '2026-04-11', 2.7, 9100,  7.5),
(@user_id, '2026-04-12', 3.1, 10800, 8.0);

-- Insert 15 days of Diet Logs (2026-03-29 to 2026-04-12)
INSERT INTO diet_logs (user_id, date, total_calories, protein, carbs, fats, food_name) VALUES
(@user_id, '2026-03-29', 2100, 110, 220, 60, 'Oatmeal, Grilled Chicken Salad, Rice'),
(@user_id, '2026-03-30', 2400, 130, 250, 75, 'Eggs, Steak & Sweet Potato, Avocado'),
(@user_id, '2026-03-31', 1850, 95,  190, 55, 'Smoothie, Turkey Wrap, Sushi Bag'),
(@user_id, '2026-04-01', 2600, 140, 280, 80, 'Pancakes, Salmon Bowl, Pizza slice'),
(@user_id, '2026-04-02', 2250, 120, 230, 70, 'Yogurt, Chicken Pasta, Nuts & Fruits'),
(@user_id, '2026-04-03', 2500, 135, 260, 75, 'Oats, Tuna Sandwich, Roast Beef'),
(@user_id, '2026-04-04', 2800, 150, 300, 85, 'Eggs & Bacon, Burger, Ice Cream'),
(@user_id, '2026-04-05', 1700, 90,  180, 50, 'Toast, Caesar Salad, Baked Cod'),
(@user_id, '2026-04-06', 2300, 125, 240, 70, 'Protein Shake, Chicken Wrap, Tacos'),
(@user_id, '2026-04-07', 2450, 130, 255, 75, 'Eggs, Pork Chops & Potatoes, Salad'),
(@user_id, '2026-04-08', 2150, 115, 225, 65, 'Oatmeal, Chicken Soup, Vegetable Curry'),
(@user_id, '2026-04-09', 2750, 145, 290, 85, 'Bagel, Beef Stew, Protein Bar & Rice'),
(@user_id, '2026-04-10', 1900, 100, 200, 55, 'Fruit Bowl, Tuna Salad, Lentil Dal'),
(@user_id, '2026-04-11', 2350, 125, 245, 70, 'Omelet, Quinoa Bowl, Chicken Breast'),
(@user_id, '2026-04-12', 2550, 135, 265, 80, 'Pancakes, Grilled Salmon, Spaghetti');
