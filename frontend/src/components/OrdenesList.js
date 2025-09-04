import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function OrdenesList() {
  // Estado local donde se guardan las órdenes que vienen de la API
  const [ordenes, setOrdenes] = useState([]);
//
  // useEffect se ejecuta cuando carga el componente
  useEffect(() => {
    //axios.get("http://localhost:8000/orders/") // Petición GET al backend FastAPI
    axios.get(`${process.env.REACT_APP_API_URL}/orders/`) //
      .then(res => setOrdenes(res.data))       // Guardamos respuesta en "ordenes"
      .catch(err => console.error(err));
  }, []);  // [] significa que solo se ejecuta una vez al inicio

  return (
    <div>
      <h2>📋 Listado de Órdenes</h2>
      <table border="1" cellPadding="5" style={{ marginTop: "10px" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Cliente</th>
            <th>Dron</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {ordenes.map(o => (
            <tr key={o.id}>
              <td>{o.id}</td>
              <td>{o.cliente}</td>
              <td>{o.dron}</td>
              <td>{o.estado}</td>
              <td>
                {/* Link para actualizar estado de una orden */}
                <Link to={`/actualizar/${o.id}`}>✏️ Cambiar Estado</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default OrdenesList;
