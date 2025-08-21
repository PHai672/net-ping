// src/components/BranchForm.jsx
import React, { useState, useEffect } from "react";

const BranchForm = ({ onSubmit, editingBranch, cancelEdit }) => {
  const [branch, setBranch] = useState({ branch_name: "", ip: "" });

  useEffect(() => {
    if (editingBranch) setBranch(editingBranch);
  }, [editingBranch]);

  const handleChange = (e) => {
    setBranch({ ...branch, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(branch);
    setBranch({ branch_name: "", ip: "" });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-3 mt-4">
      <input
        type="text"
        name="branch_name"
        placeholder="ชื่อสาขา"
        value={branch.branch_name}
        onChange={handleChange}
        className="border px-3 py-2 rounded w-full"
        required
      />
      <input
        type="text"
        name="ip"
        placeholder="IP Address"
        value={branch.ip}
        onChange={handleChange}
        className="border px-3 py-2 rounded w-full"
        required
        disabled={!!editingBranch}
      />
      <div className="space-x-2">
        <button
          type="submit"
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          {editingBranch ? "บันทึกการแก้ไข" : "เพิ่มสาขา"}
        </button>
        {editingBranch && (
          <button
            type="button"
            onClick={cancelEdit}
            className="bg-gray-400 hover:bg-gray-500 text-white px-4 py-2 rounded"
          >
            ยกเลิก
          </button>
        )}
      </div>
    </form>
  );
};

export default BranchForm;
