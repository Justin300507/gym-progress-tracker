import React, { useState } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import { useNavigate } from 'react-router-dom';

const NewWorkoutPage = ({ API }) => {
  const [date, setDate] = useState('');
  const [notes, setNotes] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await API.post('/workouts', { date, notes });
      navigate('/workouts');
    } catch (e) {}
  };

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <h2 className="text-2xl font-semibold text-slate-900 dark:text-white mb-4">New Workout</h2>
        <form className="bg-white dark:bg-slate-800 rounded-xl border border-slate-100 dark:border-slate-700 p-6 space-y-4" onSubmit={handleSubmit}>
          <div className="space-y-1">
            <label className="text-xs font-medium text-slate-700 dark:text-slate-300">Date</label>
            <input type="date" value={date} onChange={e => setDate(e.target.value)} className="input" />
          </div>
          <div className="space-y-1">
            <label className="text-xs font-medium text-slate-700 dark:text-slate-300">Notes</label>
            <textarea value={notes} onChange={e => setNotes(e.target.value)} className="input" rows={4} />
          </div>
          <div className="flex gap-2">
            <button type="submit" className="bg-orange-600 hover:bg-orange-700 text-white font-medium py-2 px-4 rounded">Save</button>
            <button type="button" onClick={() => navigate(-1)} className="bg-slate-300 hover:bg-slate-400 text-slate-800 font-medium py-2 px-4 rounded">Cancel</button>
          </div>
        </form>
      </main>
    </div>
  );
};

export default NewWorkoutPage;