CREATE TABLE `Category` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`type`	TEXT NOT NULL
	
);

CREATE TABLE `User` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL,
    `first_name`    TEXT NOT NULL,
    `last_name`    TEXT NOT NULL,
    `is_admin` TEXT NOT NULL,
    `orderId` INTEGER NOT NULL,
    FOREIGN KEY(`orderId`) REFERENCES `Order`(`id`)
    
);

CREATE TABLE `Product` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`title`  TEXT NOT NULL,
	`price` INTEGER NOT NULL,
	`deliveryTime` TEXT NOT NULL,
	`inStock` INTEGER NOT NULL,
	`typeId` INTEGER NOT NULL,
	FOREIGN KEY(`typeId`) REFERENCES `Category`(`id`)
	
);


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

INSERT INTO `User` VALUES (null, "jasonli99193@gmail.com", "403234", "Jason", "Li", True, 0);

INSERT INTO `Product` VALUES (null, "rug", 25.99, "2 weeks", 3, 1);
INSERT INTO `Product` VALUES (null, "couch", 30.99, "2 weeks", 2, 1);

INSERT INTO `Order` VALUES (null, "01/20/2024", 1, 1);