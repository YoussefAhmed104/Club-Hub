import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Club_Hub.settings')
django.setup()

from django.contrib.auth import get_user_model
from Apps.accounts.models import Club, Interests

User = get_user_model()

def seed_database():
    print("Starting database seed process...")

    # 1. Create or get default admin user (accounting for CustomUser fields)
    default_user, created = User.objects.get_or_create(
        email='admin@example.com',
        defaults={
            'first_name': 'Admin',
            'last_name': 'User',
            'nickname': 'Admin',
            'school_code': 'ADM0001',  # Required unique CharField(max_length=7)
            'phone_number': '01000000000',
            'grade': '12th',
            'is_staff': True,
            'is_superuser': True,
            'email_verified': True,
        }
    )
    if created:
        default_user.set_password('admin123')
        default_user.save()
        print(f"Created default user '{default_user.email}' for club leadership.")

    # 2. Define and create all interests
    interest_names = [
        "Robotics", "Engineering", "English", "Physics", "Mathematics",
        "Cyber security", "Game development", "Astronomy", "Visual arts",
        "Machine learning", "Generative AI", "Chemistry", "Biology",
        "Geology", "Humanities", "Web development", "Quantum computing"
    ]

    interest_objs = {}
    for name in interest_names:
        obj, _ = Interests.objects.get_or_create(name=name)
        interest_objs[name] = obj

    print(f"Ensured {len(interest_objs)} interests exist in the database.")

    # 3. Define the 10 Clubs with their details and associated interests
    clubs_data = [
        {
            "name": "Robotics & Automation Guild",
            "description": "Building next-generation autonomous systems, competing in robotics leagues, and hosting hardware workshops.",
            "interests": ["Robotics", "Engineering", "Machine learning"]
        },
        {
            "name": "Quantum & Theoretical Physics Society",
            "description": "Exploring quantum computing paradigms, advanced physics, and abstract mathematical modeling.",
            "interests": ["Physics", "Mathematics", "Quantum computing"]
        },
        {
            "name": "AI Explorers & Innovators",
            "description": "Focused on deep learning, generative AI applications, and ethical artificial intelligence developments.",
            "interests": ["Machine learning", "Generative AI", "Mathematics"]
        },
        {
            "name": "Cyber Defense Initiative",
            "description": "Capture the Flag (CTF) competitions, network safety research, and ethical hacking practices.",
            "interests": ["Cyber security", "Web development"]
        },
        {
            "name": "Game Craft Collective",
            "description": "Designing games from concept to release, integrating interactive visual arts with game mechanics.",
            "interests": ["Game development", "Visual arts", "Web development"]
        },
        {
            "name": "Cosmic Explorers Club",
            "description": "Observational astronomy, planetary geology research, and astrophysics discussions.",
            "interests": ["Astronomy", "Geology", "Physics"]
        },
        {
            "name": "BioTech Innovations",
            "description": "Connecting molecular biology, organic chemistry, and computational biology to solve healthcare challenges.",
            "interests": ["Biology", "Chemistry", "Engineering"]
        },
        {
            "name": "Literary & Humanities Forum",
            "description": "Fostering creative writing, analytical reading, philosophy, and interdisciplinary humanities research.",
            "interests": ["English", "Humanities"]
        },
        {
            "name": "Full-Stack Developers Network",
            "description": "Building modern web platforms, open-source projects, and training emerging developers.",
            "interests": ["Web development", "Cyber security"]
        },
        {
            "name": "Creative Tech & Design Studio",
            "description": "Where art meets technology—exploring visual design, generative art, and digital medium experimentation.",
            "interests": ["Visual arts", "Generative AI", "Game development"]
        }
    ]

    # 4. Create clubs and populate ManyToMany interests
    for club_info in clubs_data:
        club, created = Club.objects.get_or_create(
            name=club_info["name"],
            defaults={
                "description": club_info["description"],
                "president": default_user,
                "vice_president": default_user,
            }
        )

        selected_interests = [interest_objs[name] for name in club_info["interests"] if name in interest_objs]
        club.interests.set(selected_interests)

        action = "Created" if created else "Updated"
        print(f"{action} club: {club.name}")

    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()