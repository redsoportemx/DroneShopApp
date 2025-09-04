import React, { useState } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

function ActualizarEstado() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [estado, setEstado] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.patch(`${process.env.REACT_APP_API_URL}/orders/${id}`, { 
        estado 
    })
      .then(res => {
        console.log("Estado actualizado:", res.data);
        navigate("/");
      })
      .catch(err => console.error("Error al actualizar estado:", err));
  };

  return (
    <div>
      <h2>✏️ Actualizar Estado de la Orden #{id}</h2>
      <form onSubmit={handleSubmit}>
        <select value={estado} onChange={(e) => setEstado(e.target.value)}>
          <option value="">Seleccione estado</option>
          <option value="pendiente">Pendiente</option>
          <option value="en progreso">En Progreso</option>
          <option value="terminado">Terminado</option>
        </select>
        <button type="submit">Actualizar</button>
      </form>
    </div>
  );
}

export default ActualizarEstado;
