"""
Pure business logic for SQL formatting and normalization.
Zero Streamlit or UI dependencies.
"""

import re
from typing import Dict, Any

SQL_KEYWORDS = [
    "SELECT", "FROM", "WHERE", "GROUP BY", "ORDER BY", "HAVING",
    "JOIN", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "OUTER JOIN",
    "INSERT INTO", "VALUES", "UPDATE", "SET", "DELETE FROM",
    "CREATE TABLE", "ALTER TABLE", "DROP TABLE", "LIMIT", "OFFSET",
    "AND", "OR", "IN", "AS", "DISTINCT"
]


def format_sql_query(query: str, uppercase_keywords: bool = True) -> Dict[str, Any]:
    """Formats and aligns SQL query statements."""
    clean = query.strip()
    if not clean:
        return {"formatted": "", "line_count": 0, "detected_keywords": []}

    formatted = clean
    detected = []

    for kw in sorted(SQL_KEYWORDS, key=len, reverse=True):
        pattern = re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE)
        if pattern.search(formatted):
            detected.append(kw)
            if uppercase_keywords:
                formatted = pattern.sub(kw, formatted)

    # Basic structural line breaks on major clauses
    for clause in ["FROM", "WHERE", "GROUP BY", "ORDER BY", "HAVING", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN"]:
        formatted = re.sub(rf"\s+({clause})\b", rf"\n\1", formatted)

    lines = [l.strip() for l in formatted.splitlines() if l.strip()]

    return {
        "formatted": "\n".join(lines),
        "line_count": len(lines),
        "detected_keywords": detected,
    }
