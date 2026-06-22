import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import WorkoutCard from '../components/WorkoutCard';
import SearchBar from '../components/SearchBar';
import { Plus } from 'lucide-react';
import { Link } from 'react-router-dom';

const WorkoutListPage = ({ API }) => {
  const [workouts, setWorkouts] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    const fetch = async () => {
      try {
        const res = await API.get('/workouts');
        setWorkouts(res.data);
      } catch (e) {}
    };
    fetch();
  }, [API]);

  const filtered = workouts.filter(w => w.notes?.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900">
      <Sidebar />
      <main className="ml-56 flex-1 p-6 overflow-auto">
        <Header />
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-semibold text-slate-900 dark:text-white">Workouts</h2>
          <Link to="/workouts/new" className="bg-orange-600 hover:bg-orange-700 text-white font-medium py-2 px-4 rounded flex items-center gap-1.5">
            <Plus size={16} /> Add Workout
          </Link>
        </div>
        <SearchBar value={search} onChange={setSearch} />
        <div className="mt-4 space-y-3">
          {filtered.map(w => (
            <WorkoutCard key={w.id} workout={w} />
          ))}
        </div>
      </main>
    </div>
  );
};

export default WorkoutListPage;