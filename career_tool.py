# ============================================
# AI Career Tool — Skill Analyzer
# Author: Padma Shree
# Features: Skill analysis, Career matching,
#            Gap analysis, Action plan, Report
# ============================================

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from datetime import datetime
import json
import os

# ─────────────────────────────────────────────
# CAREER DATABASE
# ─────────────────────────────────────────────

CAREERS = {
    "Bioinformatician": {
        "description" : "Analyze biological data using computational tools",
        "avg_salary"  : "8-20 LPA",
        "demand"      : "High",
        "skills_required": {
            "Python"       : 9,
            "R"            : 8,
            "Biology"      : 9,
            "SQL"          : 6,
            "Statistics"   : 7,
            "Linux/Bash"   : 7,
            "Machine Learning": 5,
            "Data Visualization": 6
        },
        "top_companies": ["TCS Life Sciences", "Strand Life Sciences",
                          "MedGenome", "Ocimum Bio", "Jubilant Biosys"],
        "certifications": ["Bioinformatics Specialization (Coursera)",
                           "Python for Genomics (edX)"],
        "job_titles"   : ["Bioinformatics Analyst", "Genomics Scientist",
                          "Computational Biologist"]
    },
    "Data Scientist": {
        "description" : "Extract insights from large datasets using ML and statistics",
        "avg_salary"  : "10-25 LPA",
        "demand"      : "Very High",
        "skills_required": {
            "Python"       : 9,
            "Machine Learning": 9,
            "Statistics"   : 8,
            "SQL"          : 7,
            "Data Visualization": 7,
            "Deep Learning": 6,
            "R"            : 5,
            "Cloud"        : 5
        },
        "top_companies": ["Google", "Amazon", "Flipkart",
                          "PhonePe", "Zomato", "CRED"],
        "certifications": ["Google Data Analytics (Coursera)",
                           "IBM Data Science Professional"],
        "job_titles"   : ["Data Scientist", "ML Analyst",
                          "AI Research Scientist"]
    },
    "ML Engineer": {
        "description" : "Build and deploy machine learning models at scale",
        "avg_salary"  : "15-35 LPA",
        "demand"      : "Very High",
        "skills_required": {
            "Python"       : 9,
            "Machine Learning": 9,
            "Deep Learning": 8,
            "Cloud"        : 8,
            "SQL"          : 6,
            "Statistics"   : 7,
            "Linux/Bash"   : 7,
            "Data Visualization": 5
        },
        "top_companies": ["Microsoft", "Google", "Meta",
                          "Uber", "Swiggy", "Ola"],
        "certifications": ["AWS ML Specialty",
                           "TensorFlow Developer Certificate"],
        "job_titles"   : ["ML Engineer", "AI Engineer",
                          "Deep Learning Engineer"]
    },
    "Computational Biologist": {
        "description" : "Model biological systems using mathematical and computational methods",
        "avg_salary"  : "8-18 LPA",
        "demand"      : "High",
        "skills_required": {
            "Python"       : 8,
            "R"            : 9,
            "Biology"      : 10,
            "Statistics"   : 9,
            "Machine Learning": 6,
            "Linux/Bash"   : 7,
            "SQL"          : 5,
            "Data Visualization": 7
        },
        "top_companies": ["NCBS Bangalore", "IISc", "TIFR",
                          "InStem", "Genentech India"],
        "certifications": ["Systems Biology (MIT OpenCourseWare)",
                           "Computational Genomics (Johns Hopkins)"],
        "job_titles"   : ["Computational Biologist", "Research Scientist",
                          "Systems Biologist"]
    },
    "Clinical Data Analyst": {
        "description" : "Analyze clinical trial and healthcare data",
        "avg_salary"  : "6-15 LPA",
        "demand"      : "High",
        "skills_required": {
            "SQL"          : 9,
            "Statistics"   : 8,
            "R"            : 7,
            "Python"       : 6,
            "Biology"      : 7,
            "Data Visualization": 7,
            "Machine Learning": 4,
            "Linux/Bash"   : 4
        },
        "top_companies": ["Sun Pharma", "Dr Reddys", "Biocon",
                          "Cipla", "IQVIA", "Covance"],
        "certifications": ["SAS Clinical Trials",
                           "Clinical Data Management (ACDM)"],
        "job_titles"   : ["Clinical Data Analyst", "Biostatistician",
                          "Pharmacovigilance Analyst"]
    },
    "Biotech Data Analyst": {
        "description" : "Analyze laboratory and research data in biotech companies",
        "avg_salary"  : "6-14 LPA",
        "demand"      : "Medium",
        "skills_required": {
            "Python"       : 7,
            "R"            : 8,
            "Biology"      : 9,
            "Statistics"   : 8,
            "SQL"          : 6,
            "Data Visualization": 8,
            "Machine Learning": 5,
            "Linux/Bash"   : 5
        },
        "top_companies": ["Biocon", "Serum Institute",
                          "Piramal", "Divi's Labs", "Lupin"],
        "certifications": ["Biostatistics (Johns Hopkins Coursera)",
                           "R for Data Science"],
        "job_titles"   : ["Biotech Analyst", "Research Data Analyst",
                          "Lab Data Scientist"]
    },
    "Research Scientist": {
        "description" : "Conduct original research in biology or computational fields",
        "avg_salary"  : "6-16 LPA",
        "demand"      : "Medium",
        "skills_required": {
            "Biology"      : 10,
            "Statistics"   : 9,
            "R"            : 8,
            "Python"       : 7,
            "Machine Learning": 6,
            "Data Visualization": 7,
            "SQL"          : 5,
            "Linux/Bash"   : 6
        },
        "top_companies": ["CSIR", "DBT", "ICMR",
                          "IISc", "IITs", "AIIMS"],
        "certifications": ["Research Methodology",
                           "Scientific Writing (Coursera)"],
        "job_titles"   : ["Research Scientist", "Junior Researcher",
                          "Postdoctoral Fellow"]
    },
    "Full Stack Developer": {
        "description" : "Build complete web applications from frontend to backend",
        "avg_salary"  : "8-22 LPA",
        "demand"      : "Very High",
        "skills_required": {
            "Python"       : 8,
            "SQL"          : 8,
            "Linux/Bash"   : 7,
            "Machine Learning": 4,
            "Statistics"   : 4,
            "R"            : 2,
            "Biology"      : 2,
            "Data Visualization": 6
        },
        "top_companies": ["Infosys", "Wipro", "TCS",
                          "HCL", "Cognizant", "Startups"],
        "certifications": ["Full Stack Web Dev (Udemy)",
                           "Django REST Framework"],
        "job_titles"   : ["Full Stack Developer", "Backend Developer",
                          "Python Developer"]
    }
}

