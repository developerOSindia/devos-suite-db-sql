"""
UI components and DeveloperOS universal promotional banners for Database & SQL Suite.
"""

from typing import Optional
try:
    import streamlit as st
except ImportError:
    st = None

MAIN_SITE_URL = "https://developeros.in"
TOOLS_DIRECTORY_URL = "https://tools.developeros.in"
GITHUB_ORG_URL = "https://github.com/developerOSindia"
PRIVACY_URL = "https://developeros.in/privacy"

DEVOS_LOGO_SVG = """<svg viewBox="0 0 64 64" width="38" height="38" fill="none" style="flex-shrink: 0;" aria-hidden="true">
  <defs>
    <linearGradient id="suiteFavGrad" x1="10%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff3b30"/>
      <stop offset="48%" stop-color="#ff5a3d"/>
      <stop offset="100%" stop-color="#ff914d"/>
    </linearGradient>
    <linearGradient id="suitePanelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1b1b1f"/>
      <stop offset="100%" stop-color="#242428"/>
    </linearGradient>
  </defs>
  <rect x="34" y="12" width="22" height="10" rx="2.5" fill="url(#suitePanelGrad)" stroke="rgba(255,255,255,0.06)"/>
  <rect x="34" y="26" width="22" height="10" rx="2.5" fill="url(#suitePanelGrad)" stroke="rgba(255,255,255,0.06)"/>
  <rect x="34" y="40" width="22" height="10" rx="2.5" fill="url(#suitePanelGrad)" stroke="rgba(255,255,255,0.06)"/>
  <path d="M15 20.5L33.5 14V49.5L15 46Z" fill="#05070a" stroke="url(#suiteFavGrad)" stroke-width="2.8" stroke-linejoin="round"/>
  <path d="M15 20.5V46" stroke="url(#suiteFavGrad)" stroke-width="2.8" stroke-linecap="round"/>
  <path d="M33.5 14V49.5" stroke="url(#suiteFavGrad)" stroke-width="2.8" stroke-linecap="round"/>
  <path d="M22 23L27 25.8L22 28.6" stroke="#f8fafc" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="23.5" y1="34.2" x2="29.2" y2="34.2" stroke="#f8fafc" stroke-width="2.8" stroke-linecap="round"/>
</svg>"""


def render_suite_header(title: str, description: str):
    """Renders suite header with brand identification and Compact Header Banner."""
    if st is None:
        return
    st.markdown(
        f"""
        <header role="banner" style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 14px; margin-bottom: 24px; flex-wrap: wrap; gap: 10px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                {DEVOS_LOGO_SVG}
                <div>
                    <a href="{MAIN_SITE_URL}" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: #f97316; font-weight: 700; font-size: 0.95rem; letter-spacing: 0.05em; text-transform: uppercase;">
                        DeveloperOS
                    </a>
                    <span style="color: #64748b; margin: 0 8px;">/</span>
                    <span style="color: #cbd5e1; font-size: 0.9rem;">Database & SQL Suite</span>
                    <h1 style="margin: 4px 0 0 0; font-size: 1.75rem; font-weight: 700; color: #f8fafc;">{title}</h1>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                <a href="{MAIN_SITE_URL}?utm_source=developeros_tools&utm_medium=header_banner&utm_campaign=powered_by" target="_blank" rel="noopener noreferrer" style="
                    display: inline-flex;
                    align-items: center;
                    gap: 4px;
                    background: rgba(249, 115, 22, 0.12);
                    border: 1px solid rgba(249, 115, 22, 0.35);
                    color: #f97316;
                    font-size: 0.78rem;
                    font-weight: 600;
                    padding: 4px 10px;
                    border-radius: 9999px;
                    text-decoration: none;
                ">
                    <span>⚡</span>
                    <span>Powered by DeveloperOS ↗</span>
                </a>
                <span style="background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 9999px; padding: 3px 10px; font-size: 0.75rem; font-weight: 600;">
                    Active Utility
                </span>
            </div>
        </header>
        <p style="color: #94a3b8; font-size: 1rem; margin-top: -12px; margin-bottom: 24px;">{description}</p>
        """,
        unsafe_allow_html=True,
    )


