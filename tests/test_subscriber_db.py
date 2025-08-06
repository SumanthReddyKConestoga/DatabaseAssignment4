"""Module for unittesting CRUD operations on the subscriber_db schema."""

import os
import unittest

import mysql.connector


class SubscriberDBTest(unittest.TestCase):
    """Test suite for validating subscriber database CRUD functionality."""

    @classmethod
    def setUpClass(cls):
        """Establish a connection to subscriber_db as subscriber_user."""
        cls.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="subscriber_user",
            password=os.getenv("MYSQL_USER_PASSWORD"),
            database="subscriber_db",
        )
        cls.cursor = cls.conn.cursor()

    def setUp(self):
        """Ensure a clean slate before each test by truncating the table."""
        self.cursor.execute("DELETE FROM subscriber;")
        self.conn.commit()

    def test_create(self):
        """Verify that inserting a new subscriber record works correctly."""
        self.cursor.execute(
            "INSERT INTO subscriber (email) "
            "VALUES ('a@example.com');"
        )
        self.conn.commit()
        self.cursor.execute("SELECT COUNT(*) FROM subscriber;")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 1)

    def test_read(self):
        """Verify querying an existing subscriber returns correct row."""
        self.cursor.execute(
            "INSERT INTO subscriber (email) "
            "VALUES ('b@example.com');"
        )
        self.conn.commit()
        self.cursor.execute(
            "SELECT email FROM subscriber "
            "WHERE email='b@example.com';"
        )
        email = self.cursor.fetchone()[0]
        self.assertEqual(email, "b@example.com")

    def test_update(self):
        """Verify that updating a subscriber's email is persisted."""
        self.cursor.execute(
            "INSERT INTO subscriber (email) "
            "VALUES ('c@example.com');"
        )
        self.conn.commit()
        self.cursor.execute(
            "UPDATE subscriber "
            "SET email='c2@example.com' "
            "WHERE email='c@example.com';"
        )
        self.conn.commit()
        self.cursor.execute("SELECT email FROM subscriber;")
        email = self.cursor.fetchone()[0]
        self.assertEqual(email, "c2@example.com")

    def test_delete(self):
        """Verify that deleting a subscriber record removes it."""
        self.cursor.execute(
            "INSERT INTO subscriber (email) "
            "VALUES ('d@example.com');"
        )
        self.conn.commit()
        self.cursor.execute(
            "DELETE FROM subscriber "
            "WHERE email='d@example.com';"
        )
        self.conn.commit()
        self.cursor.execute("SELECT COUNT(*) FROM subscriber;")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 0)

    @classmethod
    def tearDownClass(cls):
        """Close cursor and database connection after tests."""
        cls.cursor.close()
        cls.conn.close()


if __name__ == "__main__":
    unittest.main()
