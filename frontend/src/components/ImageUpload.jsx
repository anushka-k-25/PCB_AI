import { useState, useRef } from "react";
import {
  FaCloudUploadAlt,
  FaFileImage,
  FaSearch,
} from "react-icons/fa";

import api from "../services/api";
import DefectCard from "./DefectCard";
import SummaryCards from "./SummaryCards";
import GenerateReport from "./GenerateReport";

import "../styles/ImageUpload.css";

function ImageUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const inputRef = useRef();

  const handleFile = (file) => {
    if (!file) return;

    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handleFileChange = (e) => {
    handleFile(e.target.files[0]);
  };

  const handleDrop = (e) => {
    e.preventDefault();

    const file = e.dataTransfer.files[0];

    handleFile(file);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a PCB image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      setLoading(true);

      const response = await api.post("/upload/", formData);

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">

      <h2 className="upload-title">
       Upload Your PCB Image for Defect Detection
      </h2>

      <p className="upload-subtitle">
        Upload a PCB image to detect manufacturing defects
        and receive repair recommendations.
      </p>

      <div
        className="upload-box"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
      >
        <FaCloudUploadAlt className="upload-icon" />

        <h3>Drag & Drop PCB Image</h3>

        <p>or</p>

        <input
          type="file"
          accept="image/*"
          ref={inputRef}
          onChange={handleFileChange}
          hidden
        />

        <button
          className="browse-button"
          onClick={() => inputRef.current.click()}
        >
          <FaFileImage />
          Browse Image
        </button>

        {selectedFile && (
          <div className="selected-file">
            ✅ {selectedFile.name}
          </div>
        )}
      </div>

      <button
        className="upload-button"
        disabled={loading}
        onClick={handleUpload}
      >
        <FaSearch />

        {loading
          ? " Detecting..."
          : " Detect Defects"}
      </button>

      {loading && (
        <div className="loading-container">

          <div className="loading-spinner"></div>

          <p className="loading-text">
            AI is analyzing your PCB...
          </p>

        </div>
      )}

      {result && (
        <>

          <h2 className="result-title">
            Detection Result
          </h2>

          <div className="image-comparison">

            <div className="image-card">

              <h3>Original PCB</h3>

              <img
                src={preview}
                alt="Original PCB"
              />

            </div>

            <div className="image-card">

              <h3>Detected PCB</h3>

              <img
                src={`http://127.0.0.1:8000${result.annotated_image}`}
                alt="Detected PCB"
              />

            </div>

          </div>

          <SummaryCards
            detections={result.detections}
          />

          <GenerateReport
            detections={result.detections}
            originalImage={preview}
            detectedImage={`http://127.0.0.1:8000${result.annotated_image}`}
          />

          <h2 className="result-title">
            Detected Defects
          </h2>

          <div className="defect-grid">
            {result.detections.map((defect, index) => (
              <DefectCard
                key={index}
                defect={defect}
              />
            ))}
          </div>
        </>
      )}

    </div>
  );
}

export default ImageUpload;