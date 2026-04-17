# ============================================
# AI Career Tool (with Charts)
# Author: Padma Shree
# Capstone Project 2
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ============================================
# SKILL DATABASE
# ============================================

SKILLS_DB = {
    "Python": ["Data Science", "Software Development", "AI/ML", "Backend"],
    "SQL": ["Data Analyst", "Database Admin", "Backend"],
    "Machine Learning": ["AI/ML Engineer", "Data Scientist", "Research"],
    "Deep Learning": ["AI Researcher", "Computer Vision", "NLP Engineer"],
    "Data Visualization": ["Data Analyst", "BI Developer", "Data Scientist"],
    "Statistics": ["Data Scientist", "Data Analyst", "Research"],
    "R": ["Data Scientist", "Bioinformatics", "Statistician"],
    "Java": ["Software Engineer", "Android Dev", "Backend"],
    "JavaScript": ["Frontend Dev", "Full Stack", "Web Dev"],
    "React": ["Frontend Dev", "UI Engineer"],
    "HTML": ["Frontend Dev", "Web Designer"],
    "CSS": ["Frontend Dev", "Web Designer"],
    "Git": ["All Software Roles"],
    "Docker": ["DevOps", "Cloud Engineer"],
    "Cloud": ["Cloud Engineer", "DevOps"],
    "AWS": ["Cloud Engineer", "DevOps"],
    "Azure": ["Cloud Engineer", "DevOps"],
    "Communication": ["All Roles"],
    "Problem Solving": ["All Roles"],
    "Teamwork": ["All Roles"],
    "Leadership": ["Manager", "Tech Lead", "Senior Roles"],
    "Project Management": ["Project Manager", "Scrum Master"],
    "Bioinformatics": ["Bioinformatics Scientist", "Computational Biologist"],
    "Pandas": ["Data Scientist", "Data Analyst"],
    "NumPy": ["Data Scientist", "Data Analyst"],
    "Matplotlib": ["Data Scientist", "Data Analyst"],
    "Seaborn": ["Data Scientist", "Data Analyst"],
    "Scikit-learn": ["Machine Learning Engineer", "Data Scientist"],
    "TensorFlow": ["Deep Learning Engineer", "AI Researcher"],
    "PyTorch": ["Deep Learning Engineer", "AI Researcher"],
    "Excel": ["Data Analyst", "Business Analyst"],
    "Tableau": ["Data Analyst", "BI Developer"],
    "Power BI": ["Data Analyst", "BI Developer"],
    "Spark": ["Data Engineer", "Big Data Engineer"],
    "Hadoop": ["Data Engineer", "Big Data Engineer"],
    "Kafka": ["Data Engineer", "Streaming Engineer"],
}

# ============================================
# JOB DATABASE
# ============================================

JOBS_DB = pd.DataFrame([
    {"title": "Data Scientist", "skills": ["Python", "SQL", "Machine Learning", "Statistics", "Data Visualization", "Pandas", "Scikit-learn"], "salary": "8-15 LPA", "growth": "High"},
    {"title": "Data Analyst", "skills": ["Python", "SQL", "Data Visualization", "Statistics", "Excel", "Tableau"], "salary": "5-10 LPA", "growth": "High"},
    {"title": "Machine Learning Engineer", "skills": ["Python", "Machine Learning", "Deep Learning", "SQL", "TensorFlow", "PyTorch"], "salary": "10-20 LPA", "growth": "Very High"},
    {"title": "Software Developer", "skills": ["Python", "Java", "Git", "Problem Solving"], "salary": "6-15 LPA", "growth": "High"},
    {"title": "Frontend Developer", "skills": ["JavaScript", "React", "HTML", "CSS", "Git"], "salary": "5-12 LPA", "growth": "High"},
    {"title": "Backend Developer", "skills": ["Python", "SQL", "Git", "Docker", "Java"], "salary": "6-14 LPA", "growth": "High"},
    {"title": "DevOps Engineer", "skills": ["Docker", "Git", "Cloud", "AWS", "Python"], "salary": "8-18 LPA", "growth": "Very High"},
    {"title": "Data Engineer", "skills": ["Python", "SQL", "Docker", "Cloud", "Spark", "Kafka"], "salary": "7-16 LPA", "growth": "Very High"},
    {"title": "Bioinformatics Scientist", "skills": ["Python", "R", "Bioinformatics", "Statistics"], "salary": "6-12 LPA", "growth": "High"},
    {"title": "AI Researcher", "skills": ["Python", "Deep Learning", "Machine Learning", "Statistics", "TensorFlow", "PyTorch"], "salary": "12-25 LPA", "growth": "Very High"},
    {"title": "Project Manager", "skills": ["Project Management", "Leadership", "Communication", "Problem Solving"], "salary": "10-20 LPA", "growth": "High"},
    {"title": "Business Analyst", "skills": ["Excel", "Communication", "Problem Solving", "SQL", "Tableau"], "salary": "6-12 LPA", "growth": "High"},
    {"title": "Full Stack Developer", "skills": ["JavaScript", "React", "Python", "SQL", "HTML", "CSS", "Git"], "salary": "7-16 LPA", "growth": "High"},
], columns=["title", "skills", "salary", "growth"])

