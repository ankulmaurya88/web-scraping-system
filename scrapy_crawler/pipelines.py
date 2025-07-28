# Data pipelines
import sqlite3

class SaveToSQLitePipeline:
    def open_spider(self, spider):
        # Connect to SQLite database (creates db if it doesn't exist)
        self.conn = sqlite3.connect("scrapy_data.db")
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist (customize fields as per your items)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                title TEXT,
                link TEXT,
                description TEXT
            )
        ''')
        self.conn.commit()

    def process_item(self, item, spider):
        # Insert scraped item into the SQLite table
        self.cursor.execute('''
            INSERT INTO items (title, link, description) VALUES (?, ?, ?)
        ''', (
            item.get('title'),
            item.get('link'),
            item.get('description')
        ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
