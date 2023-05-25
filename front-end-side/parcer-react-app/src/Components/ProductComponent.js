import React, { useEffect, useState } from 'react';

export default function ProductComponent(){
    const[models, setModels] = useState([]);
    const[modelName, setModelName] = useState('');

    const fetchModelData = () => {
        fetch("http://localhost:8080/parcer/all")
          .then(response => {
            return response.json()
          })
          .then(data => {
            setModels(data)
          })
      }

    useEffect(() => {
        fetchModelData()
    }, [])

    return(
        <table class="container">
            <thead>
            <tr>
                <th><h1>Model Name</h1></th>
                <th><h1>Price</h1></th>
                <th><h1>Available</h1></th>
            </tr>
            </thead>
            <tbody>
            {models.map(model=>(
                <tr key={model.id}>
                    <td><a href={model.modelLink}>{model.modelName}</a></td>
                    <td>{model.price}</td>
                    <td>{model.available}</td>
                </tr>
            ))}
            </tbody>
        </table>
    )
}