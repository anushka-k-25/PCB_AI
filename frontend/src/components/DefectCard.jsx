import "../styles/DefectCard.css";

function DefectCard({ defect }) {

  const severityClass =
    defect.severity?.toLowerCase() || "low";

  return (
    <div className="defect-card">

      <div className="defect-title">
        {defect.name}
      </div>

      <div className="defect-item">
        <strong>Confidence:</strong>{" "}
        {(defect.confidence * 100).toFixed(2)}%
      </div>

      <div className="defect-item">
        <strong>Severity:</strong>{" "}
        <span className={`badge ${severityClass}`}>
          {defect.severity}
        </span>
      </div>

      <div className="defect-item">
        <strong>Description:</strong><br />
        {defect.description}
      </div>

      <div className="defect-item">
        <strong>Possible Causes:</strong><br />
        {defect.possible_causes}
      </div>

      <div className="defect-item">
        <strong>Repair Recommendation:</strong><br />
        {defect.repair_recommendation}
      </div>

      <div className="defect-item">
        <strong>Inspection Tips:</strong><br />
        {defect.inspection_tips}
      </div>

    </div>
  );
}

export default DefectCard;