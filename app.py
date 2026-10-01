import json
from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerAI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# FILE LOCATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
CAREERS_FILE = BASE_DIR / "careers.json"


# ============================================================
# LOAD CAREERS
# ============================================================

try:
    with open(CAREERS_FILE, "r", encoding="utf-8") as file:
        careers = json.load(file)

except FileNotFoundError:
    st.error("❌ careers.json was not found.")
    st.info("Make sure careers.json is in the same folder as app.py.")
    st.stop()

except json.JSONDecodeError:
    st.error("❌ careers.json contains invalid JSON.")
    st.stop()


if not isinstance(careers, list):
    st.error("❌ careers.json must contain a list of career objects.")
    st.stop()


# ============================================================
# NEW CAREERAI THEME
# MIDNIGHT NAVY + TEAL + SKY BLUE
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN APP
       ======================================================== */

    .stApp {
        background-color: #F4F8FB;
        color: #172033;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background-color: #071A2B;
        border-right: 1px solid #123A52;
    }

    [data-testid="stSidebar"] * {
        color: #F5FAFF !important;
    }

    [data-testid="stSidebar"] .stCaption {
        color: #8FB7CC !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: #1B4056;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1 {
        color: #071A2B !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        color: #0B3449 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #075985 !important;
        font-weight: 700 !important;
    }

    p {
        color: #405466;
    }


    /* ========================================================
       SIDEBAR RADIO
       ======================================================== */

    [data-testid="stSidebar"] [role="radiogroup"] label {
        background-color: transparent;
        border-radius: 10px;
        padding: 8px 10px;
        margin-bottom: 4px;
        transition: 0.2s;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background-color: #10344A;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        background-color: #087EA4;
        color: white !important;
        border: 1px solid #087EA4;
        border-radius: 10px;
        padding: 0.55rem 1rem;
        font-weight: 650;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #05647F;
        border-color: #05647F;
        color: white !important;
        transform: translateY(-1px);
    }


    /* ========================================================
       SELECTBOX
       ======================================================== */

    [data-baseweb="select"] > div {
        background-color: white;
        border: 1px solid #C7D8E2;
        border-radius: 10px;
    }


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    .stTextInput input {
        background-color: white;
        color: #172033;
        border: 1px solid #C7D8E2;
        border-radius: 10px;
    }

    .stTextInput input:focus {
        border-color: #0EA5C9;
        box-shadow: 0 0 0 1px #0EA5C9;
    }


    /* ========================================================
       NUMBER INPUT
       ======================================================== */

    .stNumberInput input {
        background-color: white;
        color: #172033;
        border: 1px solid #C7D8E2;
        border-radius: 10px;
    }


    /* ========================================================
       MULTISELECT
       ======================================================== */

    [data-baseweb="select"] {
        border-radius: 10px;
    }


    /* ========================================================
       METRICS
       ======================================================== */

    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #D7E4EB;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 3px 12px rgba(7, 26, 43, 0.06);
    }

    [data-testid="stMetricLabel"] {
        color: #587080 !important;
    }

    [data-testid="stMetricValue"] {
        color: #075985 !important;
        font-weight: 800 !important;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    [data-testid="stExpander"] {
        background-color: white;
        border: 1px solid #D7E4EB;
        border-radius: 14px;
        margin-bottom: 10px;
    }

    [data-testid="stExpander"]:hover {
        border-color: #7CC9DD;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ========================================================
       PROGRESS
       ======================================================== */

    [data-testid="stProgress"] > div > div > div {
        background-color: #0EA5C9;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {
        border-color: #D7E4EB;
    }


    /* ========================================================
       CHECKBOX
       ======================================================== */

    [data-testid="stCheckbox"] label {
        color: #263B4A !important;
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    [data-testid="stFileUploader"] {
        background-color: white;
        border: 1px dashed #9BBAC8;
        border-radius: 12px;
    }


    /* ========================================================
       DATAFRAME
       ======================================================== */

    [data-testid="stDataFrame"] {
        border: 1px solid #D7E4EB;
        border-radius: 12px;
    }


    /* ========================================================
       SCROLLBAR
       ======================================================== */

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #EAF1F5;
    }

    ::-webkit-scrollbar-thumb {
        background: #7AAFC0;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #087EA4;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clean_list(value):
    """Convert a JSON value into a clean list of strings."""

    if value is None:
        return []

    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]

    if isinstance(value, str):
        return [
            item.strip()
            for item in value.split(",")
            if item.strip()
        ]

    return []


def get_career_name(career):
    """Get career name from different possible JSON keys."""

    return (
        career.get("career")
        or career.get("name")
        or career.get("title")
        or "Unnamed Career"
    )


def get_icon(career):
    return career.get("icon", "💼")


def get_skills(career):
    return clean_list(career.get("skills", []))


def get_interests(career):
    return clean_list(career.get("interests", []))


def get_roadmap(career):
    return clean_list(career.get("roadmap", []))


def get_description(career):
    return (
        career.get("description")
        or career.get("overview")
        or career.get("about")
        or "Explore this career path and build the skills required for it."
    )


# ============================================================
# COURSE KEYWORDS
# Used when careers.json does not contain a courses field.
# ============================================================

COURSE_KEYWORDS = {

    "CSE": [
        "software",
        "developer",
        "programmer",
        "web",
        "app",
        "application",
        "database",
        "cloud",
        "cyber",
        "security",
        "data",
        "artificial intelligence",
        "ai",
        "machine learning",
        "ml",
        "computer",
        "python",
        "java",
        "programming",
    ],

    "CSE (AI & ML)": [
        "artificial intelligence",
        "ai",
        "machine learning",
        "ml",
        "deep learning",
        "data scientist",
        "data science",
        "nlp",
        "natural language",
        "computer vision",
        "robotics",
        "python",
    ],

    "IT": [
        "software",
        "developer",
        "web",
        "cloud",
        "network",
        "cyber",
        "security",
        "database",
        "it",
        "technical",
        "support",
        "programming",
        "data",
    ],

    "ECE": [
        "embedded",
        "electronics",
        "vlsi",
        "iot",
        "internet of things",
        "communication",
        "telecommunication",
        "robotics",
        "hardware",
        "semiconductor",
        "electronics engineer",
    ],

    "EEE": [
        "electrical",
        "power",
        "energy",
        "electronics",
        "control",
        "automation",
        "embedded",
        "renewable",
        "electric",
    ],

    "Mechanical": [
        "mechanical",
        "manufacturing",
        "automobile",
        "automotive",
        "cad",
        "design engineer",
        "production",
        "thermal",
        "robotics",
        "industrial",
    ],

    "Civil": [
        "civil",
        "construction",
        "structural",
        "architecture",
        "building",
        "survey",
        "infrastructure",
        "environmental",
        "urban",
    ],

    "BCA": [
        "software",
        "developer",
        "programming",
        "web",
        "database",
        "data",
        "cloud",
        "cyber",
        "computer",
        "python",
        "java",
    ],

    "Data Science": [
        "data",
        "data science",
        "data scientist",
        "analytics",
        "statistics",
        "machine learning",
        "ml",
        "python",
        "artificial intelligence",
        "ai",
    ],
}


COURSE_OPTIONS = [
    "All Courses",
    "CSE",
    "CSE (AI & ML)",
    "IT",
    "ECE",
    "EEE",
    "Mechanical",
    "Civil",
    "BCA",
    "Data Science",
]


def career_matches_course(career, selected_course):
    """
    Check whether a career belongs to the selected course.

    If careers.json contains a 'courses' field, that field is used.
    Otherwise a keyword-based fallback is used.
    """

    if selected_course == "All Courses":
        return True

    career_courses = clean_list(career.get("courses", []))

    if career_courses:

        normalized_courses = [
            course.lower().strip()
            for course in career_courses
        ]

        return selected_course.lower().strip() in normalized_courses

    career_name = get_career_name(career)

    searchable_text = " ".join(
        [
            career_name,
            get_description(career),
            " ".join(get_skills(career)),
            " ".join(get_interests(career)),
        ]
    ).lower()

    keywords = COURSE_KEYWORDS.get(selected_course, [])

    return any(
        keyword.lower() in searchable_text
        for keyword in keywords
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎓 CareerAI")

    st.caption("Smart Student Career Assistant")

    st.success("🟢 System Ready")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🎯 Career Analyzer",
            "📚 Career Explorer",
            "ℹ️ About",
        ],
    )

    st.divider()

    st.caption("CareerAI helps students explore technology careers based on skills, interests and learning goals.")


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.title("🎓 CareerAI")

    st.subheader(
        "Smart Student Career Assistant"
    )

    st.write(
        "Discover suitable technology careers based on your "
        "skills, interests and learning goals."
    )

    st.divider()

    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------

    all_skills = set()
    all_interests = set()

    for career in careers:

        all_skills.update(get_skills(career))
        all_interests.update(get_interests(career))

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Career Paths",
            len(careers),
        )

    with col2:
        st.metric(
            "Skills",
            len(all_skills),
        )

    with col3:
        st.metric(
            "Interests",
            len(all_interests),
        )

    with col4:
        st.metric(
            "Courses",
            len(COURSE_OPTIONS) - 1,
        )

    st.divider()

    # --------------------------------------------------------
    # How it works
    # --------------------------------------------------------

    st.header("🚀 How CareerAI Works")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.subheader("1️⃣ Build Your Profile")
        st.write(
            "Enter your academic details, skills and interests."
        )

    with step2:
        st.subheader("2️⃣ Analyze Your Match")
        st.write(
            "CareerAI compares your profile with different career paths."
        )

    with step3:
        st.subheader("3️⃣ Plan Your Journey")
        st.write(
            "See matching skills, missing skills and a learning roadmap."
        )

    st.divider()

    # --------------------------------------------------------
    # Features
    # --------------------------------------------------------

    st.header("✨ Explore CareerAI")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.info(
            "🎯 **Career Analyzer**\n\n"
            "Find career paths that match your skills and interests."
        )

    with f2:
        st.info(
            "📚 **Career Explorer**\n\n"
            "Explore careers according to your course."
        )

    with f3:
        st.info(
            "🛣️ **Learning Roadmap**\n\n"
            "Understand what skills you can learn next."
        )

    st.divider()

    st.success(
        "💡 Tip: Explore multiple careers before choosing your learning path."
    )


