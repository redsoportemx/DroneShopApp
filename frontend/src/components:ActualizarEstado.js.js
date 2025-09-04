import React, { useState } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

function ActualizarEstado() {
  // Extraemos el ID de la orden desde la URL
  const { id } = useParams();
  const [estado, setEstado] = useState("");
  const navigate = useNavigate();

  // Enviar nuevo estado al backend
  const handleSubmit = (e) => {
    e.preventDefault();
    // PATCH al endpoint del backend
    axios.patch(`http://localhost:8000/orders/${id}?estado=${estado}`)
      .then(() => navigate("/")) // Redirige al listado
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>✏️ Actualizar Estado de la Orden #{id}</h2>
      <form onSubmit={handleSubmit}>
        <select value={estado} onChange={(e) => setEstado(e.target.value)}>
          <option value="">-- Seleccionar Estado --</option>
          <option value="pendiente">Pendiente</option>
          <option value="en proceso">En Proceso</option>
          <option value="terminado">Terminado</option>
          <option value="entregado">Entregado</option>
        </select><br />
        <button type="submit">Actualizar</button>
      </form>
    </div>
  );
}

export default ActualizarEstado;
