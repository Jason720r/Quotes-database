CREATE TABLE `Category` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`type`	TEXT NOT NULL
	
);

-- CREATE TABLE `User` (
--     `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `email`    TEXT NOT NULL,
--     `password`    TEXT NOT NULL,
--     `first_name`    TEXT NOT NULL,
--     `last_name`    TEXT NOT NULL,
--     `is_admin` TEXT NOT NULL,
--     `orderId` INTEGER NOT NULL,
--     FOREIGN KEY(`orderId`) REFERENCES `Order`(`id`)
    
-- );

CREATE TABLE `U` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL,
    `firstName`    TEXT NOT NULL,
    `lastName`    TEXT NOT NULL,
    `isAdmin` TEXT NOT NULL,
    `orderId` INTEGER NOT NULL,
    FOREIGN KEY(`orderId`) REFERENCES `Order`(`id`)
    
);

CREATE TABLE `U_new` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `firstName` TEXT NOT NULL,
    `lastName` TEXT NOT NULL,
    `isAdmin` TEXT NOT NULL,
    `orderId` INTEGER NOT NULL,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    FOREIGN KEY(`orderId`) REFERENCES `Order`(`id`)
);



CREATE TABLE `Product` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`title`  TEXT NOT NULL,
    `image` TEXT NOT NULL,
	`price` INTEGER NOT NULL,
	`deliveryTime` TEXT NOT NULL,
	`inStock` INTEGER NOT NULL,
	`typeId` INTEGER NOT NULL,
	FOREIGN KEY(`typeId`) REFERENCES `Category`(`id`)
	
);
ALTER TABLE `Product`
ADD COLUMN `image` TEXT NOT NULL DEFAULT 'default_image_url';


CREATE TABLE `Order` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`productId`	INTEGER NOT NULL,
	`userId` INTEGER NOT NULL,
	FOREIGN KEY(`productId`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`userId`) REFERENCES `User`(`id`)

);

INSERT INTO `Category` VALUES (null, "Furniture");
INSERT INTO `Category` VALUES (null, "Kitchen");

INSERT INTO `U_new` VALUES (null, "Jason", "Li", True, 0, "jasonli99193@gmail.com", "403234");

INSERT INTO `Product` VALUES (null, "rug", "https://atlas-content-cdn.pixelsquid.com/stock-images/rug-ENAeoGE-600.jpg", 25.99, "2 weeks", 3, 1);
INSERT INTO `Product` VALUES (null, "couch", "https://atlas-content-cdn.pixelsquid.com/stock-images/rug-ENAeoGE-600.jpg", 30.99, "2 weeks", 2, 1);

INSERT INTO `Order` VALUES (null, "01/20/2024", 1, 1);