ALL_SKILLS = [
    "Python", "R", "Biology", "SQL", "Statistics",
    "Machine Learning", "Deep Learning", "Linux/Bash",
    "Data Visualization", "Cloud"
]

# ─────────────────────────────────────────────
# GET USER SKILLS
# ─────────────────────────────────────────────

def get_user_skills():
    """Collect user skill ratings."""
    print("\n" + "="*60)
    print("  SKILL ASSESSMENT")
    print("="*60)
    print("  Rate your skills from 0 to 10:")
    print("  0 = No knowledge")
    print("  3 = Beginner")
    print("  5 = Intermediate")
    print("  7 = Advanced")
    print("  10 = Expert\n")

    user_skills = {}
    for skill in ALL_SKILLS:
        while True:
            try:
                score = int(input(f"  {skill:<25}: ").strip())
                if 0 <= score <= 10:
                    user_skills[skill] = score
                    break
                else:
                    print("  Please enter a number between 0 and 10!")
            except ValueError:
                print("  Please enter a valid number!")

    return user_skills

# ─────────────────────────────────────────────
# GET USER PROFILE
# ─────────────────────────────────────────────

def get_user_profile():
    """Collect user profile information."""
    print("\n" + "="*60)
    print("  YOUR PROFILE")
    print("="*60)
    name       = input("  Name                  : ").strip()
    education  = input("  Education (e.g. BSc Biology): ").strip()
    experience = input("  Years of experience   : ").strip()
    interests  = input("  Interests (e.g. genomics, ML): ").strip()
    goal       = input("  Career goal in 1 line : ").strip()

    return {
        "name"      : name,
        "education" : education,
        "experience": experience,
        "interests" : interests,
        "goal"      : goal
    }

# ─────────────────────────────────────────────
# ANALYZE CAREER MATCH
# ─────────────────────────────────────────────

