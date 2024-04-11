import React, { useState } from 'react';
import app from './firebase';
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

import './App.css';

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const auth = getAuth(app);

  const handleSubmit = (e) => {
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // do nothing
      })
      .catch((error) => {
        console.log(error);
      });
  }

  return (
    <div className="App">

      <input type='email' placeholder='Email' value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type='password' placeholder='Password' value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleSubmit}>Create Account</button>

    </div>
  );
}

export default App;
