import React from "react";
import { useAuth } from "../contexts/AuthContext.new";

export default function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          Welcome, {user?.full_name || user?.email || "Developer"}
        </h1>
        <p className="text-gray-600">
          This is your blank canvas. Start building your features here.
        </p>
      </div>
    </div>
  );
}
