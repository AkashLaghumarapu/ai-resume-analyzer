import re


# ---------- SECTION HEADERS ----------

SECTION_PATTERNS = {

    "education": [

        "education",
        "academic background",
        "qualification"

    ],

    "skills": [

        "skills",
        "technical skills",
        "core skills"

    ],

    "projects": [

        "projects",
        "personal projects",
        "academic projects"

    ],

    "experience": [

        "experience",
        "work experience",
        "professional experience"

    ]

}


# ---------- EXTRACT SECTIONS ----------

def extract_resume_sections(text):

    if not text:

        return {}

    text_lower = text.lower()

    sections = {}

    for section, patterns in SECTION_PATTERNS.items():

        found = False

        for pattern in patterns:

            regex = rf"{pattern}(.*?)(?=\n[A-Z ]{{3,}}|\Z)"

            match = re.search(

                regex,
                text_lower,
                re.DOTALL

            )

            if match:

                content = match.group(1).strip()

                if len(content) > 20:

                    sections[section] = content

                    found = True

                    break

        if not found:

            sections[section] = ""

    return sections