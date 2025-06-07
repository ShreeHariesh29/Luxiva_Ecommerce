import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  const [data, setdata] = useState([])

  useEffect(() => {
    fetch("http://192.168.60.218:8000/home")
    .then(res => res.json())
    .then(data => setdata(data))
    .catch(err => console.log("API ERROR", err))
  },[])
  return (
    <div className="App">
      <h1>
        hello welcome to home page
      </h1>
      {data.map((item, index)=> (
        <div>
          <p>{item.name}</p>
          <p>{item.price}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
