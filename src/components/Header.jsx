import React, { useState, useEffect } from 'react';
import { Sun, Moon } from 'lucide-react';

const Header = () => {
  const [dark, setDark] = useState(false);
  useEffect(() => {
    document.documentElement.classList.toggle('dark', dark);
  }, [dark]);
  return (
    <header className="flex justify-between items-center mb-6">
      <h1 className="text-2xl font-bold text-slate-900 dark:text-white">FitApp</h1>
      <button onClick={() => setDark(d => !d)} className="p-2 rounded-lg text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors">
        {dark ? <Sun size={18} /> : <Moon size={18} />}
      </button>
    </header>
  );
};

export default Header;