import React from 'react';
import { Search } from 'lucide-react';

const SearchBar = ({ value, onChange }) => {
  return (
    <div className="flex items-center gap-2 bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 rounded-lg px-3 py-2">
      <Search size={16} className="text-slate-500 dark:text-slate-400" />
      <input
        type="text"
        value={value}
        onChange={e => onChange(e.target.value)}
        placeholder="Search..."
        className="flex-1 bg-transparent focus:outline-none text-slate-900 dark:text-white"
      />
    </div>
  );
};

export default SearchBar;