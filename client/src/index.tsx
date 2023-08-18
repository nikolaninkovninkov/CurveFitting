import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css';
import App from './components/App';
import axios from 'axios';
const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
axios.defaults.baseURL = process.env.REACT_APP_SERVER_URL;
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
