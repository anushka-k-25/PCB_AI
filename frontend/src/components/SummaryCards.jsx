import "../styles/SummaryCards.css";

import { FaBug } from "react-icons/fa";
import { FaBullseye } from "react-icons/fa";
import { FaExclamationTriangle } from "react-icons/fa";
import { FaCheckCircle } from "react-icons/fa";

function SummaryCards({ detections }) {
  const totalDefects = detections.length;

  const averageConfidence =
    totalDefects === 0
      ? 0
      : (
          detections.reduce(
            (sum, defect) => sum + defect.confidence,
            0
          ) / totalDefects
        ) * 100;

  const highCount = detections.filter(
    (d) => d.severity === "High"
  ).length;

  const mediumCount = detections.filter(
    (d) => d.severity === "Medium"
  ).length;

  const lowCount = detections.filter(
    (d) => d.severity === "Low"
  ).length;

  return (
    <div className="summary-container">

        <div className="summary-card">
            <FaBug className="summary-icon" />
            <h3>Total Defects</h3>
            <h2>{totalDefects}</h2>
        </div>

        <div className="summary-card">
            <FaBullseye className="summary-icon" />
            <h3>Avg Confidence</h3>
            <h2>{averageConfidence.toFixed(1)}%</h2>
        </div>

        <div className="summary-card">
            <FaExclamationTriangle className="summary-icon" />
            <h3>High Severity</h3>
            <h2>{highCount}</h2>
        </div>

        <div className="summary-card">
            <FaCheckCircle className="summary-icon" />
            <h3>Medium / Low</h3>
            <h2>{mediumCount + lowCount}</h2>
        </div>

    </div>
  );
}

export default SummaryCards;