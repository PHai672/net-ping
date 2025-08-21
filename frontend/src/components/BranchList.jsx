// src/components/BranchList.jsx
import React from "react";

const BranchList = ({ branches, onEdit, onDelete }) => {
  return (
    <div className="mt-4">
      <table className="min-w-full table-auto border border-gray-300">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">ชื่อสาขา</th>
            <th className="p-2 border">IP</th>
            <th className="p-2 border">Actions</th>
          </tr>
        </thead>
        <tbody>
          {branches.map((branch, index) => (
            <tr key={index} className="text-center">
              <td className="p-2 border">{branch.branch_name}</td>
              <td className="p-2 border">{branch.ip}</td>
              <td className="p-2 border space-x-2">
                <button
                  onClick={() => onEdit(branch)}
                  className="bg-yellow-400 hover:bg-yellow-500 px-3 py-1 rounded text-white"
                >
                  แก้ไข
                </button>
                <button
                  onClick={() => onDelete(branch.ip)}
                  className="bg-red-500 hover:bg-red-600 px-3 py-1 rounded text-white"
                >
                  ลบ
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BranchList;