def analyze_career_match(user_skills):
    """Calculate match percentage for each career."""
    matches = {}

    for career, info in CAREERS.items():
        required = info["skills_required"]
        total_required = sum(required.values())
        score = 0

        for skill, req_level in required.items():
            user_level = user_skills.get(skill, 0)
            contribution = min(user_level, req_level)
            score += contribution

        match_pct = round((score / total_required) * 100, 1)
        matches[career] = match_pct

    return dict(sorted(matches.items(),
                       key=lambda x: x[1], reverse=True))

# ─────────────────────────────────────────────
# GAP ANALYSIS
# ─────────────────────────────────────────────

def gap_analysis(user_skills, career):
    """Identify skill gaps for a specific career."""
    required = CAREERS[career]["skills_required"]
    gaps     = {}

    for skill, req_level in required.items():
        user_level = user_skills.get(skill, 0)
        gap = req_level - user_level
        if gap > 0:
            gaps[skill] = {
                "current" : user_level,
                "required": req_level,
                "gap"     : gap
            }

    return dict(sorted(gaps.items(),
                       key=lambda x: x[1]["gap"], reverse=True))

# ─────────────────────────────────────────────
# ACTION PLAN
# ─────────────────────────────────────────────

def generate_action_plan(gaps, career):
    """Generate personalized action plan."""
    info   = CAREERS[career]
    plan   = []

    if not gaps:
        plan.append("You are fully qualified for this role!")
        plan.append("Start applying to companies immediately!")
        return plan

    # Priority skills to develop
    for skill, gap_info in list(gaps.items())[:3]:
        gap = gap_info["gap"]
        if gap >= 5:
            plan.append(f"HIGH PRIORITY: Improve {skill} from {gap_info['current']}/10 to {gap_info['required']}/10")
        elif gap >= 3:
            plan.append(f"MEDIUM PRIORITY: Improve {skill} from {gap_info['current']}/10 to {gap_info['required']}/10")
        else:
            plan.append(f"LOW PRIORITY: Polish {skill} from {gap_info['current']}/10 to {gap_info['required']}/10")

    # Certifications
    if info["certifications"]:
        plan.append(f"Recommended certification: {info['certifications'][0]}")

    # Timeline
    total_gap = sum(g["gap"] for g in gaps.values())
    if total_gap <= 10:
        plan.append("Estimated time to be job-ready: 3-6 months")
    elif total_gap <= 20:
        plan.append("Estimated time to be job-ready: 6-12 months")
    else:
        plan.append("Estimated time to be job-ready: 12-18 months")

    return plan

# ─────────────────────────────────────────────
# VISUALIZE
# ─────────────────────────────────────────────

