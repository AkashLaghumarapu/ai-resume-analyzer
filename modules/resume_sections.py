import re

SECTION_HEADERS = [
    "Professional Summary",
    "Summary",
    "Experience",
    "Work Experience",
    "Education",
    "Skills",
    "Technical Skills",
    "Projects",
    "Certifications",
    "Awards",
    "Achievements",
    "Qualifications",
]


def extract_resume_sections(text):
    sections = {header: "" for header in SECTION_HEADERS}
    sections["Summary"] = ""
    current_section = "Summary"
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:
        header_match = next((header for header in SECTION_HEADERS if header.lower() in line.lower()), None)
        if header_match:
            current_section = header_match
            sections[current_section] = ""
            continue

        sections[current_section] += f" {line}"

    trimmed_sections = {section: content.strip() for section, content in sections.items() if content.strip()}
    if not trimmed_sections:
        trimmed_sections["Summary"] = text.strip()
    return trimmed_sections