def render_main_promotional_banner(tool_name: Optional[str] = None):
    """Renders Main Promotional Banner below primary tool interface."""
    if st is None:
        return
    heading = f"Enjoying {tool_name}?" if tool_name else "Enjoying this free tool?"
    st.markdown(
        f"""
        <section class="devos-promotional-banner" role="region" aria-label="DeveloperOS Promotion" style="
            background: linear-gradient(135deg, rgba(249, 115, 22, 0.08) 0%, rgba(244, 63, 94, 0.04) 50%, rgba(6, 182, 212, 0.06) 100%), #0c0f15;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1.5rem 1.75rem;
            margin: 2.5rem 0 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.25rem;
        ">
            <div style="display: flex; align-items: center; gap: 1.25rem; max-width: 650px;">
                {DEVOS_LOGO_SVG}
                <div>
                    <h3 style="margin: 0 0 0.35rem 0; font-size: 1.2rem; font-weight: 700; color: #f8fafc; letter-spacing: -0.01em;">
                        {heading}
                    </h3>
                    <p style="margin: 0; color: #94a3b8; font-size: 0.95rem; line-height: 1.5;">
                        Discover more developer tools, AI resources, and automation solutions from DeveloperOS.
                    </p>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 0.85rem; flex-wrap: wrap;">
                <a href="{MAIN_SITE_URL}?utm_source=developeros_tools&utm_medium=main_banner&utm_campaign=ecosystem_referral" target="_blank" rel="noopener noreferrer" style="
                    background-color: #f97316;
                    color: #ffffff;
                    font-weight: 600;
                    font-size: 0.9rem;
                    padding: 0.55rem 1.25rem;
                    border-radius: 6px;
                    text-decoration: none;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.4rem;
                    box-shadow: 0 2px 4px rgba(249, 115, 22, 0.25);
                ">
                    Explore DeveloperOS &rarr;
                </a>
                <a href="{TOOLS_DIRECTORY_URL}?utm_source=developeros_tools&utm_medium=secondary_cta&utm_campaign=tools_directory" target="_blank" rel="noopener noreferrer" style="
                    background-color: rgba(255, 255, 255, 0.06);
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    color: #f8fafc;
                    font-weight: 600;
                    font-size: 0.9rem;
                    padding: 0.55rem 1.15rem;
                    border-radius: 6px;
                    text-decoration: none;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.4rem;
                ">
                    More Free Tools
                </a>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_suite_footer():
    """Renders Universal Footer Banner: 'Built with ❤️ by DeveloperOS'."""
    if st is None:
        return
    st.markdown(
        f"""
        <footer class="devos-footer-banner" role="contentinfo" style="
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            margin-top: 48px;
            padding-top: 24px;
            text-align: center;
            font-size: 0.875rem;
            color: #cbd5e1;
        ">
            <p style="font-size: 1rem; font-weight: 600; color: #f8fafc; margin: 0 0 10px 0;">
                Built with ❤️ by <a href="{MAIN_SITE_URL}?utm_source=developeros_tools&utm_medium=footer_tagline&utm_campaign=ecosystem_referral" target="_blank" rel="noopener noreferrer" style="color: #f97316; text-decoration: none; font-weight: 700;">DeveloperOS</a>
            </p>
            <div style="display: flex; justify-content: center; align-items: center; gap: 18px; flex-wrap: wrap; margin-bottom: 12px;">
                <a href="{MAIN_SITE_URL}?utm_source=developeros_tools&utm_medium=footer_link&utm_campaign=ecosystem_referral" target="_blank" rel="noopener noreferrer" style="color: #67e8f9; text-decoration: none;">
                    DeveloperOS Home
                </a>
                <span style="color: rgba(255, 255, 255, 0.2);">•</span>
                <a href="{TOOLS_DIRECTORY_URL}?utm_source=developeros_tools&utm_medium=footer_link&utm_campaign=ecosystem_referral" target="_blank" rel="noopener noreferrer" style="color: #67e8f9; text-decoration: none;">
                    All Tools Directory
                </a>
                <span style="color: rgba(255, 255, 255, 0.2);">•</span>
                <a href="{GITHUB_ORG_URL}" target="_blank" rel="noopener noreferrer" style="color: #67e8f9; text-decoration: none;">
                    GitHub Organization
                </a>
                <span style="color: rgba(255, 255, 255, 0.2);">•</span>
                <a href="{PRIVACY_URL}?utm_source=developeros_tools&utm_medium=footer_link&utm_campaign=ecosystem_referral" target="_blank" rel="noopener noreferrer" style="color: #67e8f9; text-decoration: none;">
                    Privacy Policy
                </a>
            </div>
            <p style="margin: 4px 0; color: #94a3b8; font-size: 0.8rem;">
                🛡️ <strong>Zero-Trust Privacy:</strong> Queries and schemas processed client-side. No telemetry or connection caching.
            </p>
            <p style="margin: 0; color: #6b7c94; font-size: 0.78rem;">
                DeveloperOS Open-Source Ecosystem • Licensed under MIT • Zero Storage &amp; Zero Tracking
            </p>
        </footer>
        """,
        unsafe_allow_html=True,
    )
