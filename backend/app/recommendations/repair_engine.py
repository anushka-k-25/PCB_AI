from app.recommendations.pcb_defects import PCB_DEFECTS


def get_repair_recommendation(defect_class: str):
    """
    Returns detailed information for a detected PCB defect.

    Parameters:
        defect_class (str): Defect class predicted by YOLO.

    Returns:
        dict: Defect details if found, otherwise Unknown Defect.
    """

    return PCB_DEFECTS.get(
        defect_class,
        {
            "name": "Unknown Defect",
            "severity": "Unknown",
            "description": "No information available for this defect.",
            "possible_causes": [],
            "repair_recommendation": [],
            "inspection_tips": []
        }
    )