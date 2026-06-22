import React from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import Chart from '../components/Chart';

const StatsPage = ({ API }) => {
  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <h2 className="text-2xl font-semibold text-slate-900 dark:text-white mb-4">Statistics</h2>
        <Chart API={API} />
      </main>
    </div>
  );
};

export default StatsPage;