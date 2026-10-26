CREATE TABLE `ratings` (
	`workshop` text NOT NULL,
	`rater` text NOT NULL,
	`target` text NOT NULL,
	`item` text NOT NULL,
	`value` integer,
	`note` text DEFAULT '' NOT NULL,
	PRIMARY KEY(`workshop`, `rater`, `target`, `item`)
);
--> statement-breakpoint
CREATE TABLE `workshops` (
	`id` text PRIMARY KEY NOT NULL,
	`host_hash` text NOT NULL,
	`title` text NOT NULL,
	`card` text NOT NULL,
	`people` text NOT NULL,
	`slide` integer DEFAULT 0 NOT NULL,
	`revealed` integer DEFAULT 0 NOT NULL,
	`created` text NOT NULL
);