# ============================================
# EXTRACT SKILLS FROM TEXT
# ============================================

def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILLS_DB.keys():
        if skill.lower() in text:
            found_skills.append(skill)
    return list(set(found_skills))

# ============================================
# MATCH JOBS
# ============================================

def match_jobs(skills):
    matches = []
    for idx, job in JOBS_DB.iterrows():
        required_skills = set(job["skills"])
        user_skills = set(skills)
        matching_skills = required_skills.intersection(user_skills)
        missing_skills = required_skills - user_skills
        if len(required_skills) > 0:
            match_percent = (len(matching_skills) / len(required_skills)) * 100
        else:
            match_percent = 0
        matches.append({
            "job_title": job["title"],
            "match_percent": round(match_percent, 1),
            "matching_skills": list(matching_skills),
            "missing_skills": list(missing_skills),
            "salary": job["salary"],
            "growth": job["growth"]
        })
    matches.sort(key=lambda x: x["match_percent"], reverse=True)
    return matches

# ============================================
# RECOMMEND LEARNING
# ============================================

def recommend_learning(missing_skills):
    recommendations = []
    learning_resources = {
        "Python": "https://www.python.org/about/gettingstarted/",
        "SQL": "https://www.w3schools.com/sql/",
        "Machine Learning": "https://www.coursera.org/learn/machine-learning",
        "Deep Learning": "https://www.deeplearning.ai/",
        "Data Visualization": "https://www.tableau.com/learn",
        "Statistics": "https://www.khanacademy.org/math/statistics-probability",
        "JavaScript": "https://www.javascript.com/",
        "React": "https://reactjs.org/docs/getting-started.html",
        "Docker": "https://docs.docker.com/get-started/",
        "Cloud": "https://aws.amazon.com/training/",
        "AWS": "https://aws.amazon.com/training/",
        "Git": "https://git-scm.com/doc",
        "Pandas": "https://pandas.pydata.org/docs/getting_started/",
        "NumPy": "https://numpy.org/learn/",
        "Matplotlib": "https://matplotlib.org/stable/tutorials/index.html",
        "Scikit-learn": "https://scikit-learn.org/stable/getting_started.html",
        "Java": "https://www.w3schools.com/java/",
        "Tableau": "https://www.tableau.com/learn/training",
        "Excel": "https://support.microsoft.com/en-us/excel",
    }
    for skill in missing_skills[:5]:
        resource = learning_resources.get(skill, f"https://www.google.com/search?q={skill}+tutorial")
        recommendations.append({"skill": skill, "resource": resource})
    return recommendations

# ============================================
# CAREER ANALYSIS
# ============================================

def career_analysis(skills):
    domains = set()
    for skill in skills:
        if skill in SKILLS_DB:
            for domain in SKILLS_DB[skill]:
                domains.add(domain)
    skill_count = len(skills)
    if skill_count >= 15:
        level = "Expert"
    elif skill_count >= 10:
        level = "Advanced"
    elif skill_count >= 5:
        level = "Intermediate"
    else:
        level = "Beginner"
    base_salary = 3 + (skill_count * 0.5)
    if "Python" in skills and "Machine Learning" in skills:
        recommended = "Data Scientist / ML Engineer"
    elif "Python" in skills and "SQL" in skills:
        recommended = "Data Analyst / Data Engineer"
    elif "JavaScript" in skills or "React" in skills:
        recommended = "Frontend / Full Stack Developer"
    elif "Java" in skills:
        recommended = "Software Developer"
    else:
        recommended = "Keep learning! Add Python or JavaScript first"
    return {
        "domains": list(domains),
        "skill_level": level,
        "total_skills": skill_count,
        "estimated_salary": f"{base_salary:.1f} - {base_salary + 5:.1f} LPA",
        "recommended_role": recommended
    }

