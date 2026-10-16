"""
Unit tests for suite-db-sql business logic.
"""

import sys
import unittest
from pathlib import Path

# Ensure suite root is in sys.path
SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.sql_formatter import format_sql_query


class TestSqlFormatter(unittest.TestCase):
    def test_format_query_keywords(self):
        query = "select id, name from users where active = 1 order by id desc"
        res = format_sql_query(query, uppercase_keywords=True)
        self.assertIn("SELECT", res["formatted"])
        self.assertIn("FROM", res["formatted"])
        self.assertIn("WHERE", res["formatted"])
        self.assertIn("ORDER BY", res["formatted"])
        self.assertGreaterEqual(res["line_count"], 3)

    def test_empty_query(self):
        res = format_sql_query("")
        self.assertEqual(res["formatted"], "")
        self.assertEqual(res["line_count"], 0)


if __name__ == "__main__":
    unittest.main()
