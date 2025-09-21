
# make_curriculum_pdf.py
# Generates a clean PDF (A4) with the 18-month cybersecurity curriculum and clickable links.
# Requires: fpdf2 2.x (install with: python -m pip install fpdf2)

from fpdf import FPDF

TITLE = "18-Month Ivy-Level Cybersecurity Curriculum"

# Keep ASCII-only text to avoid font encoding issues with core fonts.
# Each entry: (months, section_title, items)
# items: list of (label, text, url_or_None)
CURRICULUM = [
    ("Months 1-2", "Cybersecurity Foundations", [
        ("Course:", "CS50's Introduction to Cybersecurity (HarvardX)", "https://www.edx.org/learn/cybersecurity/harvard-university-cs50-s-introduction-to-cybersecurity"),
        ("Textbook:", "Computer Security: Principles and Practice (Stallings & Brown, 5th ed.)", "https://www.pearson.com/en-us/subject-catalog/p/computer-security-principles-and-practice/P200000005355/9780137465383"),
        ("Supplement:", "Cybersecurity for Everyone (University of Maryland)", "https://www.coursera.org/learn/cyber-security"),
    ]),
    ("Months 3-4", "Cryptography & Secure Communications", [
        ("Course:", "Cryptography I (Stanford University)", "https://www.coursera.org/learn/crypto"),
        ("Textbook:", "Understanding Cryptography (Paar & Pelzl)", "https://link.springer.com/book/10.1007/978-3-642-04101-3"),
        ("Reference:", "Applied Cryptography (Bruce Schneier)", "https://www.schneier.com/books/applied_cryptography/"),
    ]),
    ("Months 5-6", "Software & Application Security", [
        ("Course:", "Software Security (University of Maryland)", "https://www.edx.org/course/software-security"),
        ("Textbook:", "The Web Application Hacker's Handbook (Stuttard & Pinto)", "https://www.wiley.com/en-us/The+Web+Application+Hacker%27s+Handbook%3A+Finding+and+Exploiting+Security+Flaws%2C+2nd+Edition-p-9781118026472"),
        ("Labs:", "PortSwigger Web Security Academy", "https://portswigger.net/web-security"),
    ]),
    ("Months 7-8", "Operating System & Cloud Security", [
        ("Course:", "IBM Cybersecurity Analyst - Cloud Security (Course 5)", "https://www.coursera.org/professional-certificates/ibm-cybersecurity-analyst"),
        ("Textbook:", "Cloud Security and Privacy (Mather, Kumaraswamy, Latif)", "https://www.oreilly.com/library/view/cloud-security-and/9780596806235/"),
        ("Supplement:", "AWS Cloud Security Fundamentals", "https://www.aws.training/Details/Curriculum?id=20685"),
    ]),
    ("Months 9-10", "Risk Management & Governance", [
        ("Course:", "Cybersecurity: Managing Risk in the Information Age (Harvard Online)", "https://pll.harvard.edu/course/cybersecurity-managing-risk-information-age"),
        ("Textbook:", "Cybersecurity and Cyberwar (Singer & Friedman)", "https://www.oup.com/us/he/companion.websites/9780199918096/"),
        ("Reference:", "NIST Cybersecurity Framework", "https://www.nist.gov/cyberframework"),
    ]),
    ("Months 11-12", "Digital Forensics & Incident Response", [
        ("Course:", "IBM Cybersecurity Analyst - Forensics", "https://www.coursera.org/learn/cybersecurity-analyst-forensics"),
        ("Textbook:", "Incident Response & Computer Forensics (Luttgens, Pepe, Mandia)", "https://www.mhprofessional.com/9781260463676-usa-incident-response-computer-forensics-third-edition-group"),
        ("Labs:", "CyberDefenders: Blue-team challenges", "https://cyberdefenders.org/"),
    ]),
    ("Months 13-14", "Privacy Engineering & Usability", [
        ("Course:", "Privacy and Security (MITx)", "https://www.edx.org/course/privacy-and-security"),
        ("Textbook:", "Privacy Engineering: A Dataflow and Ontological Approach (Ian Oliver)", "https://www.springer.com/gp/book/9783319570000"),
        ("Supplement:", "Usable Security (University of Maryland)", "https://www.coursera.org/learn/usable-security"),
    ]),
    ("Months 15-16", "Cyber Law & Ethics", [
        ("Course:", "Cybersecurity: The Intersection of Policy and Technology (Harvard Kennedy School)", "https://pll.harvard.edu/course/cybersecurity-intersection-policy-and-technology"),
        ("Textbook:", "Cybersecurity Law (Jeff Kosseff)", "https://www.wiley.com/en-us/Cybersecurity+Law%2C+2nd+Edition-p-9781119859833"),
        ("Reference:", "Stanford Cyber Policy Center", "https://cyber.fsi.stanford.edu/"),
    ]),
    ("Month 17", "Emerging Threats & AI Security", [
        ("Course:", "AI & Cybersecurity (Stanford / DeepLearning.AI)", "https://www.coursera.org/learn/ai-cybersecurity"),
        ("Textbook:", "Artificial Intelligence and Cybersecurity (Mark Stamp)", "https://www.springer.com/gp/book/9783030917548"),
        ("Research:", "MIT CSAIL: Cybersecurity research", "https://www.csail.mit.edu/research/cybersecurity"),
    ]),
    ("Month 18", "Capstone Project & Certification Prep", [
        ("Course:", "Cybersecurity Capstone Project (University of Maryland)", "https://www.coursera.org/learn/cybersecurity-capstone"),
        ("Certification:", "ISC2 Certified in Cybersecurity (CC) on Coursera", "https://www.coursera.org/learn/certified-in-cybersecurity"),
        ("Labs:", "TryHackMe (hands-on) / Hack The Box", "https://tryhackme.com/"),
    ]),
]

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, TITLE, ln=True, align="C")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(120)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def add_section(pdf, months, title, items):
    pdf.set_text_color(0)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, f"{months}: {title}", ln=True)
    pdf.ln(1)

    pdf.set_font("Helvetica", "", 11)
    for label, text, url in items:
        # Label
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(22, 6, label, ln=0)
        # Text (with optional link)
        pdf.set_font("Helvetica", "", 11)
        if url:
            # Make link visibly blue and clickable
            pdf.set_text_color(0, 0, 200)
            # Use write to embed link; then reset color
            pdf.write(6, text, url)
            pdf.set_text_color(0)
        else:
            pdf.write(6, text)
        pdf.ln(7)
    pdf.ln(3)

def build_pdf(filename="Cybersecurity_Curriculum.pdf"):
    pdf = PDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Intro
    pdf.set_font("Helvetica", "", 12)
    intro = (
        "This 18-month, Ivy-level aligned cybersecurity curriculum is paced at ~7-10 hours per week. "
        "Each section pairs elite online courses with textbooks and lab resources. Links are clickable."
    )
    pdf.multi_cell(0, 6, intro)
    pdf.ln(3)

    # Sections
    for months, title, items in CURRICULUM:
        add_section(pdf, months, title, items)

    pdf.output(filename)
    return filename

if __name__ == "__main__":
    out = build_pdf()
    print(f"Generated: {out}")
