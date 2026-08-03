import { StrictMode } from 'react' //StrictMode is a wrapper component that helps identify potential problems in an application. It activates additional checks and warnings for its descendants.
import { createRoot } from 'react-dom/client' //Imports the function that renders the React application into the browser.
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
