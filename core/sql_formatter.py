"""
Pure business logic for SQL formatting and normalization.
Zero Streamlit or UI dependencies.
"""

import re
from typing import Dict, Any, List

SQL_KEYWORDS = [
    "SELECT", "FROM", "WHERE", "GROUP BY", "ORDER BY", "HAVING",
    "JOIN", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "OUTER JOIN",
    "INSERT INTO", "VALUES", "UPDATE", "SET", "DELETE FROM",
    "CREATE TABLE", "ALTER TABLE", "DROP TABLE", "LIMIT", "OFFSET",
    "AND", "OR", "IN", "AS", "DISTINCT", "UNION", "ALL", "EXISTS"
]


def format_sql_query(query: str, uppercase_keywords: bool = True) -> Dict[str, Any]:
    """Formats and aligns SQL query statements."""
    clean = (query or "").strip()
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


def minify_sql(query: str) -> str:
    """Removes unnecessary whitespaces, line breaks, and SQL comments."""
    clean = (query or "").strip()
    if not clean:
        return ""
    # Remove single-line comments
    clean = re.sub(r"--.*$", "", clean, flags=re.MULTILINE)
    # Remove multi-line comments
    clean = re.sub(r"/\*.*?\*/", "", clean, flags=re.DOTALL)
    # Collapse multiple whitespaces
    return re.sub(r"\s+", " ", clean).strip()


def analyze_sql_safety(query: str) -> Dict[str, Any]:
    """Analyzes SQL queries for high-risk operations (e.g. unconstrained DELETE/UPDATE, DROP)."""
    clean = (query or "").upper()
    warnings: List[str] = []

    if "DROP TABLE" in clean or "DROP DATABASE" in clean:
        warnings.append("Destructive schema operation: DROP detected.")
    if "TRUNCATE" in clean:
        warnings.append("Destructive table operation: TRUNCATE detected.")
    if "DELETE FROM" in clean and "WHERE" not in clean:
        warnings.append("High risk: DELETE without WHERE clause affects all rows.")
    if "UPDATE " in clean and "WHERE" not in clean:
        warnings.append("High risk: UPDATE without WHERE clause affects all rows.")

    return {
        "is_safe": len(warnings) == 0,
        "warnings": warnings,
        "risk_level": "HIGH" if warnings else "LOW"
    }