def visualize_results(user_skills, matches, top_career, profile):
    """Generate career analysis visualization."""
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle(f"AI Career Analysis — {profile['name']}",
                fontsize=14, fontweight="bold")
    gs  = gridspec.GridSpec(2, 3, figure=fig)

    # Chart 1 — Career match scores
    ax1    = fig.add_subplot(gs[0, 0:2])
    careers = list(matches.keys())
    scores  = list(matches.values())
    colors1 = ["#E91E63" if s >= 80 else "#4CAF50" if s >= 60
               else "#FF9800" for s in scores]
    bars   = ax1.barh(careers[::-1], scores[::-1],
                     color=colors1[::-1], edgecolor="black")
    for bar, val in zip(bars, scores[::-1]):
        ax1.text(val + 0.5, bar.get_y() + bar.get_height()/2,
                f"{val}%", va="center", fontweight="bold", fontsize=9)
    ax1.axvline(x=70, color="green", linestyle="--",
               alpha=0.7, label="Good match (70%)")
    ax1.set_title("Career Match Scores", fontweight="bold")
    ax1.set_xlabel("Match Percentage (%)")
    ax1.set_xlim(0, 115)
    ax1.legend(fontsize=8)

    # Chart 2 — User skill profile
    ax2 = fig.add_subplot(gs[0, 2])
    skills = list(user_skills.keys())
    values = list(user_skills.values())
    colors2 = ["#4CAF50" if v >= 7 else "#FF9800" if v >= 4
               else "#E91E63" for v in values]
    bars2  = ax2.barh(skills, values, color=colors2, edgecolor="black")
    for bar, val in zip(bars2, values):
        ax2.text(val + 0.1, bar.get_y() + bar.get_height()/2,
                str(val), va="center", fontweight="bold", fontsize=9)
    ax2.set_title("Your Skill Profile", fontweight="bold")
    ax2.set_xlabel("Skill Level (0-10)")
    ax2.set_xlim(0, 12)
    ax2.axvline(x=7, color="green", linestyle="--", alpha=0.5)

    # Chart 3 — Gap analysis for top career
    ax3  = fig.add_subplot(gs[1, 0])
    gaps = gap_analysis(user_skills, top_career)
    if gaps:
        gap_skills  = list(gaps.keys())
        current     = [gaps[s]["current"] for s in gap_skills]
        required    = [gaps[s]["required"] for s in gap_skills]
        x           = range(len(gap_skills))
        ax3.bar([i - 0.2 for i in x], current, 0.4,
               color="#2196F3", label="Current", edgecolor="black")
        ax3.bar([i + 0.2 for i in x], required, 0.4,
               color="#E91E63", label="Required", edgecolor="black")
        ax3.set_xticks(list(x))
        ax3.set_xticklabels(gap_skills, rotation=30, ha="right", fontsize=8)
        ax3.legend()
    ax3.set_title(f"Skill Gaps — {top_career[:20]}", fontweight="bold")
    ax3.set_ylabel("Skill Level")
    ax3.set_ylim(0, 12)

    # Chart 4 — Demand and salary comparison
    ax4 = fig.add_subplot(gs[1, 1])
    demand_map  = {"Very High": 4, "High": 3, "Medium": 2, "Low": 1}
    top5_careers = list(matches.keys())[:5]
    demands = [demand_map.get(CAREERS[c]["demand"], 2) for c in top5_careers]
    colors4 = ["#E91E63" if d == 4 else "#4CAF50" if d == 3
               else "#FF9800" for d in demands]
    bars4   = ax4.bar([c[:10] for c in top5_careers],
                     demands, color=colors4, edgecolor="black")
    ax4.set_yticks([1, 2, 3, 4])
    ax4.set_yticklabels(["Low", "Medium", "High", "Very High"])
    ax4.set_title("Market Demand (Top 5 Matches)", fontweight="bold")
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=30, ha="right")

    # Chart 5 — Profile summary
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.axis("off")
    summary = f"""
CAREER ANALYSIS SUMMARY

Name       : {profile['name']}
Education  : {profile['education'][:20]}
Experience : {profile['experience']} years
Goal       : {profile['goal'][:30]}

Top Match  : {list(matches.keys())[0]}
Score      : {list(matches.values())[0]}%

Salary Range:
{CAREERS[list(matches.keys())[0]]['avg_salary']}

Date: {datetime.now().strftime('%d-%m-%Y')}
"""
    ax5.text(0.05, 0.95, summary, transform=ax5.transAxes,
            fontsize=9, verticalalignment="top",
            fontfamily="monospace",
            bbox=dict(boxstyle="round",
                     facecolor="lightyellow", alpha=0.5))
    ax5.set_title("Profile Summary", fontweight="bold")

    plt.tight_layout()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = f"career_analysis_{profile['name']}_{timestamp}.png"
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n   Chart saved as: {filename}")
    return filename

# ─────────────────────────────────────────────
# DISPLAY RESULTS
# ─────────────────────────────────────────────

