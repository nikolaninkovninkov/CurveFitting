import React, { useEffect, useState } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';
import axios from 'axios';
import NewtonsMethodResponseData from '../types/NewtonsMethodResponseData';
import '../styles/NewtonsMethod.css';
export default function NewtonsMethod() {
  const [functionValue, setFunctionValue] = useLocalStorage(
    'newtonsmethod.functionValue',
    '',
  );
  const [responseData, setResponseData] = useLocalStorage(
    'newtonsmethod.responseData',
    {} as NewtonsMethodResponseData,
  );
  const [resultShow, setResultShow] = useState(false);
  function handleApply() {
    axios
      .post('/math/newtons-method/', {
        function: functionValue,
      })
      .then((response) => setResponseData(response.data))
      .catch((err) => console.log(err));
  }
  useEffect(() => {
    if (!Object.keys(responseData).length) return setResultShow(false);
    setResultShow(true);
  }, [responseData]);
  return (
    <div className='newtons-method'>
      <div className='func-input'>
        <div className='label'>Function input</div>
        <input
          type='text'
          onChange={(e) => setFunctionValue(e.target.value)}
          value={functionValue}
        />
      </div>
      <div className='apply-button'>
        <button onClick={handleApply}>Apply</button>
      </div>
      {resultShow && (
        <div className='table-container'>
          <table>
            <thead>
              <tr>
                <th>Parameter</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>x</td>
                <td>{responseData.root}</td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
