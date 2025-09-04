// Importamos librerías necesarias
import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"; // Router para navegación
import OrdenesList from "./components/OrdenesList";     // Componente de listado
import NuevaOrden from "./components/NuevaOrden";       // Componente de creación
import ActualizarEstado from "./components/ActualizarEstado"; // Componente de actualización

function App() {
  return (
    // Router envuelve toda la app
    <Router>
      <div style={{ padding: "20px" }}>
        <h1>Gestión de Órdenes de Servicio - Drones</h1>

        {/* Menú de navegación */}
        <nav>
          <Link to="/">📋 Ver Órdenes</Link> |{" "}
          <Link to="/nueva">➕ Nueva Orden</Link>
        </nav>

        {/* Definición de rutas */}
        <Routes>
          <Route path="/" element={<OrdenesList />} />
          <Route path="/nueva" element={<NuevaOrden />} />
          <Route path="/actualizar/:id" element={<ActualizarEstado />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
