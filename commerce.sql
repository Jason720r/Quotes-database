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
	`typeId` INTEGER,
	FOREIGN KEY(`typeId`) REFERENCES `Type`(`id`),
	
);


CREATE TABLE `Order` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`productId`	TEXT NOT NULL,
	`userId` INTEGER NOT NULL,
	FOREIGN KEY(`productId`) REFERENCES `Product`(`id`)
    FOREIGN KEY(`userId`) REFERENCES `User`(`id`)

);