import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

const initial = [
  [-1, 5, -1, 9, -1, -1, -1, -1, -1],
  [8, -1, -1, -1, 4, -1, 3, -1, 7],
  [-1, -1, -1, 2, 8, -1, 1, 9, -1],
  [5, 3, 8, 6, -1, 7, 9, 4, -1],
  [-1, 2, -1, 3, -1, 1, -1, -1, -1],
  [1, -1, 9, 8, -1, 4, 6, 2, 3],
  [9, -1, 7, 4, -1, -1, -1, -1, -1],
  [-1, 4, 5, -1, -1, -1, 2, -1, 9],
  [-1, -1, -1, -1, 3, -1, -1, 7, -1]
];

function handleSubmitButton() {
  const data = {
    type: 'your_type_value',
    message: 'your_message_value'
  };

  fetch("/api/", {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Error: " + response.url);
      }
    })
    .then((data) => {
      console.log(data); // Handle the response data
    })
    .catch((err) => {
      console.log(err); // Handle any errors that occurred
    });
}


function App() {
  const [sudokuArr, setSudokuArr] = useState(initial);

  function getDeepCopy(arr){
    return JSON.parse(JSON.stringify(arr));
  }
  function onInputChange(e, row, col){
    var val= parseInt(e.target.value || -1, arr = getDeepCopy(sudokuArr))

    if((val === -1 || val >=1) && val <=9){
      arr[row][col] = val;
    }
    setSudokuArr(arr);
  }

  var arr = [...Array(initial.length).keys()];

  return (
    <div className="App">
      <header className="App-header">
        <table>
          <tbody>
            {
              arr.map((row, rIndex) =>{
                return <tr key={rIndex}>
                  {
                  arr.map((col, cIndex) => {
                    return <td key={rIndex+cIndex}>
                      <input 
                      onChange={(e) => onInputChange(e,row,col)} 
                      value={sudokuArr[row][col] === -1 ? '' : sudokuArr[row][col]} 
                      className="block"/>
                    </td>
                  })}
                  
                </tr>
                
              })
            }
          </tbody>
        </table>
        <div className='Buttons'>
          <button onClick={handleSubmitButton} className='submit'>submit</button>
        </div>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
