// import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

function App() {

  const [entitiesList, setEntitiesList] = useState([]);

  let list = 'data is loading';

  useEffect(() => {
    fetch('/api/v1/orders/')
        .then(response => response.json())
        .then(data => { setEntitiesList(data);});
  }, []);

  list = entitiesList.map( i => (<div>{i.order_id}: {i.usd_price}: {i.rur_price}: {i.delivery_date}</div>));

  return (
      <div className="App">
        <h1>Заказы</h1>
        { list }
      </div>
  );
}



export default App;
