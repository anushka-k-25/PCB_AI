import ImageUpload from "../components/ImageUpload";
import "../styles/Home.css";

function Home() {
  return (
    <div className="home-page">

      {/* Background Effects */}
      <div className="bg-circle circle1"></div>
      <div className="bg-circle circle2"></div>
      <div className="bg-circle circle3"></div>

      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">
          PCB Inspector AI
        </div>

        <ul className="nav-links">
          <li><a href="#">Home</a></li>
          <li><a href="#upload">Inspection</a></li>
          <li><a href="#">Features</a></li>
        </ul>
      </nav>

      {/* Hero Section */}
      <section className="hero">

        <div className="hero-left">

          <span className="tag">
            AI Powered Inspection
          </span>

          <h1>
            Detect PCB Defects
            <br />
            with Artificial Intelligence
          </h1>

          <p>
            Upload PCB images, detect manufacturing defects,
            analyse confidence scores and generate repair
            recommendations instantly.
          </p>

          <div className="hero-buttons">
            <a href="#upload" className="primary-btn">
              Start Inspection
            </a>

            <button className="secondary-btn">
              Learn More
            </button>
          </div>

        </div>

        <div className="hero-right">

          <div className="glass-card">

            <h3>Inspection Features</h3>

            <div className="feature">
              AI Defect Detection
            </div>

            <div className="feature">
              Confidence Analysis
            </div>

            <div className="feature">
              Repair Recommendation
            </div>

            <div className="feature">
              PDF Report Generation
            </div>

          </div>

        </div>

      </section>

      {/* Upload Section */}

      <section id="upload">
        <ImageUpload />
      </section>

    </div>
  );
}

export default Home;