```python
from datetime import datetime

def report_header_footer(function):
    def decorated_function(*parameters, **options):
        print("=" * 50)
        print("          DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        function(*parameters, **options)
        print("=" * 50)
        print("           END OF REPORT")
        print("=" * 50)
    return decorated_function


class Report:

    total_created = 0

    def __init__(self, report_name, creator):
        self.report_name = report_name
        self.creator = creator
        self.sections = []
        Report.total_created += 1

    def __str__(self):
        return f"Report Title: {self.report_name}\nAuthor: {self.creator}"

    def __len__(self):
        return len(self.sections)

    def add_section(self, section_title, section_text):
        self.sections.append((section_title, section_text))

    @report_header_footer
    def generate(self):
        print(self)
        print(f"Generated On: {datetime.now()}")
        print()

        for section_title, section_text in self.sections:
            print(f"{section_title}")
            print("-" * len(section_title))
            print(section_text)
            print()

    @classmethod
    def total_reports(cls):
        print(f"Total Reports Created: {cls.total_created}")


my_report = Report("Student Performance Report", "Umar Mulani")

my_report.add_section(
    "Introduction",
    "This report summarizes the academic performance of students."
)

my_report.add_section(
    "Performance Analysis",
    "The average result is 82%. Attendance has improved significantly."
)

my_report.add_section(
    "Conclusion",
    "Overall performance is satisfactory. More focus is needed on practical skills."
)

my_report.generate()

print("Number of Sections:", len(my_report))

Report.total_reports()
```
