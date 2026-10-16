"""
Unit tests for suite-db-sql SQL formatter and safety analyzer.
"""

import sys
import unittest
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.sql_formatter import format_sql_query, minify_sql, analyze_sql_safety


class TestSqlFormatter(unittest.TestCase):
    def test_format_basic_query(self):
        query = "select id, name from users where status = 'active' order by id desc"
        res = format_sql_query(query)
        self.assertIn("SELECT id, name", res["formatted"])
        self.assertIn("FROM users", res["formatted"])
        self.assertIn("WHERE status = 'active'", res["formatted"])
        self.assertIn("ORDER BY id desc", res["formatted"])
        self.assertIn("SELECT", res["detected_keywords"])
        self.assertIn("FROM", res["detected_keywords"])

    def test_format_empty_query(self):
        res = format_sql_query("")
        self.assertEqual(res["formatted"], "")
        self.assertEqual(res["line_count"], 0)

    def test_format_none_query(self):
        res = format_sql_query(None)
        self.assertEqual(res["formatted"], "")

    def test_minify_sql(self):
        query = """
        -- Select all active users
        SELECT id, name /* comment */
        FROM users
        WHERE active = 1;
        """
        minified = minify_sql(query)
        self.assertNotIn("comment", minified)
        self.assertNotIn("\n", minified)
        self.assertEqual(minified, "SELECT id, name FROM users WHERE active = 1;")

    def test_safety_check_safe_query(self):
        query = "SELECT * FROM orders WHERE user_id = 100"
        safety = analyze_sql_safety(query)
        self.assertTrue(safety["is_safe"])
        self.assertEqual(safety["risk_level"], "LOW")
        self.assertEqual(len(safety["warnings"]), 0)

    def test_safety_check_dangerous_drop(self):
        query = "DROP TABLE users;"
        safety = analyze_sql_safety(query)
        self.assertFalse(safety["is_safe"])
        self.assertEqual(safety["risk_level"], "HIGH")
        self.assertIn("DROP detected", safety["warnings"][0])

    def test_safety_check_unconstrained_delete(self):
        query = "DELETE FROM customers;"
        safety = analyze_sql_safety(query)
        self.assertFalse(safety["is_safe"])
        self.assertIn("DELETE without WHERE", safety["warnings"][0])


if __name__ == "__main__":
    unittest.main()
