import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [branches, setBranches] = useState([]);
  const [form, setForm] = useState({ branch_name: "", ip: "" });
  const [editingIndex, setEditingIndex] = useState(null);

  const API = "http://localhost:8000/branches";

  const fetchBranches = async () => {
    const res = await axios.get(API);
    setBranches(res.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.branch_name || !form.ip) return;

    try {
      if (editingIndex !== null) {
        await axios.put(API, form);
      } else {
        await axios.post(API, form);
      }
      setForm({ branch_name: "", ip: "" });
      setEditingIndex(null);
      fetchBranches();
    } catch (err) {
      alert("เกิดข้อผิดพลาด: " + err.message);
    }
  };

  const handleEdit = (branch) => {
    setForm(branch);
    setEditingIndex(branch.branch_name);
  };

  const handleDelete = async (branch_name) => {
    if (window.confirm("ลบสาขานี้ใช่ไหม?")) {
      await axios.delete(`${API}/${branch_name}`);
      fetchBranches();
    }
  };

  useEffect(() => {
    fetchBranches();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-xl mx-auto bg-white p-6 rounded shadow">
        <h1 className="text-2xl font-bold mb-4">จัดการสาขา</h1>

        <form onSubmit={handleSubmit} className="mb-6 space-y-4">
          <input
            type="text"
            placeholder="ชื่อสาขา"
            className="w-full p-2 border rounded"
            value={form.branch_name}
            onChange={(e) => setForm({ ...form, branch_name: e.target.value })}
          />
          <input
            type="text"
            placeholder="IP Address"
            className="w-full p-2 border rounded"
            value={form.ip}
            onChange={(e) => setForm({ ...form, ip: e.target.value })}
          />
          <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
            {editingIndex !== null ? "บันทึกการแก้ไข" : "เพิ่มสาขา"}
          </button>
        </form>

        <table className="w-full table-auto text-left">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-2">ชื่อสาขา</th>
              <th className="p-2">IP</th>
              <th className="p-2">การกระทำ</th>
            </tr>
          </thead>
          <tbody>
            {branches.map((b) => (
              <tr key={b.branch_name}>
                <td className="p-2">{b.branch_name}</td>
                <td className="p-2">{b.ip}</td>
                <td className="p-2 space-x-2">
                  <button onClick={() => handleEdit(b)} className="text-blue-600">แก้ไข</button>
                  <button onClick={() => handleDelete(b.branch_name)} className="text-red-600">ลบ</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
