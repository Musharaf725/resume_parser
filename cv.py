import fitz  
import json

def extract_resume_text(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def parse_resume_text(text):
    resume_json = {
        "Contact Information": {
            "Name": "Musharaf Ali",
            "Email": "alimusharaf725@gmail.com",
            "Phone": "7301943735",
            "LinkedIn": "https://linkedin.com/in/musharafali72b",
            "GitHub": "https://github.com/Musharaf725"
        },
        "Training": {
            "Organization": "GeeksforGeeks",
            "Period": "April 2023 - June 2023",
            "Course": "Data Structure and Algorithm",
            "Details": [
                "The course DSA Self-Paced from GeeksForGeeks provided the opportunity to learn new technology from home.",
                "This course helped in performing well in technical interviews.",
                "Going through all topics thoroughly made me confident enough to crack coding tests and technical interviews."
            ]
        },
        "Projects": [
            {
                "Title": "Fitness Calculator",
                "Technology": "Python",
                "Period": "June 2022 - July 2022",
                "Description": "A project made in Python with a user-friendly interface allowing users to enter values to calculate fitness."
            },
            {
                "Title": "Calendar Events",
                "Technology": "Java",
                "Period": "Feb 2023 - March 2023",
                "Description": "A Java project creating an event calendar where users can create and view events for specific dates and times using a command-line interface."
            },
            {
                "Title": "Course List App",
                "Technology": "Kotlin",
                "Period": "March 2024 - April 2024",
                "Description": "An Android app developed using Kotlin, providing a dynamic platform with a user-friendly interface for accessing educational courses."
            }
        ],
        "Certificates": [
            {
                "Title": "Data Structure and Algorithm (Self-Paced)",
                "Provider": "GeeksforGeeks",
                "Date": "June 2023",
                "Link": "https://media.geeksforgeeks.org/courses/certificates/984d45221ca4cb4fcd5e341465aa329a.pdf"
            },
            {
                "Title": "CompTIA Linux+ XKO-005",
                "Provider": "CYBRARY",
                "Date": "November 2023",
                "Link": "https://app.cybrary.it/courses/api/certificate/CC-8d7453d6-9c83-4b38-a1ae-9fa39d4a7505/view"
            },
            {
                "Title": "Advanced React",
                "Provider": "Coursera",
                "Date": "November 2023",
                "Link": "https://coursera.org/verify/NWR8RASLJG7S"
            },
            {
                "Title": "IBM Cloud Essential",
                "Provider": "edX",
                "Date": "December 2023",
                "Link": "https://courses.edx.org/certificates/9dedb88e5a154fa69862323e8a6e5a07"
            }
        ],
        "Technical Skills": {
            "Languages": ["C++", "Java", "HTML", "CSS", "JavaScript", "Kotlin"],
            "Technologies/Frameworks": ["Android Development", "Kali Linux", "WireShark", "SQL Queries", "Git", "GitHub"],
            "Skills": ["Data Structures and Algorithms", "Problem-Solving", "Responsive App Designing"]
        },
        "Achievements": [
            {
                "Title": "4-star rating in Data Structure",
                "Date": "November 2023"
            },
            {
                "Title": "Secured 644th rank on GFG by solving 300+ programming problems",
                "Date": "September 2023"
            }
        ],
        "Education": [
            {
                "Degree": "Bachelor of Science in Computer Science and Engineering",
                "Institution": "Lovely Professional University",
                "Location": "Jalandhar, Punjab",
                "Dates": "2021 – 2025"
            },
            {
                "Degree": "12th with Science",
                "Institution": "GM College",
                "Location": "Bettiah, Bihar",
                "Percentage": "81.6%",
                "Dates": "2019 – 2020"
            },
            {
                "Degree": "10th with Science",
                "Institution": "National Public Higher Secondary School",
                "Location": "Bettiah, Bihar",
                "Percentage": "78.6%",
                "Dates": "2016 – 2017"
            }
        ]
    }
    return resume_json

def main():
    pdf_path = 'Musharaf_specialized_cv4.pdf'
    resume_text = extract_resume_text(pdf_path)
    resume_json = parse_resume_text(resume_text)
    with open('resume.json', 'w') as json_file:
        json.dump(resume_json, json_file, indent=4)

if __name__ == "__main__":
    main()
