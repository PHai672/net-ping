// src/App.jsx
import React, { useEffect, useState } from "react";
import axios from "axios";
import BranchList from "./components/BranchList";
import BranchForm from "./components/BranchForm";

const API_BASE = "http://localhost:8000";

function App() {
  const [branches, setBranches] = useState([]);
  const [editing, setEditing] = useState(null);

  const fetchBranches = async () => {
    const res = await axios.get(`${API_BASE}/branches`);
    setBranches(res.data);
  };

  useEffect(() => {
    fetchBranches();
  }, []);

  const handleAddOrEdit = async (branch) => {
    if (editing) {
      await axios.put(`${API_BASE}/branches/${branch.ip}`, branch);
    } else {
      await axios.post(`${API_BASE}/branches`, branch);
    }
    fetchBranches();
    setEditing(null);
  };

  const handleDelete = async (ip) => {
    await axios.delete(`${API_BASE}/branches/${ip}`);
    fetchBranches();
  };

  return (
    <div className="max-w-xl mx-auto mt-10 p-4 bg-white shadow rounded">
      <h1 className="text-2xl font-bold text-center">📋 จัดการสาขา</h1>
      <BranchForm
        onSubmit={handleAddOrEdit}
        editingBranch={editing}
        cancelEdit={() => setEditing(null)}
      />
      <BranchList
        branches={branches}
        onEdit={(branch) => setEditing(branch)}
        onDelete={handleDelete}
      />
    </div>
  );
}

export default App;
