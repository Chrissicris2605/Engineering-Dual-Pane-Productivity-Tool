"""Fictional component data for the public dual-pane demo."""

COMPONENTS = [
    {
        "id": "MOD-001",
        "name": "Control Module",
        "category": "Module",
        "status": "Ready for review",
        "owner": "Systems Team",
        "notes": "Central unit used as the main reference element in this fictional assembly.",
        "rect": (80, 80, 190, 90),
    },
    {
        "id": "CAB-002",
        "name": "Signal Cable",
        "category": "Cable",
        "status": "Needs validation",
        "owner": "Integration Team",
        "notes": "Fictional connection between the control module and the connector housing.",
        "rect": (270, 115, 180, 35),
    },
    {
        "id": "BRK-003",
        "name": "Support Bracket",
        "category": "Mechanical",
        "status": "Ready for review",
        "owner": "Product Team",
        "notes": "Fictional support element used to demonstrate visual-to-data mapping.",
        "rect": (110, 215, 140, 70),
    },
    {
        "id": "CON-004",
        "name": "Connector Housing",
        "category": "Connector",
        "status": "Updated",
        "owner": "Electrical Team",
        "notes": "Fictional connector element highlighted when selected in the data table.",
        "rect": (490, 85, 165, 90),
    },
    {
        "id": "TER-005",
        "name": "Ground Terminal",
        "category": "Terminal",
        "status": "Ready for review",
        "owner": "Quality Team",
        "notes": "Fictional terminal element included to show a complete review workflow.",
        "rect": (430, 240, 165, 65),
    },
]
