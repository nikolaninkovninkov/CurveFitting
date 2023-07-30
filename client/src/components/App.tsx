import React from 'react';
import logo from '../img/logo.svg';
import '../styles/App.css';
import { createBrowserRouter, RouterProvider, Route, Link } from 'react-router-dom';
import Home from './Home';
import CurveFitter from './CurveFitter';
function App() {
  const router = createBrowserRouter([
    {
      path: '/',
      element: <Home></Home>,
    },
    { path: '/curvefitter', element: <CurveFitter></CurveFitter> },
  ]);
  return (
    <div className='App'>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