# ============================================================
# CAREER ANALYZER
# ============================================================

elif page == "🎯 Career Analyzer":

    st.title("🎯 Career Analyzer")

    st.write(
        "Tell CareerAI about yourself and discover careers "
        "that match your current profile."
    )

    st.divider()

    # --------------------------------------------------------
    # Student details
    # --------------------------------------------------------

    st.header("👨‍🎓 Your Profile")

    col1, col2, col3 = st.columns(3)

    with col1:

        student_name = st.text_input(
            "Your Name",
            placeholder="Enter your name",
        )

    with col2:

        degree = st.text_input(
            "Degree / Branch",
            placeholder="Example: B.Tech CSE",
        )

    with col3:

        percentage = st.number_input(
            "Academic Percentage",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=0.5,
        )

    st.divider()

    # --------------------------------------------------------
    # Collect skills and interests
    # --------------------------------------------------------

    all_skills = sorted(
        {
            skill
            for career in careers
            for skill in get_skills(career)
        }
    )

    all_interests = sorted(
        {
            interest
            for career in careers
            for interest in get_interests(career)
        }
    )

    st.header("💻 Your Skills")

    selected_skills = st.multiselect(
        "Select the skills you already have",
        all_skills,
        placeholder="Choose your skills",
    )

    st.header("❤️ Your Interest")

    selected_interest = st.selectbox(
        "Which area interests you the most?",
        ["Select an interest"] + all_interests,
    )

    st.divider()

    analyze = st.button(
        "🔍 Analyze My Career",
        use_container_width=True,
    )

    if analyze:

        if not student_name.strip():

            st.warning(
                "Please enter your name first."
            )

        elif not selected_skills:

            st.warning(
                "Please select at least one skill."
            )

        elif selected_interest == "Select an interest":

            st.warning(
                "Please select your interest."
            )

        else:

            # ------------------------------------------------
            # Calculate career scores
            # ------------------------------------------------

            results = []

            selected_skill_set = {
                skill.lower()
                for skill in selected_skills
            }

            for career in careers:

                career_skills = get_skills(career)

                career_skill_set = {
                    skill.lower()
                    for skill in career_skills
                }

                matching_skills = [
                    skill
                    for skill in career_skills
                    if skill.lower() in selected_skill_set
                ]

                missing_skills = [
                    skill
                    for skill in career_skills
                    if skill.lower() not in selected_skill_set
                ]

                if career_skills:

                    skill_score = (
                        len(matching_skills)
                        / len(career_skills)
                    ) * 75

                else:

                    skill_score = 0

                career_interests = get_interests(career)

                interest_score = 0

                for interest in career_interests:

                    if interest.lower() == selected_interest.lower():

                        interest_score = 25
                        break

                total_score = min(
                    100,
                    round(
                        skill_score + interest_score,
                        1,
                    ),
                )

                results.append(
                    {
                        "career": career,
                        "score": total_score,
                        "matching_skills": matching_skills,
                        "missing_skills": missing_skills,
                    }
                )

            results.sort(
                key=lambda item: item["score"],
                reverse=True,
            )

            st.divider()

            st.header(
                f"🎯 Career Matches for {student_name.strip()}"
            )

            if degree.strip():

                st.caption(
                    f"Profile: {degree.strip()} • "
                    f"Academic Score: {percentage:.1f}%"
                )

            # ------------------------------------------------
            # Top results
            # ------------------------------------------------

            top_results = results[:3]

            for index, result in enumerate(top_results):

                career = result["career"]

                career_name = get_career_name(career)

                icon = get_icon(career)

                score = result["score"]

                matching = result["matching_skills"]

                missing = result["missing_skills"]

                st.subheader(
                    f"{icon} {index + 1}. {career_name}"
                )

                st.progress(
                    int(score),
                    text=f"Career Match: {score:.1f}%",
                )

                c1, c2 = st.columns(2)

                with c1:

                    st.write("### ✅ Matching Skills")

                    if matching:

                        st.write(
                            ", ".join(matching)
                        )

                    else:

                        st.write(
                            "No direct skill matches yet."
                        )

                with c2:

                    st.write("### 📚 Skills to Learn")

                    if missing:

                        st.write(
                            ", ".join(missing)
                        )

                    else:

                        st.write(
                            "You already have the listed skills."
                        )

                roadmap = get_roadmap(career)

                if roadmap:

                    st.write("### 🛣️ Suggested Roadmap")

                    for step_number, step in enumerate(
                        roadmap,
                        start=1,
                    ):

                        st.write(
                            f"**{step_number}.** {step}"
                        )

                st.divider()


