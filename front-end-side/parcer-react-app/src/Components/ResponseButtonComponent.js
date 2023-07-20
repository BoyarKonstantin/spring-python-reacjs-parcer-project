import React from 'react';
import axios from 'axios';

const Button = () => {

  const handleClick = () => {
    const url = 'http://localhost:5000/main';
    const reload_url = 'https://8080/actuator/restart' 
    const requestData = {
      url: 'https://www.ebay.co.uk/b/Apple-Mobile-Smartphones/9355/bn_449685?LH_ItemCondition=1000%7C1500&rt=nc&_udlo=280&mag=1', 
    };

    axios.post(url, requestData)
      .then(response => {
        console.log(response.data); 
      })
      .catch(error => {
        console.error('Error:', error);
      });

      axios.post(reload_url)
      .then(response =>{
        console.log("Server has been reload \n", response.data);
      })
      .catch(error => {
        console.error('Error:', error)
      });
  };


  return (
    <button onClick={handleClick}>Update data!</button>
  );
};

export default Button;