# ============================================
# CREATE CHARTS
# ============================================

def create_charts(matches, skills, name):
    """Generate career visualization charts"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Chart 1: Top 5 job matches
    top5 = matches[:5]
    job_titles = [m["job_title"] for m in top5]
    match_scores = [m["match_percent"] for m in top5]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f"AI Career Tool - Career Dashboard for {name}", fontsize=14, fontweight="bold")
    
    # Chart 1: Horizontal bar chart of match scores
    colors = ["#4CAF50" if s >= 70 else "#FF9800" if s >= 50 else "#E91E63" for s in match_scores]
    bars1 = axes[0].barh(job_titles, match_scores, color=colors, edgecolor="black")
    axes[0].set_title("Top 5 Job Matches (%)", fontweight="bold")
    axes[0].set_xlabel("Match Percentage")
    axes[0].set_xlim(0, 105)
    for bar, val in zip(bars1, match_scores):
        axes[0].text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f"{val}%", va="center", fontweight="bold")
    
    # Chart 2: Skills analysis
    skill_count = len(skills)
    if matches and matches[0]["missing_skills"]:
        missing_count = len(matches[0]["missing_skills"])
        values = [skill_count, missing_count]
        colors2 = ["#2196F3", "#E91E63"]
        labels2 = ["Your Skills", f"Missing for {matches[0]['job_title']}"]
    else:
        values = [skill_count, 0]
        colors2 = ["#2196F3", "#9E9E9E"]
        labels2 = ["Your Skills", "No missing skills!"]
    
    bars2 = axes[1].bar(labels2, values, color=colors2, edgecolor="black")
    axes[1].set_title("Skills Gap Analysis", fontweight="bold")
    axes[1].set_ylabel("Number of Skills")
    for bar, val in zip(bars2, values):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), ha="center", fontweight="bold")
    
    plt.tight_layout()
    filename = f"career_charts_{name}_{timestamp}.png"
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"\n   📊 Chart saved: {filename}")
    return filename

# ============================================
# DISPLAY RESULTS
# ============================================

def display_results(skills, matches, insights, recommendations):
    print("\n" + "="*60)
    print("  🤖 AI CAREER TOOL — YOUR RESULTS")
    print("="*60)
    print("\n📊 YOUR SKILLS:")
    if skills:
        print(f"   {', '.join(skills)}")
    else:
        print("   No skills detected.")
    print("\n📈 CAREER INSIGHTS:")
    print(f"   Skill Level      : {insights['skill_level']}")
    print(f"   Total Skills     : {insights['total_skills']}")
    print(f"   Estimated Salary : {insights['estimated_salary']}")
    print(f"   Recommended Role : {insights['recommended_role']}")
    if insights['domains']:
        print(f"   Matching Domains : {', '.join(insights['domains'][:5])}")
    print("\n💼 TOP JOB MATCHES:")
    for i, match in enumerate(matches[:5], 1):
        print(f"\n   {i}. {match['job_title']} — {match['match_percent']}% match")
        print(f"      💰 Salary: {match['salary']} | 📈 Growth: {match['growth']}")
        if match['matching_skills']:
            print(f"      ✅ Matching: {', '.join(match['matching_skills'][:4])}")
        if match['missing_skills']:
            print(f"      ❌ Missing: {', '.join(match['missing_skills'][:3])}")
    print("\n📚 WHAT TO LEARN NEXT:")
    if recommendations:
        for rec in recommendations[:3]:
            print(f"   • {rec['skill']}")
            print(f"     → {rec['resource']}")
    else:
        print("   Great job! You're already well-matched!")
    print("\n" + "="*60)

# ============================================
# SAVE REPORT
# ============================================

def save_report(name, skills, matches, insights):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"career_report_{name}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write("="*60 + "\n")
        f.write("AI CAREER TOOL — CAREER REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write(f"Name: {name}\n")
        f.write("="*60 + "\n\n")
        f.write("YOUR SKILLS:\n")
        f.write("-"*40 + "\n")
        for skill in skills:
            f.write(f"  - {skill}\n")
        f.write("\nCAREER INSIGHTS:\n")
        f.write("-"*40 + "\n")
        f.write(f"Skill Level      : {insights['skill_level']}\n")
        f.write(f"Total Skills     : {insights['total_skills']}\n")
        f.write(f"Estimated Salary : {insights['estimated_salary']}\n")
        f.write(f"Recommended Role : {insights['recommended_role']}\n")
        f.write("\nTOP JOB MATCHES:\n")
        f.write("-"*40 + "\n")
        for match in matches[:5]:
            f.write(f"\n{'-'*40}\n")
            f.write(f"Job Title    : {match['job_title']}\n")
            f.write(f"Match Score  : {match['match_percent']}%\n")
            f.write(f"Salary Range : {match['salary']}\n")
            f.write(f"Growth       : {match['growth']}\n")
            if match['matching_skills']:
                f.write(f"Matching     : {', '.join(match['matching_skills'])}\n")
            if match['missing_skills']:
                f.write(f"Missing      : {', '.join(match['missing_skills'][:5])}\n")
        f.write("\n" + "="*60 + "\n")
        f.write("Report generated by AI Career Tool\n")
        f.write("Author: Padma Shree | Capstone Project 2\n")
        f.write("="*60 + "\n")
    print(f"\n   📄 Report saved: {filename}")
    return filename

# ============================================
# SHOW MENU
# ============================================

def show_menu():
    print("\n" + "="*50)
    print("  🤖 AI CAREER TOOL")
    print("="*50)
    print("  1. Enter your skills manually")
    print("  2. Paste resume text (extract skills)")
    print("  3. Sample: Beginner Profile")
    print("  4. Sample: Advanced Profile")
    print("  0. Exit")
    print("="*50)

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("    AI CAREER TOOL")
    print("    Author: Padma Shree | Capstone Project 2")
    print("="*50)
    
    while True:
        show_menu()
        choice = input("\n👉 Enter choice (0-4): ").strip()
        
        if choice == "0":
            print("\n   Good luck with your career Paddu! 🚀")
            break
        
        elif choice == "1":
            name = input("\n📝 Enter your name: ").strip()
            print("\n📊 Enter your skills (comma-separated)")
            print("   Example: Python, SQL, Machine Learning, Git, Pandas")
            skills_input = input("   Skills: ").strip()
            skills = [s.strip() for s in skills_input.split(",") if s.strip()]
            
        elif choice == "2":
            name = input("\n📝 Enter your name: ").strip()
            print("\n📄 Paste your resume text below (type 'DONE' on a new line when finished):")
            lines = []
            while True:
                line = input()
                if line == "DONE":
                    break
                lines.append(line)
            resume_text = " ".join(lines)
            skills = extract_skills(resume_text)
            if skills:
                print(f"\n   ✅ Extracted {len(skills)} skills: {', '.join(skills[:10])}")
            else:
                print("\n   ⚠️ No skills found. Try Option 1 to enter manually.")
            
        elif choice == "3":
            name = "Sample_Beginner"
            skills = ["Python", "HTML", "CSS", "Git", "Excel", "Communication"]
            print(f"\n   📋 Sample Beginner Profile")
            print(f"   Skills: {', '.join(skills)}")
            
        elif choice == "4":
            name = "Sample_Advanced"
            skills = ["Python", "SQL", "Machine Learning", "Data Visualization", 
                     "Statistics", "Git", "Pandas", "NumPy", "Communication",
                     "Problem Solving", "Teamwork", "Tableau"]
            print(f"\n   📋 Sample Advanced Profile")
            print(f"   Skills: {', '.join(skills)}")
            
        else:
            print("   ❌ Invalid choice! Please enter 0-4")
            continue
        
        if not skills:
            print("   ⚠️ No skills detected! Please try again.")
            continue
        
        matches = match_jobs(skills)
        insights = career_analysis(skills)
        if matches and matches[0]["missing_skills"]:
            recommendations = recommend_learning(matches[0]["missing_skills"])
        else:
            recommendations = []
        
        display_results(skills, matches, insights, recommendations)
        save_report(name, skills, matches, insights)
        
        # Generate charts
        chart_file = create_charts(matches, skills, name.replace(" ", "_"))