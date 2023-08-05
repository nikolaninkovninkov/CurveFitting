import React, { useEffect, useState } from 'react';
import '../styles/CurveFitter.css';
import parseData from '../utils/parseData';
import useLocalStorage from '../hooks/useLocalStorage';
import axios from 'axios';
import CurveFitResponseData from '../types/CurveFitResponseData';
import functionPlot from 'function-plot';
import splitArrays from '../utils/splitArrays';
axios.defaults.baseURL = process.env.REACT_APP_SERVER_URL;
export default function CurveFitter() {
  const [xvalue, setXvalue] = useLocalStorage('xvalue', '');
  const [yvalue, setYvalue] = useLocalStorage('yvalue', '');
  const [functionValue, setFunctionValue] = useLocalStorage(
    'functionValue',
    '',
  );
  const [responseData, setResponseData] = useLocalStorage(
    'responseData',
    {} as CurveFitResponseData,
  );
  const [tableShow, setTableShow] = useState(false);
  useEffect(() => {
    console.log(JSON.parse(JSON.stringify(responseData))['a']);
    const data = parseData(xvalue, yvalue);
    functionPlot({
      target: '#graph',
      width: 800,
      height: 500,
      grid: true,
      yAxis: { domain: [Math.min(...data[1]) - 1, Math.max(...data[1]) + 1] },
      xAxis: { domain: [Math.min(...data[0]) - 1, Math.max(...data[0]) + 1] },
      data: [
        {
          graphType: 'polyline',
          fn: responseData.output_function,
        },
        {
          points: splitArrays(data[0], data[1]),
          fnType: 'points',
          graphType: 'scatter',
        },
      ],
    });
    const circles = document.querySelectorAll('circle');
    for (let i = 0; i < circles.length; i++) {
      circles[i].setAttribute('r', '3');
    }
    setTableShow(!!Object.keys(responseData));
  }, [responseData, xvalue, yvalue]);
  function handleApply() {
    const data = parseData(xvalue, yvalue);
    axios
      .post('/curvefitter/api/fit-curve/', {
        xdata: data[0],
        ydata: data[1],
        function: functionValue,
      })
      .then((response) => setResponseData(response.data))
      .catch((err) => console.log(err));
  }
  return (
    <div className='curve-fitter'>
      <div id='graph'></div>
      <div className='func-input'>
        <div className='label'>Function input</div>
        <input
          type='text'
          onChange={(e) => setFunctionValue(e.target.value)}
          value={functionValue}
        />
      </div>
      <div className='data-input'>
        <div className='data-col'>
          <div className='label'>X Axis</div>
          <textarea
            rows={10}
            onChange={(e) =>
              setXvalue((v) =>
                /^[0-9.\n]*$/.test(e.target.value) ? e.target.value : v,
              )
            }
            value={xvalue}></textarea>
        </div>
        <div className='data-col'>
          <div className='label'>Y Axis</div>
          <textarea
            rows={10}
            onChange={(e) =>
              setYvalue((v) =>
                /^[0-9.\n]*$/.test(e.target.value) ? e.target.value : v,
              )
            }
            value={yvalue}></textarea>
        </div>
      </div>
      <div className='apply-button'>
        <button onClick={handleApply}>Apply</button>
      </div>
      {tableShow && (
        <div className='table-container'>
          <table>
            <thead>
              <tr>
                <th colSpan={2}>Property</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td colSpan={2}>
                  R<sup>2</sup>
                </td>
                <td>{responseData.r_squared}</td>
              </tr>
            </tbody>
            <thead>
              <tr>
                <th>Parameter</th>
                <th>Value</th>
                <th>Variance</th>
              </tr>
            </thead>
            <tbody>
              {Object.keys(responseData)
                .sort()
                .map((key) => (
                  <tr key={key}>
                    {typeof responseData[key] === 'object' ? (
                      <>
                        <td>{key}</td>
                        <td>
                          {
                            (
                              responseData[key] as {
                                value: number;
                                var: number;
                              }
                            ).value
                          }
                        </td>
                        <td>
                          ±
                          {
                            (
                              responseData[key] as {
                                value: number;
                                var: number;
                              }
                            ).var
                          }
                        </td>
                      </>
                    ) : (
                      <></>
                    )}
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      )}
      {tableShow && (
        <div className='output-func'>
          <p>{responseData.output_function}</p>
          <button
            onClick={() =>
              navigator.clipboard.writeText(responseData.output_function)
            }>
            Copy
          </button>
        </div>
      )}
    </div>
  );
}
