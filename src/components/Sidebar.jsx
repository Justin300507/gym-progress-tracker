import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Dumbbell, Trophy, BarChart2, Settings } from 'lucide-react';

const Sidebar = () => {
  return (
    <aside className="w-56 bg-orange-950 text-orange-100 flex flex-col px-3 py-4 fixed h-full">
      <div className="flex items-center gap-2 px-2 mb-6">
        <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-orange-500 to-amber-500 flex items-center justify-center">
          <span className="text-white text-sm font-bold">A</span>
        </div>
        <span className="font-bold text-white text-sm">FitApp</span>
      </div>
      <nav className="flex-1 space-y-0.5">
        <NavLink to="/dashboard" className={({ isActive }) => `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${isActive ? 'bg-orange-800 text-white' : 'text-orange-300 hover:bg-orange-900 hover:text-white'}`}>
          <LayoutDashboard size={16} /> Dashboard
        </NavLink>
        <NavLink to="/workouts" className={({ isActive }) => `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${isActive ? 'bg-orange-800 text-white' : 'text-orange-300 hover:bg-orange-900 hover:text-white'}`}>
          <Dumbbell size={16} /> Workouts
        </NavLink>
        <NavLink to="/personal-records" className={({ isActive }) => `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${isActive ? 'bg-orange-800 text-white' : 'text-orange-300 hover:bg-orange-900 hover:text-white'}`}>
          <Trophy size={16} /> Records
        </NavLink>
        <NavLink to="/stats" className={({ isActive }) => `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${isActive ? 'bg-orange-800 text-white' : 'text-orange-300 hover:bg-orange-900 hover:text-white'}`}>
          <BarChart2 size={16} /> Stats
        </NavLink>
        <NavLink to="/settings" className={({ isActive }) => `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${isActive ? 'bg-orange-800 text-white' : 'text-orange-300 hover:bg-orange-900 hover:text-white'}`}>
          <Settings size={16} /> Settings
        </NavLink>
      </nav>
    </aside>
  );
};

export default Sidebar;