# ============================================================
# CAREER EXPLORER
# ============================================================

elif page == "📚 Career Explorer":

    st.title("📚 Career Explorer")

    st.write(
        "Explore technology career paths based on your course."
    )

    st.divider()

    # --------------------------------------------------------
    # Course selector
    # --------------------------------------------------------

    st.header("🎓 Choose Your Course")

    selected_course = st.selectbox(
        "Select a course",
        COURSE_OPTIONS,
    )

    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    search_text = st.text_input(
        "🔎 Search careers",
        placeholder="Example: Python, Data, AI, Developer...",
    )

    # --------------------------------------------------------
    # Filter careers
    # --------------------------------------------------------

    filtered_careers = []

    for career in careers:

        if not career_matches_course(
            career,
            selected_course,
        ):
            continue

        if search_text.strip():

            searchable_text = " ".join(
                [
                    get_career_name(career),
                    get_description(career),
                    " ".join(get_skills(career)),
                    " ".join(get_interests(career)),
                ]
            ).lower()

            if search_text.lower() not in searchable_text:

                continue

        filtered_careers.append(career)

    # --------------------------------------------------------
    # Result count
    # --------------------------------------------------------

    st.caption(
        f"Showing {len(filtered_careers)} career path(s)"
    )

    st.divider()

    # --------------------------------------------------------
    # Display careers
    # --------------------------------------------------------

    if not filtered_careers:

        st.warning(
            "No careers found for this course/search."
        )

        st.info(
            "Try another course or remove the search text."
        )

    else:

        for career in filtered_careers:

            career_name = get_career_name(career)

            icon = get_icon(career)

            description = get_description(career)

            skills = get_skills(career)

            interests = get_interests(career)

            roadmap = get_roadmap(career)

            with st.expander(
                f"{icon} {career_name}",
                expanded=False,
            ):

                st.write(
                    description
                )

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.write("### 💻 Required Skills")

                    if skills:

                        for skill in skills:

                            st.write(
                                f"• {skill}"
                            )

                    else:

                        st.write(
                            "Skills information not available."
                        )

                with col2:

                    st.write("### ❤️ Related Interests")

                    if interests:

                        for interest in interests:

                            st.write(
                                f"• {interest}"
                            )

                    else:

                        st.write(
                            "Interest information not available."
                        )

                if roadmap:

                    st.divider()

                    st.write(
                        "### 🛣️ Learning Roadmap"
                    )

                    for step_number, step in enumerate(
                        roadmap,
                        start=1,
                    ):

                        st.write(
                            f"**{step_number}.** {step}"
                        )


# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About CareerAI")

    st.write(
        "CareerAI is a student-focused career exploration "
        "application designed to help learners understand "
        "technology career opportunities."
    )

    st.divider()

    st.header("🎯 What CareerAI Does")

    st.write(
        "CareerAI uses your selected skills and interests "
        "to identify career paths that may match your profile."
    )

    st.write(
        "The application also provides information about "
        "skills, interests and learning roadmaps for different careers."
    )

    st.divider()

    st.header("✨ Main Features")

    features = [
        "🎯 Career matching",
        "💻 Skill comparison",
        "❤️ Interest-based matching",
        "📚 Course-based career exploration",
        "🛣️ Learning roadmaps",
        "🔎 Career search",
    ]

    for feature in features:

        st.write(
            f"• {feature}"
        )

    st.divider()

    st.header("🧠 How Matching Works")

    st.write(
        "CareerAI considers two main areas:"
    )

    st.write(
        "1. **Skills** — compares your selected skills "
        "with the skills associated with each career."
    )

    st.write(
        "2. **Interests** — checks whether your selected "
        "interest is related to the career."
    )

    st.info(
        "💡 CareerAI is an exploration tool. "
        "Students can use the information to research "
        "different career paths and learning options."
    )

    st.divider()

    st.caption(
        "CareerAI • Smart Student Career Assistant"
    )