def display_results(matches, user_skills, profile):
    """Display career analysis results."""
    print("\n" + "="*60)
    print("  AI CAREER ANALYSIS RESULTS")
    print("="*60)
    print(f"  Name      : {profile['name']}")
    print(f"  Education : {profile['education']}")
    print(f"  Goal      : {profile['goal']}")

    print("\n  TOP CAREER MATCHES:")
    print(f"  {'Career':<30} {'Match%':>8} {'Demand':>10} {'Salary'}")
    print("  " + "-"*65)
    for career, score in list(matches.items())[:5]:
        info   = CAREERS[career]
        marker = " ← BEST FIT!" if score == max(matches.values()) else ""
        print(f"  {career:<30} {score:>7}% "
              f"{info['demand']:>10} "
              f"{info['avg_salary']}{marker}")

    # Top career details
    top_career = list(matches.keys())[0]
    info       = CAREERS[top_career]
    gaps       = gap_analysis(user_skills, top_career)
    plan       = generate_action_plan(gaps, top_career)

    print(f"\n  BEST FIT: {top_career}")
    print(f"  {info['description']}")
    print(f"  Salary: {info['avg_salary']}")
    print(f"  Demand: {info['demand']}")

    print(f"\n  TOP COMPANIES:")
    for company in info["top_companies"][:3]:
        print(f"    - {company}")

    print(f"\n  JOB TITLES:")
    for title in info["job_titles"]:
        print(f"    - {title}")

    if gaps:
        print(f"\n  SKILL GAPS TO FILL:")
        for skill, gap_info in list(gaps.items())[:4]:
            print(f"    {skill:<20}: {gap_info['current']}/10 "
                  f"→ {gap_info['required']}/10 "
                  f"(gap: {gap_info['gap']})")

    print(f"\n  ACTION PLAN:")
    for step in plan:
        print(f"    - {step}")

    print("="*60)

# ─────────────────────────────────────────────
# GENERATE REPORT
# ─────────────────────────────────────────────

def generate_report(matches, user_skills, profile):
    """Generate career analysis report."""
    timestamp  = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename   = f"career_report_{profile['name']}_{timestamp}.txt"
    top_career = list(matches.keys())[0]
    info       = CAREERS[top_career]
    gaps       = gap_analysis(user_skills, top_career)
    plan       = generate_action_plan(gaps, top_career)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write("AI CAREER ANALYSIS REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("="*60 + "\n\n")

        f.write(f"Name         : {profile['name']}\n")
        f.write(f"Education    : {profile['education']}\n")
        f.write(f"Experience   : {profile['experience']} years\n")
        f.write(f"Interests    : {profile['interests']}\n")
        f.write(f"Career Goal  : {profile['goal']}\n\n")

        f.write("YOUR SKILLS\n")
        f.write("-"*40 + "\n")
        for skill, level in user_skills.items():
            bar = "█" * level
            f.write(f"  {skill:<25}: {level}/10 {bar}\n")

        f.write("\nCAREER MATCH SCORES\n")
        f.write("-"*40 + "\n")
        for career, score in matches.items():
            f.write(f"  {career:<30}: {score}%\n")

        f.write(f"\nBEST FIT: {top_career}\n")
        f.write("-"*40 + "\n")
        f.write(f"Description  : {info['description']}\n")
        f.write(f"Salary Range : {info['avg_salary']}\n")
        f.write(f"Market Demand: {info['demand']}\n\n")

        f.write("SKILL GAPS\n")
        f.write("-"*40 + "\n")
        for skill, gap_info in gaps.items():
            f.write(f"  {skill:<20}: {gap_info['current']} → "
                   f"{gap_info['required']} (gap: {gap_info['gap']})\n")

        f.write("\nACTION PLAN\n")
        f.write("-"*40 + "\n")
        for step in plan:
            f.write(f"  - {step}\n")

        f.write("\nRECOMMENDED CERTIFICATIONS\n")
        f.write("-"*40 + "\n")
        for cert in info["certifications"]:
            f.write(f"  - {cert}\n")

        f.write("\n" + "="*60 + "\n")

    print(f"   Report saved: {filename}")
    return filename

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*60)
    print("    AI Career Tool — Skill Analyzer")
    print("    Author: Padma Shree")
    print("    Careers: Bioinformatics to Tech")
    print("="*60)
    print("\n  This tool analyzes your skills and suggests")
    print("  the best career paths for you!")

    while True:
        print("\n  Options:")
        print("  1. Analyze my career fit")
        print("  0. Exit")

        choice = input("\n  Enter choice: ").strip()

        if choice == "1":
            profile     = get_user_profile()
            user_skills = get_user_skills()
            matches     = analyze_career_match(user_skills)
            top_career  = list(matches.keys())[0]

            display_results(matches, user_skills, profile)
            print("\n  Generating career analysis chart...")
            visualize_results(user_skills, matches, top_career, profile)
            print("  Generating career report...")
            generate_report(matches, user_skills, profile)

        elif choice == "0":
            print("\n  Best of luck with your career Paddu!")
            print("  You are going to do amazing things! 🚀")
            break
        else:
            print("  Invalid choice!")