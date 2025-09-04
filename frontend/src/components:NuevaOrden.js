import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function NuevaOrden() {
  // Estado local para manejar datos del formulario
  const [form, setForm] = useState({
    id: "",
    cliente: "",
    dron: "",
    descripcion: "",
    estado: "pendiente",
    fecha_ingreso: new Date().toISOString().split("T")[0], // Fecha actual por defecto
    fecha_entrega: null
  });

  const navigate = useNavigate(); // Para redirigir tras crear la orden

  // Manejo de cambios en los inputs
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Enviar datos al backend
  const handleSubmit = (e) => {
    e.preventDefault(); // Evita recargar página
    axios.post("http://localhost:8000/orders/", form)
      .then(() => navigate("/")) // Redirige al listado
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>➕ Crear Nueva Orden</h2>
      <form onSubmit={handleSubmit}>
        <input name="id" placeholder="ID" onChange={handleChange} required /><br />
        <input name="cliente" placeholder="Cliente" onChange={handleChange} required /><br />
        <input name="dron" placeholder="Dron" onChange={handleChange} required /><br />
        <textarea name="descripcion" placeholder="Descripción" onChange={handleChange}></textarea><br />
        <button type="submit">Guardar</button>
      </form>
    </div>
  );
}

export default NuevaOrden;
