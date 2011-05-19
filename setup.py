from setuptools import find_packages, setup

setup(
    name='TracGanttCalendarPlugin', version='0.11',
    packages=find_packages(exclude=['*.tests*']),

    author = "Dave Perrett",
    author_email='mail@recursive-design.com',
    url="http://recursive-design.com/projects/gantt-calendar/",
    description='Provide calendar and gantt chart functionality.',
    license = "New BSD",

    entry_points = """
        [trac.plugins]
        ganttcalendar.ticketcalendar = ganttcalendar.ticketcalendar
        ganttcalendar.ticketgantt = ganttcalendar.ticketgantt
    """,
    package_data={'ganttcalendar': ['templates/*.html','htdocs/img/*']},
)