import { useRef } from "react";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import ReportTemplate from "./ReportTemplate";

function GenerateReport({
  detections,
  originalImage,
  detectedImage,
}) {

  const reportRef = useRef();

  const generatePDF = async () => {

    const element = reportRef.current;

    const canvas = await html2canvas(element, {
      scale: 2,
      useCORS: true,
      allowTaint: true,
      backgroundColor: "#ffffff",
    });

    const imgData = canvas.toDataURL("image/jpeg", 1.0);

    const pdf = new jsPDF("p", "mm", "a4");

    const pdfWidth = pdf.internal.pageSize.getWidth();

    const pdfHeight = pdf.internal.pageSize.getHeight();

    const imgWidth = pdfWidth;

    const imgHeight =
      (canvas.height * imgWidth) / canvas.width;

    let heightLeft = imgHeight;

    let position = 0;

    pdf.addImage(
      imgData,
      "JPEG",
      0,
      position,
      imgWidth,
      imgHeight
    );

    heightLeft -= pdfHeight;

    while (heightLeft > 0) {

      position = heightLeft - imgHeight;

      pdf.addPage();

      pdf.addImage(
        imgData,
        "JPEG",
        0,
        position,
        imgWidth,
        imgHeight
      );

      heightLeft -= pdfHeight;
    }

    const today = new Date();

    const fileName =
      `PCB_Inspection_Report_${
        today.toISOString().split("T")[0]
      }.pdf`;

    pdf.save(fileName);
  };

  return (
    <>
      <div
        style={{
          textAlign: "center",
          marginTop: "30px",
        }}
      >
        <button
          onClick={generatePDF}
          style={{
            background: "#16a34a",
            color: "white",
            border: "none",
            padding: "14px 28px",
            borderRadius: "8px",
            cursor: "pointer",
            fontSize: "16px",
            fontWeight: "600",
          }}
        >
          📄 Download Inspection Report
        </button>
      </div>

      <div
        style={{
          position: "absolute",
          left: "-9999px",
          top: "0",
        }}
      >
        <div ref={reportRef}>
          <ReportTemplate
            detections={detections}
            originalImage={originalImage}
            detectedImage={detectedImage}
          />
        </div>
      </div>
    </>
  );
}

export default GenerateReport;