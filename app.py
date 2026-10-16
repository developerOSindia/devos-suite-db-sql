"""
DeveloperOS Database & SQL Suite - Interactive Application
"""

import streamlit as st
from core.sql_formatter import format_sql_query
from ui.components import render_suite_header, render_suite_footer, render_main_promotional_banner

st.set_page_config(
    page_title="DeveloperOS - Database Suite",
    page_icon="🗄️",
    layout="wide",
)


def main():
    render_suite_header(
        title="SQL Query Formatter & Prettifier",
        description="Format, align clauses, and normalize keyword casing for SQL queries across dialect types.",
    )

    sample_sql = "select u.id, u.username, count(o.id) as total_orders from users u left join orders o on u.id = o.user_id where u.created_at >= '2026-01-01' group by u.id, u.username order by total_orders desc limit 50"

    raw_query = st.text_area("Input SQL Query:", value=sample_sql, height=120)
    uppercase = st.checkbox("Uppercase SQL Keywords", value=True)

    if raw_query:
        res = format_sql_query(raw_query, uppercase_keywords=uppercase)

        st.subheader("Formatted SQL")
        st.code(res["formatted"], language="sql")
        st.caption(f"Lines: {res['line_count']} | Keywords Normalized: {len(res['detected_keywords'])}")

    render_main_promotional_banner()
    render_suite_footer()


if __name__ == "__main__":
    main()
