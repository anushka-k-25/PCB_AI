import axios from "axios";

const api = axios.create({
  baseURL: "https://pcb-ai.onrender.com",
});

export default api;