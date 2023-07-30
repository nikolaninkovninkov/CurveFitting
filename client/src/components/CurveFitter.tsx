import React, { SetStateAction, useEffect, useState } from 'react';
import '../styles/CurveFitter.css';
import parseData from '../utils/parseData';
import useDebounce from '../hooks/useDebounce';
import useLocalStorage from '../hooks/useLocalStorage';
import axios from 'axios';
axios.defaults.baseURL = process.env.REACT_APP_SERVER_URL;
export default function CurveFitter() {
  const [xvalue, setXvalue] = useLocalStorage('xvalue', '');
  const [yvalue, setYvalue] = useLocalStorage('yvalue', '');
  const [functionValue, setFunctionValue] = useLocalStorage('functionValue', '');
  function handleApply() {
    const data = parseData(xvalue, yvalue);
    console.log(functionValue);
    console.log(data);
    axios
      .post('/curvefitter/api/fit-curve/', {
        xdata: data[0],
        ydata: data[1],
        function: functionValue,
      })
      .then((response) => console.log(response.data))
      .catch((err) => console.log(err));
  }
  return (
    <div className='curve-fitter'>
      <div className='func-input'>
        <div className='label'>Function input</div>
        <input type='text' onChange={(e) => setFunctionValue(e.target.value)} value={functionValue} />
      </div>
      <div className='data-input'>
        <div className='data-col'>
          <div className='label'>X Axis</div>
          <textarea
            rows={10}
            onChange={(e) => setXvalue((v) => (/^[0-9.\n]*$/.test(e.target.value) ? e.target.value : v))}
            value={xvalue}></textarea>
        </div>
        <div className='data-col'>
          <div className='label'>Y Axis</div>
          <textarea
            rows={10}
            onChange={(e) => setYvalue((v) => (/^[0-9.\n]*$/.test(e.target.value) ? e.target.value : v))}
            value={yvalue}></textarea>
        </div>
      </div>
      <div className='apply-button'>
        <button onClick={handleApply}>Apply</button>
      </div>
    </div>
  );
}
