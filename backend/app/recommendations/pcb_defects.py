PCB_DEFECTS = {
    "open": {
        "name": "Open Circuit",
        "severity": "High",
        "description": "A break in the copper trace interrupts electrical continuity.",
        "possible_causes": [
            "Broken copper trace",
            "Manufacturing defect",
            "Mechanical damage"
        ],
        "repair_recommendation": [
            "Inspect the damaged trace under magnification.",
            "Clean the affected area.",
            "Reconnect the trace using solder or jumper wire.",
            "Verify continuity using a multimeter."
        ],
        "inspection_tips": [
            "Check nearby traces for damage.",
            "Perform continuity testing before powering the PCB."
        ]
    },

    "short": {
        "name": "Short Circuit",
        "severity": "Critical",
        "description": "Two conductive traces are unintentionally connected.",
        "possible_causes": [
            "Excess copper",
            "Solder bridge",
            "Manufacturing error"
        ],
        "repair_recommendation": [
            "Remove excess solder or copper.",
            "Inspect for bridging under magnification.",
            "Verify isolation using a multimeter."
        ],
        "inspection_tips": [
            "Check adjacent traces carefully.",
            "Measure resistance between neighbouring tracks."
        ]
    },

    "mousebite": {
        "name": "Mouse Bite",
        "severity": "Medium",
        "description": "Small missing portions along the PCB edge caused during manufacturing.",
        "possible_causes": [
            "Improper depanelization",
            "Mechanical stress"
        ],
        "repair_recommendation": [
            "Inspect edge quality.",
            "Smooth rough edges if necessary.",
            "Replace PCB if structural integrity is compromised."
        ],
        "inspection_tips": [
            "Inspect all PCB edges.",
            "Look for cracks extending inward."
        ]
    },

    "spur": {
        "name": "Spur",
        "severity": "Medium",
        "description": "Unwanted copper protrusions extending from a trace.",
        "possible_causes": [
            "Etching defect",
            "Manufacturing contamination"
        ],
        "repair_recommendation": [
            "Remove excess copper carefully.",
            "Inspect surrounding traces.",
            "Verify electrical isolation."
        ],
        "inspection_tips": [
            "Use magnification.",
            "Check for accidental contact with nearby traces."
        ]
    },

    "copper": {
        "name": "Spurious Copper",
        "severity": "Medium",
        "description": "Unwanted copper particles remain on the PCB after etching.",
        "possible_causes": [
            "Incomplete etching",
            "Copper residue"
        ],
        "repair_recommendation": [
            "Remove unwanted copper.",
            "Clean the PCB thoroughly.",
            "Inspect surrounding area."
        ],
        "inspection_tips": [
            "Look for isolated copper fragments.",
            "Ensure proper insulation between traces."
        ]
    },

    "pin-hole": {
        "name": "Missing Hole",
        "severity": "High",
        "description": "A required drilled hole is absent from the PCB.",
        "possible_causes": [
            "Drilling machine failure",
            "Manufacturing error"
        ],
        "repair_recommendation": [
            "Verify PCB design.",
            "Re-drill if permitted.",
            "Replace PCB if required."
        ],
        "inspection_tips": [
            "Compare with PCB design files.",
            "Check all mounting and via holes."
        ]
    }
}