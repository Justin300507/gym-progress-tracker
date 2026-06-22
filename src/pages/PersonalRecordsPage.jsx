import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import { Trophy } from 'lucide-react';

const PersonalRecordsPage = ({ API }) => {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    const fetch = async () => {
      try {
        const res = await API.get('/personal_records');
        setRecords(res.data);
      } catch (e) {}
    };
    fetch();
  }, [API]);

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-semibold text-slate-900 dark:text-white">Personal Records</h2>
        </div>
        {records.length === 0 ? (
          <p className="text-slate-500 dark:text-slate-400">No records found.</p>
        ) : (
          <div className="space-y-3">
            {records.map(rec => (
              <div key={rec.id} className="bg-white dark:bg-slate-800 rounded-xl border border-slate-100 dark:border-slate-700 p-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-9 h-9 rounded-lg bg-orange-50 dark:bg-orange-900/30 flex items-center justify-center">
                    <Trophy size={18} className="text-orange-600" />
                  </div>
                  <div>
                    <p className="text-sm font-semibold text-slate-900 dark:text-white">{rec.exercise_name}</p>
                    <p className="text-xs text-slate-500 dark:text-slate-400">Max {rec.max_weight} kg × {rec.max_reps} reps</p>
                  </div>
                </div>
                <span className="text-sm font-medium text-slate-700 dark:text-slate-300">{new Date(rec.record_date).toLocaleDateString()}</span>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
};

export default PersonalRecordsPage;