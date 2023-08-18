import React from 'react';
import { Link } from 'react-router-dom';
export default function Home() {
  return (
    <div>
      <p>
        <Link to='/curvefitter'>Curve Fitter</Link>
      </p>
      <p>
        <Link to='/newtons_method'>Newton's Method</Link>
      </p>
    </div>
  );
}
