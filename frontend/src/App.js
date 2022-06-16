import logo from './logo.svg';
import './App.css';
import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [phone, setPhone] = useState("");
  const [status, setStatus] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res = await fetch("/call", {method: "POST", body: JSON.stringify({message: message, ph_no: phone,}),});
      let resJson = await res.json();
      if (res.status === 200) {
        setMessage("");
        setPhone("");
        setStatus("Call added successfully");
      } else {
        setStatus("Some error occurred");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input type="text" value={message} placeholder="Message" onChange={(e) => setMessage(e.target.value)}/>
        <input type="text" value={phone} placeholder="Phone Number" onChange={(e) => setPhone(e.target.value)}/>
        <button type="submit">Call</button>
        </form>
        <div className="status">{status ? <p>{status}</p> : null}</div>
    </div>
  );
}

export default App;
