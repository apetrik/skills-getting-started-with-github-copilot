"""Shared data definitions for the high school API.

This module holds the canonical set of activities and provides helpers for
creating fresh copies. Separating the data from the application logic makes it
easier to reuse (for tests, CLI scripts, etc.) and keeps `app.py` focused on
routing behaviour.
"""

import copy

# canonical list of activities used by the API
DEFAULT_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"],
    },
    "Basketball Team": {
        "description": "Competitive basketball team for interscholastic tournaments",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"],
    },
    "Tennis Club": {
        "description": "Learn tennis skills and compete in matches",
        "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["sarah@mergington.edu"],
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"],
    },
    "Drama Club": {
        "description": "Perform in school plays and develop acting skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["mia@mergington.edu"],
    },
    "Debate Team": {
        "description": "Develop critical thinking and public speaking through debate",
        "schedule": "Mondays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["alexander@mergington.edu", "victoria@mergington.edu"],
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 3:30 PM - 4:45 PM",
        "max_participants": 20,
        "participants": ["ryan@mergington.edu"],
    },
}


def get_initial_activities() -> dict:
    """Return a deep copy of the default activities dictionary.

    This should be used whenever a fresh, mutable copy is required (for
    application state or for tests) to avoid accidental mutation of the module
    constant.
    """
    return copy.deepcopy(DEFAULT_ACTIVITIES)
