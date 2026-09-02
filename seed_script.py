import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Club_Hub.settings')
django.setup()

from django.contrib.auth import get_user_model
from Apps.accounts.models import Club, Membership  # Update path if Membership is in another app

User = get_user_model()

def seed_memberships():
    print("Starting membership seeding process...")

    # 1. Fetch clubs
    club_names = [
        "Robotics & Automation Guild",
        "Quantum & Theoretical Physics Society",
        "AI Explorers & Innovators",
        "Cyber Defense Initiative",
        "Game Craft Collective",
        "Cosmic Explorers Club",
        "BioTech Innovations",
        "Literary & Humanities Forum",
        "Full-Stack Developers Network",
        "Creative Tech & Design Studio"
    ]
    
    clubs = list(Club.objects.filter(name__in=club_names))
    if len(clubs) < 10:
        print(f"Warning: Only found {len(clubs)}/10 clubs in database. Please run the club seeding script first.")
        return

    # 2. Fetch available users
    all_users = list(User.objects.all())
    # Each club requires 1 + 1 + 2 + 8 = 12 memberships.
    # To ensure distinct Pres/VP per club, we need at least 20 distinct users for 10 Pres + 10 VP.
    if len(all_users) < 20:
        print(f"Error: Need at least 20 users to assign unique Presidents and Vice-Presidents across 10 clubs. Found {len(all_users)}.")
        return

    # 3. Track executive assignments to enforce uniqueness rule
    assigned_executive_users = set()

    for club in clubs:
        print(f"\nProcessing memberships for: {club.name}")
        
        # Clear existing memberships for a clean re-run if needed
        Membership.objects.filter(club=club).delete()

        # --- A. Assign President & Vice-President ---
        # Pick from users who are not yet a President or Vice-President in any club
        available_for_exec = [u for u in all_users if u.id not in assigned_executive_users]
        
        executives = random.sample(available_for_exec, 2)
        president_user = executives[0]
        vp_user = executives[1]

        # Mark them as assigned executive
        assigned_executive_users.add(president_user.id)
        assigned_executive_users.add(vp_user.id)

        # Create President membership
        Membership.objects.create(
            user=president_user,
            club=club,
            role='president',
            points=random.randint(300, 500)
        )

        # Create Vice-President membership
        Membership.objects.create(
            user=vp_user,
            club=club,
            role='vice-president',
            points=random.randint(250, 450)
        )

        # --- B. Assign 2 Mentors ---
        # Exclude the current club's Pres & VP
        available_for_mentors = [u for u in all_users if u not in (president_user, vp_user)]
        mentors = random.sample(available_for_mentors, 2)

        for mentor_user in mentors:
            Membership.objects.create(
                user=mentor_user,
                club=club,
                role='mentor',
                points=random.randint(150, 300)
            )

        # --- C. Assign 8 Members ---
        # Exclude current club's Pres, VP, and Mentors
        club_assigned = {president_user, vp_user, *mentors}
        available_for_members = [u for u in all_users if u not in club_assigned]

        # If user count is less than 12, sample with replacement or take all available
        sample_size = min(8, len(available_for_members))
        members = random.sample(available_for_members, sample_size)

        for member_user in members:
            Membership.objects.create(
                user=member_user,
                club=club,
                role='member',
                points=random.randint(50, 200)
            )

        print(f" -> Assigned 1 Pres ({president_user.email}), 1 VP ({vp_user.email}), 2 Mentors, {sample_size} Members.")

    print("\nMembership seeding finished successfully!")

if __name__ == "__main__":
    seed_memberships()